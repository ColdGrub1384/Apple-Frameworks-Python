'''
Classes from the 'InputAssistant' framework.
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

    
InputAssistantView = _Class('InputAssistant.InputAssistantView')
InputAssistantCollectionView = _Class('InputAssistant.InputAssistantCollectionView')
