
'''
Classes from the 'CoreMaterial' framework.
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
    
    
MTCoreMaterialVisualStylingProvider = _Class('MTCoreMaterialVisualStylingProvider')
MTVisualStyleSet = _Class('MTVisualStyleSet')
MTMaterialSettingsInterpolator = _Class('MTMaterialSettingsInterpolator')
MTCoreMaterialVisualStyling = _Class('MTCoreMaterialVisualStyling')
MTPrunePromise = _Class('MTPrunePromise')
MTColor = _Class('MTColor')
MTWhiteColor = _Class('MTWhiteColor')
MTRGBColor = _Class('MTRGBColor')
MTTintingMaterialSettings = _Class('MTTintingMaterialSettings')
MTTintingFilteringMaterialSettings = _Class('MTTintingFilteringMaterialSettings')
MTRecipeMaterialSettings = _Class('MTRecipeMaterialSettings')
MTStylingProvidingSolidColorLayer = _Class('MTStylingProvidingSolidColorLayer')
MTMaterialLayer = _Class('MTMaterialLayer')