from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *

# initialize Qt resources from file resouces.py
import resources

from csv2vector_controller import Csv2vectorDialog

class Csv2VectorPlugin:

  def __init__(self, iface):
    self.iface = iface

  def initGui(self):
    self.action = QAction(QIcon(":/plugins/testplug/x_office_spreadsheet.png"), "CSV2Vector", self.iface.mainWindow())
    self.action.setWhatsThis("Create points shapefile from csv file")
    self.action.setStatusTip("Create points shapefile from csv file")
    QObject.connect(self.action, SIGNAL("triggered()"), self.run)

    #self.iface.addToolBarIcon(self.action)
    #self.iface.addPluginToMenu("&Test plugins", self.action)
    
    if hasattr( self.iface, "addPluginToVectorMenu" ):
      self.iface.addPluginToVectorMenu( "CSV2Vector", self.action )
      self.iface.addVectorToolBarIcon( self.action )
    else:
      self.iface.addPluginToMenu( "CSV2Vector", self.action )
      self.iface.addToolBarIcon( self.action )
      
    #QObject.connect(self.iface.mapCanvas(), SIGNAL("renderComplete(QPainter *)"), self.renderTest)

  def unload(self):
    self.iface.removePluginMenu("&Test plugins",self.action)
    self.iface.removeToolBarIcon(self.action)
    
    if hasattr( self.iface, "addPluginToVectorMenu" ):
      self.iface.removePluginVectorMenu( "CSV2Vector", self.action )
      self.iface.removeVectorToolBarIcon( self.action )
    else:
      self.iface.removePluginMenu( "CSV2Vector", self.action )
      self.iface.removeToolBarIcon( self.action )
    #QObject.disconnect(self.iface.mapCanvas(), SIGNAL("renderComplete(QPainter *)"), self.renderTest)

  def run(self):
    uid = Csv2vectorDialog()
    uid.exec_()

#  def renderTest(self, painter):
#    # use painter for drawing to map canvas
#    print "TestPlugin: renderTest called!"