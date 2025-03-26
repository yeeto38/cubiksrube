from setuptools import setup, find_packages

setup(
    name='Cubiks_Rube',  # Replace with your own program name
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'pygame',
        'numpy',
        # Standard library dependencies
        # 'tk',
        # 'random',
        # 'os',
        # 'csv',
        # 'math',
        # 'sys', 
        'pyinstaller'
        # Add any other dependencies your program needs
    ],
    entry_points={
        'console_scripts': [
            'my_program=my_program.main:main',  # Replace with your main entry point
        ],
    },
    author='yeeto38',
    author_email='',
    description='Rubik\'s Cube Utility',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yeeto38/cubiksrube',  # Replace with your project's URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)