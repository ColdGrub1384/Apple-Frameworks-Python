'''
Classes from the 'IDSFoundation' framework.
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
    
    
IDSLocalDeliverySocketOpenedMetric = _Class('IDSLocalDeliverySocketOpenedMetric')