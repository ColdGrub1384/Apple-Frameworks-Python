'''
Classes from the 'Espresso' framework.
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

    
EspressoANEIOSurface = _Class('EspressoANEIOSurface')
EspressoFDOverfeatNetwork = _Class('EspressoFDOverfeatNetwork')
EspressoBrickTensor = _Class('EspressoBrickTensor')
EspressoBrickTensorMetal = _Class('EspressoBrickTensorMetal')
EspressoBrickTensorCPU = _Class('EspressoBrickTensorCPU')
EspressoBrickTensorShape = _Class('EspressoBrickTensorShape')
EspressoBrickRegistry = _Class('EspressoBrickRegistry')
EspressoProfilingNetworkInfo = _Class('EspressoProfilingNetworkInfo')
EspressoProfilingLayerInfo = _Class('EspressoProfilingLayerInfo')
EspressoProfilingLayerSupportInfo = _Class('EspressoProfilingLayerSupportInfo')
EspressoProfilingLayerRuntime = _Class('EspressoProfilingLayerRuntime')
EspressoMetalKernelsCache = _Class('EspressoMetalKernelsCache')
ETVariablesDefinition = _Class('ETVariablesDefinition')
Espresso_mxnetTools_ImageBinaryRecordReader = _Class('Espresso_mxnetTools_ImageBinaryRecordReader')
ETOptimizerDefinition = _Class('ETOptimizerDefinition')
ETDataTensor = _Class('ETDataTensor')
MLRangeBrickTest = _Class('MLRangeBrickTest')
MyMPSCNNConvolutionGradientState = _Class('MyMPSCNNConvolutionGradientState')
_ETBufferDataSource = _Class('_ETBufferDataSource')
ETImageFolderDataProvider = _Class('ETImageFolderDataProvider')
ETImagePreprocessor = _Class('ETImagePreprocessor')
ETImagePreprocessParams = _Class('ETImagePreprocessParams')
ETDataPointDictionary = _Class('ETDataPointDictionary')
EspressoSharedKernelCacheEntry = _Class('EspressoSharedKernelCacheEntry')
ETLossConfig = _Class('ETLossConfig')
ETTask = _Class('ETTask')
ETTaskClassifier = _Class('ETTaskClassifier')
ETDataSourceWithCache = _Class('ETDataSourceWithCache')
ETDataSourceWithExtractor = _Class('ETDataSourceWithExtractor')
ETDataSourceBuf = _Class('ETDataSourceBuf')
ETDataSourceBlobF4 = _Class('ETDataSourceBlobF4')
ETDataSourceFromFolderData = _Class('ETDataSourceFromFolderData')
ETImageDescriptorExtractor = _Class('ETImageDescriptorExtractor')
ETVariable = _Class('ETVariable')
ETOpaqueCopy = _Class('ETOpaqueCopy')
ETModelDef = _Class('ETModelDef')
ETModelWithExtractor = _Class('ETModelWithExtractor')
ETModelDefLeNet = _Class('ETModelDefLeNet')
ETModelDefMLP = _Class('ETModelDefMLP')
ETOptimizerDef = _Class('ETOptimizerDef')
ETOptimizerDefSGD = _Class('ETOptimizerDefSGD')
ETDataPoint = _Class('ETDataPoint')
EspressoContext = _Class('EspressoContext')
EspressoNetwork = _Class('EspressoNetwork')
EspressoMetalSingleton = _Class('EspressoMetalSingleton')
EspressoInnerProductWeightsForMPS = _Class('EspressoInnerProductWeightsForMPS')
EspressoTrainingInnerProductWeightsForMPS = _Class('EspressoTrainingInnerProductWeightsForMPS')
EspressoConvolutionWeightsForMPS = _Class('EspressoConvolutionWeightsForMPS')
EspressoTrainingConvolutionWeightsForMPS = _Class('EspressoTrainingConvolutionWeightsForMPS')
EspressoDCNEspressoOverfeatDetector = _Class('EspressoDCNEspressoOverfeatDetector')
EspressoOJBC = _Class('EspressoOJBC')
EspressoFaceLandmarkDetector = _Class('EspressoFaceLandmarkDetector')
ETModelDefinition = _Class('ETModelDefinition')
ETLayerInitializationParameters = _Class('ETLayerInitializationParameters')
EspressoFaceDetectedObject = _Class('EspressoFaceDetectedObject')
ETLossDefinition = _Class('ETLossDefinition')
TwoNetsStyleTransfer = _Class('TwoNetsStyleTransfer')
EspressoImage2Image = _Class('EspressoImage2Image')
EspressoCustomPass = _Class('EspressoCustomPass')
EspressoPass_squeeze_devop = _Class('EspressoPass_squeeze_devop')
EspressoPass_style_transfer_parameterize_transplant = _Class('EspressoPass_style_transfer_parameterize_transplant')
EspressoPass_style_transfer_two_nets = _Class('EspressoPass_style_transfer_two_nets')
EspressoPass_style_transfer_two_nets_onlyanepart = _Class('EspressoPass_style_transfer_two_nets_onlyanepart')
EspressoPass_lstm_atomizer = _Class('EspressoPass_lstm_atomizer')
EspressoPass_make_fully_conv = _Class('EspressoPass_make_fully_conv')
EspressoPass_debug_mode = _Class('EspressoPass_debug_mode')
EspressoPass_wavernn_ane = _Class('EspressoPass_wavernn_ane')
EspressoPass_multi_head_program_gen = _Class('EspressoPass_multi_head_program_gen')
EspressoPass_find_shared_weights = _Class('EspressoPass_find_shared_weights')
EspressoPass_multi_head_prune_undeclared = _Class('EspressoPass_multi_head_prune_undeclared')
EspressoPass_rpn_tracker_merge_convs = _Class('EspressoPass_rpn_tracker_merge_convs')
EspressoPass_transpose_inner_product_weights = _Class('EspressoPass_transpose_inner_product_weights')
ETTaskDefinition = _Class('ETTaskDefinition')
ETTaskState = _Class('ETTaskState')
EspressoDataFrameStorageExecutor = _Class('EspressoDataFrameStorageExecutor')
EspressoDataFrameExecutor = _Class('EspressoDataFrameExecutor')
EspressoDataFrameStorageExecutorMatchingBufferSet = _Class('EspressoDataFrameStorageExecutorMatchingBufferSet')
EspressoDataFrameStorage = _Class('EspressoDataFrameStorage')
EspressoDataFrame = _Class('EspressoDataFrame')
EspressoDataFrameAttachment = _Class('EspressoDataFrameAttachment')
EspressoDataFrameTensorAttachment = _Class('EspressoDataFrameTensorAttachment')
EspressoDataFrameImageAttachment = _Class('EspressoDataFrameImageAttachment')
EspressoDataFrameMappedFile = _Class('EspressoDataFrameMappedFile')
