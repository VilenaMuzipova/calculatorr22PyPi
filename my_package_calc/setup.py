import setuptools

with open('readme.md', encoding='utf-8') as file:
    read_me_desc = file.read()


setuptools.setup(
    name='calculatorr22',
    version='0.1',
    author='Vilena',
    author_email='vilenamuzipova@gmail.com',
    description='calculator is a python method for simple math actions',
    long_description=read_me_desc,
    long_description_content_type="text/markdown",
    url='https://github.com/VilenaMuzipova/calculatorr22PyPi',
    packages=['calculatorr22'],
    install_requires=['logging'],
    python_requires='>=3.6'
)