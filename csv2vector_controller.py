# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created: Tue Aug 27 21:12:02 2013
#      by: PyQt4 UI code generator 4.10.2
#
import csv, os

from PyQt4 import QtCore, QtGui

from qgis.core import *
from qgis.gui import *

from csv2vector_dialog_view import Ui_Dialog
from csv2vector_model import Csv2vectorModel

def renderCSVPreviewDecorator(method_to_decorate):
    def wrapper(self):
        method_to_decorate(self)
        self.renderCSVPreview()
    return wrapper

class Csv2vectorDialog( QtGui.QDialog, Ui_Dialog ):
    def __init__( self ):
        QtGui.QDialog.__init__( self )
        self.setupUi( self )
        
        self.__model = Csv2vectorModel();
        
        QtCore.QObject.connect( self.selectCSVFileButton, QtCore.SIGNAL( "clicked()" ), self.selectCSVFile )
        QtCore.QObject.connect( self.selectSHPFileButton, QtCore.SIGNAL( "clicked()" ), self.selectSHPFile )
        
        QtCore.QObject.connect(self.delimiterTabRadioButton, QtCore.SIGNAL( "clicked()" ), self.checkTabDelimiter )
        QtCore.QObject.connect(self.delimiterSpaceRadioButton, QtCore.SIGNAL( "clicked()" ), self.checkSpaceDelimiter )
        QtCore.QObject.connect(self.delimiterCommaRadioButton, QtCore.SIGNAL( "clicked()" ), self.checkCommaDelimiter )
        QtCore.QObject.connect(self.delimiterSemicolonRadioButton, QtCore.SIGNAL( "clicked()" ), self.checkSemicolonDelimiter )
        QtCore.QObject.connect(self.delimiterColonRadioButton, QtCore.SIGNAL( "clicked()" ), self.checkColonDelimiter )
        
        self.__model.csvDelimiter = " "
        self.delimiterSpaceRadioButton.setChecked(True)
    
    @renderCSVPreviewDecorator
    def checkTabDelimiter(self):
        self.__model.csvDelimiter = "\t"
        
    @renderCSVPreviewDecorator
    def checkSpaceDelimiter(self):
        self.__model.csvDelimiter = " "
        
    @renderCSVPreviewDecorator
    def checkCommaDelimiter(self):
        self.__model.csvDelimiter = ","
    
    @renderCSVPreviewDecorator    
    def checkSemicolonDelimiter(self):
        self.__model.csvDelimiter = ";"
        
    @renderCSVPreviewDecorator
    def checkColonDelimiter(self):
        self.__model.csvDelimiter = ":"
        
    def accept( self ):
        
        if self.__model.shpFilePath == None:
            QtGui.QMessageBox.warning(self,
                                self.tr("Wrong output file"),
                                self.tr("Output file is improperly defined.\nPlease enter a valid filename and try again.")
                               )
            return
        
        outFile = QtCore.QFile( self.__model.shpFilePath )
        if outFile.exists():
            if not QgsVectorFileWriter.deleteShapeFile( self.__model.shpFilePath ):
                QtGui.QMessageBox.warning( self, self.tr( "Delete error" ), self.tr( "Can't delete file %1" ).arg( self.__model.shpFilePath ) )
                return
    
        csvfile = open(os.path.abspath( unicode( QtCore.QFileInfo( self.__model.csvFilePath ).absoluteFilePath() ) ))
        csvfilereader = csv.reader(csvfile, delimiter=self.__model.csvDelimiter)
        
        xAttrIndex = self.attrXCoordComboBox.currentIndex()
        yAttrIndex = self.attrYCoordComboBox.currentIndex()
        azAttrIndex = self.attrAzCoordComboBox.currentIndex()
        distAttrIndex = self.attrDistCoordComboBox.currentIndex()
        
        header = csvfilereader.next()
        
        attrIndexesForInfo = list(set(range(header.__len__())) ^ set([xAttrIndex, yAttrIndex, azAttrIndex, distAttrIndex]))
        
        shapeFields = dict(zip(range(attrIndexesForInfo.__len__()), [QgsField( header[attrIndex], QtCore.QVariant.String, QtCore.QString(), 255 ) for  attrIndex in attrIndexesForInfo]))
        crs = QgsCoordinateReferenceSystem( 4326 )
        
        shapeFileWriter = QgsVectorFileWriter( self.__model.shpFilePath, self.__model.shpFileEncoding, shapeFields, QGis.WKBPoint, crs )
        
        for dataRow in csvfilereader:
            try:
                coordX = float(dataRow[xAttrIndex])
                coordY = float(dataRow[yAttrIndex])
                az = float(dataRow[azAttrIndex])
                dist = float(dataRow[distAttrIndex])
                
                feature = QgsFeature()
                geometry = QgsGeometry()
                
                newCoord = self.__model.recalculateCoordinates(( coordX, coordY), az, dist)
                
                point = QgsPoint( newCoord[0], newCoord[1] )
                feature.setGeometry( geometry.fromPoint( point ) )
                
                
                for attrCounter in range(attrIndexesForInfo.__len__()):
                    feature.addAttribute( attrCounter, dataRow[attrIndexesForInfo[attrCounter]] )
    
                shapeFileWriter.addFeature( feature )
            except ValueError:
                 msgBox = QtGui.QMessageBox(self)
                 msgBox.setWindowTitle(self.tr("Wrong attribute type"))
                 msgBox.setText("Point with attributes %s has incorrect attribute type" %str(dataRow))
                 ignorethisButton = msgBox.addButton(self.tr("Ignore this"), QtGui.QMessageBox.ActionRole)
                 ignoreallButton = msgBox.addButton(self.tr("Ignore all"), QtGui.QMessageBox.ActionRole)
                 
                 
                 msgBox.exec_()

                 if (msgBox.clickedButton() == ignorethisButton):
                     pass
                 elif (msgBox.clickedButton() == ignoreallButton):
                     break
                 #.warning(self,
                 #               self.tr("Wrong attribute type"),
                 #               self.tr("Point with attributes %s has incorrect attribute type" %str(dataRow))
                 #              )
                
        
        del shapeFileWriter
        del csvfilereader
        csvfile.close()
        
        newLayer = QgsVectorLayer(self.__model.shpFilePath, QtCore.QFileInfo( self.__model.shpFilePath ).baseName(), "ogr" )
        QgsMapLayerRegistry.instance().addMapLayer( newLayer )
        
        self.close()

    @renderCSVPreviewDecorator
    def selectCSVFile(self):
        csvFilter = QtCore.QString( "CSV files (*.csv *.CSV)" )
        fileDialog = QgsEncodingFileDialog( self, self.tr( "Select input csv file" ), QtCore.QString(), csvFilter, QtCore.QString() )
        fileDialog.setDefaultSuffix( QtCore.QString( "csv" ) )
        fileDialog.setFileMode( QtGui.QFileDialog.AnyFile )

        if not fileDialog.exec_() == QtGui.QDialog.Accepted:
            return

        self.__model.csvFilePath = fileDialog.selectedFiles()[0]
        
        self.csvFileEdit.setText( self.__model.csvFilePath )
        self.groupBox.setEnabled(True)
        self.groupBox_2.setEnabled(True)
        self.groupBox_3.setEnabled(True)
        
    def renderCSVPreview(self):
        csvfile = open(os.path.abspath(unicode( QtCore.QFileInfo( self.__model.csvFilePath ).absoluteFilePath() ) ))
        csvfilereader = csv.reader(csvfile, delimiter=self.__model.csvDelimiter)
        
        self.tableWidget.clear()
        self.attrXCoordComboBox.clear()
        self.attrYCoordComboBox.clear()
        self.attrAzCoordComboBox.clear()
        self.attrDistCoordComboBox.clear()
        
        header = csvfilereader.next()
        self.tableWidget.setColumnCount(header.__len__())
        
        listOfLables = [QtCore.QString(lable) for lable in header]
        self.tableWidget.setHorizontalHeaderLabels ( listOfLables)
        
        self.attrXCoordComboBox.insertItems ( 0, listOfLables )
        self.attrYCoordComboBox.insertItems ( 0, listOfLables )
        self.attrAzCoordComboBox.insertItems ( 0, listOfLables )
        self.attrDistCoordComboBox.insertItems ( 0, listOfLables )
        
        numOfDataRows = 3
        self.tableWidget.setRowCount(numOfDataRows)
        for rowCounter in range(numOfDataRows):
            dataRow = csvfilereader.next()
            for colCounter in range(header.__len__()):
                self.tableWidget.setItem(rowCounter, colCounter, QtGui.QTableWidgetItem(QtCore.QString(dataRow[colCounter])) )
            
        del csvfilereader
        csvfile.close()
        
    def selectSHPFile(self):
        shpFilter = QtCore.QString( "Shapefiles (*.shp *.SHP)" )
        fileDialog = QgsEncodingFileDialog( self, self.tr( "Select output shapefile" ), QtCore.QString(), shpFilter, QtCore.QString() )
        fileDialog.setDefaultSuffix( QtCore.QString( "shp" ) )
        fileDialog.setFileMode( QtGui.QFileDialog.AnyFile )
        fileDialog.setAcceptMode( QtGui.QFileDialog.AcceptSave )
        fileDialog.setConfirmOverwrite( True )
        
        if not fileDialog.exec_() == QtGui.QDialog.Accepted:
            return
        
        self.__model.shpFilePath = fileDialog.selectedFiles()[0]
        self.__model.shpFileEncoding = fileDialog.encoding()
        
        self.shpFileEdit.setText( self.__model.shpFilePath )