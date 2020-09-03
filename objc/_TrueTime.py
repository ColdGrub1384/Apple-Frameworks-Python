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

    
HostResolver = _Class('TrueTime.HostResolver')
NTPConnection = _Class('TrueTime.NTPConnection')
Reachability = _Class('TrueTime.Reachability')
NTPClient = _Class('TrueTime.NTPClient')
PodsDummy_TrueTime = _Class('PodsDummy_TrueTime')
NTPReferenceTime = _Class('NTPReferenceTime')
TrueTimeClient = _Class('TrueTime.TrueTimeClient')
