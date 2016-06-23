import logging


class Logger(object):
    def __init__(self):
        self.logger = logging
        self.logger.basicConfig(filename='superoctochainsaw.log', level=logging.DEBUG, format='%(asctime)s %level%s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

    def log(self, msg):
        logger.log(msg)
