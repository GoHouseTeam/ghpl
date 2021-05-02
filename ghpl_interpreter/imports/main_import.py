import sys
import logging

sys.path.insert(0, './ghpl_interpreter/imports/sub_imports')

from ghpl_interpreter.imports.sub_imports.system_import import System_import

#logger = logging.getLogger('ghpl_interpreter_imports')
#logger.setLevel(logging.DEBUG)
#handler = logging.FileHandler(filename='../ghpl_logs/ghpl_interpreter_imports.log', encoding='utf-8', mode='w')
#handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
#logger.addHandler(handler)

class Main_import:

    def __init__(self, data):
        return

    def check_imports(self, v):
        #system imports

        if v == 'system.*':
            System_import.check_system_imports(self, v)
        if v == 'system.variables.64bits':
            System_import.check_system_imports(self, v)
        if v == 'system.logs':
            System_import.check_system_imports(self, v)
        
            
