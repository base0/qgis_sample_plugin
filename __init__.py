# http://docs.qgis.org/testing/en/docs/pyqgis_developer_cookbook/plugins.html

def classFactory(iface):
  from MainPlugin import TestPlugin
  return TestPlugin(iface)
