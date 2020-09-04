'''
Classes from the 'AppSupportUI' framework.
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

    
NUIGridArrangement = _Class('NUIGridArrangement')
NUISizeCache = _Class('NUISizeCache')
NUIBoxArrangement = _Class('NUIBoxArrangement')
NUIGridDimension = _Class('NUIGridDimension')
_NUIViewContainerViewInfo = _Class('_NUIViewContainerViewInfo')
NUIWidgetGridView = _Class('NUIWidgetGridView')
NUIWidgetGridViewEmptyCell = _Class('NUIWidgetGridViewEmptyCell')
NUIContainerView = _Class('NUIContainerView')
NUIContainerFlowView = _Class('NUIContainerFlowView')
NUIContainerGridView = _Class('NUIContainerGridView')
NUIContainerBoxView = _Class('NUIContainerBoxView')
NUIContainerStackView = _Class('NUIContainerStackView')
NUIWidgetGridViewCell = _Class('NUIWidgetGridViewCell')
NUICollectionViewContainerCell = _Class('NUICollectionViewContainerCell')
NUITableViewContainerCell = _Class('NUITableViewContainerCell')
NUIContentScrollView = _Class('NUIContentScrollView')
