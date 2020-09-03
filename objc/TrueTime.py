
'''
Classes from the 'TrueTime' framework.
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
    
    
TrueTime.HostResolver = _Class('TrueTime.HostResolver')
TrueTime.NTPConnection = _Class('TrueTime.NTPConnection')
TrueTime.Reachability = _Class('TrueTime.Reachability')
TrueTime.NTPClient = _Class('TrueTime.NTPClient')
PodsDummy_TrueTime = _Class('PodsDummy_TrueTime')
NTPReferenceTime = _Class('NTPReferenceTime')
TrueTime.TrueTimeClient = _Class('TrueTime.TrueTimeClient')