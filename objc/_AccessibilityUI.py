'''
Classes from the 'AccessibilityUI' framework.
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

    
AXUIClientConnection = _Class('AXUIClientConnection')
AXUIClient = _Class('AXUIClient')
