from setuptools import setup, find_packages

setup(
    name='gameboy-emulator',
    description='This is a Gameboy emulator, which allows you to play Gameboy games on your computer.',
    author='Rémi Boivin',
    author_email='remi.boivin@epitech.eu',
    url='https://github.com/remi-boivin/gameboy-emulator',
    packages=find_packages(exclude=['tests']),
    install_requires=[
        # List of dependencies
    ],
    tests_require=[
        # List of testing dependencies
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
    ],
    setup_requires=['setuptools_scm'],
    use_scm_version=True,
)
