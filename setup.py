from setuptools import setup

VERSION = "0.0.1"

setup(
    name="jiami",
    version=VERSION,
    description="encrypt/decrypt text with password",
    author="Cliff Xuan",
    py_modules=["cli"],
    install_requires=["click", "cryptography"],
    extras_require={"dev": ["pytest"]},
    entry_points="""
        [console_scripts]
        jiami=cli.main:cli
    """,
)
