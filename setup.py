import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="crim-T-GCN",
    version="0.1",
    author="Luis Da Costa (for CRIM)",
    author_email="luis.dacosta@crim.ca",
    description="Fork of T-GCN",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/crim-ca/T-GCN",
    packages=setuptools.find_packages(),
    install_requires=[
        "tensorflow",
        "pandas",
        "numpy",
        "Pigments",
        "sklearn",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
