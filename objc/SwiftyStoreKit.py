
'''
Classes from the 'SwiftyStoreKit' framework.
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
    
    
SwiftyStoreKit.InAppReceipt = _Class('SwiftyStoreKit.InAppReceipt')
SwiftyStoreKit.CompleteTransactionsController = _Class('SwiftyStoreKit.CompleteTransactionsController')
SwiftyStoreKit.RestorePurchasesController = _Class('SwiftyStoreKit.RestorePurchasesController')
SwiftyStoreKit.PaymentsController = _Class('SwiftyStoreKit.PaymentsController')
SwiftyStoreKit.InAppProductQueryRequestBuilder = _Class('SwiftyStoreKit.InAppProductQueryRequestBuilder')
SwiftyStoreKit.SwiftyStoreKit = _Class('SwiftyStoreKit.SwiftyStoreKit')
SwiftyStoreKit.InAppReceiptRefreshRequest = _Class('SwiftyStoreKit.InAppReceiptRefreshRequest')
PodsDummy_SwiftyStoreKit = _Class('PodsDummy_SwiftyStoreKit')
SwiftyStoreKit.InAppProductQueryRequest = _Class('SwiftyStoreKit.InAppProductQueryRequest')
SwiftyStoreKit.InAppReceiptVerificator = _Class('SwiftyStoreKit.InAppReceiptVerificator')
SwiftyStoreKit.PaymentQueueController = _Class('SwiftyStoreKit.PaymentQueueController')
SwiftyStoreKit.ProductsInfoController = _Class('SwiftyStoreKit.ProductsInfoController')