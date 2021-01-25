class System_logs:

    def __init__(self, data):
        return

    def system_logs(self, v):
        cache_folder = './ghpl_cache/'

        if v == 'system.logs':
            f = open( cache_folder + "cache_imports_1.ghplc", "w")
            f.writelines("import system.logs")
            f.close()
