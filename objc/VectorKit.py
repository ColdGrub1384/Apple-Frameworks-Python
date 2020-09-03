
'''
Classes from the 'VectorKit' framework.
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
    
    
VKLabelNavRouteEta = _Class('VKLabelNavRouteEta')
VKOverlay = _Class('VKOverlay')
VKCameraRegionRestriction = _Class('VKCameraRegionRestriction')
VKImageSourceKey = _Class('VKImageSourceKey')
VKStylesheetVendorResourceManifestTileGroupObserverProxy = _Class('VKStylesheetVendorResourceManifestTileGroupObserverProxy')
VKCameraDelegateMediator = _Class('VKCameraDelegateMediator')
VKManifestTileGroupObserverProxy = _Class('VKManifestTileGroupObserverProxy')
VKClusterFeatureAnnotation = _Class('VKClusterFeatureAnnotation')
VKMuninJunction = _Class('VKMuninJunction')
VKObjectBoundsContext = _Class('VKObjectBoundsContext')
VKLabelNavRoadGraph = _Class('VKLabelNavRoadGraph')
VKLabelNavTileData = _Class('VKLabelNavTileData')
VKLabelNavRoadLabel = _Class('VKLabelNavRoadLabel')
VKViewportInfo = _Class('VKViewportInfo')
VKVectorOverlayPolygon = _Class('VKVectorOverlayPolygon')
VKVectorOverlayPolyline = _Class('VKVectorOverlayPolyline')
VKVectorOverlayData = _Class('VKVectorOverlayData')
VKVectorOverlayPolygonGroup = _Class('VKVectorOverlayPolygonGroup')
VKVectorOverlayCircle = _Class('VKVectorOverlayCircle')
VKVectorOverlayPolylineGroup = _Class('VKVectorOverlayPolylineGroup')
VKMercatorTerrainHeightCache = _Class('VKMercatorTerrainHeightCache')
MDDisplayLayer = _Class('MDDisplayLayer')
VKPuckAnimatorLocationProjector = _Class('VKPuckAnimatorLocationProjector')
VKLabelNavJunction = _Class('VKLabelNavJunction')
MIController = _Class('MIController')
AltTileFetcher = _Class('AltTileFetcher')
RegionalResourceObserver = _Class('RegionalResourceObserver')
GRLResourceGroupObserver = _Class('GRLResourceGroupObserver')
VKTimer = _Class('VKTimer')
VKCustomFeatureDataSourceObserverThunk = _Class('VKCustomFeatureDataSourceObserverThunk')
VKMapSnapshot = _Class('VKMapSnapshot')
VKClientLocalizedStrings = _Class('VKClientLocalizedStrings')
MDARController = _Class('MDARController')
VKGuidanceStepInfo = _Class('VKGuidanceStepInfo')
VKRouteRoadInfo = _Class('VKRouteRoadInfo')
LabelNavRouteLabeler = _Class('LabelNavRouteLabeler')
VKLabelNavRoad = _Class('VKLabelNavRoad')
VKDebugSettings = _Class('VKDebugSettings')
VKGlobeLineContainer = _Class('VKGlobeLineContainer')
VKPolylineOverlay = _Class('VKPolylineOverlay')
VKPolylineOverlayRenderRegion = _Class('VKPolylineOverlayRenderRegion')
VKResourceManager = _Class('VKResourceManager')
GlobeLineContainerDelegate = _Class('GlobeLineContainerDelegate')
VKImage = _Class('VKImage')
VKRouteLine = _Class('VKRouteLine')
VKMapSnapshotCreator = _Class('VKMapSnapshotCreator')
GGLImageCanvas = _Class('GGLImageCanvas')
VKCustomFeature = _Class('VKCustomFeature')
VKLabelExternalIconElement = _Class('VKLabelExternalIconElement')
VKLabelExternalTextElement = _Class('VKLabelExternalTextElement')
VKRouteContext = _Class('VKRouteContext')
VKRoadSignArtwork = _Class('VKRoadSignArtwork')
VKRouteContextObserverThunk = _Class('VKRouteContextObserverThunk')
VKRouteLineObserver = _Class('VKRouteLineObserver')
VKTrafficFeature = _Class('VKTrafficFeature')
VKTrafficSignalFeature = _Class('VKTrafficSignalFeature')
VKRouteAnnotation = _Class('VKRouteAnnotation')
VKTrafficCameraFeature = _Class('VKTrafficCameraFeature')
VKTrafficIncidentFeature = _Class('VKTrafficIncidentFeature')
VKTestIdentifiedMapDataRequester = _Class('VKTestIdentifiedMapDataRequester')
VKTestTileRequester = _Class('VKTestTileRequester')
VKRunningCurve = _Class('VKRunningCurve')
VKRouteWaypointInfo = _Class('VKRouteWaypointInfo')
VKEVChargeStationRouteWaypoint = _Class('VKEVChargeStationRouteWaypoint')
VKPolygonalItemGroup = _Class('VKPolygonalItemGroup')
VKPolygonGroup = _Class('VKPolygonGroup')
VKVenueGroup = _Class('VKVenueGroup')
VKBuildingGroup = _Class('VKBuildingGroup')
VKMuninMarker = _Class('VKMuninMarker')
VKRouteInfo = _Class('VKRouteInfo')
VKAlternateRouteInfo = _Class('VKAlternateRouteInfo')
VKNavContext = _Class('VKNavContext')
VKLabelMarkerShield = _Class('VKLabelMarkerShield')
VKLabelMarkerFeatureHandle = _Class('VKLabelMarkerFeatureHandle')
VKPuckAnimator = _Class('VKPuckAnimator')
VKAnchorWrapper = _Class('VKAnchorWrapper')
LabelNavRouteContextObserverProxy = _Class('LabelNavRouteContextObserverProxy')
VKIconManager = _Class('VKIconManager')
VKIconImage = _Class('VKIconImage')
VKIconModifiers = _Class('VKIconModifiers')
VKNotificationObserver = _Class('VKNotificationObserver')
VKPolylineGroupOverlay = _Class('VKPolylineGroupOverlay')
VKPlatform = _Class('VKPlatform')
VKNavigationPuck = _Class('VKNavigationPuck')
VKMuninRoad = _Class('VKMuninRoad')
VKPolylinePath = _Class('VKPolylinePath')
VKTransitStationPolylinePath = _Class('VKTransitStationPolylinePath')
VKTransitPolylinePath = _Class('VKTransitPolylinePath')
VKLabelExclusionRegion = _Class('VKLabelExclusionRegion')
VKDebugTree = _Class('VKDebugTree')
VKInternalIconManager = _Class('VKInternalIconManager')
VKImageCanvas = _Class('VKImageCanvas')
VKGlobeImageCanvas = _Class('VKGlobeImageCanvas')
VKMapImageCanvas = _Class('VKMapImageCanvas')
VKGestureCameraBehavior = _Class('VKGestureCameraBehavior')
VKDetachedNavGestureCameraBehavior = _Class('VKDetachedNavGestureCameraBehavior')
VKAttachedNavGestureCameraBehavior = _Class('VKAttachedNavGestureCameraBehavior')
VKARGestureCameraBehavior = _Class('VKARGestureCameraBehavior')
VKMapGestureCameraController = _Class('VKMapGestureCameraController')
VKGlobeGestureCameraController = _Class('VKGlobeGestureCameraController')
VKFeatureMarker = _Class('VKFeatureMarker')
VKVenueBuildingFeatureMarker = _Class('VKVenueBuildingFeatureMarker')
VKVenueFeatureMarker = _Class('VKVenueFeatureMarker')
VKLabelMarker = _Class('VKLabelMarker')
VKStateCaptureHandler = _Class('VKStateCaptureHandler')
VKRouteEtaDescription = _Class('VKRouteEtaDescription')
VKCameraController = _Class('VKCameraController')
VKNavCameraController = _Class('VKNavCameraController')
VKMuninCameraController = _Class('VKMuninCameraController')
VKAnnotationTrackingCameraController = _Class('VKAnnotationTrackingCameraController')
VKMapAnnotationTrackingCameraController = _Class('VKMapAnnotationTrackingCameraController')
VKGlobeAnnotationTrackingCameraController = _Class('VKGlobeAnnotationTrackingCameraController')
VKScreenCameraController = _Class('VKScreenCameraController')
VKGlobeCameraController = _Class('VKGlobeCameraController')
VKARCameraController = _Class('VKARCameraController')
VKMapCameraController = _Class('VKMapCameraController')
ReachabilityCallbacker = _Class('ReachabilityCallbacker')
VKTransitLineMarker = _Class('VKTransitLineMarker')
VKDebugTreeNode = _Class('VKDebugTreeNode')
VKDebugTreePropertyNode = _Class('VKDebugTreePropertyNode')
VKDebugTreeDataNode = _Class('VKDebugTreeDataNode')
VKMapModel = _Class('VKMapModel')
VKAnimation = _Class('VKAnimation')
VKCompoundAnimation = _Class('VKCompoundAnimation')
VKDynamicAnimation = _Class('VKDynamicAnimation')
VKQuickDynamicAnimation = _Class('VKQuickDynamicAnimation')
VKTimedAnimation = _Class('VKTimedAnimation')
VKScreenCanvas = _Class('VKScreenCanvas')
VKClassicGlobeCanvas = _Class('VKClassicGlobeCanvas')
VKMapCanvas = _Class('VKMapCanvas')
VKViewVolume = _Class('VKViewVolume')
VKFootprint = _Class('VKFootprint')
RouteRenderLayerObserverProxy = _Class('RouteRenderLayerObserverProxy')
VKCamera = _Class('VKCamera')
VKSceneConfiguration = _Class('VKSceneConfiguration')
VKSharedResourcesManager = _Class('VKSharedResourcesManager')
VKSharedResources = _Class('VKSharedResources')
VKPGenericShieldVariant = _Class('VKPGenericShieldVariant')
VKPGenericShieldStylePack = _Class('VKPGenericShieldStylePack')
VKPGenericShield = _Class('VKPGenericShield')
VKPShieldIndexTextEntry = _Class('VKPShieldIndexTextEntry')
VKPShieldIndexEntry = _Class('VKPShieldIndexEntry')
VKPShieldIndex = _Class('VKPShieldIndex')
VKPShieldIndexVariantEntry = _Class('VKPShieldIndexVariantEntry')
VKPGenericShieldStyleInfo = _Class('VKPGenericShieldStyleInfo')
VKPShieldVariant = _Class('VKPShieldVariant')
VKPShieldPack = _Class('VKPShieldPack')
VKPShield = _Class('VKPShield')
VKPTextureAtlas = _Class('VKPTextureAtlas')
VKPIconPack = _Class('VKPIconPack')
VKPIcon = _Class('VKPIcon')
MetalLayer = _Class('MetalLayer')
VKMapView = _Class('VKMapView')
VKInternedString = _Class('VKInternedString')