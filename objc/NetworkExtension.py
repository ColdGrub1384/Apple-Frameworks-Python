
'''
Classes from the 'NetworkExtension' framework.
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
    
    
NWTLSParameters = _Class('NWTLSParameters')
NEFilterPacketContext = _Class('NEFilterPacketContext')
NEVPNIKEv1ProposalParameters = _Class('NEVPNIKEv1ProposalParameters')
NEVPNIKEv2SecurityAssociationParameters = _Class('NEVPNIKEv2SecurityAssociationParameters')
NEIKEv2RTT = _Class('NEIKEv2RTT')
NEProviderServer = _Class('NEProviderServer')
NEVPN = _Class('NEVPN')
NEVPNApp = _Class('NEVPNApp')
NEUserNotification = _Class('NEUserNotification')
NEFilterSettings = _Class('NEFilterSettings')
NEIPCWrapper = _Class('NEIPCWrapper')
NEVPNConnection = _Class('NEVPNConnection')
NETunnelProviderSession = _Class('NETunnelProviderSession')
NEFilterRule = _Class('NEFilterRule')
NEAppPushCallKitXPCClient = _Class('NEAppPushCallKitXPCClient')
NEProxyServer = _Class('NEProxyServer')
NEProxySettings = _Class('NEProxySettings')
NEUtilConfigurationClient = _Class('NEUtilConfigurationClient')
NEProviderAppConfigurationClient = _Class('NEProviderAppConfigurationClient')
NEProvider_Subsystem = _Class('NEProvider_Subsystem')
NEAppSidecarPolicySession = _Class('NEAppSidecarPolicySession')
NEProfilePayloadBase = _Class('NEProfilePayloadBase')
NEProfilePayloadContentFilter = _Class('NEProfilePayloadContentFilter')
NEProfilePayloadBaseVPN = _Class('NEProfilePayloadBaseVPN')
NEProfilePayloadAOVPN = _Class('NEProfilePayloadAOVPN')
NEProfileIngestionPayloadInfo = _Class('NEProfileIngestionPayloadInfo')
NEProfileIngestion = _Class('NEProfileIngestion')
NEAccountIdentifiers = _Class('NEAccountIdentifiers')
NEPolicySession = _Class('NEPolicySession')
NEPolicy = _Class('NEPolicy')
NEPolicyResult = _Class('NEPolicyResult')
NEPolicyRouteRule = _Class('NEPolicyRouteRule')
NEPolicyCondition = _Class('NEPolicyCondition')
NEAgentFilterExtension = _Class('NEAgentFilterExtension')
NEByteParser = _Class('NEByteParser')
NEPathEventObserver = _Class('NEPathEventObserver')
NEPathEvent = _Class('NEPathEvent')
NEPathController = _Class('NEPathController')
NEFilterPacketInterpose = _Class('NEFilterPacketInterpose')
NEPacketTunnelFlow = _Class('NEPacketTunnelFlow')
NEPacket = _Class('NEPacket')
NEEvaluateConnectionRule = _Class('NEEvaluateConnectionRule')
NEOnDemandRule = _Class('NEOnDemandRule')
NEOnDemandRuleEvaluateConnection = _Class('NEOnDemandRuleEvaluateConnection')
NEOnDemandRuleIgnore = _Class('NEOnDemandRuleIgnore')
NEOnDemandRuleDisconnect = _Class('NEOnDemandRuleDisconnect')
NEOnDemandRuleConnect = _Class('NEOnDemandRuleConnect')
NENexusBrowse = _Class('NENexusBrowse')
NENexusFlowAssignedProperties = _Class('NENexusFlowAssignedProperties')
NENexusFlowManager = _Class('NENexusFlowManager')
NENexusAgent = _Class('NENexusAgent')
NEDNSSettingsManager = _Class('NEDNSSettingsManager')
NENetworkAgent = _Class('NENetworkAgent')
NEProxyConfigurationNetworkAgent = _Class('NEProxyConfigurationNetworkAgent')
NEDNSSettingsNetworkAgent = _Class('NEDNSSettingsNetworkAgent')
NEPathControllerNetworkAgent = _Class('NEPathControllerNetworkAgent')
NEContentFilterNetworkAgent = _Class('NEContentFilterNetworkAgent')
NEAOVPNNetworkAgent = _Class('NEAOVPNNetworkAgent')
NEAppVPNNetworkAgent = _Class('NEAppVPNNetworkAgent')
NEVPNNetworkAgent = _Class('NEVPNNetworkAgent')
NELaunchServices = _Class('NELaunchServices')
NEBundleProxy = _Class('NEBundleProxy')
NEKeychainItem = _Class('NEKeychainItem')
NEIdentityKeychainItem = _Class('NEIdentityKeychainItem')
NEIPv6Settings = _Class('NEIPv6Settings')
NEIPv6Route = _Class('NEIPv6Route')
NEIPv4Settings = _Class('NEIPv4Settings')
NEIPv4Route = _Class('NEIPv4Route')
NEIPSecSASession = _Class('NEIPSecSASession')
NEIPSecSALocalSession = _Class('NEIPSecSALocalSession')
NEIPSecSAKernelSession = _Class('NEIPSecSAKernelSession')
NEIPSecSA = _Class('NEIPSecSA')
NEProcessInfo = _Class('NEProcessInfo')
NEIPC = _Class('NEIPC')
NEIKEv2Transport = _Class('NEIKEv2Transport')
NEIKEv2TransportClient = _Class('NEIKEv2TransportClient')
NEIKEv2RequestContext = _Class('NEIKEv2RequestContext')
NEIKEv2DeleteIKEContext = _Class('NEIKEv2DeleteIKEContext')
NEIKEv2DeleteChildContext = _Class('NEIKEv2DeleteChildContext')
NEIKEv2NewChildContext = _Class('NEIKEv2NewChildContext')
NEIKEv2MOBIKEContext = _Class('NEIKEv2MOBIKEContext')
NEIKEv2InformationalContext = _Class('NEIKEv2InformationalContext')
NEIKEv2RekeyChildContext = _Class('NEIKEv2RekeyChildContext')
NEIKEv2RekeyIKEContext = _Class('NEIKEv2RekeyIKEContext')
NEIKEv2Session = _Class('NEIKEv2Session')
NELoopbackConnection = _Class('NELoopbackConnection')
NEIKEv2Helper = _Class('NEIKEv2Helper')
NEIKEv2MOBIKE = _Class('NEIKEv2MOBIKE')
NEIKEv2Server = _Class('NEIKEv2Server')
NEIKEv2AddressList = _Class('NEIKEv2AddressList')
NEIKEv2Rekey = _Class('NEIKEv2Rekey')
NEIKEv2TimerResponder = _Class('NEIKEv2TimerResponder')
NEIKEv2Packet = _Class('NEIKEv2Packet')
NEIKEv2InformationalPacket = _Class('NEIKEv2InformationalPacket')
NEIKEv2CreateChildPacket = _Class('NEIKEv2CreateChildPacket')
NEIKEv2IKEAuthPacket = _Class('NEIKEv2IKEAuthPacket')
NEIKEv2IKESAInitPacket = _Class('NEIKEv2IKESAInitPacket')
NEIKEv2Payload = _Class('NEIKEv2Payload')
NEIKEv2ConfigPayload = _Class('NEIKEv2ConfigPayload')
NEIKEv2ResponseConfigPayload = _Class('NEIKEv2ResponseConfigPayload')
NEIKEv2TrafficSelectorPayload = _Class('NEIKEv2TrafficSelectorPayload')
NEIKEv2ResponderTrafficSelectorPayload = _Class('NEIKEv2ResponderTrafficSelectorPayload')
NEIKEv2InitiatorTrafficSelectorPayload = _Class('NEIKEv2InitiatorTrafficSelectorPayload')
NEIKEv2NotifyPayload = _Class('NEIKEv2NotifyPayload')
NEIKEv2DeletePayload = _Class('NEIKEv2DeletePayload')
NEIKEv2EAPPayload = _Class('NEIKEv2EAPPayload')
NEIKEv2AuthPayload = _Class('NEIKEv2AuthPayload')
NEIKEv2CertificateRequestPayload = _Class('NEIKEv2CertificateRequestPayload')
NEIKEv2CertificatePayload = _Class('NEIKEv2CertificatePayload')
NEIKEv2VendorIDPayload = _Class('NEIKEv2VendorIDPayload')
NEIKEv2NoncePayload = _Class('NEIKEv2NoncePayload')
NEIKEv2IdentifierPayload = _Class('NEIKEv2IdentifierPayload')
NEIKEv2ResponderIdentifierPayload = _Class('NEIKEv2ResponderIdentifierPayload')
NEIKEv2InitiatorIdentifierPayload = _Class('NEIKEv2InitiatorIdentifierPayload')
NEIKEv2KeyExchangePayload = _Class('NEIKEv2KeyExchangePayload')
NEIKEv2ChildSAPayload = _Class('NEIKEv2ChildSAPayload')
NEIKEv2IKESAPayload = _Class('NEIKEv2IKESAPayload')
NEIKEv2EncryptedPayload = _Class('NEIKEv2EncryptedPayload')
NEIKEv2EncryptedFragmentPayload = _Class('NEIKEv2EncryptedFragmentPayload')
NEIKEv2CustomPayload = _Class('NEIKEv2CustomPayload')
NEIKEv2Listener = _Class('NEIKEv2Listener')
NEIKEv2IKESA = _Class('NEIKEv2IKESA')
NEIKEv2EAP = _Class('NEIKEv2EAP')
NEIKEv2Crypto = _Class('NEIKEv2Crypto')
NEIKEv2DHKeys = _Class('NEIKEv2DHKeys')
NEIKEv2ConfigurationMessage = _Class('NEIKEv2ConfigurationMessage')
NEIKEv2ConfigurationAttribute = _Class('NEIKEv2ConfigurationAttribute')
NEIKEv2StringAttribute = _Class('NEIKEv2StringAttribute')
NEIKEv2SupportedAttribute = _Class('NEIKEv2SupportedAttribute')
NEIKEv2AppVersionAttribute = _Class('NEIKEv2AppVersionAttribute')
NEIKEv2DNSDomainAttribute = _Class('NEIKEv2DNSDomainAttribute')
NEIKEv2SubnetAttribute = _Class('NEIKEv2SubnetAttribute')
NEIKEv2IPv6SubnetAttribute = _Class('NEIKEv2IPv6SubnetAttribute')
NEIKEv2IPv6AddressAttribute = _Class('NEIKEv2IPv6AddressAttribute')
NEIKEv2IPv4SubnetAttribute = _Class('NEIKEv2IPv4SubnetAttribute')
NEIKEv2AddressAttribute = _Class('NEIKEv2AddressAttribute')
NEIKEv2ResponderTransportIPv6Address = _Class('NEIKEv2ResponderTransportIPv6Address')
NEIKEv2InitiatorTransportIPv6Address = _Class('NEIKEv2InitiatorTransportIPv6Address')
NEIKEv2IPv6PCSCFAttribute = _Class('NEIKEv2IPv6PCSCFAttribute')
NEIKEv2IPv4PCSCFAttribute = _Class('NEIKEv2IPv4PCSCFAttribute')
NEIKEv2IPv6DHCPAttribute = _Class('NEIKEv2IPv6DHCPAttribute')
NEIKEv2IPv6DNSAttribute = _Class('NEIKEv2IPv6DNSAttribute')
NEIKEv2IPv4NetmaskAttribute = _Class('NEIKEv2IPv4NetmaskAttribute')
NEIKEv2IPv4DHCPAttribute = _Class('NEIKEv2IPv4DHCPAttribute')
NEIKEv2IPv4DNSAttribute = _Class('NEIKEv2IPv4DNSAttribute')
NEIKEv2IPv4AddressAttribute = _Class('NEIKEv2IPv4AddressAttribute')
NEIKEv2VendorData = _Class('NEIKEv2VendorData')
NEIKEv2CustomData = _Class('NEIKEv2CustomData')
NEIKEv2Identifier = _Class('NEIKEv2Identifier')
NEIKEv2KeyIDIdentifier = _Class('NEIKEv2KeyIDIdentifier')
NEIKEv2AddressIdentifier = _Class('NEIKEv2AddressIdentifier')
NEIKEv2ASN1DNIdentifier = _Class('NEIKEv2ASN1DNIdentifier')
NEIKEv2UserFQDNIdentifier = _Class('NEIKEv2UserFQDNIdentifier')
NEIKEv2FQDNIdentifier = _Class('NEIKEv2FQDNIdentifier')
NEIKEv2ChildSAConfiguration = _Class('NEIKEv2ChildSAConfiguration')
NEIKEv2IKESAConfiguration = _Class('NEIKEv2IKESAConfiguration')
NEIKEv2SessionConfiguration = _Class('NEIKEv2SessionConfiguration')
NEIKEv2TrafficSelector = _Class('NEIKEv2TrafficSelector')
NEIKEv2ChildSAProposal = _Class('NEIKEv2ChildSAProposal')
NEIKEv2IKESAProposal = _Class('NEIKEv2IKESAProposal')
NEIKEv2DHProtocol = _Class('NEIKEv2DHProtocol')
NEIKEv2IntegrityProtocol = _Class('NEIKEv2IntegrityProtocol')
NEIKEv2PRFProtocol = _Class('NEIKEv2PRFProtocol')
NEIKEv2EncryptionProtocol = _Class('NEIKEv2EncryptionProtocol')
NEIKEv2EAPProtocol = _Class('NEIKEv2EAPProtocol')
NEIKEv2AuthenticationProtocol = _Class('NEIKEv2AuthenticationProtocol')
NEIKEv2SignatureHashProtocol = _Class('NEIKEv2SignatureHashProtocol')
NEIKEv2SPI = _Class('NEIKEv2SPI')
NEIKEv2ESPSPI = _Class('NEIKEv2ESPSPI')
NEIKEv2IKESPI = _Class('NEIKEv2IKESPI')
NEIKEv2PrivateNotify = _Class('NEIKEv2PrivateNotify')
NEIKEv2ChildSA = _Class('NEIKEv2ChildSA')
NETunnelNetworkSettings = _Class('NETunnelNetworkSettings')
NEPacketTunnelNetworkSettings = _Class('NEPacketTunnelNetworkSettings')
NETransparentProxyNetworkSettings = _Class('NETransparentProxyNetworkSettings')
NEHotspotHelper = _Class('NEHotspotHelper')
NEHotspotHelperCommand = _Class('NEHotspotHelperCommand')
NEHotspotHelperResponse = _Class('NEHotspotHelperResponse')
NEHotspotNetwork = _Class('NEHotspotNetwork')
NEHotspotConfigurationManager = _Class('NEHotspotConfigurationManager')
NEHotspotConfiguration = _Class('NEHotspotConfiguration')
NEHotspotEAPSettings = _Class('NEHotspotEAPSettings')
NEHotspotHS20Settings = _Class('NEHotspotHS20Settings')
NEDNSSettingsBundle = _Class('NEDNSSettingsBundle')
NEHotspotConfigurationHelper = _Class('NEHotspotConfigurationHelper')
NEHelper = _Class('NEHelper')
NEAppPushManager = _Class('NEAppPushManager')
NENexus = _Class('NENexus')
NEInternetNexus = _Class('NEInternetNexus')
NEIPsecNexus = _Class('NEIPsecNexus')
NEFlowNexus = _Class('NEFlowNexus')
NENexusFlow = _Class('NENexusFlow')
NENexusPathFlow = _Class('NENexusPathFlow')
NENexusFlowDivertFlow = _Class('NENexusFlowDivertFlow')
NEFlowMetaData = _Class('NEFlowMetaData')
NEFilterVerdict = _Class('NEFilterVerdict')
NEFilterRemediationVerdict = _Class('NEFilterRemediationVerdict')
NEFilterAbsoluteVerdict = _Class('NEFilterAbsoluteVerdict')
NEFilterNewFlowVerdict = _Class('NEFilterNewFlowVerdict')
NEFilterControlVerdict = _Class('NEFilterControlVerdict')
NEFilterDataVerdict = _Class('NEFilterDataVerdict')
NEFilterSource = _Class('NEFilterSource')
NEFilterProviderConfiguration = _Class('NEFilterProviderConfiguration')
NEFilterReport = _Class('NEFilterReport')
NEFilterManager = _Class('NEFilterManager')
NEFilterFlow = _Class('NEFilterFlow')
NEFilterSocketFlow = _Class('NEFilterSocketFlow')
NEFilterBrowserFlow = _Class('NEFilterBrowserFlow')
NEFilterDataSavedMessageHandler = _Class('NEFilterDataSavedMessageHandler')
NEAppPush = _Class('NEAppPush')
NEFilterBlockPage = _Class('NEFilterBlockPage')
NEFileHandleMaintainer = _Class('NEFileHandleMaintainer')
NEFileHandle = _Class('NEFileHandle')
NENetworkAgentRegistrationFileHandle = _Class('NENetworkAgentRegistrationFileHandle')
NEFlowDivertFileHandle = _Class('NEFlowDivertFileHandle')
NEPolicySessionFileHandle = _Class('NEPolicySessionFileHandle')
NEDNSPacket = _Class('NEDNSPacket')
NEDNSQuery = _Class('NEDNSQuery')
NEDNSResourceRecord = _Class('NEDNSResourceRecord')
NEDNSSettings = _Class('NEDNSSettings')
NEDNSOverHTTPSSettings = _Class('NEDNSOverHTTPSSettings')
NEDNSOverTLSSettings = _Class('NEDNSOverTLSSettings')
NEVPNProtocol = _Class('NEVPNProtocol')
NEVPNProtocolPlugin = _Class('NEVPNProtocolPlugin')
NEVPNProtocolPPP = _Class('NEVPNProtocolPPP')
NEVPNProtocolPPTP = _Class('NEVPNProtocolPPTP')
NEVPNProtocolL2TP = _Class('NEVPNProtocolL2TP')
NEVPNProtocolIPSec = _Class('NEVPNProtocolIPSec')
NEVPNProtocolIKEv2 = _Class('NEVPNProtocolIKEv2')
NETunnelProviderProtocol = _Class('NETunnelProviderProtocol')
NEDNSProxyProviderProtocol = _Class('NEDNSProxyProviderProtocol')
NEDNSProxyManager = _Class('NEDNSProxyManager')
NEDNSProxy = _Class('NEDNSProxy')
NEContentFilter = _Class('NEContentFilter')
NEConfigurationManager = _Class('NEConfigurationManager')
NEAgentExtension = _Class('NEAgentExtension')
NEAgentTunnelExtension = _Class('NEAgentTunnelExtension')
NEAgentPacketTunnelExtension = _Class('NEAgentPacketTunnelExtension')
NEAgentAppProxyExtension = _Class('NEAgentAppProxyExtension')
NEAgentDNSProxyExtension = _Class('NEAgentDNSProxyExtension')
NEAgentAppPushExtension = _Class('NEAgentAppPushExtension')
NEConfiguration = _Class('NEConfiguration')
NEAppRule = _Class('NEAppRule')
NEPathRule = _Class('NEPathRule')
NEAppProxyFlow = _Class('NEAppProxyFlow')
NEAppProxyUDPFlow = _Class('NEAppProxyUDPFlow')
NEAppProxyTCPFlow = _Class('NEAppProxyTCPFlow')
NEAppProxyProviderContainer = _Class('NEAppProxyProviderContainer')
NEVPNManager = _Class('NEVPNManager')
NETunnelProviderManager = _Class('NETunnelProviderManager')
NEAppProxyProviderManager = _Class('NEAppProxyProviderManager')
NETransparentProxyManager = _Class('NETransparentProxyManager')
NEProvider = _Class('NEProvider')
NEAppPushProvider = _Class('NEAppPushProvider')
NEFilterProvider = _Class('NEFilterProvider')
NEFilterPacketProvider = _Class('NEFilterPacketProvider')
NEFilterDataProvider = _Class('NEFilterDataProvider')
NEFilterControlProvider = _Class('NEFilterControlProvider')
NEDNSProxyProvider = _Class('NEDNSProxyProvider')
NETunnelProvider = _Class('NETunnelProvider')
NEPacketTunnelProvider = _Class('NEPacketTunnelProvider')
NEIKEv2PacketTunnelProvider = _Class('NEIKEv2PacketTunnelProvider')
NEAppProxyProvider = _Class('NEAppProxyProvider')
NEAppInfoCache = _Class('NEAppInfoCache')
NEAppInfo = _Class('NEAppInfo')
NEAOVPN = _Class('NEAOVPN')
NEAOVPNException = _Class('NEAOVPNException')
NENetworkRule = _Class('NENetworkRule')
NEProviderXPCListener = _Class('NEProviderXPCListener')
NEExtensionProviderHostContext = _Class('NEExtensionProviderHostContext')
NEExtensionAppPushProviderHostContext = _Class('NEExtensionAppPushProviderHostContext')
NEFilterExtensionProviderHostContext = _Class('NEFilterExtensionProviderHostContext')
NEFilterPacketExtensionProviderHostContext = _Class('NEFilterPacketExtensionProviderHostContext')
NEFilterDataExtensionProviderHostContext = _Class('NEFilterDataExtensionProviderHostContext')
NEFilterControlExtensionProviderHostContext = _Class('NEFilterControlExtensionProviderHostContext')
NEExtensionTunnelProviderHostContext = _Class('NEExtensionTunnelProviderHostContext')
NEExtensionPacketTunnelProviderHostContext = _Class('NEExtensionPacketTunnelProviderHostContext')
NEExtensionAppProxyProviderHostContext = _Class('NEExtensionAppProxyProviderHostContext')
NEExtensionDNSProxyProviderHostContext = _Class('NEExtensionDNSProxyProviderHostContext')
NEExtensionProviderContext = _Class('NEExtensionProviderContext')
NEExtensionAppPushProviderContext = _Class('NEExtensionAppPushProviderContext')
NEFilterExtensionProviderContext = _Class('NEFilterExtensionProviderContext')
NEFilterPacketExtensionProviderContext = _Class('NEFilterPacketExtensionProviderContext')
NEFilterDataExtensionProviderContext = _Class('NEFilterDataExtensionProviderContext')
NEFilterControlExtensionProviderContext = _Class('NEFilterControlExtensionProviderContext')
NEExtensionTunnelProviderContext = _Class('NEExtensionTunnelProviderContext')
NEExtensionPacketTunnelProviderContext = _Class('NEExtensionPacketTunnelProviderContext')
NEExtensionAppProxyProviderContext = _Class('NEExtensionAppProxyProviderContext')
NEExtensionDNSProxyProviderContext = _Class('NEExtensionDNSProxyProviderContext')
NEHasher = _Class('NEHasher')