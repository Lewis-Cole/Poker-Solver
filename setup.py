import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

with open("LICENSE") as f:
    license_text = f.read()

setuptools.setup(
    name="Poker-Solver-Lewis-Cole",  # Replace with your own username
    version="0.0.1",
    author="Lewis Cole",
    author_email="lcole.mail@gmail.com",
    description="A poker computational package",
    long_description=long_description,
    long_description_content_type="rst",
    url="https://https://github.com/Lewis-Cole/Poker-Solver",
    license=license_text,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
