import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    print(f.read())
    
    long_description = f.read()
    
    
__version__ = "0.0.0"
    
AUTHOR_NAME = "Aman123lug"
SOCIAL_MEDIA = "lug__aman"
AUTHER_EMAIL = "ak06465676@gmail.com"
SRC_REPO = "cnnClassifier"
REPO_NAME = "End-to-End-Chicken-Disease-implementation"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHER_EMAIL,
    description="Solved Classification promlem using CNN",
    long_description=long_description,
    download_url = f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
    
)

