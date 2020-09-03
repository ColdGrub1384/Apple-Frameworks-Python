
'''
Classes from the 'ContactsAutocomplete' framework.
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
    
    
CNAutocompleteRecentsSearch = _Class('CNAutocompleteRecentsSearch')
CNAutocompleteResultTracing = _Class('CNAutocompleteResultTracing')
CNAutocompleteResultFactory = _Class('CNAutocompleteResultFactory')
CNAutocompleteSuggestionsSearch = _Class('CNAutocompleteSuggestionsSearch')
CNAutocompleteResult = _Class('CNAutocompleteResult')
CNAutocompleteGroupResult = _Class('CNAutocompleteGroupResult')
CNAutocompleteDuetContactResult = _Class('CNAutocompleteDuetContactResult')
CNAutocompleteCalendarServerResult = _Class('CNAutocompleteCalendarServerResult')
CNAutocompleteDirectoryServerResult = _Class('CNAutocompleteDirectoryServerResult')
CNAutocompleteExtensionResult = _Class('CNAutocompleteExtensionResult')
CNAutocompleteSuggestedContactResult = _Class('CNAutocompleteSuggestedContactResult')
CNAutocompleteRecentResult = _Class('CNAutocompleteRecentResult')
CNAutocompleteInfrequentRecentResult = _Class('CNAutocompleteInfrequentRecentResult')
CNAutocompleteFrequentRecentResult = _Class('CNAutocompleteFrequentRecentResult')
CNAutocompleteStoreQueryHelper = _Class('CNAutocompleteStoreQueryHelper')
CNAutocompleteCalendarServerSearch = _Class('CNAutocompleteCalendarServerSearch')
CNAutocompleteSourceInclusionPolicy = _Class('CNAutocompleteSourceInclusionPolicy')
CNAutocompleteResultValue = _Class('CNAutocompleteResultValue')
CNAutocompleteStoreQueryContext = _Class('CNAutocompleteStoreQueryContext')
CNAutocompleteCoreAnalyticsUsageMonitorProbe = _Class('CNAutocompleteCoreAnalyticsUsageMonitorProbe')
CNAutocompleteQueryResponseUniqueResultFinder = _Class('CNAutocompleteQueryResponseUniqueResultFinder')
CNAutocompleteQueryResponsePreparer = _Class('CNAutocompleteQueryResponsePreparer')
CNAutocompleteResultTokenMatcher = _Class('CNAutocompleteResultTokenMatcher')
CNAutocompleteFetchContext = _Class('CNAutocompleteFetchContext')
CNAutocompleteQueryCacheMissAuditor = _Class('CNAutocompleteQueryCacheMissAuditor')
CNAutocompleteAggdPerformanceProbe = _Class('CNAutocompleteAggdPerformanceProbe')
CNAutocompleteQuery = _Class('CNAutocompleteQuery')
CNAutocompleteQueryCacheHelper = _Class('CNAutocompleteQueryCacheHelper')
CNAutocompleteObservableBuilder = _Class('CNAutocompleteObservableBuilder')
CNAutocompleteNetworkActivityThrottlingPolicy = _Class('CNAutocompleteNetworkActivityThrottlingPolicy')
CNAutocompleteNetworkActivityPolicy = _Class('CNAutocompleteNetworkActivityPolicy')
CNAutocompleteNameComponents = _Class('CNAutocompleteNameComponents')
CNAutocompleteProbeKeyBuilder = _Class('CNAutocompleteProbeKeyBuilder')
CNAutocompleteRecentContactsTransform = _Class('CNAutocompleteRecentContactsTransform')
CNAutocompleteEntitlementVerifier = _Class('CNAutocompleteEntitlementVerifier')
CNAClassKitResultTransformVisitor = _Class('CNAClassKitResultTransformVisitor')
CNAutocompleteLocalSearch = _Class('CNAutocompleteLocalSearch')
CNAutocompleteDirectoryServerSearch = _Class('CNAutocompleteDirectoryServerSearch')
CNAutocompleteLocalExtensionSearch = _Class('CNAutocompleteLocalExtensionSearch')
CNAutocompleteLocalGroupsFetcher = _Class('CNAutocompleteLocalGroupsFetcher')
CNAutocompleteInputStringTokenizer = _Class('CNAutocompleteInputStringTokenizer')
CNAutocompleteSearchObservableProvider = _Class('CNAutocompleteSearchObservableProvider')
CNAutocompleteLocalContactsFetcher = _Class('CNAutocompleteLocalContactsFetcher')
CNAutocompleteObservableBuilderBatchingHelperFactory = _Class('CNAutocompleteObservableBuilderBatchingHelperFactory')
CNAutocompleteLocalQuery = _Class('CNAutocompleteLocalQuery')
CNAutocompleteLocalContactResultTransformBuilder = _Class('CNAutocompleteLocalContactResultTransformBuilder')
CNAutocompleteDuetSearch = _Class('CNAutocompleteDuetSearch')
CNAutocompleteFetchBlockDelegate = _Class('CNAutocompleteFetchBlockDelegate')
CNAutocompleteSearchProviderFactory = _Class('CNAutocompleteSearchProviderFactory')
CNAutocompleteTokenMatcher = _Class('CNAutocompleteTokenMatcher')
CNAutocompleteCalendarQueryAssembler = _Class('CNAutocompleteCalendarQueryAssembler')
CNAutocompleteStore = _Class('CNAutocompleteStore')
CNAutocompleteFetchRequestTracing = _Class('CNAutocompleteFetchRequestTracing')
CNAutocompleteFetchRequest = _Class('CNAutocompleteFetchRequest')
CNAutocompleteDelegateWrapper = _Class('CNAutocompleteDelegateWrapper')
CNAutocompleteCalendarServerOperationFactory = _Class('CNAutocompleteCalendarServerOperationFactory')
CNAutocompleteQueryCacheMissLogger = _Class('CNAutocompleteQueryCacheMissLogger')
CNAutocompleteStoreReproStringRecorder = _Class('CNAutocompleteStoreReproStringRecorder')
CNAutocompleteProbeProviderFactory = _Class('CNAutocompleteProbeProviderFactory')
CNAutocompleteSuggestionsProbe = _Class('CNAutocompleteSuggestionsProbe')
CNAutocompleteUsageMonitor = _Class('CNAutocompleteUsageMonitor')
CNAutocompleteAggdProbeAggdWrapper = _Class('CNAutocompleteAggdProbeAggdWrapper')
CNAutocompleteAggdProbe = _Class('CNAutocompleteAggdProbe')
CNAutocompleteUserSession = _Class('CNAutocompleteUserSession')
CNAutocompleteRecentContactsLibrary = _Class('CNAutocompleteRecentContactsLibrary')
CNAutocompleteObservable = _Class('CNAutocompleteObservable')