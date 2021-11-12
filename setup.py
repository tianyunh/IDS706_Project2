from setuptools import setup, find_packages

setup(
    name="csv-linter",
    description="lint csv files",
    packages=find_packages(),
    author="Tianyun Hou",
    entry_points="""
    [console_scripts]
    csv-linter=csv_linter:main
    """,
    install_requires=["click==7.1.2", "pandas==1.2.0"],
    version="0.0.1"
)
