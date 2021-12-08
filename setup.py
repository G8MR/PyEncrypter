import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyEncrypter",                     
    version="0.1.18",                        
    author="AwesomeYoungCoder",
    url = "https://github.com/AwesomeYoungCoder/PyEncrypter/",
    description="A simple yet secure encryption package.",
    long_description=long_description,      
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),    
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],                                      
    python_requires='>=3.6',                
    py_modules=["PyEncrypter"],             
    install_requires=[]                     
)
