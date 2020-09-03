
'''
Classes from the 'ContactsDonation' framework.
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
    
    
CNDInMemoryDonationPreferences = _Class('CNDInMemoryDonationPreferences')
CNDDonationPreferences = _Class('CNDDonationPreferences')
CNDonationLoggerProvider = _Class('CNDonationLoggerProvider')
CNDDonorExtension = _Class('CNDDonorExtension')
CNDonationAgentXPCAdapter = _Class('CNDonationAgentXPCAdapter')
CNDCoreTelephonyServices = _Class('CNDCoreTelephonyServices')
CNDSIMCardItem = _Class('CNDSIMCardItem')
CNDonationExtensionRequestHandler = _Class('CNDonationExtensionRequestHandler')
CNDDonorLoader = _Class('CNDDonorLoader')
CNDonationStore = _Class('CNDonationStore')
CNDonationValue = _Class('CNDonationValue')
CNDSIMCardMonitor = _Class('CNDSIMCardMonitor')
CNDonationOrigin = _Class('CNDonationOrigin')
CNMutableDonationOrigin = _Class('CNMutableDonationOrigin')