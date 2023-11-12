from cx_Freeze import setup, Executable

base = None    

executables = [Executable("main.py", base=base)]

packages = ["idna", "pygame", "os", "time", "random"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "<LittleSoviet>",
    options = options,
    version = "0.1",
    description = 'A Game made by Float_3.14 <https://www.youtube.com/@float_3.14> \n This program contains GPL v.3.0. Please see the license',
    executables = executables
)