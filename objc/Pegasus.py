
'''
Classes from the 'Pegasus' framework.
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
    
    
PGControlsViewModelValues = _Class('PGControlsViewModelValues')
PGControlsViewModel = _Class('PGControlsViewModel')
PGPictureInPictureProxy = _Class('PGPictureInPictureProxy')
PGPlaybackStatePrerollAttributes = _Class('PGPlaybackStatePrerollAttributes')
PGPlaybackState = _Class('PGPlaybackState')
PGPictureInPictureRemoteObject = _Class('PGPictureInPictureRemoteObject')
PGRunLoopObserver = _Class('PGRunLoopObserver')
PGCommand = _Class('PGCommand')
PGInterruptionAssistant = _Class('PGInterruptionAssistant')
PGDisplayLink = _Class('PGDisplayLink')
PGPictureInPictureController = _Class('PGPictureInPictureController')
PGPictureInPictureApplication = _Class('PGPictureInPictureApplication')
PGHostedWindowHostingHandle = _Class('PGHostedWindowHostingHandle')
PGCABackdropLayer = _Class('PGCABackdropLayer')
PGBackdropView = _Class('PGBackdropView')
PGStashView = _Class('PGStashView')
PGStashedMaskView = _Class('PGStashedMaskView')
PGHitTestExtendableView = _Class('PGHitTestExtendableView')
PGCABackdropLayerView = _Class('PGCABackdropLayerView')
PGControlsContainerView = _Class('PGControlsContainerView')
PGVibrantFillView = _Class('PGVibrantFillView')
PGLayoutContainerView = _Class('PGLayoutContainerView')
PGControlsView = _Class('PGControlsView')
PGMaterialView = _Class('PGMaterialView')
PGButtonView = _Class('PGButtonView')
PGProgressIndicator = _Class('PGProgressIndicator')
PGPrerollIndicatorView = _Class('PGPrerollIndicatorView')
PGPortalView = _Class('PGPortalView')
PGLayerHostView = _Class('PGLayerHostView')
PGGradientView = _Class('PGGradientView')
PGHostedWindow = _Class('PGHostedWindow')
PGPictureInPictureViewController = _Class('PGPictureInPictureViewController')