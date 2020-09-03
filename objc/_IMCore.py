'''
Classes from the 'IMCore' framework.
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
    
    
IMCloudKitSyncProgressRuntimeTestPreparing = _Class('IMCloudKitSyncProgressRuntimeTestPreparing')