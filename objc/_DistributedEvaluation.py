'''
Classes from the 'DistributedEvaluation' framework.
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
    
    
DESBfloat16Transport = _Class('DESBfloat16Transport')