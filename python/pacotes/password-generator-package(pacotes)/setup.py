from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="password_generator_guirib00",
    version="0.0.1",
    author="guirib00",
    author_email="guilhermerib2013@hotmail.com",
    description="Estudante de Analise e desenvolvimento - Fatec RL",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/guirib00/python-data-engineering-DIO",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)