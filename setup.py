from setuptools import setup

setup(
    name='binCircuit',
    version='1.0',
    py_modules=['all','graycode','parserBool','printer'],
    install_packages=['click','numpy'],
    install_requires=['click','numpy'],
    entry_points='''
        [console_scripts]
        bincircuit=all:cli
    '''
)
