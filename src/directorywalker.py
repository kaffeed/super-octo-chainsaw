import sys,os

class DirChooser():
    __init__(self, path):
        self.path=path
        self.files=[]
        self.logger = Logger()

    prepare():
        logger.log('Starting to prepare path ' + self.path)
        for dirname, dirnames, filename in os.walk(self.path):
            f = os.path.join(self.path, filename)
            files.append(f)
