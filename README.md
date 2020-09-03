# Apple Frameworks Python

This project contains +400 Python scripts, each one has the name of an Apple framework and declares all of its classes. It depends on [rubicon.objc](https://rubicon-objc.readthedocs.io/en/latest/).

The script `make_frameworks.py` generates every script from the loaded frameworks. It uses the Objective-C runtime to detect every registered class. 

Private frameworks are prefixed with an underscore.

The script was executed from Pyto 13.0 on iOS 14.0 beta 6.

## Usage

```python
from Foundation import NSBundle

bundle_path = str(NSBundle.mainBundle.bundleURL.path)
```