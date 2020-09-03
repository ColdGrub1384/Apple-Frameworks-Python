'''
Classes from the 'CoreFoundation' framework.
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
    
    
CFPrefsDaemon = _Class('CFPrefsDaemon')
CFPDSourceLookUpKey = _Class('CFPDSourceLookUpKey')
CFPDSource = _Class('CFPDSource')
CFPDContainerSource = _Class('CFPDContainerSource')
CFPDCloudSource = _Class('CFPDCloudSource')
CFPDDataBuffer = _Class('CFPDDataBuffer')
CFPDPurgeableBuffer = _Class('CFPDPurgeableBuffer')
CFPDCFDataBuffer = _Class('CFPDCFDataBuffer')
NSException = _Class('NSException')
NSFileSecurity = _Class('NSFileSecurity')
NSDateComponents = _Class('NSDateComponents')
NSSharedKeySet = _Class('NSSharedKeySet')
NSInvocation = _Class('NSInvocation')
NSBlockInvocation = _Class('NSBlockInvocation')
NSCache = _Class('NSCache')
NSTaggedPointerStringCStringContainer = _Class('NSTaggedPointerStringCStringContainer')
NSMethodSignature = _Class('NSMethodSignature')
NSRunLoop = _Class('NSRunLoop')
NSUserDefaults = _Class('NSUserDefaults')
CFPrefsSource = _Class('CFPrefsSource')
CFPrefsConfigurationFileSource = _Class('CFPrefsConfigurationFileSource')
CFPrefsPlistSource = _Class('CFPrefsPlistSource')
CFPrefsCloudSource = _Class('CFPrefsCloudSource')
CFPrefsManagedSource = _Class('CFPrefsManagedSource')
CFPrefsSearchListSource = _Class('CFPrefsSearchListSource')
CFPrefsSuiteSearchListSource = _Class('CFPrefsSuiteSearchListSource')
NSEnumerator = _Class('NSEnumerator')
NSTaggedPointerString = _Class('NSTaggedPointerString')
NSBlock = _Class('NSBlock')
NSStream = _Class('NSStream')
NSOutputStream = _Class('NSOutputStream')
NSInputStream = _Class('NSInputStream')
NSCalendar = _Class('NSCalendar')
NSLocale = _Class('NSLocale')
NSTimer = _Class('NSTimer')
NSURL = _Class('NSURL')
NSNull = _Class('NSNull')
NSOrderedSet = _Class('NSOrderedSet')
NSMutableOrderedSet = _Class('NSMutableOrderedSet')
NSTimeZone = _Class('NSTimeZone')
NSSet = _Class('NSSet')
NSMutableSet = _Class('NSMutableSet')
NSDictionary = _Class('NSDictionary')
NSMutableDictionary = _Class('NSMutableDictionary')
NSSharedKeyDictionary = _Class('NSSharedKeyDictionary')
NSCFDictionary = _Class('NSCFDictionary')
NSConstantDictionary = _Class('NSConstantDictionary')
NSDate = _Class('NSDate')
NSConstantDate = _Class('NSConstantDate')
NSData = _Class('NSData')
NSConstantData = _Class('NSConstantData')
NSMutableData = _Class('NSMutableData')
NSCFData = _Class('NSCFData')
NSArray = _Class('NSArray')
NSConstantArray = _Class('NSConstantArray')
NSMutableArray = _Class('NSMutableArray')
NSCFArray = _Class('NSCFArray')