
'''
Classes from the 'ShareSheet' framework.
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
    
    
UIAirDropExtensionItemDataSource = _Class('UIAirDropExtensionItemDataSource')
UIDocumentInteractionControllerDismissMarkupAction = _Class('UIDocumentInteractionControllerDismissMarkupAction')
UISUIActivityConfiguration = _Class('UISUIActivityConfiguration')
UISUIActivityExtensionItemDataRequest = _Class('UISUIActivityExtensionItemDataRequest')
UISUISecurityContext = _Class('UISUISecurityContext')
UISUIActivityExtensionItemData = _Class('UISUIActivityExtensionItemData')
UISDActivityItemData = _Class('UISDActivityItemData')
UIAirDropNode = _Class('UIAirDropNode')
SFShareSheetSlotManager = _Class('SFShareSheetSlotManager')
UISUIActivityViewControllerConfiguration = _Class('UISUIActivityViewControllerConfiguration')
UISUISecurityScopedResource = _Class('UISUISecurityScopedResource')
UISUIOpenInByCopySecurityScopedResource = _Class('UISUIOpenInByCopySecurityScopedResource')
UISUIAirDropSecurityScopedResource = _Class('UISUIAirDropSecurityScopedResource')
UISDShareSheetSessionConfiguration = _Class('UISDShareSheetSessionConfiguration')
UICreatePDFActivityItem = _Class('UICreatePDFActivityItem')
UIActivityItemImageRep = _Class('UIActivityItemImageRep')
UIActivityItemURLRep = _Class('UIActivityItemURLRep')
UIActivityItemCustomization = _Class('UIActivityItemCustomization')
UICreatePDFActivityPrintPaper = _Class('UICreatePDFActivityPrintPaper')
UIDocumentInteractionController = _Class('UIDocumentInteractionController')
UIActivity = _Class('UIActivity')
UIAssignToContactActivity = _Class('UIAssignToContactActivity')
UIOpenInIBooksActivity = _Class('UIOpenInIBooksActivity')
UISaveToCameraRollActivity = _Class('UISaveToCameraRollActivity')
UIAddToReadingListActivity = _Class('UIAddToReadingListActivity')
UIPrintActivity = _Class('UIPrintActivity')
UICreatePDFActivity = _Class('UICreatePDFActivity')
UICopyToPasteboardActivity = _Class('UICopyToPasteboardActivity')
UIMessageActivity = _Class('UIMessageActivity')
UIMailActivity = _Class('UIMailActivity')
UIApplicationExtensionActivity = _Class('UIApplicationExtensionActivity')
UIShortcutActivity = _Class('UIShortcutActivity')
UISocialActivity = _Class('UISocialActivity')
UIFileProviderApplicationExtensionActivity = _Class('UIFileProviderApplicationExtensionActivity')
SUIShareActivity = _Class('SUIShareActivity')
UIAirDropActivity = _Class('UIAirDropActivity')
UIActivityItemProvider = _Class('UIActivityItemProvider')
UIShareGroupActivityCell = _Class('UIShareGroupActivityCell')
UIAirDropGroupActivityCell = _Class('UIAirDropGroupActivityCell')
UIActivityActionGroupCell = _Class('UIActivityActionGroupCell')
UIActivityContentViewController = _Class('UIActivityContentViewController')
ObjectManipulationViewController = _Class('ObjectManipulationViewController')
UIActivityGroupViewController = _Class('UIActivityGroupViewController')
UIActivityViewController = _Class('UIActivityViewController')
UIApplicationExtensionViewControllerHost = _Class('UIApplicationExtensionViewControllerHost')
UIPrintActivityWrapperNavigationController = _Class('UIPrintActivityWrapperNavigationController')