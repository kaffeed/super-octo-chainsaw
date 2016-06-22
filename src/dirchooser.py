import sys,os

class DirChooser():
    __init__(self, path):
        self.path=path
        self.files=[]

    prepare():
        for dirname, dirnames, filename in os.walk(self.path):
            f = os.path.join(self.path, filename)
