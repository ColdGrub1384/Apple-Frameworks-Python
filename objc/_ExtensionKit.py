'''
Classes from the 'ExtensionKit' framework.
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

    
EXRunningExtensionInfo = _Class('EXRunningExtensionInfo')
EXConcreteExtensionContextVendor = _Class('EXConcreteExtensionContextVendor')
EXSwiftUI_Subsystem = _Class('EXSwiftUI_Subsystem')
EXExtensionContextImplementation = _Class('EXExtensionContextImplementation')
EXConcreteExtension = _Class('EXConcreteExtension')
