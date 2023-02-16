from setuptools import setup, find_packages

setup_info = dict(
    name="watchtower_cli",
    version="0.0.1",
    author="Nick Cleary",
    author_email="nicholas.e.cleary@gmail.com",
    url="https://github.com/NickClearyTech/git-watchtower",
    description="A CLI to interact with the Git Watchtower service",
    license_files=["LICENSE"],
    license="MIT",
    platforms=[
        "Unix"
    ],
    python_requires=">=3.10",
    install_requires=[
        "click>8.1"
    ],
    packages=["watchtower"] + ["watchtower." + pkg for pkg in find_packages("watchtower")],
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "watchtower=watchtower.main:main"
        ]
    }
)

setup(**setup_info)