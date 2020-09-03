'''
Classes from the 'NotificationCenter' framework.
'''

try:
    from rubicon.objc import ObjCClass
except ValueError:
    def ObjCClass(name):
        return None


def _Class(name):
    try:
        return ObjCClass(name)
    except NameError:
        return None

    
NCWidgetMetrics = _Class('NCWidgetMetrics')
NCWidgetController = _Class('NCWidgetController')
NCSizeObservingView = _Class('NCSizeObservingView')
