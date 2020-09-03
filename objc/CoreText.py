'''
Classes from the 'CoreText' framework.
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

    
FontAssetDownloadManager = _Class('FontAssetDownloadManager')
NSRubyAnnotation = _Class('NSRubyAnnotation')
NSCTRubyAnnotation = _Class('NSCTRubyAnnotation')
CTGlyphStorageInterface = _Class('CTGlyphStorageInterface')
CTFeatureSetting = _Class('CTFeatureSetting')
