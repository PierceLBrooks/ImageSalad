
# Author: Pierce Brooks

import sys
import traceback
import importlib

def run(name, module, arguments):
    success = True
    print("Module:\n"+name)
    try:
        result = module.run(arguments)
        if (result == None):
            success = False
            print("Module failure!")
        else:
            print("Module result:\n"+str(result))
    except:
        success = False
        print("Module problem!")
        traceback.print_exc()
    return success

if (__name__ == "__main__"):
    arguments = sys.argv
    length = len(arguments)
    if (length > 2):
        name = arguments[1]
        module = importlib.import_module(name)
        if (run(name, module, arguments[2:])):
            print("Success!")
        else:
            print("Failure!")
    else:
        print("You need to provide a module name argument followed by at least one argument for the module.")
