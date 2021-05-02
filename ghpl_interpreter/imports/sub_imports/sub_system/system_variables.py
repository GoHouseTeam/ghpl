class System_variables:

    def __init__(self, data):
        return

    def system_variables(self, v):
        cache_folder = './ghpl_cache/'

        if v == 'system.variables.64bits':
            f = open( cache_folder + "cache_imports_1.ghplc", "w")
            f.writelines("import system.variables.64bits\n")
            f.close()
