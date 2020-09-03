
'''
Classes from the 'Zip' framework.
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
    
    
Zip.ZipUtilities = _Class('Zip.ZipUtilities')
Zip.Zip = _Class('Zip.Zip')
PodsDummy_Zip = _Class('PodsDummy_Zip')