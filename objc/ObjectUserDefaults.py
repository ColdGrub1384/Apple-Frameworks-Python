
'''
Classes from the 'ObjectUserDefaults' framework.
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
    
    
PodsDummy_ObjectUserDefaults = _Class('PodsDummy_ObjectUserDefaults')
ObjectUserDefaults.ObjectUserDefaultsItem = _Class('ObjectUserDefaults.ObjectUserDefaultsItem')
ObjectUserDefaults.ObjectUserDefaults = _Class('ObjectUserDefaults.ObjectUserDefaults')