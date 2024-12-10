from setuptools import find_packages, setup

setup(
    name="GENAIAPPWITHOPENAI",
    version="0.0.1",
    author="Dixitha",
    author_email="dixithavishwaasrao@gmail.com",
    packages=find_packages(),
    install_requires=['python-dotenv','langchain ','langchain_community','ipykernel','arxiv']
)

