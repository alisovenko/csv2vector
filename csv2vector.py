import os

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *

from csv2vector_controller import Csv2vectorDialog

class Csv2VectorPlugin:
  def __init__(self, iface):
    self.iface = iface

    #i18n
    pluginPath = QFileInfo(os.path.realpath(__file__)).path()

    overrideLocale = QSettings().value("locale/overrideFlag", False)
    if not overrideLocale:
        localeName = QLocale.system().name()
    else:
        localeName = QSettings().value("locale/userLocale", "")

    if QFileInfo(pluginPath).exists():
        self.localePath = pluginPath+"/i18n/csv2vector_" + localeName + ".qm"
        if QFileInfo(self.localePath).exists():
            self.translator = QTranslator()
            self.translator.load(self.localePath)
            QCoreApplication.installTranslator(self.translator)

  def initGui(self):
    self.action = QAction( QIcon(":/plugins/csv2vector/x_office_spreadsheet.png"), "CSV2Vector", self.iface.mainWindow())
    self.action.setWhatsThis( QCoreApplication.translate("CSV2Vector", "Create points shapefile from csv file"))
    self.action.setStatusTip( QCoreApplication.translate("CSV2Vector", "Create points shapefile from csv file"))
    QObject.connect(self.action, SIGNAL("triggered()"), self.run)

    if hasattr( self.iface, "addPluginToVectorMenu" ):
      self.iface.addPluginToVectorMenu( QCoreApplication.translate("CSV2Vector","CSV2Vector"), self.action )
      self.iface.addVectorToolBarIcon( self.action )
    else:
      self.iface.addPluginToMenu( QCoreApplication.translate("CSV2Vector","CSV2Vector"), self.action )
      self.iface.addToolBarIcon( self.action )

  def unload(self):
    self.iface.removePluginMenu("&Test plugins",self.action)
    self.iface.removeToolBarIcon(self.action)

    if hasattr( self.iface, "addPluginToVectorMenu" ):
      self.iface.removePluginVectorMenu( QCoreApplication.translate("CSV2Vector","CSV2Vector"), self.action )
      self.iface.removeVectorToolBarIcon( self.action )
    else:
      self.iface.removePluginMenu( QCoreApplication.translate("CSV2Vector","CSV2Vector"), self.action )
      self.iface.removeToolBarIcon( self.action )

  def run(self):
    uid = Csv2vectorDialog()
    uid.exec_()