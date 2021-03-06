'''
Classes from the 'MapKit' framework.
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

    
_MKMultiPartLabelCacheKey = _Class('_MKMultiPartLabelCacheKey')
_MKKVOProxy = _Class('_MKKVOProxy')
MKMapSnapshotter = _Class('MKMapSnapshotter')
MKBarViewOptions = _Class('MKBarViewOptions')
MKJunction = _Class('MKJunction')
_MKJunctionElement = _Class('_MKJunctionElement')
MKUserLocationAnnotationViewProxy = _Class('MKUserLocationAnnotationViewProxy')
MKTransitIcon = _Class('MKTransitIcon')
MKTransitShield = _Class('MKTransitShield')
MKTransitArtwork = _Class('MKTransitArtwork')
MKWebBridge = _Class('MKWebBridge')
MKPlaceCollectionMapItem = _Class('MKPlaceCollectionMapItem')
MKMapSnapshot = _Class('MKMapSnapshot')
_MKPlaceReservationInfo = _Class('_MKPlaceReservationInfo')
MKMapSnapshotFeatureAnnotation = _Class('MKMapSnapshotFeatureAnnotation')
MKMuninGroundViewInfo = _Class('MKMuninGroundViewInfo')
MKLocalSearchKeypressMetrics = _Class('MKLocalSearchKeypressMetrics')
MKThrottledGate = _Class('MKThrottledGate')
MKMapSnapshotOptions = _Class('MKMapSnapshotOptions')
MKGroupedPlacesSnapshotter = _Class('MKGroupedPlacesSnapshotter')
MKVKImageSourceKeyImageBuilder = _Class('MKVKImageSourceKeyImageBuilder')
MKVKImageSourceKeyImageResult = _Class('MKVKImageSourceKeyImageResult')
MKVKImageSourceCalculationParameters = _Class('MKVKImageSourceCalculationParameters')
MKInfoCardThemeManager = _Class('MKInfoCardThemeManager')
MKTransitItemReferenceDateUpdater = _Class('MKTransitItemReferenceDateUpdater')
MKTransitMapItemUpdater = _Class('MKTransitMapItemUpdater')
_MKPinAnnotationViewImageCacheKey = _Class('_MKPinAnnotationViewImageCacheKey')
_MKPinAnnotationViewImageCache = _Class('_MKPinAnnotationViewImageCache')
MKTileOverlayRequesterOp = _Class('MKTileOverlayRequesterOp')
MKTileOverlayTile = _Class('MKTileOverlayTile')
MKTileOverlay = _Class('MKTileOverlay')
MKPlaceCollectionsLogicController = _Class('MKPlaceCollectionsLogicController')
MKAutocompleteAnalyticsState = _Class('MKAutocompleteAnalyticsState')
MKAutocompleteAnalyticsProvider = _Class('MKAutocompleteAnalyticsProvider')
MKMapItemPhoto = _Class('MKMapItemPhoto')
MKPlaceHoursViewHelper = _Class('MKPlaceHoursViewHelper')
MKBrowseCategoryItem = _Class('MKBrowseCategoryItem')
MKDirectionsRequest = _Class('MKDirectionsRequest')
MKClusterAnnotation = _Class('MKClusterAnnotation')
_MXSerialQueue = _Class('_MXSerialQueue')
MKUserLocation = _Class('MKUserLocation')
MKUserLocationInternal = _Class('MKUserLocationInternal')
MKUserLocationAnnotation = _Class('MKUserLocationAnnotation')
MKRotationFilter = _Class('MKRotationFilter')
MKLocalPointsOfInterestRequest = _Class('MKLocalPointsOfInterestRequest')
MKUserLocationHeadingLayerFactory = _Class('MKUserLocationHeadingLayerFactory')
_MKCustomFeatureStore = _Class('_MKCustomFeatureStore')
MKPlaceCollectionsPublisherIconManager = _Class('MKPlaceCollectionsPublisherIconManager')
MKPublisherIcon = _Class('MKPublisherIcon')
MKHapticEngine = _Class('MKHapticEngine')
MKETAProvider = _Class('MKETAProvider')
MKPlaceCollectionsSizeController = _Class('MKPlaceCollectionsSizeController')
MKURLSerializer = _Class('MKURLSerializer')
MKDirections = _Class('MKDirections')
MKApplicationStateMonitor = _Class('MKApplicationStateMonitor')
MKCALayerCompletionDelegate = _Class('MKCALayerCompletionDelegate')
MKLaneDirectionCollisionCalculator = _Class('MKLaneDirectionCollisionCalculator')
_mkMapServiceWalletMerchantTicket = _Class('_mkMapServiceWalletMerchantTicket')
MKWalletMerchantResponse = _Class('MKWalletMerchantResponse')
MKWalletMerchantStylingInfo = _Class('MKWalletMerchantStylingInfo')
MKWalletMerchantLookupRequest = _Class('MKWalletMerchantLookupRequest')
MKPlaceCollectionViewModel = _Class('MKPlaceCollectionViewModel')
_MKCompassViewStyleParameter = _Class('_MKCompassViewStyleParameter')
_MKCompassViewSizeParameter = _Class('_MKCompassViewSizeParameter')
MKPlaceInfoRow = _Class('MKPlaceInfoRow')
MKMuninEntryPoint = _Class('MKMuninEntryPoint')
MKRoundingByteCountFormatter = _Class('MKRoundingByteCountFormatter')
MKPlaceEncyclopedicTextItem = _Class('MKPlaceEncyclopedicTextItem')
GEOEncyclopedicInfoUserLocation = _Class('GEOEncyclopedicInfoUserLocation')
MKMuninGestureController = _Class('MKMuninGestureController')
_MKUserLocationViewImageProvider = _Class('_MKUserLocationViewImageProvider')
_MXExtensionManager = _Class('_MXExtensionManager')
_MXExtensionLookupPolicy = _Class('_MXExtensionLookupPolicy')
MKTrafficSupport = _Class('MKTrafficSupport')
MKWebMessage = _Class('MKWebMessage')
MKPhotoGalleryTransitionAnimator = _Class('MKPhotoGalleryTransitionAnimator')
MKTransitDeparturesDataProvider = _Class('MKTransitDeparturesDataProvider')
_MKLocalizedHoursBuilder = _Class('_MKLocalizedHoursBuilder')
_MKContactPlaceItem = _Class('_MKContactPlaceItem')
_MKMapItemPlaceItem = _Class('_MKMapItemPlaceItem')
MKUGCCallToActionViewAppearance = _Class('MKUGCCallToActionViewAppearance')
MKRatingStringBuilder = _Class('MKRatingStringBuilder')
MKWalletRAPReport = _Class('MKWalletRAPReport')
_MKURLBuilder = _Class('_MKURLBuilder')
MKSpatialCollider = _Class('MKSpatialCollider')
_MKSpatialColliderPairSet = _Class('_MKSpatialColliderPairSet')
MKLocalSearchSection = _Class('MKLocalSearchSection')
_MKMultiPartLabelMetrics = _Class('_MKMultiPartLabelMetrics')
MKTextItemViewModel = _Class('MKTextItemViewModel')
MKThirdPartyRatingStringBuilder = _Class('MKThirdPartyRatingStringBuilder')
MKLocalSearchCompleter = _Class('MKLocalSearchCompleter')
MKSiriInteraction = _Class('MKSiriInteraction')
MKAllRouteETAsManager = _Class('MKAllRouteETAsManager')
_MKQuickRouteManager = _Class('_MKQuickRouteManager')
_MKRouteETAFetcher = _Class('_MKRouteETAFetcher')
_MKRouteETA = _Class('_MKRouteETA')
MKTransitDeparturesDataSource = _Class('MKTransitDeparturesDataSource')
_GEOTransitLineMarker = _Class('_GEOTransitLineMarker')
MKTransitIncidentStringProvider = _Class('MKTransitIncidentStringProvider')
_MXExtension = _Class('_MXExtension')
_MKPolygonGeoRegion = _Class('_MKPolygonGeoRegion')
MKLocalSearchResponse = _Class('MKLocalSearchResponse')
MKPlaceCollectionImageProvider = _Class('MKPlaceCollectionImageProvider')
MKWebBridgeConfiguration = _Class('MKWebBridgeConfiguration')
_MKLocalSearchExternalTransitLookupParameters = _Class('_MKLocalSearchExternalTransitLookupParameters')
_MKLocalSearchMerchantParameters = _Class('_MKLocalSearchMerchantParameters')
MKLocalSearchRequest = _Class('MKLocalSearchRequest')
MKLocalSearch = _Class('MKLocalSearch')
_MXIntentResponseObserverProxy = _Class('_MXIntentResponseObserverProxy')
MKTransitDepartureServiceGapFormatterResult = _Class('MKTransitDepartureServiceGapFormatterResult')
MKTransitDepartureServiceGapFormatter = _Class('MKTransitDepartureServiceGapFormatter')
MKMapItemMetadata = _Class('MKMapItemMetadata')
MKMapCamera = _Class('MKMapCamera')
MKMapItem = _Class('MKMapItem')
_MKMapItemUserRatingSnippetTip = _Class('_MKMapItemUserRatingSnippetTip')
_MKMapItemUserRatingSnippetReview = _Class('_MKMapItemUserRatingSnippetReview')
MKMapCameraZoomRange = _Class('MKMapCameraZoomRange')
MKMapAttributionImage = _Class('MKMapAttributionImage')
MKMapAttribution = _Class('MKMapAttribution')
_MKDataHeaderModel = _Class('_MKDataHeaderModel')
_MKLineHeaderModel = _Class('_MKLineHeaderModel')
_MKTokenAttributedString = _Class('_MKTokenAttributedString')
MKSystemController = _Class('MKSystemController')
_MKFakeNil = _Class('_MKFakeNil')
_MXExtensionProvider = _Class('_MXExtensionProvider')
_MXAssetStorage = _Class('_MXAssetStorage')
_MXExtensionServiceCenter = _Class('_MXExtensionServiceCenter')
_MXExtensionContainingAppProxy = _Class('_MXExtensionContainingAppProxy')
_MXExtensionDispatchCenter = _Class('_MXExtensionDispatchCenter')
_MXExtensionMatchingMerger = _Class('_MXExtensionMatchingMerger')
_MXBundleBlacklistEntry = _Class('_MXBundleBlacklistEntry')
_MKLocationShifter = _Class('_MKLocationShifter')
MKWebViewFactoryItem = _Class('MKWebViewFactoryItem')
MKFirstPartyRatingStringBuilder = _Class('MKFirstPartyRatingStringBuilder')
MKQuadTrie = _Class('MKQuadTrie')
MKMapSnapshotCustomFeatureAnnotation = _Class('MKMapSnapshotCustomFeatureAnnotation')
MKThreadContext = _Class('MKThreadContext')
_MXVersion = _Class('_MXVersion')
MKUsageCounter = _Class('MKUsageCounter')
_MKMultiPolygonGeoRegion = _Class('_MKMultiPolygonGeoRegion')
_MKAnnotationViewCustomFeatureAnnotation = _Class('_MKAnnotationViewCustomFeatureAnnotation')
MKAnnotationViewInternal = _Class('MKAnnotationViewInternal')
MKAnnotationManager = _Class('MKAnnotationManager')
MKPlaceActivityProvider = _Class('MKPlaceActivityProvider')
MKMuninLinkPresentationActivityProvider = _Class('MKMuninLinkPresentationActivityProvider')
MKMuninURLActivityProvider = _Class('MKMuninURLActivityProvider')
MKMuninTextActivityProvider = _Class('MKMuninTextActivityProvider')
MKPlaceLocVCardActivityProvider = _Class('MKPlaceLocVCardActivityProvider')
MKPlaceMapItemActivityProvider = _Class('MKPlaceMapItemActivityProvider')
MKPlaceURLActivityProvider = _Class('MKPlaceURLActivityProvider')
MKPlaceTextActivityProvider = _Class('MKPlaceTextActivityProvider')
MKRouteActivityProvider = _Class('MKRouteActivityProvider')
MKRouteURLActivityProvider = _Class('MKRouteURLActivityProvider')
MKRouteTextActivityProvider = _Class('MKRouteTextActivityProvider')
MKRouteLinkPresentationActivityProvider = _Class('MKRouteLinkPresentationActivityProvider')
MKPlaceLinkPresentationActivityProvider = _Class('MKPlaceLinkPresentationActivityProvider')
MKPlaceViewStyleProvider = _Class('MKPlaceViewStyleProvider')
_MKPlaceAttributionLabel = _Class('_MKPlaceAttributionLabel')
MKMapService = _Class('MKMapService')
_MKAllCollectionsViewTicket = _Class('_MKAllCollectionsViewTicket')
_MKCuratedCollectionItemsTicket = _Class('_MKCuratedCollectionItemsTicket')
_MKCuratedCollectionTicket = _Class('_MKCuratedCollectionTicket')
_MKPublisherViewTicket = _Class('_MKPublisherViewTicket')
_MKSearchHomeTicket = _Class('_MKSearchHomeTicket')
_MKSpatialPlaceLookupTicket = _Class('_MKSpatialPlaceLookupTicket')
_MKTransitLineTicket = _Class('_MKTransitLineTicket')
_MKSearchFieldPlaceholderTicket = _Class('_MKSearchFieldPlaceholderTicket')
_MKCategoriesTicket = _Class('_MKCategoriesTicket')
_MKFeedbackReportTicket = _Class('_MKFeedbackReportTicket')
_MKTicket = _Class('_MKTicket')
_MKSearchTicket = _Class('_MKSearchTicket')
MKPlaceActionManager = _Class('MKPlaceActionManager')
MKPlaceCardActionItem = _Class('MKPlaceCardActionItem')
_MKRoutingAppCoverageRegions = _Class('_MKRoutingAppCoverageRegions')
_MKSortedDepartureCollection = _Class('_MKSortedDepartureCollection')
MKFontManager = _Class('MKFontManager')
_MXExtensionRequestDispatcher = _Class('_MXExtensionRequestDispatcher')
_MXExtensionInternalStreamingServiceRequestDispatcher = _Class('_MXExtensionInternalStreamingServiceRequestDispatcher')
_MXExtensionInternalServiceRequestDispatcher = _Class('_MXExtensionInternalServiceRequestDispatcher')
MKAppLaunchController = _Class('MKAppLaunchController')
_MKZoomingGestureControlConfiguration = _Class('_MKZoomingGestureControlConfiguration')
MKMapsSuggestionsPredictor = _Class('MKMapsSuggestionsPredictor')
_MKDirectionalArrowRecognizer = _Class('_MKDirectionalArrowRecognizer')
MKMapGestureController = _Class('MKMapGestureController')
MKPOIEnrichmentAvailibility = _Class('MKPOIEnrichmentAvailibility')
_MKIconDiskCache = _Class('_MKIconDiskCache')
MKIconManager = _Class('MKIconManager')
MKRouteContextBuilder = _Class('MKRouteContextBuilder')
MKServerFormattedString = _Class('MKServerFormattedString')
MKServerFormattedStringParameters = _Class('MKServerFormattedStringParameters')
MKMapItemMetadataRequester = _Class('MKMapItemMetadataRequester')
MKMapItemMetadataRequest = _Class('MKMapItemMetadataRequest')
MKMapItemMetadataImageRequest = _Class('MKMapItemMetadataImageRequest')
_MKTransitInactiveLine = _Class('_MKTransitInactiveLine')
_MKPlaceActionButtonController = _Class('_MKPlaceActionButtonController')
_MKUserTrackingButtonController = _Class('_MKUserTrackingButtonController')
MKWebViewFactory = _Class('MKWebViewFactory')
MKPlaceholderGridCache = _Class('MKPlaceholderGridCache')
MKPointOfInterestFilter = _Class('MKPointOfInterestFilter')
MKURLContext = _Class('MKURLContext')
MKTransitSectionController = _Class('MKTransitSectionController')
MKTransitDeparturesSectionController = _Class('MKTransitDeparturesSectionController')
MKTransitInactiveLinesSectionController = _Class('MKTransitInactiveLinesSectionController')
MKSizedTransitArtwork = _Class('MKSizedTransitArtwork')
_MXExtensionService = _Class('_MXExtensionService')
_MXExtensionRequestReceipt = _Class('_MXExtensionRequestReceipt')
MKArtworkDataSourceCache = _Class('MKArtworkDataSourceCache')
MKWhenSizedBlock = _Class('MKWhenSizedBlock')
MKMapItemIdentifier = _Class('MKMapItemIdentifier')
MKCuratedCollectionsPlacecardAnalyticsManager = _Class('MKCuratedCollectionsPlacecardAnalyticsManager')
_MKPlaceCardDraggableContent = _Class('_MKPlaceCardDraggableContent')
MKTransitArtworkManager = _Class('MKTransitArtworkManager')
_MKMultiPartStringComponent = _Class('_MKMultiPartStringComponent')
MKWebViewMessageHandlerProxy = _Class('MKWebViewMessageHandlerProxy')
MKWebContentBlocker = _Class('MKWebContentBlocker')
MKETAResponse = _Class('MKETAResponse')
MKShape = _Class('MKShape')
MKMultiPolygon = _Class('MKMultiPolygon')
MKMultiPolyline = _Class('MKMultiPolyline')
MKCircle = _Class('MKCircle')
MKPointAnnotation = _Class('MKPointAnnotation')
MKMultiPoint = _Class('MKMultiPoint')
MKPolygon = _Class('MKPolygon')
MKPolyline = _Class('MKPolyline')
MKGeodesicPolyline = _Class('MKGeodesicPolyline')
MKRouteStepPolyline = _Class('MKRouteStepPolyline')
MKRoutePolyline = _Class('MKRoutePolyline')
MKRouteStep = _Class('MKRouteStep')
MKRoute = _Class('MKRoute')
MKDirectionsResponse = _Class('MKDirectionsResponse')
_MKURLHandler = _Class('_MKURLHandler')
MKOverlayRenderer = _Class('MKOverlayRenderer')
MKTileOverlayRenderer = _Class('MKTileOverlayRenderer')
MKOverlayPathRenderer = _Class('MKOverlayPathRenderer')
MKPolygonRenderer = _Class('MKPolygonRenderer')
MKCircleRenderer = _Class('MKCircleRenderer')
MKMultiPolylineRenderer = _Class('MKMultiPolylineRenderer')
MKMultiPolygonRenderer = _Class('MKMultiPolygonRenderer')
MKPolylineRenderer = _Class('MKPolylineRenderer')
MKGradientPolylineRenderer = _Class('MKGradientPolylineRenderer')
MKTransitSectionPagingFilter = _Class('MKTransitSectionPagingFilter')
_MKMapItemAttribution = _Class('_MKMapItemAttribution')
_MKMapItemReviewsAttribution = _Class('_MKMapItemReviewsAttribution')
_MKMapItemPhotosAttribution = _Class('_MKMapItemPhotosAttribution')
_MKMapItemPlaceAttribution = _Class('_MKMapItemPlaceAttribution')
_MKMapItemAttributionProviderLogoImageCache = _Class('_MKMapItemAttributionProviderLogoImageCache')
MKReverseGeocoderInternal = _Class('MKReverseGeocoderInternal')
MKReverseGeocoder = _Class('MKReverseGeocoder')
MKTransitItemIncidentsController = _Class('MKTransitItemIncidentsController')
MKLocationManagerSingleUpdater = _Class('MKLocationManagerSingleUpdater')
MKLocationManager = _Class('MKLocationManager')
MKCuratedCollectionsTestManager = _Class('MKCuratedCollectionsTestManager')
MKCoreLocationProvider = _Class('MKCoreLocationProvider')
MKBlockBasedSnapshotRequester = _Class('MKBlockBasedSnapshotRequester')
MKMapSnapshotRequest = _Class('MKMapSnapshotRequest')
MKMapSnapshotCreator = _Class('MKMapSnapshotCreator')
MKPriorityToIndexMap = _Class('MKPriorityToIndexMap')
MKMapCameraBoundary = _Class('MKMapCameraBoundary')
_MKURLParser = _Class('_MKURLParser')
MKURLParser = _Class('MKURLParser')
MKCollectionStorageRefiner = _Class('MKCollectionStorageRefiner')
MKTransitInfoPreload = _Class('MKTransitInfoPreload')
MKTransitInfoPreloader = _Class('MKTransitInfoPreloader')
MKPlacePublisherRefiner = _Class('MKPlacePublisherRefiner')
MKPlaceCuratedCollectionRefiner = _Class('MKPlaceCuratedCollectionRefiner')
_MKMarkerStyle = _Class('_MKMarkerStyle')
MKMultiPartAttributedString = _Class('MKMultiPartAttributedString')
_MKMapViewSuspendedEffectsToken = _Class('_MKMapViewSuspendedEffectsToken')
MKMapViewInternal = _Class('MKMapViewInternal')
MKMapViewLabelMarkerState = _Class('MKMapViewLabelMarkerState')
MKLocalSearchCompletion = _Class('MKLocalSearchCompletion')
MKSearchCompletion = _Class('MKSearchCompletion')
MKClipServices = _Class('MKClipServices')
MKAppleMediaServices = _Class('MKAppleMediaServices')
MKGeoJSONFeature = _Class('MKGeoJSONFeature')
MKGeoJSONDecoder = _Class('MKGeoJSONDecoder')
MKAppImageManager = _Class('MKAppImageManager')
_MKAppImageManagerContainer = _Class('_MKAppImageManagerContainer')
MKFirstPartyRatingFormatter = _Class('MKFirstPartyRatingFormatter')
_MKPlaceBusinessInfoItem = _Class('_MKPlaceBusinessInfoItem')
MKPlaceReviewAvatarGenerator = _Class('MKPlaceReviewAvatarGenerator')
MKPlaceBatchController = _Class('MKPlaceBatchController')
_MKMotionEffect = _Class('_MKMotionEffect')
_MKAnnotationViewAnchor = _Class('_MKAnnotationViewAnchor')
MKPlacemark = _Class('MKPlacemark')
_MKLabelMarkerItem = _Class('_MKLabelMarkerItem')
MKTileOverlayRequester = _Class('MKTileOverlayRequester')
MKSearchFoundationResult = _Class('MKSearchFoundationResult')
MKSearchFoundationActionItem = _Class('MKSearchFoundationActionItem')
MKSearchFoundationRichText = _Class('MKSearchFoundationRichText')
MKSearchFoundationBusinessHoursAndDistanceRichText = _Class('MKSearchFoundationBusinessHoursAndDistanceRichText')
MKSearchFoundationBusinessReviewRichText = _Class('MKSearchFoundationBusinessReviewRichText')
MKSearchFoundationImage = _Class('MKSearchFoundationImage')
MKFixedToTopCollectionViewFlowLayout = _Class('MKFixedToTopCollectionViewFlowLayout')
MKImageTextAttachment = _Class('MKImageTextAttachment')
MKEmptyTextAttachment = _Class('MKEmptyTextAttachment')
_MXExtensionContext = _Class('_MXExtensionContext')
_MXExtensionVendorContext = _Class('_MXExtensionVendorContext')
_MXExtensionHostContext = _Class('_MXExtensionHostContext')
MKUserTrackingBarButtonItem = _Class('MKUserTrackingBarButtonItem')
_MKOneHandedZoomGestureRecognizer = _Class('_MKOneHandedZoomGestureRecognizer')
_MKUserInteractionGestureRecognizer = _Class('_MKUserInteractionGestureRecognizer')
_MKConditionalPanGestureRecognizer = _Class('_MKConditionalPanGestureRecognizer')
_MKConditionalPanTiltGestureRecognizer = _Class('_MKConditionalPanTiltGestureRecognizer')
_MKConditionalPanZoomGestureRecognizer = _Class('_MKConditionalPanZoomGestureRecognizer')
_MKConditionalPanRotationGestureRecognizer = _Class('_MKConditionalPanRotationGestureRecognizer')
_MKZoomingPanGestureRecognizer = _Class('_MKZoomingPanGestureRecognizer')
MKTiltGestureRecognizer = _Class('MKTiltGestureRecognizer')
MKVariableDelayTapRecognizer = _Class('MKVariableDelayTapRecognizer')
_MKPuckAccuracyLayer = _Class('_MKPuckAccuracyLayer')
MKLayer = _Class('MKLayer')
_MKLegendString = _Class('_MKLegendString')
_MKMapLayerHostingLayer = _Class('_MKMapLayerHostingLayer')
_MKResizingLayer = _Class('_MKResizingLayer')
_MKCalloutLayer = _Class('_MKCalloutLayer')
_MKMuninLayerHostingLayer = _Class('_MKMuninLayerHostingLayer')
MKUserLocationHeadingConeLayer = _Class('MKUserLocationHeadingConeLayer')
MKUserLocationHeadingArrowLayer = _Class('MKUserLocationHeadingArrowLayer')
MKDistanceFormatter = _Class('MKDistanceFormatter')
_MKCalloutAccessoryWrapperView = _Class('_MKCalloutAccessoryWrapperView')
_MKSmallCalloutContainerView = _Class('_MKSmallCalloutContainerView')
MKSmallCalloutView = _Class('MKSmallCalloutView')
MKTransitIncidentItemCellBackgroundView = _Class('MKTransitIncidentItemCellBackgroundView')
MKStarRatingAndLabelView = _Class('MKStarRatingAndLabelView')
MKStarRatingView = _Class('MKStarRatingView')
MKPlaceCompleteHoursView = _Class('MKPlaceCompleteHoursView')
MKPlaceHoursView = _Class('MKPlaceHoursView')
MKPlaceServiceHoursView = _Class('MKPlaceServiceHoursView')
_MKBezierPathView = _Class('_MKBezierPathView')
MKAnnotationContainerView = _Class('MKAnnotationContainerView')
MKCompassView = _Class('MKCompassView')
MKMuninContainerView = _Class('MKMuninContainerView')
_MKResultView = _Class('_MKResultView')
MKScaleView = _Class('MKScaleView')
_MKScaleUnitsView = _Class('_MKScaleUnitsView')
MKAddPhotoBadgeView = _Class('MKAddPhotoBadgeView')
_MKStaticMapView = _Class('_MKStaticMapView')
MKMapItemView = _Class('MKMapItemView')
MKPlacePhotoGalleryAttributionView = _Class('MKPlacePhotoGalleryAttributionView')
MKUserTrackingButton = _Class('MKUserTrackingButton')
MKMultiPartLabel = _Class('MKMultiPartLabel')
MKThemeMultiPartLabel = _Class('MKThemeMultiPartLabel')
MKQuickLinkItemView = _Class('MKQuickLinkItemView')
MKCompassButton = _Class('MKCompassButton')
MKTransitItemIncidentView = _Class('MKTransitItemIncidentView')
MKPlaceCardActionsRowView = _Class('MKPlaceCardActionsRowView')
MKBarView = _Class('MKBarView')
MKInfoCardLoadingView = _Class('MKInfoCardLoadingView')
MKPhotoSmallAttributionView = _Class('MKPhotoSmallAttributionView')
_MKStackingPlaceholderView = _Class('_MKStackingPlaceholderView')
MKUGCCallToActionLikeDislikeAccessoryView = _Class('MKUGCCallToActionLikeDislikeAccessoryView')
_MKMapLayerHostingView = _Class('_MKMapLayerHostingView')
MKBasicMapView = _Class('MKBasicMapView')
MKPictureItemView = _Class('MKPictureItemView')
_MKGradientView = _Class('_MKGradientView')
_MKZoomSliderView = _Class('_MKZoomSliderView')
MKTextItemView = _Class('MKTextItemView')
MKAttributionLabel = _Class('MKAttributionLabel')
MKExpandingLabel = _Class('MKExpandingLabel')
MKPhotoBigAttributionView = _Class('MKPhotoBigAttributionView')
MKFirstPartyPhotoBigAttributionView = _Class('MKFirstPartyPhotoBigAttributionView')
MKThirdPartyPhotoBigAttributionView = _Class('MKThirdPartyPhotoBigAttributionView')
MKMuninContainerBadgeView = _Class('MKMuninContainerBadgeView')
MKUGCCallToActionEditAccessoryView = _Class('MKUGCCallToActionEditAccessoryView')
_MKEnvironmentLabel = _Class('_MKEnvironmentLabel')
MKPlatterView = _Class('MKPlatterView')
MKOverlayContainerView = _Class('MKOverlayContainerView')
MKCollectionsCarouselView = _Class('MKCollectionsCarouselView')
MKOverlayView = _Class('MKOverlayView')
MKOverlayPathView = _Class('MKOverlayPathView')
MKPolylineView = _Class('MKPolylineView')
MKPolygonView = _Class('MKPolygonView')
MKCircleView = _Class('MKCircleView')
MKUGCCallToActionAddPhotosAccessoryView = _Class('MKUGCCallToActionAddPhotosAccessoryView')
_MKStackView = _Class('_MKStackView')
MKPlaceSectionView = _Class('MKPlaceSectionView')
MKCalloutView = _Class('MKCalloutView')
_MKBalloonCalloutView = _Class('_MKBalloonCalloutView')
MKStandardCalloutView = _Class('MKStandardCalloutView')
_MKStandardCalloutMaskView = _Class('_MKStandardCalloutMaskView')
_MKCalloutContentView = _Class('_MKCalloutContentView')
_MKStackingViewControllerHeaderView = _Class('_MKStackingViewControllerHeaderView')
_MKUIViewControllerRootView = _Class('_MKUIViewControllerRootView')
_MKStackingContentView = _Class('_MKStackingContentView')
_MKUIViewControllerClickableRootView = _Class('_MKUIViewControllerClickableRootView')
_MKPlaceInlineMapContentView = _Class('_MKPlaceInlineMapContentView')
_MKPlacePoisInlineMapContentView = _Class('_MKPlacePoisInlineMapContentView')
MKAnnotationView = _Class('MKAnnotationView')
MKUserLocationView = _Class('MKUserLocationView')
_MKPuckAnnotationView = _Class('_MKPuckAnnotationView')
_MKUserLocationView = _Class('_MKUserLocationView')
MKModernUserLocationView = _Class('MKModernUserLocationView')
_MKUserLocationInternalView = _Class('_MKUserLocationInternalView')
_MKLabelMarkerView = _Class('_MKLabelMarkerView')
_MKBalloonLabelMarkerView = _Class('_MKBalloonLabelMarkerView')
MKPinAnnotationView = _Class('MKPinAnnotationView')
MKMarkerAnnotationView = _Class('MKMarkerAnnotationView')
MKMapView = _Class('MKMapView')
MKScrollContainerView = _Class('MKScrollContainerView')
_MKMapContentView = _Class('_MKMapContentView')
MKMuninView = _Class('MKMuninView')
_MKMuninLayerHostingView = _Class('_MKMuninLayerHostingView')
MKViewWithHairline = _Class('MKViewWithHairline')
MKPlaceSectionItemView = _Class('MKPlaceSectionItemView')
MKOverallRatingHeaderView = _Class('MKOverallRatingHeaderView')
MKRatingPlatterView = _Class('MKRatingPlatterView')
MKPlaceSectionHeaderView = _Class('MKPlaceSectionHeaderView')
MKPlaceSectionRowView = _Class('MKPlaceSectionRowView')
MKPlaceTextBlockCell = _Class('MKPlaceTextBlockCell')
MKServiceHoursRow = _Class('MKServiceHoursRow')
MKPlaceReservationRowView = _Class('MKPlaceReservationRowView')
MKPlaceEncyclopedicRowView = _Class('MKPlaceEncyclopedicRowView')
MKPlaceEncyclopedicFactoidView = _Class('MKPlaceEncyclopedicFactoidView')
MKPlaceTextCell = _Class('MKPlaceTextCell')
MKUGCCallToActionView = _Class('MKUGCCallToActionView')
MKPlaceInfoSuggestAnEditRowView = _Class('MKPlaceInfoSuggestAnEditRowView')
MKPlaceInfoContactRowView = _Class('MKPlaceInfoContactRowView')
MKPlaceInfoBusinessMessageRowView = _Class('MKPlaceInfoBusinessMessageRowView')
MKPlaceInfoPostalAddressRowView = _Class('MKPlaceInfoPostalAddressRowView')
MKPlaceInfoEmailRowView = _Class('MKPlaceInfoEmailRowView')
MKPlaceInfoURLRowView = _Class('MKPlaceInfoURLRowView')
MKPlaceInfoPhoneNumberView = _Class('MKPlaceInfoPhoneNumberView')
MKPlaceAttributionCell = _Class('MKPlaceAttributionCell')
MKPlaceDirectionsCell = _Class('MKPlaceDirectionsCell')
MKOfficialAppView = _Class('MKOfficialAppView')
MKPlaceHoursDayRow = _Class('MKPlaceHoursDayRow')
MKPlaceCardActionSectionView = _Class('MKPlaceCardActionSectionView')
_MKPlaceBusinessInfoRow = _Class('_MKPlaceBusinessInfoRow')
MKPlaceReviewsViewCell = _Class('MKPlaceReviewsViewCell')
MKMuninBumpFlash = _Class('MKMuninBumpFlash')
MKIncidentFooterView = _Class('MKIncidentFooterView')
MKPlacePhotoView = _Class('MKPlacePhotoView')
MKBrowseCategoryCollectionView = _Class('MKBrowseCategoryCollectionView')
MKNearestStationLoadingCell = _Class('MKNearestStationLoadingCell')
MKNearestStationCell = _Class('MKNearestStationCell')
MKNearestStationErrorCell = _Class('MKNearestStationErrorCell')
MKTableViewCell = _Class('MKTableViewCell')
MKIncidentDetailCell = _Class('MKIncidentDetailCell')
MKIncidentExtendedDetailCell = _Class('MKIncidentExtendedDetailCell')
MKCustomSeparatorTableViewCell = _Class('MKCustomSeparatorTableViewCell')
MKTransitDeparturesSectionFooterView = _Class('MKTransitDeparturesSectionFooterView')
MKTransitDeparturesSectionHeaderView = _Class('MKTransitDeparturesSectionHeaderView')
MKTransitDeparturesCell = _Class('MKTransitDeparturesCell')
_MKTransitConnectionCell = _Class('_MKTransitConnectionCell')
MKTransitLoadingTableViewCell = _Class('MKTransitLoadingTableViewCell')
MKTransitItemIncidentCell = _Class('MKTransitItemIncidentCell')
MKTransitSystemCell = _Class('MKTransitSystemCell')
MKTransitAttributionSummaryCell = _Class('MKTransitAttributionSummaryCell')
MKTransitMessageCell = _Class('MKTransitMessageCell')
MKBrowseCategoryCollectionViewCell = _Class('MKBrowseCategoryCollectionViewCell')
MKPlaceCollectionCell = _Class('MKPlaceCollectionCell')
MKCollectionBatchCell = _Class('MKCollectionBatchCell')
MKDebugLocationConsole = _Class('MKDebugLocationConsole')
_MKUILabel = _Class('_MKUILabel')
MKPlaceAttributionLabel = _Class('MKPlaceAttributionLabel')
MKArtworkLabelView = _Class('MKArtworkLabelView')
MKTransitInfoLabelView = _Class('MKTransitInfoLabelView')
MKMapSnapshotView = _Class('MKMapSnapshotView')
MKAppleLogoImageView = _Class('MKAppleLogoImageView')
MKArtworkImageView = _Class('MKArtworkImageView')
MKVibrantView = _Class('MKVibrantView')
MKVibrantLabel = _Class('MKVibrantLabel')
MKVibrantHairlineView = _Class('MKVibrantHairlineView')
_MKSmallCalloutPassthroughButton = _Class('_MKSmallCalloutPassthroughButton')
_MKRightImageButton = _Class('_MKRightImageButton')
MKPlaceHeaderButton = _Class('MKPlaceHeaderButton')
MKCatalystButton = _Class('MKCatalystButton')
MKButtonWithTargetArgument = _Class('MKButtonWithTargetArgument')
MKActionRowItemView = _Class('MKActionRowItemView')
MKPlaceAttributionCellButton = _Class('MKPlaceAttributionCellButton')
_MKUserTrackingButton = _Class('_MKUserTrackingButton')
MKPlacePhotoGalleryViewController = _Class('MKPlacePhotoGalleryViewController')
MKPlaceCardActionsRowViewController = _Class('MKPlaceCardActionsRowViewController')
MKAnnotatedItemListViewController = _Class('MKAnnotatedItemListViewController')
MKPictureItemContainerViewController = _Class('MKPictureItemContainerViewController')
MKPlacePhotosViewController = _Class('MKPlacePhotosViewController')
MKTextItemContainerViewController = _Class('MKTextItemContainerViewController')
MKBrowseCategoryViewController = _Class('MKBrowseCategoryViewController')
MKStackingViewController = _Class('MKStackingViewController')
MKTransitLineItemViewController = _Class('MKTransitLineItemViewController')
MKLayoutCardViewController = _Class('MKLayoutCardViewController')
_MKPlaceViewController = _Class('_MKPlaceViewController')
MKPlaceInlineMapViewController = _Class('MKPlaceInlineMapViewController')
MKPlacePoisInlineMapViewController = _Class('MKPlacePoisInlineMapViewController')
MKPlaceSectionViewController = _Class('MKPlaceSectionViewController')
MKPlaceServiceHoursViewController = _Class('MKPlaceServiceHoursViewController')
MKPlaceReviewsViewController = _Class('MKPlaceReviewsViewController')
MKPlaceCuratedCollectionsViewController = _Class('MKPlaceCuratedCollectionsViewController')
MKPlaceHeaderButtonsViewController = _Class('MKPlaceHeaderButtonsViewController')
MKPlaceMessageViewController = _Class('MKPlaceMessageViewController')
MKPlaceInfoViewController = _Class('MKPlaceInfoViewController')
MKPlaceEncyclopedicViewController = _Class('MKPlaceEncyclopedicViewController')
MKPlaceParentInfoViewController = _Class('MKPlaceParentInfoViewController')
MKPlaceParentVenueInfoViewController = _Class('MKPlaceParentVenueInfoViewController')
MKPlaceVenueInfoContentsViewController = _Class('MKPlaceVenueInfoContentsViewController')
MKPlaceQuickLinksViewController = _Class('MKPlaceQuickLinksViewController')
MKPlaceRelatedViewController = _Class('MKPlaceRelatedViewController')
MKPlaceAttributionViewController = _Class('MKPlaceAttributionViewController')
MKPlaceReservationViewController = _Class('MKPlaceReservationViewController')
MKPlaceCardHeaderViewController = _Class('MKPlaceCardHeaderViewController')
MKUGCCallToActionViewController = _Class('MKUGCCallToActionViewController')
MKAppleRatingsViewController = _Class('MKAppleRatingsViewController')
MKOfficialAppViewController = _Class('MKOfficialAppViewController')
MKWebContentViewController = _Class('MKWebContentViewController')
MKPlaceHoursViewController = _Class('MKPlaceHoursViewController')
MKPlaceMessageHoursViewController = _Class('MKPlaceMessageHoursViewController')
MKPlaceCollectionViewController = _Class('MKPlaceCollectionViewController')
MKPlaceCardActionsViewController = _Class('MKPlaceCardActionsViewController')
MKPlaceCardFooterActionsViewController = _Class('MKPlaceCardFooterActionsViewController')
MKPlaceBusinessInfoViewController = _Class('MKPlaceBusinessInfoViewController')
MKActivityViewController = _Class('MKActivityViewController')
MKNearestStationViewController = _Class('MKNearestStationViewController')
_MKTableViewController = _Class('_MKTableViewController')
MKTransitLineIncidentsViewController = _Class('MKTransitLineIncidentsViewController')
MKTransitDeparturesViewController = _Class('MKTransitDeparturesViewController')
MKIncidentsViewController = _Class('MKIncidentsViewController')
MKTransitAttributionViewController = _Class('MKTransitAttributionViewController')
