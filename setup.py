import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="playwright-sm",
    version="0.0.1",
    author="AtuboDad",
    author_email="maxxrk@pm.me",
    description="playwright stealth",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MaxxRK/playwright_stealth",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_data={"playwright_stealth": ["js/*.js"]},
    python_requires=">=3.10",
    install_requires=[
        "playwright==1.52.0",
    ],
    extras_require={
        "test": [
            "pytest",
        ]
    },
)
