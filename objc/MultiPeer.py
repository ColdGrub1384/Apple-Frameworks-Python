
'''
Classes from the 'MultiPeer' framework.
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
    
    
MultiPeer.Peer = _Class('MultiPeer.Peer')
MultiPeer.MultiPeer = _Class('MultiPeer.MultiPeer')
PodsDummy_MultiPeer = _Class('PodsDummy_MultiPeer')