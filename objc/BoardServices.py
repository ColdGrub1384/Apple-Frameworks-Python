
'''
Classes from the 'BoardServices' framework.
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
    
    
BSServiceSpecification = _Class('BSServiceSpecification')
BSServiceConnectionListener = _Class('BSServiceConnectionListener')
BSXPCServiceConnectionListener = _Class('BSXPCServiceConnectionListener')
BSServiceDomain = _Class('BSServiceDomain')
BSService = _Class('BSService')
BSServiceDomainSpecification = _Class('BSServiceDomainSpecification')
BSServiceConnectionEndpointInjector = _Class('BSServiceConnectionEndpointInjector')
BSXPCServiceConnectionPeer = _Class('BSXPCServiceConnectionPeer')
BSXPCServiceConnectionProxy = _Class('BSXPCServiceConnectionProxy')
BSXPCServiceConnectionMessage = _Class('BSXPCServiceConnectionMessage')
BSXPCServiceConnectionMessageReply = _Class('BSXPCServiceConnectionMessageReply')
BSXPCServiceConnectionEventHandler = _Class('BSXPCServiceConnectionEventHandler')
BSXPCServiceConnectionContext = _Class('BSXPCServiceConnectionContext')
BSXPCServiceConnectionChildContext = _Class('BSXPCServiceConnectionChildContext')
BSXPCServiceConnectionRootContext = _Class('BSXPCServiceConnectionRootContext')
BSXPCServiceConnectionRootClientServiceContext = _Class('BSXPCServiceConnectionRootClientServiceContext')
BSXPCServiceConnectionRootServerContext = _Class('BSXPCServiceConnectionRootServerContext')
BSXPCServiceConnectionNullContext = _Class('BSXPCServiceConnectionNullContext')
BSXPCServiceConnectionRootClientEndpointContext = _Class('BSXPCServiceConnectionRootClientEndpointContext')
BSXPCServiceConnection = _Class('BSXPCServiceConnection')
BSServiceConnection = _Class('BSServiceConnection')
BSServiceQuality = _Class('BSServiceQuality')
BSServicesConfiguration = _Class('BSServicesConfiguration')
BSServiceManager = _Class('BSServiceManager')
BSServiceConnectionEndpointMonitor = _Class('BSServiceConnectionEndpointMonitor')
BSServiceConnectionEndpoint = _Class('BSServiceConnectionEndpoint')
BSServiceInterface = _Class('BSServiceInterface')
BSMutableServiceInterface = _Class('BSMutableServiceInterface')