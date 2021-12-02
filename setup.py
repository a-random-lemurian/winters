from setuptools import setup

setup(
    name="winters",
    description="Endless Sky utilities",
    version="0.1.0",
    author="Lemuria",
    install_requires=["Click"],
    entry_points={"console_scripts": ["winters = winters.entry:cli"]},
)
