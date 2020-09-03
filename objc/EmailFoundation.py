
'''
Classes from the 'EmailFoundation' framework.
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
    
    
EFWatchdog = _Class('EFWatchdog')
EFStringHash = _Class('EFStringHash')
EFStoppableScheduler = _Class('EFStoppableScheduler')
EFSQLUpsertStatement = _Class('EFSQLUpsertStatement')
EFSQLUpdateStatement = _Class('EFSQLUpdateStatement')
EFSQLUnaryExpression = _Class('EFSQLUnaryExpression')
EFSQLTableSchema = _Class('EFSQLTableSchema')
EFSQLSelectStatement = _Class('EFSQLSelectStatement')
EFSQLSchema = _Class('EFSQLSchema')
EFSQLRow = _Class('EFSQLRow')
EFSQLQueryGenerator = _Class('EFSQLQueryGenerator')
EFSQLPropertyMapper = _Class('EFSQLPropertyMapper')
EFSQLPreparedStatement = _Class('EFSQLPreparedStatement')
EFSQLOrderExpression = _Class('EFSQLOrderExpression')
EFSQLObjectPropertyMapper = _Class('EFSQLObjectPropertyMapper')
EFSQLInsertStatement = _Class('EFSQLInsertStatement')
EFSQLIndexSchema = _Class('EFSQLIndexSchema')
EFSQLIndexedColumnSchema = _Class('EFSQLIndexedColumnSchema')
EFSQLGeneratorComparisonPredicateNode = _Class('EFSQLGeneratorComparisonPredicateNode')
EFSQLGeneratorCompoundPredicateNode = _Class('EFSQLGeneratorCompoundPredicateNode')
EFSQLAggregateFunction = _Class('EFSQLAggregateFunction')
EFSQLFunction = _Class('EFSQLFunction')
EFSQLOrderByExpressionGenerator = _Class('EFSQLOrderByExpressionGenerator')
EFSQLSelectExpressionGenerator = _Class('EFSQLSelectExpressionGenerator')
EFSQLJoinOnExpressionGenerator = _Class('EFSQLJoinOnExpressionGenerator')
EFSQLGeneratorTableRelationship = _Class('EFSQLGeneratorTableRelationship')
EFSQLExpressionGenerator = _Class('EFSQLExpressionGenerator')
EFSQLBitExpressionGenerator = _Class('EFSQLBitExpressionGenerator')
EFParenthesizedSQLExpression = _Class('EFParenthesizedSQLExpression')
EFSQLDeleteStatement = _Class('EFSQLDeleteStatement')
EFSQLConnection = _Class('EFSQLConnection')
EFSQLOrExpression = _Class('EFSQLOrExpression')
EFSQLAndExpression = _Class('EFSQLAndExpression')
EFSQLColumnSchema = _Class('EFSQLColumnSchema')
EFSQLColumnExpression = _Class('EFSQLColumnExpression')
EFSQLDisqualifiedColumnExpression = _Class('EFSQLDisqualifiedColumnExpression')
EFSQLColumn = _Class('EFSQLColumn')
EFSQLCaseExpression = _Class('EFSQLCaseExpression')
EFSQLBinding = _Class('EFSQLBinding')
EFSQLBitExpression = _Class('EFSQLBitExpression')
EFSQLLikeEscapedExpression = _Class('EFSQLLikeEscapedExpression')
EFSQLBinaryExpression = _Class('EFSQLBinaryExpression')
EFSearchableIndexObjectPropertyMapper = _Class('EFSearchableIndexObjectPropertyMapper')
EFSchedulerTrampoline = _Class('EFSchedulerTrampoline')
EFScheduler = _Class('EFScheduler')
EFSandboxedURLWrapper = _Class('EFSandboxedURLWrapper')
EFResource = _Class('EFResource')
EFResourcePool = _Class('EFResourcePool')
EFQueue = _Class('EFQueue')
EFQuery = _Class('EFQuery')
EFProcessTransaction = _Class('EFProcessTransaction')
EFProcessBoost = _Class('EFProcessBoost')
EFPrivacy = _Class('EFPrivacy')
EFPriorityDesignator = _Class('EFPriorityDesignator')
EFPathComponent = _Class('EFPathComponent')
EFPair = _Class('EFPair')
EFSQLBetweenExpression = _Class('EFSQLBetweenExpression')
EFOperationQueueScheduler = _Class('EFOperationQueueScheduler')
EFObserver = _Class('EFObserver')
EFMutableInt64Set = _Class('EFMutableInt64Set')
EFMutableIndexMap = _Class('EFMutableIndexMap')
EFMeasuredObject = _Class('EFMeasuredObject')
EFQueueScheduler = _Class('EFQueueScheduler')
EFMainThreadScheduler = _Class('EFMainThreadScheduler')
EFLRUCache = _Class('EFLRUCache')
EFLocked = _Class('EFLocked')
EFLinearFunction = _Class('EFLinearFunction')
EFLazyCache = _Class('EFLazyCache')
EFImmediateScheduler = _Class('EFImmediateScheduler')
EFHTMLUtilities = _Class('EFHTMLUtilities')
EFPromise = _Class('EFPromise')
EFFuture = _Class('EFFuture')
EFLazyFuture = _Class('EFLazyFuture')
EFDevice = _Class('EFDevice')
EFDebouncer = _Class('EFDebouncer')
EFCoalescer = _Class('EFCoalescer')
EFInvocationToken = _Class('EFInvocationToken')
EFDeallocInvocationToken = _Class('EFDeallocInvocationToken')
EFCancelationToken = _Class('EFCancelationToken')
EFAutoCancelationToken = _Class('EFAutoCancelationToken')
EFByteSet = _Class('EFByteSet')
EFMutableByteSet = _Class('EFMutableByteSet')
EFAutoBugCaptureReporter = _Class('EFAutoBugCaptureReporter')
EFObservable = _Class('EFObservable')
EFFileWrapper = _Class('EFFileWrapper')
EFSortDescriptor = _Class('EFSortDescriptor')