import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="playwright_stealth",
    version="1.0.0",
    author="ASAS1314",
    author_email="lcjasas@sina.com",
    description="playwright stealth",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ASAS1314/playwright_stealth",
    packages=setuptools.find_packages(),
    package_data={"playwright_stealth": ["js/*.js"]},
)
