'''
Classes from the 'AXSpeechImplementation' framework.
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

    
__AXSpeechActionPublicImplementation_super = _Class('__AXSpeechActionPublicImplementation_super')
AXSpeechActionPublicImplementation = _Class('AXSpeechActionPublicImplementation')
AXSpeechPublicInterface = _Class('AXSpeechPublicInterface')
