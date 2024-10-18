import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = 'Win32Gui'

setup(
    name='Check class',
    version='1.0',
    description='marca a quantidade de aulas informadas de uma determinado curso da plataforma OneBitCode',
    author='Alexsander Sautier',
    executables=[Executable('main.py', base=base, icon="robot.ico")]
)