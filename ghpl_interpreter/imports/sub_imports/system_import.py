import sys

sys.path.insert(0, './ghpl_interpreter/imports/sub_imports/sub_system/')

from ghpl_interpreter.imports.sub_imports.sub_system.system_logs import System_logs
from ghpl_interpreter.imports.sub_imports.sub_system.system_variables import System_variables

class System_import:

    def __init__(self, data):
        return

    def check_system_imports(self, v):
        if v == 'system.*':
            cache_folder = './ghpl_cache/'

            f = open( cache_folder + "cache_imports_1.ghplc", "w")
            f.write("import system.variables.64bits\n")
            f.write("import system.logs")
            f.close()
        if v == 'system.logs':
            System_logs.system_logs(self, v)
        if v == 'system.variables.64bits':
            System_variables.system_variables(self, v)
