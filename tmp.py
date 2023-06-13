#run python3 tmp.py
#https://docs.python.org/3/howto/logging-cookbook.html#logging-cookbook

print("Running SampleLogger")

import logging
import auxiliary_module

# create logger with 'SampleLogger'
logger = logging.getLogger('SampleLogger')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler('spam.log')
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)

logger.info('a. creating an instance of auxiliary_module.Auxiliary')
a = auxiliary_module.Auxiliary()
logger.info('b. created an instance of auxiliary_module.Auxiliary')
logger.info('c. calling auxiliary_module.Auxiliary.do_something')

#tämä ei kirjoita!
a.do_something()
logger.info('d. finished auxiliary_module.Auxiliary.do_something')
logger.info('e. calling auxiliary_module.some_function()')

#tämä kirjoittaa
auxiliary_module.some_function()
logger.info('f. done with auxiliary_module.some_function()')