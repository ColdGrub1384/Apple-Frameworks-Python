
'''
Classes from the 'NetAppsUtilities' framework.
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
    
    
NAIdentityBuilder = _Class('NAIdentityBuilder')
NAIdentity = _Class('NAIdentity')
NAIdentityCharacteristic = _Class('NAIdentityCharacteristic')
NADescriptionBuilder = _Class('NADescriptionBuilder')
NAItemDiffOperation = _Class('NAItemDiffOperation')
NAGroupDiffOperation = _Class('NAGroupDiffOperation')
NAGroupedItemDiff = _Class('NAGroupedItemDiff')
NASimpleDiffableItemGroup = _Class('NASimpleDiffableItemGroup')
NAQueue = _Class('NAQueue')
NADelegateMethodLogSettings = _Class('NADelegateMethodLogSettings')
NADelegateDispatcher = _Class('NADelegateDispatcher')
NAPromise = _Class('NAPromise')
NACancelationToken = _Class('NACancelationToken')
NADecayingTimer = _Class('NADecayingTimer')
NAScheduler = _Class('NAScheduler')
NAValueThrottler = _Class('NAValueThrottler')
NAUniqueArrayDiff = _Class('NAUniqueArrayDiff')
NAUniqueArrayDiffOptions = _Class('NAUniqueArrayDiffOptions')
NADeallocationSentinel = _Class('NADeallocationSentinel')
NADeallocationTracer = _Class('NADeallocationTracer')
NAFuture = _Class('NAFuture')
NATreeNode = _Class('NATreeNode')
NAMutableTreeNode = _Class('NAMutableTreeNode')
NAPair = _Class('NAPair')
NAFlatMapEnumerator = _Class('NAFlatMapEnumerator')
NAFilterEnumerator = _Class('NAFilterEnumerator')
NATreeNodeDeepNodeEnumerator = _Class('NATreeNodeDeepNodeEnumerator')