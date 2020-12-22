import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="playwright-stealth",
    version="1.0.4",
    author="ASAS1314",
    author_email="lcjasas@sina.com",
    description="playwright stealth",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ASAS1314/playwright_stealth",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_data={"playwright_stealth": ["js/*.js"]},
)
