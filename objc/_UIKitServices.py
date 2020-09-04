'''
Classes from the 'UIKitServices' framework.
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

    
UISApplicationSupportService = _Class('UISApplicationSupportService')
UISCurrentUserInterfaceStyleValue = _Class('UISCurrentUserInterfaceStyleValue')
UISApplicationSupportDisplayEdgeInsetsWrapper = _Class('UISApplicationSupportDisplayEdgeInsetsWrapper')
UISApplicationStateService = _Class('UISApplicationStateService')
UISUserInterfaceStyleMode = _Class('UISUserInterfaceStyleMode')
UISIntentForwardingActionResponse = _Class('UISIntentForwardingActionResponse')
UISFetchContentInBackgroundActionResponse = _Class('UISFetchContentInBackgroundActionResponse')
UISDeviceContext = _Class('UISDeviceContext')
UISMutableDeviceContext = _Class('UISMutableDeviceContext')
UISApplicationSupportDisplayEdgeInfo = _Class('UISApplicationSupportDisplayEdgeInfo')
UISDisplayContext = _Class('UISDisplayContext')
UISMutableDisplayContext = _Class('UISMutableDisplayContext')
UISApplicationInitializationContext = _Class('UISApplicationInitializationContext')
UISMutableApplicationInitializationContext = _Class('UISMutableApplicationInitializationContext')
UISHandleRemoteNotificationAction = _Class('UISHandleRemoteNotificationAction')
UISIntentForwardingAction = _Class('UISIntentForwardingAction')
UISFetchContentInBackgroundAction = _Class('UISFetchContentInBackgroundAction')
UISApplicationInitializationContextParameters = _Class('UISApplicationInitializationContextParameters')
UISApplicationSupportClient = _Class('UISApplicationSupportClient')
UISApplicationStateClient = _Class('UISApplicationStateClient')
UISApplicationState = _Class('UISApplicationState')
