
'''
Classes from the 'MobileAsset' framework.
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
    
    
MAXpcConnection = _Class('MAXpcConnection')
MAProgressNotification = _Class('MAProgressNotification')
MADownloadConfig = _Class('MADownloadConfig')
MADownloadOptions = _Class('MADownloadOptions')
MAMsuDownloadOptions = _Class('MAMsuDownloadOptions')
MAAssetDiff = _Class('MAAssetDiff')
MAXpcManager = _Class('MAXpcManager')
ASAssetQuery = _Class('ASAssetQuery')
ASAsset = _Class('ASAsset')
MAAssetQuery = _Class('MAAssetQuery')
MAAsset = _Class('MAAsset')
MAAbsoluteAssetId = _Class('MAAbsoluteAssetId')
MAProgressHandler = _Class('MAProgressHandler')