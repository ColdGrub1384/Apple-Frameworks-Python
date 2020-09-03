'''
Classes from the 'Frameworks' framework.
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
    
    
WK_RTCCodecSpecificInfoH264 = _Class('WK_RTCCodecSpecificInfoH264')