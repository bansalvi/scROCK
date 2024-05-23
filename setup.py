import os
from distutils.core import setup

try:
    readme = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()
except:
    readme = ''

version = '0.0.1'

install_requires = ['numpy', 'scipy', 'torch', 'tqdm', 'scikit-learn', 'matplotlib']

setup(
    name='scrock',
    version=version,
    description="scROCK (single-cell Refinement Of Cluster Knitting) is an algorithm for correcting cluster labels for scRNA-seq data",
    long_description=readme,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
    ],
    keywords='scRNA-seq, ADE, scROCK',
    author='dos257',
    author_email='149811921+dos257@users.noreply.github.com',
    url='https://github.com/dos257/ADE',
    py_modules=['scrock'],
    license='MIT',
    install_requires=install_requires,
)