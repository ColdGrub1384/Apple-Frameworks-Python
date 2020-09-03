
'''
Classes from the 'AccessibilityUIShared' framework.
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
    
    
AXUIMessageSender = _Class('AXUIMessageSender')
AXUIMessageReplyHandler = _Class('AXUIMessageReplyHandler')
AXUIMessageContext = _Class('AXUIMessageContext')