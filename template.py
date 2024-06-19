import os
from pathlib import Path

project_name="Text_To_Speech_SRC"

list_of_files=[
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/exception/__init__.py",
    f"requirements.py",
    "Dockerfile",
    ".dockerignore",
    "app.py",
    "setup.py",
]


for file in list_of_files:
    filepath=Path(file)
    filedir,filename=os.path.split(filepath)
    
    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
    
    if not (os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass
    else:
        print("file already exists")
    