'''
Classes from the 'CoreParsec' framework.
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

    
PARReply = _Class('PARReply')
PARRequest = _Class('PARRequest')
PARFlightSearchRequest = _Class('PARFlightSearchRequest')
PARLookupRequest = _Class('PARLookupRequest')
PARZeroKeywordRequest = _Class('PARZeroKeywordRequest')
PARCardRequest = _Class('PARCardRequest')
PARMoreResultsRequest = _Class('PARMoreResultsRequest')
PARSearchRequest = _Class('PARSearchRequest')
PARSearchReplayRequest = _Class('PARSearchReplayRequest')
PARSession = _Class('PARSession')
PARHashtagImagesVisibility = _Class('PARHashtagImagesVisibility')
PARImageLoader = _Class('PARImageLoader')
PARResponse = _Class('PARResponse')
PARFlightResponse = _Class('PARFlightResponse')
PARTask = _Class('PARTask')
PARNewsVisibility = _Class('PARNewsVisibility')
PARSmartSearchV2Parameters = _Class('PARSmartSearchV2Parameters')
PARSmartSearchV1Parameters = _Class('PARSmartSearchV1Parameters')
PARFuture = _Class('PARFuture')
PARPromise = _Class('PARPromise')
FutureValue = _Class('FutureValue')
PARAsyncMoreResults = _Class('PARAsyncMoreResults')
PARBag = _Class('PARBag')
PARAsyncCard = _Class('PARAsyncCard')
PARSyncCard = _Class('PARSyncCard')
PARSessionConfiguration = _Class('PARSessionConfiguration')
PARDefaultFactory = _Class('PARDefaultFactory')
PARSearchClient = _Class('PARSearchClient')
WeakSession = _Class('WeakSession')
PAREngagedCompletionCache = _Class('PAREngagedCompletionCache')
