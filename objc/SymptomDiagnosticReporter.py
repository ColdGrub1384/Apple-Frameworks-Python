
'''
Classes from the 'SymptomDiagnosticReporter' framework.
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
    
    
SDRDiagnosticReporter = _Class('SDRDiagnosticReporter')