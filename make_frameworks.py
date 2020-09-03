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
private_frameworks = {}

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
    
    _frameworks = frameworks
    
    if "PrivateFrameworks" in bundle.bundleURL.path and framework != "UIKitCore":
        _frameworks = private_frameworks
    
    if ".app" in bundle.bundleURL.path:
        _frameworks = private_frameworks
    
    if framework == "UIKitCore":
        framework = "UIKit"
    
    if framework not in frameworks:
        _frameworks[framework] = []

    _frameworks[framework].append(n)

all = {**frameworks, **private_frameworks}

for framework in all:
    name = framework
    if name in private_frameworks:
        name = "_"+name

    with open(name+".py", "w+") as f: 
        code = """'''
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
        
        for _class in all[framework]:
            code += f"\n{_class.split('.')[-1]} = _Class('{_class}')"
            
        f.write(code)