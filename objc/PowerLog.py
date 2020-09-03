
'''
Classes from the 'PowerLog' framework.
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
    
    
PLClientLogger = _Class('PLClientLogger')
PLClientLogAggregator = _Class('PLClientLogAggregator')
PLModelingUtilities = _Class('PLModelingUtilities')
PLNetworkEnergyModel = _Class('PLNetworkEnergyModel')
PLDuetActivitySchedulerUsageSnapshot = _Class('PLDuetActivitySchedulerUsageSnapshot')
PLUsageSnapshot = _Class('PLUsageSnapshot')
PLEnergyBucket = _Class('PLEnergyBucket')
PLCoreDuetEvent = _Class('PLCoreDuetEvent')
PLCoreDuetEventInterval = _Class('PLCoreDuetEventInterval')