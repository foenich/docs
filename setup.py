from setuptools import setup, find_packages

setup(
    name="mkdocs-github-repos-plugin",
    version="0.1.0",
    description="MkDocs plugin to display GitHub organization repositories and releases",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/PPUC/docs",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "mkdocs>=1.0.0",
        "requests>=2.25.1",
    ],
    entry_points={
        "mkdocs.plugins": [
            "github_repos = plugins.github_repos:GitHubReposPlugin",
        ]
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
