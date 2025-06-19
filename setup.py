import cx_Freeze
from cx_Freeze import setup, Executable
executaveis = [
    Executable(script="main.py", icon="recursos/icone.ico", base="Win32GUI")
]
setup(
    name="Profanum Samsarae",
    version="1.0",
    description="Jogo Profanum Samsarae",
    author="João GWM",
    options={
        "build_exe": {
            "packages": ["pygame", "pyttsx3", "speech_recognition"],
            "include_files": ["recursos"]
        }
    },
    executables=executaveis
)
