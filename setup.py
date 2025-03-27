import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='Cubiks_Rube',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'pygame',
        'numpy',
    ],
    extras_require={
        'dev': ['pyinstaller'],
    },
    entry_points={
        'console_scripts': [
            'cubiksrube=cubiksrube.main:main',
        ],
    },
    author='yeeto38',
    # author_email='your_email@example.com',
    description='Rubik\'s Cube Utility',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/yeeto38/cubiksrube',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)