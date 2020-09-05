import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fxdr",
    version="0.0.0",
    author="smallpythoncode",
    author_email="smallpythoncode@gmail.com",
    description="Does nothing.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/smallpythoncode/fxdr",
    packages=setuptools.find_packages(),
    install_requires=[
        "oandapyV20",
        "six",
        "v20",
    ],



)