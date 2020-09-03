'''
Classes from the 'GenerationalStorage' framework.
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

    
GSTemporaryStorage = _Class('GSTemporaryStorage')
GSStorageManager = _Class('GSStorageManager')
GSClientManagedLibrary = _Class('GSClientManagedLibrary')
GSPermanentStorage = _Class('GSPermanentStorage')
GSStagingPrefix = _Class('GSStagingPrefix')
GSDocumentIdentifier = _Class('GSDocumentIdentifier')
GSAddition = _Class('GSAddition')
GSTemporaryAddtionEnumerator = _Class('GSTemporaryAddtionEnumerator')
GSPermanentAdditionEnumerator = _Class('GSPermanentAdditionEnumerator')
GSDaemonProxySync = _Class('GSDaemonProxySync')
