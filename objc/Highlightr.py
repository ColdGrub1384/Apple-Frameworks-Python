
'''
Classes from the 'Highlightr' framework.
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
    
    
Highlightr.HTMLUtils = _Class('Highlightr.HTMLUtils')
PodsDummy_Highlightr = _Class('PodsDummy_Highlightr')
HighlightHints = _Class('HighlightHints')
Highlightr.Theme = _Class('Highlightr.Theme')
Highlightr.Highlightr = _Class('Highlightr.Highlightr')
CodeAttributedString = _Class('CodeAttributedString')