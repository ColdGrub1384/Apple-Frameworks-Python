
'''
Classes from the 'FileBrowser' framework.
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
    
    
FileBrowser.FileParser = _Class('FileBrowser.FileParser')
FileBrowser.PreviewItem = _Class('FileBrowser.PreviewItem')
FileBrowser.PreviewManager = _Class('FileBrowser.PreviewManager')
FileBrowser.FBFile = _Class('FileBrowser.FBFile')
PodsDummy_FileBrowser = _Class('PodsDummy_FileBrowser')
FileBrowser.WebviewPreviewViewContoller = _Class('FileBrowser.WebviewPreviewViewContoller')
FileBrowser.PreviewTransitionViewController = _Class('FileBrowser.PreviewTransitionViewController')
FileBrowser.FileListViewController = _Class('FileBrowser.FileListViewController')
FileBrowser.FileBrowser = _Class('FileBrowser.FileBrowser')