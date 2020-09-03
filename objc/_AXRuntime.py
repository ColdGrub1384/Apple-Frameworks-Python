'''
Classes from the 'AXRuntime' framework.
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

    
AXElementFetcher = _Class('AXElementFetcher')
AXElement = _Class('AXElement')
AXMVisionFeature_AXRuntime = _Class('AXMVisionFeature_AXRuntime')
AXMLElementCoagulation = _Class('AXMLElementCoagulation')
AXMLElementGroup = _Class('AXMLElementGroup')
AXMLTabButtonGroup = _Class('AXMLTabButtonGroup')
AXRemoteElement = _Class('AXRemoteElement')
AXRemoteMLElement = _Class('AXRemoteMLElement')
AXPidSuspensionInfo = _Class('AXPidSuspensionInfo')
AXObserverElementPair = _Class('AXObserverElementPair')
AXElementGroupPruner = _Class('AXElementGroupPruner')
AXElementGrouper = _Class('AXElementGrouper')
AXVisualElementGrouper = _Class('AXVisualElementGrouper')
AXElementGroupingKeyboardExtrasConsolidationPass = _Class('AXElementGroupingKeyboardExtrasConsolidationPass')
AXUIElement = _Class('AXUIElement')
AXUIMLElement = _Class('AXUIMLElement')
AXUIMockElement = _Class('AXUIMockElement')
AXSimpleRuntimeManager = _Class('AXSimpleRuntimeManager')
AXAttributedString = _Class('AXAttributedString')
AXElementAttributedString = _Class('AXElementAttributedString')
AXElementGroup = _Class('AXElementGroup')
