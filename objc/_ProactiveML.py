'''
Classes from the 'ProactiveML' framework.
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
    
    
AWDProactiveModelFittingEvaluation = _Class('AWDProactiveModelFittingEvaluation')