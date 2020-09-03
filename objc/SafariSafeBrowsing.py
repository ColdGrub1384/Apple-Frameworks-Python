
'''
Classes from the 'SafariSafeBrowsing' framework.
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
    
    
SSBServiceLookupResult = _Class('SSBServiceLookupResult')
SSBLookupResult = _Class('SSBLookupResult')
SSBLookupContext = _Class('SSBLookupContext')
RemoteConfigurationController = _Class('RemoteConfigurationController')
ProviderConfiguration = _Class('ProviderConfiguration')
SSBDatabaseUpdateSupport = _Class('SSBDatabaseUpdateSupport')
SSBDatabaseUpdaterStatus = _Class('SSBDatabaseUpdaterStatus')
SSBManagedConfigurationManager = _Class('SSBManagedConfigurationManager')
SSBAvailability = _Class('SSBAvailability')