from ctypes import *
from rubicon.objc.api import ObjCClass

NSBundle = ObjCClass("NSBundle")

c = CDLL(None)
objc_getClassList = c.objc_getClassList
objc_getClassList.restype = c_int
objc_getClassList.argtypes = [c_void_p, c_int]

count = objc_getClassList(None, 0)
buffer = (c_void_p * count)()
objc_getClassList(buffer, count)

class_getName = c.class_getName
class_getName.restype = c_char_p
class_getName.argtypes = [c_void_p]

frameworks = {}

for i in range(count):
    n = class_getName(buffer[i])
    n = n.decode()
    
    if n.startswith("_"):
        continue
    
    _class = ObjCClass(n)
    
    try:
        bundle = NSBundle.bundleForClass(_class)
    except NameError:
        continue
    
    framework = bundle.bundleURL.lastPathComponent.split(".")[0]
    if framework == "UIKitCore":
        framework = "UIKit"
    
    if framework not in frameworks:
        frameworks[framework] = []
    
    frameworks[framework].append(n)

for framework in frameworks:
    with open(framework+".py", "w+") as f: 
        code = """
'''
Classes from the '{}' framework.
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
    
    """.format(framework)
        
        for _class in frameworks[framework]:
            code += f"\n{_class} = _Class('{_class}')"
            
        f.write(code)        