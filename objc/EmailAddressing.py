
'''
Classes from the 'EmailAddressing' framework.
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
    
    
EAEmailAddressParser = _Class('EAEmailAddressParser')
EAEmailAddressLists = _Class('EAEmailAddressLists')
EAEmailAddressGenerator = _Class('EAEmailAddressGenerator')
EAEmailAddressSet = _Class('EAEmailAddressSet')