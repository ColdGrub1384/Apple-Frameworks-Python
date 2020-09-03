
'''
Classes from the 'Pasteboard' framework.
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
    
    
PBDataTransferMonitor = _Class('PBDataTransferMonitor')
PBDataTransferRequest = _Class('PBDataTransferRequest')
PBObjectToObjectCoercion = _Class('PBObjectToObjectCoercion')
PBRepresentationToObjectCoercion = _Class('PBRepresentationToObjectCoercion')
PBObjectToRepresentationCoercion = _Class('PBObjectToRepresentationCoercion')
PBCoercionRegistry = _Class('PBCoercionRegistry')
PBItemCollection = _Class('PBItemCollection')
PBItemDetection = _Class('PBItemDetection')
PBItemCollectionServicer = _Class('PBItemCollectionServicer')
PBItem = _Class('PBItem')
PBCallbackSerialization = _Class('PBCallbackSerialization')
PBServerConnection = _Class('PBServerConnection')
PBSecurityScopedURLWrapper = _Class('PBSecurityScopedURLWrapper')
PBItemRepresentation = _Class('PBItemRepresentation')
PBKeyedUnarchiver = _Class('PBKeyedUnarchiver')