'''
Created on 5 feb. 2014

@author: Pieter
'''
from PIL import Image

def info(obj, spacing=10, collapse=1, attribute="callable"):
    """Print methods and doc strings.\nTakes module, class, list, dictionary, or string."""
    if attribute=="callable":
        methodList = [method for method in dir(obj) if callable(getattr(obj, method))]        
    elif attribute=="attribute":
        methodList = [method for method in dir(obj) if not callable(getattr(obj, method))]
    processFunc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)
    print "\n".join(["%s %s" %
                      (method.ljust(spacing),
                       processFunc(str(getattr(obj, method).__doc__)))
                     for method in methodList])

if __name__ == "__main__":
    print info.__doc__
    li = Image.open("dungeonz\\artwork\\cards\\red_anger.png")
    print li.__module__