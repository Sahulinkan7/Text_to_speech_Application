from setuptools import setup,find_packages
HYPHEN_E_DOT="-e ."

def get_requirements(filename="requirements.txt"):
    with open(filename,'r') as file:
        requirements=file.readlines()
        requirements=[r.replace("\n","") for r in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
        return requirements

def get_long_description():
    with open("README.md",'r') as file:
        content=file.read()
        return content
    
setup(
    name="Text_to_speech",
    author_email="sahulinkan7@gmail.com",
    author="Linkan Kumar Sahu",
    packages=find_packages(),
    install_requires=get_requirements(),
    version="0.0.1",
    long_description=get_long_description()
)