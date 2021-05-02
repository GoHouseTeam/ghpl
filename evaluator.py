import os
import sys
import logging

sys.path.insert(0, './ghpl_interpreter/imports/')
from ghpl_interpreter.imports.main_import import Main_import

sys.path.insert(0, './ghpl_interpreter/system/logs/')
from ghpl_interpreter.system.logs.create_logger import Create_logger

try:
    os.mkdir("ghpl_logs")
except OSError:
    print()
else:
    print()

logger = logging.getLogger('ghpl_interpreter_files')
logger.setLevel(logging.ERROR)
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='./ghpl_logs/ghpl_interpreter_files.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

class Evaluator:

    def __init__(self, AST):
        self.AST = AST
        pass

    def run(self, node):
        if isinstance(node, list):
            for n in node:
                for k, v in n.items():
                    self.execute([k, v])
        elif isinstance(node, dict):
            for k, v in node.items():
                self.execute([k, v])

    def execute(self, loc):
        if isinstance(loc[1], list):
            self.run(loc[1])
        elif loc[0] == 'say.console':
            self.say_console(loc[1])
        elif loc[0] == 'go.class':
            self.go_class(loc[1])
        elif loc[0] == 'system.stop':
            self.system_stop([1])
        elif loc[0] == 'int':
            self.int_ghpl(loc[1])
        elif loc[0] == 'system.exit':
            self.system_exit()
        elif loc[0] == 'int64':
            self.int_ghpl_64_bit(loc[1])
        elif loc[0] == 'import':
            self.import_ghpl(loc[1])
        elif loc[0] == 'create.logger':
            self.create_logger(loc[1])
        elif loc[0] == 'log.debug':
            self.log_debug(loc[1])
        elif loc[0] == 'log.info':
            self.import_ghpl(loc[1])
        elif loc[0] == 'log.warning':
            self.import_ghpl(loc[1])
        elif loc[0] == 'log.error':
            self.import_ghpl(loc[1])

    def say_console(self, v):
        print(v)

    def go_class(self, v):
        for node in self.AST:
            try:
                self.run(node[v])
            except KeyError:
                pass

    def system_stop(self, v):
        quit()

    def int_ghpl(self, v):
        #int_ghpl_max_value = int(2147483647)
        #test = v

        #if test < int_ghpl_max_value:
        #    print("Error with int32.")
        #else:
        print(v)

    def system_exit(self):
        os._exit(os.X_OK)

    def int_ghpl_64_bit(self, v):
        print(v)

    def import_ghpl(self, v):
        Main_import.check_imports(self, v)

    def create_logger(self, v):
        Create_logger.create_logger(self, v)

    def log_debug(self, v):
        f = open("./ghpl_cache/cache_imports_1.ghplc", "r")

        if f.read() == 'import system.logs':
            return
        else:
            logger.error("log.debug require: import system.logs")
            print("log.debug require: import system.logs")
            quit()
        
        try:
            f = open("./")
        except OSError:
            print()
        else:
            print()