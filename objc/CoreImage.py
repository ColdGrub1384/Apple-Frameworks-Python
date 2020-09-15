'''
Classes from the 'CoreImage' framework.
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

    
InpaintingVImageWrapper = _Class('InpaintingVImageWrapper')
CIKernelLibrary = _Class('CIKernelLibrary')
InpaintingFullPipelineFilter = _Class('InpaintingFullPipelineFilter')
CIRedEyeRepair = _Class('CIRedEyeRepair')
XMattingSolver = _Class('XMattingSolver')
XMattingRGBFilter = _Class('XMattingRGBFilter')
XMattingRGBDFilter = _Class('XMattingRGBDFilter')
XMattingBoxTensorFilter = _Class('XMattingBoxTensorFilter')
XFocalPlane = _Class('XFocalPlane')
CIAutoEnhanceFace = _Class('CIAutoEnhanceFace')
CIEnhancementHistogram = _Class('CIEnhancementHistogram')
CIEnhancementCalculation = _Class('CIEnhancementCalculation')
CIEnhancementCalculator = _Class('CIEnhancementCalculator')
CIVector = _Class('CIVector')
InpaintingEspressoHelpers = _Class('InpaintingEspressoHelpers')
InpaintingEspressoExecutionResources = _Class('InpaintingEspressoExecutionResources')
InpaintingImageHelpers = _Class('InpaintingImageHelpers')
CISampler = _Class('CISampler')
CIRenderTask = _Class('CIRenderTask')
CIRenderInfo = _Class('CIRenderInfo')
CIRenderDestination = _Class('CIRenderDestination')
CIRedEyeRepair3 = _Class('CIRedEyeRepair3')
CIPerspectiveAutoCalc = _Class('CIPerspectiveAutoCalc')
CIPerspectiveAutoCalcV1 = _Class('CIPerspectiveAutoCalcV1')
CIPerspectiveAutoCalcV2 = _Class('CIPerspectiveAutoCalcV2')
InpaintingTilingFilter = _Class('InpaintingTilingFilter')
CIMetalConverter = _Class('CIMetalConverter')
CIKernel = _Class('CIKernel')
CIWarpKernel = _Class('CIWarpKernel')
CIColorKernel = _Class('CIColorKernel')
CIBlendKernel = _Class('CIBlendKernel')
CIImageRowReader = _Class('CIImageRowReader')
CIImageProcessorInOut = _Class('CIImageProcessorInOut')
CIImageProcessorInput = _Class('CIImageProcessorInput')
CIImageProcessorOutput = _Class('CIImageProcessorOutput')
CIImageAccumulator = _Class('CIImageAccumulator')
CIImage = _Class('CIImage')
DOTRenderer = _Class('DOTRenderer')
CGRenderer = _Class('CGRenderer')
PNGRenderer = _Class('PNGRenderer')
PDFRenderer = _Class('PDFRenderer')
CIFilterShape = _Class('CIFilterShape')
CIFilterClassInfo = _Class('CIFilterClassInfo')
CIFilterClassDefaults = _Class('CIFilterClassDefaults')
CIFilterClassCategories = _Class('CIFilterClassCategories')
CIFilterClassAttributes = _Class('CIFilterClassAttributes')
CIFeature = _Class('CIFeature')
CIVNFeature = _Class('CIVNFeature')
CIVNRectFeature = _Class('CIVNRectFeature')
CITextFeature = _Class('CITextFeature')
CIQRCodeFeature = _Class('CIQRCodeFeature')
CIRectangleFeature = _Class('CIRectangleFeature')
CIFaceFeature = _Class('CIFaceFeature')
CIDualRedEyeRepairTuning = _Class('CIDualRedEyeRepairTuning')
CIDualRedEyeRepairSession = _Class('CIDualRedEyeRepairSession')
RedEyeFace = _Class('RedEyeFace')
CIFeatureProviderImage = _Class('CIFeatureProviderImage')
CIFeatureProviderMultiArray = _Class('CIFeatureProviderMultiArray')
CIPredictionModel = _Class('CIPredictionModel')
CIImageProcessorKernel = _Class('CIImageProcessorKernel')
InpaintingMembraneGeneration = _Class('InpaintingMembraneGeneration')
CISaliencyMapKernel = _Class('CISaliencyMapKernel')
InpaintingSinglePassFilter = _Class('InpaintingSinglePassFilter')
CIHighlightRecoveryProcessor = _Class('CIHighlightRecoveryProcessor')
CIMorphologyProcessor = _Class('CIMorphologyProcessor')
CIMetalProcessor = _Class('CIMetalProcessor')
CIMedianProcessor = _Class('CIMedianProcessor')
CIMattingRGBDProcessor = _Class('CIMattingRGBDProcessor')
CILensModelKernelMetalProcessor = _Class('CILensModelKernelMetalProcessor')
CILensModelCalculatorCPU = _Class('CILensModelCalculatorCPU')
CIIntegralImageProcessorCPU = _Class('CIIntegralImageProcessorCPU')
CIIntegralImageProcessorGPU = _Class('CIIntegralImageProcessorGPU')
CIFileSaverProcessor = _Class('CIFileSaverProcessor')
CIGenericMetalProcessor = _Class('CIGenericMetalProcessor')
CIGenericMetalProcessorSingleChannel = _Class('CIGenericMetalProcessorSingleChannel')
CIFocalPlaneProcessor = _Class('CIFocalPlaneProcessor')
FBSProcessor = _Class('FBSProcessor')
FBSProcessorGPU = _Class('FBSProcessorGPU')
FBSProcessorCPU = _Class('FBSProcessorCPU')
CIFaceMaskKernel = _Class('CIFaceMaskKernel')
CISeedFillProcessor = _Class('CISeedFillProcessor')
ConvexFillProcessor = _Class('ConvexFillProcessor')
PercentileClipProcessor_RGBA8_CPU = _Class('PercentileClipProcessor_RGBA8_CPU')
CIDisparitySmoothingProcessor = _Class('CIDisparitySmoothingProcessor')
CICoreMLProcessorImageArray = _Class('CICoreMLProcessorImageArray')
CICoreMLKernel = _Class('CICoreMLKernel')
CIConvolutionProcessor = _Class('CIConvolutionProcessor')
InpaintingExecutionContext = _Class('InpaintingExecutionContext')
CIContextCache = _Class('CIContextCache')
CIColor = _Class('CIColor')
CIBurstYUVImage = _Class('CIBurstYUVImage')
CIBurstThumbnailCluster = _Class('CIBurstThumbnailCluster')
CIBurstImageStat = _Class('CIBurstImageStat')
CIBurstFaceStat = _Class('CIBurstFaceStat')
CIBurstImageSetInternal = _Class('CIBurstImageSetInternal')
InpaintingGeneralHelpers = _Class('InpaintingGeneralHelpers')
InpaintingMultiresolutionFilter = _Class('InpaintingMultiresolutionFilter')
CIBurstImageSet = _Class('CIBurstImageSet')
CIBurstImageFaceAnalysisContext = _Class('CIBurstImageFaceAnalysisContext')
CIBurstFaceInfo = _Class('CIBurstFaceInfo')
CIBurstFaceScoreEntry = _Class('CIBurstFaceScoreEntry')
CIBurstFaceConfigEntry = _Class('CIBurstFaceConfigEntry')
CIBurstClusterDivider = _Class('CIBurstClusterDivider')
CIBurstActionClassifier = _Class('CIBurstActionClassifier')
CIContext = _Class('CIContext')
CIBitmapContext = _Class('CIBitmapContext')
CIDetector = _Class('CIDetector')
CIVNFaceDetector = _Class('CIVNFaceDetector')
CIVNDetector = _Class('CIVNDetector')
CIVNRectDetector = _Class('CIVNRectDetector')
CITextDetector = _Class('CITextDetector')
CIFaceCoreDetector = _Class('CIFaceCoreDetector')
CIRectangleDetector = _Class('CIRectangleDetector')
CIBarcodeDetector = _Class('CIBarcodeDetector')
CIBarcodeDescriptor = _Class('CIBarcodeDescriptor')
CIDataMatrixCodeDescriptor = _Class('CIDataMatrixCodeDescriptor')
CIPDF417CodeDescriptor = _Class('CIPDF417CodeDescriptor')
CIAztecCodeDescriptor = _Class('CIAztecCodeDescriptor')
CIQRCodeDescriptor = _Class('CIQRCodeDescriptor')
CIFilter = _Class('CIFilter')
CIKeystoneCorrection = _Class('CIKeystoneCorrection')
CIKeystoneCorrectionVertical = _Class('CIKeystoneCorrectionVertical')
CIKeystoneCorrectionHorizontal = _Class('CIKeystoneCorrectionHorizontal')
CIKeystoneCorrectionCombined = _Class('CIKeystoneCorrectionCombined')
CIPerspectiveRotate = _Class('CIPerspectiveRotate')
CIBlurmapRefinementDistanceDelta = _Class('CIBlurmapRefinementDistanceDelta')
CIBlurmapRefinementLinearMapping = _Class('CIBlurmapRefinementLinearMapping')
CIBlurmapRefinementThreshold = _Class('CIBlurmapRefinementThreshold')
CIColorAbsoluteDifference = _Class('CIColorAbsoluteDifference')
RedEyeChannel = _Class('RedEyeChannel')
RedEyeGradient = _Class('RedEyeGradient')
RedEyeDifference = _Class('RedEyeDifference')
RedEyeMaxMorphology = _Class('RedEyeMaxMorphology')
RedEyeMinMorphology = _Class('RedEyeMinMorphology')
RedEyeGlintFinder = _Class('RedEyeGlintFinder')
CUIOuterBevelEmbossFilter = _Class('CUIOuterBevelEmbossFilter')
CUIInnerBevelEmbossFilter = _Class('CUIInnerBevelEmbossFilter')
CUIShapeEffectBlur1 = _Class('CUIShapeEffectBlur1')
CUIOuterGlowOrShadowFilter = _Class('CUIOuterGlowOrShadowFilter')
CUIInnerGlowOrShadowFilter = _Class('CUIInnerGlowOrShadowFilter')
CUIScaleClampFilter = _Class('CUIScaleClampFilter')
CIDepthBlurEffect = _Class('CIDepthBlurEffect')
CIDepthEffect = _Class('CIDepthEffect')
CIDepthEffectApplyBlurMap = _Class('CIDepthEffectApplyBlurMap')
CIDepthEffectMakeBlurMap = _Class('CIDepthEffectMakeBlurMap')
CIDisparityRefinementV3 = _Class('CIDisparityRefinementV3')
CIDisparityRefinementAntialiasV3 = _Class('CIDisparityRefinementAntialiasV3')
CIDisparityRefinementSparseSamplerV3 = _Class('CIDisparityRefinementSparseSamplerV3')
CIDisparityPreprocV3 = _Class('CIDisparityPreprocV3')
CIDisparityWeightsV3 = _Class('CIDisparityWeightsV3')
CILensModelApplyV3 = _Class('CILensModelApplyV3')
CISegmentationFusion = _Class('CISegmentationFusion')
CIDepthDisparityConverter = _Class('CIDepthDisparityConverter')
CIDisparityToDepth = _Class('CIDisparityToDepth')
CIDepthToDisparity = _Class('CIDepthToDisparity')
CIWrapMirror = _Class('CIWrapMirror')
CIVortexDistortion = _Class('CIVortexDistortion')
CIVignetteEffect = _Class('CIVignetteEffect')
CIVignette = _Class('CIVignette')
CIVibrance = _Class('CIVibrance')
CIVariableBoxBlur = _Class('CIVariableBoxBlur')
CIUnsharpMask = _Class('CIUnsharpMask')
CITwirlDistortion = _Class('CITwirlDistortion')
CITriangleTile = _Class('CITriangleTile')
CITriangleKaleidoscope = _Class('CITriangleKaleidoscope')
CIToneCurve = _Class('CIToneCurve')
CIAttributedTextImageGenerator = _Class('CIAttributedTextImageGenerator')
CITextImageGenerator = _Class('CITextImageGenerator')
CIFalseColor = _Class('CIFalseColor')
CIWhitePointAdjust = _Class('CIWhitePointAdjust')
CITemperatureAndTint = _Class('CITemperatureAndTint')
CISwipeTransition = _Class('CISwipeTransition')
CISunbeamsGenerator = _Class('CISunbeamsGenerator')
CIStripesGenerator = _Class('CIStripesGenerator')
CINinePartTiled = _Class('CINinePartTiled')
CINinePartStretched = _Class('CINinePartStretched')
CIStretchCrop = _Class('CIStretchCrop')
CIStretch = _Class('CIStretch')
CIStraightenFilter = _Class('CIStraightenFilter')
CIStarShineGenerator = _Class('CIStarShineGenerator')
CISpotLight = _Class('CISpotLight')
CISoftCubicUpsample = _Class('CISoftCubicUpsample')
CIBicubicScaleTransform = _Class('CIBicubicScaleTransform')
CISmartColorFilter = _Class('CISmartColorFilter')
CISmartToneFilter = _Class('CISmartToneFilter')
CISmartBlackAndWhite = _Class('CISmartBlackAndWhite')
CISkyAndGrassAdjust = _Class('CISkyAndGrassAdjust')
CISharpenLuminance = _Class('CISharpenLuminance')
CIProSharpenEdges = _Class('CIProSharpenEdges')
CINoiseReduction = _Class('CINoiseReduction')
CIShadedMaterial = _Class('CIShadedMaterial')
CISepiaTone = _Class('CISepiaTone')
CISampleNearest = _Class('CISampleNearest')
CISaliencyMapFilter = _Class('CISaliencyMapFilter')
CILinearToSRGBToneCurve = _Class('CILinearToSRGBToneCurve')
CISRGBToneCurveToLinear = _Class('CISRGBToneCurveToLinear')
CIRippleTransition = _Class('CIRippleTransition')
CITileFilter = _Class('CITileFilter')
CISixfoldReflectedTile = _Class('CISixfoldReflectedTile')
CIEightfoldReflectedTile = _Class('CIEightfoldReflectedTile')
CIGlideReflectedTile = _Class('CIGlideReflectedTile')
CITwelvefoldReflectedTile = _Class('CITwelvefoldReflectedTile')
CISixfoldRotatedTile = _Class('CISixfoldRotatedTile')
CIFourfoldRotatedTile = _Class('CIFourfoldRotatedTile')
CITile2Filter = _Class('CITile2Filter')
CIFourfoldReflectedTile = _Class('CIFourfoldReflectedTile')
CIFourfoldTranslatedTile = _Class('CIFourfoldTranslatedTile')
CIPaletteCentroid = _Class('CIPaletteCentroid')
CICircularMaskFromPointImage = _Class('CICircularMaskFromPointImage')
CIAreaMinMaxRedNormalize = _Class('CIAreaMinMaxRedNormalize')
CIAreaMinMaxNormalize = _Class('CIAreaMinMaxNormalize')
CIReductionFilter = _Class('CIReductionFilter')
CIAreaCentroid = _Class('CIAreaCentroid')
CIAreaRedCentroid = _Class('CIAreaRedCentroid')
CIAreaRedRadialCentroid = _Class('CIAreaRedRadialCentroid')
CIKMeans = _Class('CIKMeans')
CIAreaMinMaxRed = _Class('CIAreaMinMaxRed')
CIAreaMaximumAlpha = _Class('CIAreaMaximumAlpha')
CIAreaMinimumAlpha = _Class('CIAreaMinimumAlpha')
CIAreaMinimum = _Class('CIAreaMinimum')
CIAreaMaximum = _Class('CIAreaMaximum')
CIAreaMinMax = _Class('CIAreaMinMax')
CIColumnAverage = _Class('CIColumnAverage')
CIRowAverage = _Class('CIRowAverage')
CIAreaAverage = _Class('CIAreaAverage')
CIRedEyeCorrections = _Class('CIRedEyeCorrections')
CIRedEyeCorrection = _Class('CIRedEyeCorrection')
CIRoundedRectangleGenerator = _Class('CIRoundedRectangleGenerator')
CIRectangleGenerator = _Class('CIRectangleGenerator')
CIRandomGenerator = _Class('CIRandomGenerator')
CIRAWGamutMapping = _Class('CIRAWGamutMapping')
CIRAWTemperatureAdjust = _Class('CIRAWTemperatureAdjust')
CIRAWFilterImpl = _Class('CIRAWFilterImpl')
CIUnpremultiply = _Class('CIUnpremultiply')
CIPremultiply = _Class('CIPremultiply')
CIPortraitBlurCombiner = _Class('CIPortraitBlurCombiner')
CIPortraitBlurV2 = _Class('CIPortraitBlurV2')
CISparseRenderer = _Class('CISparseRenderer')
CISparseRendererPreFiltering = _Class('CISparseRendererPreFiltering')
CIPortraitAntialias = _Class('CIPortraitAntialias')
CIHighlightRecovery = _Class('CIHighlightRecovery')
CISDOFHighlightRecovery = _Class('CISDOFHighlightRecovery')
CIPortraitBlurPreProcess = _Class('CIPortraitBlurPreProcess')
CIPortraitBlur = _Class('CIPortraitBlur')
CIPortraitBlurDirectionalBlur = _Class('CIPortraitBlurDirectionalBlur')
CIPortraitBlurNoise = _Class('CIPortraitBlurNoise')
CIBlurmapSmoothing = _Class('CIBlurmapSmoothing')
CIPointillize = _Class('CIPointillize')
CIHexagonalPixellate = _Class('CIHexagonalPixellate')
CIPixellate = _Class('CIPixellate')
CIPinchDistortion = _Class('CIPinchDistortion')
CIPhotoGrain = _Class('CIPhotoGrain')
CIPhotoEffect3D = _Class('CIPhotoEffect3D')
CIPhotoEffect3DNoir = _Class('CIPhotoEffect3DNoir')
CIPhotoEffect3DCommercial = _Class('CIPhotoEffect3DCommercial')
CIPhotoEffect3DSilverplate = _Class('CIPhotoEffect3DSilverplate')
CIPhotoEffect3DDramaticCool = _Class('CIPhotoEffect3DDramaticCool')
CIPhotoEffect3DDramaticWarm = _Class('CIPhotoEffect3DDramaticWarm')
CIPhotoEffect3DDramatic = _Class('CIPhotoEffect3DDramatic')
CIPhotoEffect3DVividCool = _Class('CIPhotoEffect3DVividCool')
CIPhotoEffect3DVividWarm = _Class('CIPhotoEffect3DVividWarm')
CIPhotoEffect3DVivid = _Class('CIPhotoEffect3DVivid')
CIPhotoEffect = _Class('CIPhotoEffect')
CIPhotoEffectStageMono = _Class('CIPhotoEffectStageMono')
CIPhotoEffectTransfer = _Class('CIPhotoEffectTransfer')
CIPhotoEffectTonal = _Class('CIPhotoEffectTonal')
CIPhotoEffectProcess = _Class('CIPhotoEffectProcess')
CIPhotoEffectMono = _Class('CIPhotoEffectMono')
CIPhotoEffectInstant = _Class('CIPhotoEffectInstant')
CIPhotoEffectFade = _Class('CIPhotoEffectFade')
CIPhotoEffectChrome = _Class('CIPhotoEffectChrome')
CIPhotoEffectNoir = _Class('CIPhotoEffectNoir')
CIPerspectiveCorrection = _Class('CIPerspectiveCorrection')
CIPerspectiveTile = _Class('CIPerspectiveTile')
CIPerspectiveTransform = _Class('CIPerspectiveTransform')
CIPerspectiveTransformWithExtent = _Class('CIPerspectiveTransformWithExtent')
CIParallelogramTile = _Class('CIParallelogramTile')
CIPageCurlWithShadowTransition = _Class('CIPageCurlWithShadowTransition')
CIPageCurlTransition = _Class('CIPageCurlTransition')
CIOpacity = _Class('CIOpacity')
CIOpTile = _Class('CIOpTile')
CIZoomBlur = _Class('CIZoomBlur')
CIMotionBlur = _Class('CIMotionBlur')
CIMorphologyRectangle = _Class('CIMorphologyRectangle')
CIMorphologyRectangleMinimum = _Class('CIMorphologyRectangleMinimum')
CIMorphologyRectangleMaximum = _Class('CIMorphologyRectangleMaximum')
CIPseudoMedian = _Class('CIPseudoMedian')
CIMorphology = _Class('CIMorphology')
CIMorphologyLaplacian = _Class('CIMorphologyLaplacian')
CIMorphologyGradient = _Class('CIMorphologyGradient')
CIMorphologyMaximum = _Class('CIMorphologyMaximum')
CIMorphologyMinimum = _Class('CIMorphologyMinimum')
CICheapMorphology = _Class('CICheapMorphology')
CIModTransition = _Class('CIModTransition')
CIMirror = _Class('CIMirror')
CIMaximumComponent = _Class('CIMaximumComponent')
CIMinimumComponent = _Class('CIMinimumComponent')
CIMetalWrapper = _Class('CIMetalWrapper')
CIMeshGenerator = _Class('CIMeshGenerator')
CIMedianFilter = _Class('CIMedianFilter')
CIMattingSolverInternal = _Class('CIMattingSolverInternal')
CIMattingSolver = _Class('CIMattingSolver')
CIMaskedVariableBlur = _Class('CIMaskedVariableBlur')
CIMaskToAlpha = _Class('CIMaskToAlpha')
CILumaMap = _Class('CILumaMap')
CIThermal = _Class('CIThermal')
CIXRay = _Class('CIXRay')
CILocalLightFilter = _Class('CILocalLightFilter')
CILocalLightMapPrepare = _Class('CILocalLightMapPrepare')
CILocalContrast = _Class('CILocalContrast')
CILightTunnel = _Class('CILightTunnel')
CILenticularHaloGenerator = _Class('CILenticularHaloGenerator')
CILensModelApply = _Class('CILensModelApply')
CILensModelCalculator = _Class('CILensModelCalculator')
CITorusLensDistortion = _Class('CITorusLensDistortion')
CIGlassLozenge = _Class('CIGlassLozenge')
CILanczosScaleTransform = _Class('CILanczosScaleTransform')
CILabDeltaE = _Class('CILabDeltaE')
CIKaleidoscope = _Class('CIKaleidoscope')
CIIntegralImage = _Class('CIIntegralImage')
CIImageWriter = _Class('CIImageWriter')
CIHoleDistortion = _Class('CIHoleDistortion')
CIHistogramDisplayFilter = _Class('CIHistogramDisplayFilter')
CIHighlightShadowAdjust = _Class('CIHighlightShadowAdjust')
CIHeightFieldFromMask = _Class('CIHeightFieldFromMask')
CICircularScreen = _Class('CICircularScreen')
_CIScreenFilter = _Class('_CIScreenFilter')
CILineScreen = _Class('CILineScreen')
CIHatchedScreen = _Class('CIHatchedScreen')
CIDotScreen = _Class('CIDotScreen')
CIGuidedFilter = _Class('CIGuidedFilter')
CIHueSaturationValueGradient = _Class('CIHueSaturationValueGradient')
CIGaussianGradient = _Class('CIGaussianGradient')
CISmoothLinearGradient = _Class('CISmoothLinearGradient')
CILinearGradient = _Class('CILinearGradient')
CIRadialGradient = _Class('CIRadialGradient')
CIGlassDistortion = _Class('CIGlassDistortion')
CIGaussianBlurXY = _Class('CIGaussianBlurXY')
CIGaussianBlur = _Class('CIGaussianBlur')
CIGammaAdjust = _Class('CIGammaAdjust')
CIModifyBlurmap = _Class('CIModifyBlurmap')
CIFocalPlaneNative = _Class('CIFocalPlaneNative')
CIFocalPlanePreprocessorInternal = _Class('CIFocalPlanePreprocessorInternal')
CIFocalPlane = _Class('CIFocalPlane')
CIFlashTransition = _Class('CIFlashTransition')
CIFastBilateralSolver = _Class('CIFastBilateralSolver')
CIFaceSegmentationFilter = _Class('CIFaceSegmentationFilter')
CIFaceMaskCalculator = _Class('CIFaceMaskCalculator')
CIFaceMaskDelta = _Class('CIFaceMaskDelta')
CIFaceMaskApply = _Class('CIFaceMaskApply')
CIFaceBalance = _Class('CIFaceBalance')
CIExposureAdjust = _Class('CIExposureAdjust')
CIGaborGradients = _Class('CIGaborGradients')
CIEdges = _Class('CIEdges')
CIEdgeWork = _Class('CIEdgeWork')
CIEdgePreserveUpsampleFilter = _Class('CIEdgePreserveUpsampleFilter')
CIEdgePreserveUpsampleRGFilter = _Class('CIEdgePreserveUpsampleRGFilter')
CIRedEyeRaw = _Class('CIRedEyeRaw')
RedPupilLocalizer = _Class('RedPupilLocalizer')
RedEyeRecolor = _Class('RedEyeRecolor')
RedEyeSpecular = _Class('RedEyeSpecular')
CICircularityDescriptor = _Class('CICircularityDescriptor')
CISeedFill = _Class('CISeedFill')
CIConvexFill = _Class('CIConvexFill')
HistoClip_RGBA8_CPU = _Class('HistoClip_RGBA8_CPU')
RadialFalloffFilter = _Class('RadialFalloffFilter')
CheapRandomness = _Class('CheapRandomness')
CIDroste = _Class('CIDroste')
CIContrastEnhancer = _Class('CIContrastEnhancer')
CIPaperWash = _Class('CIPaperWash')
CIDocumentEnhancer = _Class('CIDocumentEnhancer')
CIDissolveTransition = _Class('CIDissolveTransition')
CIDisplacementDistortion = _Class('CIDisplacementDistortion')
CIDisparitySmoothing = _Class('CIDisparitySmoothing')
CIDisparityRefinement = _Class('CIDisparityRefinement')
CIInpaintingFilter = _Class('CIInpaintingFilter')
CIDisintegrateWithMaskTransition = _Class('CIDisintegrateWithMaskTransition')
CIRingBlur = _Class('CIRingBlur')
CIDiscBlur = _Class('CIDiscBlur')
CIBokehBlur = _Class('CIBokehBlur')
CIConvolution = _Class('CIConvolution')
CIDepthOfField = _Class('CIDepthOfField')
CICrystallize = _Class('CICrystallize')
CICrop = _Class('CICrop')
CICoreMLModelFilter = _Class('CICoreMLModelFilter')
CICopyMachineTransition = _Class('CICopyMachineTransition')
CIConvolution9Vertical = _Class('CIConvolution9Vertical')
CIConvolution9Horizontal = _Class('CIConvolution9Horizontal')
CIConvolution7X7 = _Class('CIConvolution7X7')
CIConvolution5X5 = _Class('CIConvolution5X5')
CIConvolution3X3 = _Class('CIConvolution3X3')
CIConstantColorGenerator = _Class('CIConstantColorGenerator')
_CICompositeFilter = _Class('_CICompositeFilter')
CIPlusLighterCompositing = _Class('CIPlusLighterCompositing')
CIPlusDarkerCompositing = _Class('CIPlusDarkerCompositing')
CIMaximumCompositing = _Class('CIMaximumCompositing')
CIMinimumCompositing = _Class('CIMinimumCompositing')
CIMultiplyCompositing = _Class('CIMultiplyCompositing')
CIAdditionCompositing = _Class('CIAdditionCompositing')
CISourceAtopCompositing = _Class('CISourceAtopCompositing')
CISourceOutCompositing = _Class('CISourceOutCompositing')
CISourceInCompositing = _Class('CISourceInCompositing')
CISourceOverCompositing = _Class('CISourceOverCompositing')
CIComicEffect = _Class('CIComicEffect')
CISpotColor = _Class('CISpotColor')
CILineOverlay = _Class('CILineOverlay')
CIFusionTwoImagesDelta = _Class('CIFusionTwoImagesDelta')
CIFusionDelta = _Class('CIFusionDelta')
CIColorPosterize = _Class('CIColorPosterize')
CIColorCrossPolynomial = _Class('CIColorCrossPolynomial')
CIColorPolynomial = _Class('CIColorPolynomial')
CIColorPolynomialInverse = _Class('CIColorPolynomialInverse')
CIColorInvert = _Class('CIColorInvert')
CIColorMatrix = _Class('CIColorMatrix')
CISingleChannelColorMap = _Class('CISingleChannelColorMap')
CIColorMap = _Class('CIColorMap')
CIDesaturateShadows = _Class('CIDesaturateShadows')
CIDither = _Class('CIDither')
CIPalettize = _Class('CIPalettize')
CIColorMonochrome = _Class('CIColorMonochrome')
CIColorThresholdOtsu = _Class('CIColorThresholdOtsu')
CIColorThreshold = _Class('CIColorThreshold')
CIColorCurves = _Class('CIColorCurves')
CIColorCubesMixedWithMask = _Class('CIColorCubesMixedWithMask')
CIColorCube = _Class('CIColorCube')
CIColorCubeWithColorSpace = _Class('CIColorCubeWithColorSpace')
CIHueAdjust = _Class('CIHueAdjust')
CIColorControls = _Class('CIColorControls')
CIColorClamp = _Class('CIColorClamp')
CIColorBalance = _Class('CIColorBalance')
CICircularWrap = _Class('CICircularWrap')
CICircleSplashDistortion = _Class('CICircleSplashDistortion')
CICircleGenerator = _Class('CICircleGenerator')
CICheckerboardGenerator = _Class('CICheckerboardGenerator')
CICheatBlur = _Class('CICheatBlur')
CICheapBlur = _Class('CICheapBlur')
CICameraCalibrationLensCorrection = _Class('CICameraCalibrationLensCorrection')
CICMYKHalftone = _Class('CICMYKHalftone')
CIBumpDistortionLinear = _Class('CIBumpDistortionLinear')
CIBumpDistortion = _Class('CIBumpDistortion')
CIBoxBlur = _Class('CIBoxBlur')
CIGloom = _Class('CIGloom')
CIBloom = _Class('CIBloom')
CIBlendWithMask = _Class('CIBlendWithMask')
CIBlendWithAlphaMask = _Class('CIBlendWithAlphaMask')
CIBlendWithBlueMask = _Class('CIBlendWithBlueMask')
CIBlendWithRedMask = _Class('CIBlendWithRedMask')
CIMix = _Class('CIMix')
CIBlendModeFilter = _Class('CIBlendModeFilter')
CIHardMixBlendMode = _Class('CIHardMixBlendMode')
CIPinLightBlendMode = _Class('CIPinLightBlendMode')
CILinearLightBlendMode = _Class('CILinearLightBlendMode')
CIVividLightBlendMode = _Class('CIVividLightBlendMode')
CILinearDodgeBlendMode = _Class('CILinearDodgeBlendMode')
CILinearBurnBlendMode = _Class('CILinearBurnBlendMode')
CIDivideBlendMode = _Class('CIDivideBlendMode')
CISubtractBlendMode = _Class('CISubtractBlendMode')
CIPDFNonSeparableBlendMode = _Class('CIPDFNonSeparableBlendMode')
CILuminosityBlendMode = _Class('CILuminosityBlendMode')
CIColorBlendMode = _Class('CIColorBlendMode')
CISaturationBlendMode = _Class('CISaturationBlendMode')
CIHueBlendMode = _Class('CIHueBlendMode')
CIExclusionBlendMode = _Class('CIExclusionBlendMode')
CIDifferenceBlendMode = _Class('CIDifferenceBlendMode')
CISoftLightBlendMode = _Class('CISoftLightBlendMode')
CIHardLightBlendMode = _Class('CIHardLightBlendMode')
CIColorBurnBlendMode = _Class('CIColorBurnBlendMode')
CIColorDodgeBlendMode = _Class('CIColorDodgeBlendMode')
CILightenBlendMode = _Class('CILightenBlendMode')
CIDarkenBlendMode = _Class('CIDarkenBlendMode')
CIOverlayBlendMode = _Class('CIOverlayBlendMode')
CIScreenBlendMode = _Class('CIScreenBlendMode')
CIMultiplyBlendMode = _Class('CIMultiplyBlendMode')
CICheapBilateral = _Class('CICheapBilateral')
CIBarsSwipeTransition = _Class('CIBarsSwipeTransition')
CIPercentileRed = _Class('CIPercentileRed')
CIAreaHistogram = _Class('CIAreaHistogram')
CIAppleSmithGossettScale = _Class('CIAppleSmithGossettScale')
CIASGPercent = _Class('CIASGPercent')
CIASG60Percent = _Class('CIASG60Percent')
CIASG80Percent = _Class('CIASG80Percent')
CIASG75Percent = _Class('CIASG75Percent')
CIASG66Percent = _Class('CIASG66Percent')
CIASG50Percent = _Class('CIASG50Percent')
CIAffineTransform = _Class('CIAffineTransform')
CIAffineTile = _Class('CIAffineTile')
CISimpleTile = _Class('CISimpleTile')
CIAffineClamp = _Class('CIAffineClamp')
CIClamp = _Class('CIClamp')
CIAccordionFoldTransition = _Class('CIAccordionFoldTransition')
CIBilateralSolverGPU = _Class('CIBilateralSolverGPU')
CIBilateralSolverCPU = _Class('CIBilateralSolverCPU')
CIBilateralGridHash = _Class('CIBilateralGridHash')
AutoCropper = _Class('AutoCropper')
CIGVNode = _Class('CIGVNode')
