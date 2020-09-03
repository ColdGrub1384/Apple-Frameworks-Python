
'''
Classes from the 'Combine' framework.
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
    
    
Combine.DebugHook = _Class('Combine.DebugHook')
Combine.AnyCancellable = _Class('Combine.AnyCancellable')
Combine.ObservableObjectPublisher = _Class('Combine.ObservableObjectPublisher')