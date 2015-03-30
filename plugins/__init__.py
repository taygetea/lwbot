from os import listdir, path

current_directory = path.abspath(path.split(__file__)[0])
modules = {}
for module in listdir(current_directory):
    if module[-2:] == "py" and module is not "__init__.py":
        modname = module.split(".")[0]
        plugins.pomodoro = __import__("plugins." + "pomodoro.py")
