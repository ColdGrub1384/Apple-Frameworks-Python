
'''
Classes from the 'Down' framework.
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
    
    
Down.DebugVisitor = _Class('Down.DebugVisitor')
Down.BaseNode = _Class('Down.BaseNode')
Down.ThematicBreak = _Class('Down.ThematicBreak')
Down.Text = _Class('Down.Text')
Down.Strong = _Class('Down.Strong')
Down.SoftBreak = _Class('Down.SoftBreak')
Down.Paragraph = _Class('Down.Paragraph')
Down.List = _Class('Down.List')
Down.Link = _Class('Down.Link')
Down.LineBreak = _Class('Down.LineBreak')
Down.Item = _Class('Down.Item')
Down.Image = _Class('Down.Image')
Down.HtmlInline = _Class('Down.HtmlInline')
Down.HtmlBlock = _Class('Down.HtmlBlock')
Down.Heading = _Class('Down.Heading')
Down.Emphasis = _Class('Down.Emphasis')
Down.Document = _Class('Down.Document')
Down.CustomInline = _Class('Down.CustomInline')
Down.CustomBlock = _Class('Down.CustomBlock')
Down.CodeBlock = _Class('Down.CodeBlock')
Down.Code = _Class('Down.Code')
Down.BlockQuote = _Class('Down.BlockQuote')
Down.AttributedStringVisitor = _Class('Down.AttributedStringVisitor')
PodsDummy_Down = _Class('PodsDummy_Down')
Down.DownView = _Class('Down.DownView')