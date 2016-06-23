import sys,os, ConfigParser


class ConfigReader:
    """
        Read configuration file in dosini format

    """
    conf = 'config'
    dotconf = '.SuperOctoChainsaw.conf'

    def __init__(self, projectName):
        self.projectName = projectName
        self.config = None
        self.fileLocs = dict()
        self.filelocs[conf] = set()
        self.fileLocs[conf].add(os.path.join(os.path.get("XDG_CONFIG_HOME"), 'SuperOctoChainsaw')
        self.fileLocs[dotconf] = set()
        self.fileLocs[dotconf].add(os.curdir)
        self.fileLocs[dotconf].add(os.path.expanduser("~")

    def read(self):
        for filename, path in self.fileLocs:
            fullpath = os.path.join(path, filename)
            try:
                with open(fullpath) as source:
                    config.readfp(source)
            except IOError:
               pass

        if self.config == None:
            #TODO: Add Logger!
