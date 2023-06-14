import logging

# create logger
module_logger = logging.getLogger('SampleLogger.xx')

class Auxiliary:
    def __init__(self):
        self.logger = logging.getLogger('SampleLogger.xx.Auxiliary')
        self.logger.info('1. creating an instance of Auxiliary')

    def do_something(self):
        self.logger.info('2. doing something')
        a = 1 + 1
        self.logger.warning('2.1 be carefull..')
        self.logger.error('2.2 something went wrong')
        self.logger.info('3. done doing something')

def some_function():
    module_logger.info('4. received a call to "some_function"')