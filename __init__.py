def name():
  return "CSVtoVector"

def description():
  return "This plugin has no real use."

def category():
    return "Vector"

def version():
  return "Version 0.1"

def qgisMinimumVersion():
  return "1.0"

def authorName():
  return "Alexander Lisovenko"

def classFactory(iface):
  from csv2vector import Csv2VectorPlugin
  return Csv2VectorPlugin(iface)
