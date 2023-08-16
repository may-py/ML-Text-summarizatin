import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.1"

REPO_NAME = "ML-Text-summarization"
AUTHOR_USER_NAME = 'MAYUR SUTHAR'
SEC_REPO = 'textSummarizer'
AUTHOR_EMAIL = 'mayur1601@yahoo.in'


setuptools.setup(
    name=SEC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Text Summarization",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/may-py/{REPO_NAME}/",
    project_urls={
        'Bug Tracker': f'https://github.com/may-py/{REPO_NAME}/issues'
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
