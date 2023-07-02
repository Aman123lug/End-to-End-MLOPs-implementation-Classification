import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    print(f.read())
    
    long_description = f.read()
    
    
AUTHER_NAME = "Aman123lug"
SOCIAL_MEDIA = "lug__aman"
AUTHER_EMAIL = "ak06465676@gmail.com"
PROJECT_NAME = "CnnClassifier"
REPO_NAME = "End-to-End-Chicken-Disease-implementation"


setuptools.setup(
    name=REPO_NAME,
    version="0.0.0",
    author=AUTHER_NAME,
    author_email=AUTHER_EMAIL,
    description="Solved Classification promlem using CNN",
    long_description=long_description,
    clone_url = f"https://github.com/{AUTHER_NAME}/{REPO_NAME}",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
    
)