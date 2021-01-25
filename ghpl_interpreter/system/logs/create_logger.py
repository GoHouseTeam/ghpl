class Create_logger:

    def __init__(self, data):
        return

    def create_logger(self, v):
        cache_folder = './ghpl_cache/'

        f = open("./ghpl_cache/cache_imports_1.ghplc", "r")

        if f.read() == 'import system.logs':
            f = open("./" + v + ".log", "w")
        
            f = open( cache_folder + "cache_createlogger_1.ghplc", "w")
            f.writelines("Ciao")
            return f.close()
        else:
            #logger.error("create.logger require: import system.logs")
            print("create.logger require: import system.logs")
            quit()

