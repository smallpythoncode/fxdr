import setuptools

with open("README.md", "r") as rm:
    README = rm.read()
with open("CHANGELOG.md", "r") as cl:
    CHANGELOG = cl.read()

version = {}
with open("fxdr/_version.py") as vf:
    exec(vf.read(), version)

setuptools.setup(
    name="fxdr",
    version="0.0.0",
    author="smallpythoncode",
    author_email="smallpythoncode@gmail.com",
    # description="Does nothing.",
    long_description=README + "\n\n" + CHANGELOG,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    # install_requires=[
    #     "oandpyV20",
    #     "six",
    #     "v20",
    # ],
    include_package_data=True,
    url="https://github.com/smallpythoncode/fxdr",
    keywords="nothing",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3',

)
