from ctypes import *
from rubicon.objc.api import ObjCClass
import sys

NSBundle = ObjCClass("NSBundle")

c = CDLL(None)
objc_getClassList = c.objc_getClassList
objc_getClassList.restype = c_int
objc_getClassList.argtypes = [c_void_p, c_int]

class_getName = c.class_getName
class_getName.restype = c_char_p
class_getName.argtypes = [c_void_p]

# Get all classes
count = objc_getClassList(None, 0)
buffer = (c_void_p * count)()
objc_getClassList(buffer, count)

# Separate between public and private frameworks
frameworks = {}
private_frameworks = {}

for i in range(count):
    n = class_getName(buffer[i])
    n = n.decode()      
    
    try:
        _class = ObjCClass(n)   
    except NameError:
        continue
    
    sys.__stdout__.write(n+"\n")
    bundle = NSBundle.bundleForClass(_class)
    
    framework = bundle.bundleURL.lastPathComponent.split(".")[0]
       
    _frameworks = frameworks
    
    if "PrivateFrameworks" in bundle.bundleURL.path and framework != "UIKitCore":
        _frameworks = private_frameworks
    
    if ".app" in bundle.bundleURL.path:
        _frameworks = private_frameworks
    
    # UIKitCore == UIKit
    if framework == "UIKitCore":
        framework = "UIKit"   
    
    if framework not in _frameworks:
        _frameworks[framework] = []

    _frameworks[framework].append(n)

# Nobody imports UIFoundation for UIFont or CoreFoundation for NSData
# I'm not sure if macOS has some cases like that with AppKit
if "UIFoundation" in private_frameworks and "UIKit" in frameworks:
    for _class in private_frameworks["UIFoundation"]:
        frameworks["UIKit"].append(_class)

if "CoreFoundation" in frameworks and "Foundation" in frameworks:
    for _class in frameworks["CoreFoundation"]:
        frameworks["Foundation"].append(_class)

if "AVFAudio" in frameworks and "AVFCapture" in private_frameworks and "AVFCore" in private_frameworks:
    frameworks["AVFoundation"] = []
    
    for _class in frameworks["AVFAudio"]+private_frameworks["AVFCore"]+private_frameworks["AVFCapture"]:
        frameworks["AVFoundation"].append(_class)

if "lib" in frameworks and "Foundation" in frameworks:
    for _class in frameworks["lib"]:
        frameworks["Foundation"].append(_class)

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
            python_name = _class.split('.')[-1]
            python_name = python_name.replace("<", "_")
            python_name = python_name.replace(">", "_")
            code += f"\n{python_name} = _Class('{_class}')"
        
        code += "\n"
        f.write(code)