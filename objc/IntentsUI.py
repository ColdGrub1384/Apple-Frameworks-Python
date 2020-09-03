
'''
Classes from the 'IntentsUI' framework.
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
    
    
INUIExtensionViewControllerConfiguration = _Class('INUIExtensionViewControllerConfiguration')
INUIInterfaceSection = _Class('INUIInterfaceSection')
INUIAppIntentDeliverer = _Class('INUIAppIntentDeliverer')
INUIExtensionRequestInfo = _Class('INUIExtensionRequestInfo')
INUIImageLoader = _Class('INUIImageLoader')
INUIPortableImageLoaderHelper = _Class('INUIPortableImageLoaderHelper')
INUIImageSizeProvider = _Class('INUIImageSizeProvider')
INUIImageServiceConnection = _Class('INUIImageServiceConnection')
INUIVoiceShortcutXPCInterface = _Class('INUIVoiceShortcutXPCInterface')
INUIAppIntentForwardingActionExecutor = _Class('INUIAppIntentForwardingActionExecutor')
INUISearchFoundationImageAdapter = _Class('INUISearchFoundationImageAdapter')
INUIAddVoiceShortcutButton = _Class('INUIAddVoiceShortcutButton')
INUIEditVoiceShortcutViewController = _Class('INUIEditVoiceShortcutViewController')
INUILoadingVoiceShortcutViewController = _Class('INUILoadingVoiceShortcutViewController')
INUIAddVoiceShortcutViewController = _Class('INUIAddVoiceShortcutViewController')
INUIRemoteViewController = _Class('INUIRemoteViewController')
INUIVoiceShortcutHostViewController = _Class('INUIVoiceShortcutHostViewController')