
'''
Classes from the 'BiomePubSub' framework.
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
    
    
BPSFutureResult = _Class('BPSFutureResult')
BPSSubscriberList = _Class('BPSSubscriberList')
BPSSubscriptionStatus = _Class('BPSSubscriptionStatus')
BPSAggregations = _Class('BPSAggregations')
BPSAggregator = _Class('BPSAggregator')
BPSDrivableSink = _Class('BPSDrivableSink')
BPSSink = _Class('BPSSink')
BPSPartialCompletion = _Class('BPSPartialCompletion')
BPSCompletion = _Class('BPSCompletion')
BPSTuple = _Class('BPSTuple')
BPSPublisher = _Class('BPSPublisher')
BPSFuture = _Class('BPSFuture')
BPSCollect = _Class('BPSCollect')
BPSScan = _Class('BPSScan')
BPSPassThroughSubject = _Class('BPSPassThroughSubject')
BPSZipMany = _Class('BPSZipMany')
BPSZip = _Class('BPSZip')
BPSMap = _Class('BPSMap')
BPSReduce = _Class('BPSReduce')
BPSLast = _Class('BPSLast')
BPSCombineLatest = _Class('BPSCombineLatest')
BPSFlatMap = _Class('BPSFlatMap')
BPSOrderedMerge = _Class('BPSOrderedMerge')
BPSFilter = _Class('BPSFilter')
BPSMergeMany = _Class('BPSMergeMany')
BPSMerge = _Class('BPSMerge')
BPSSequence = _Class('BPSSequence')
BPSRemoveDuplicates = _Class('BPSRemoveDuplicates')
BPSSubscription = _Class('BPSSubscription')
BPSEmpty = _Class('BPSEmpty')
BPSReduceProducer = _Class('BPSReduceProducer')
BPSFilterProducer = _Class('BPSFilterProducer')