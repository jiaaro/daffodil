from distutils.core import setup

# TODO: in the future distribute c sources instead of pyx files
#   https://stackoverflow.com/questions/4505747/how-should-i-structure-a-python-package-that-contains-cython-code
from Cython.Build import cythonize
import Cython.Compiler.Options
Cython.Compiler.Options.cimport_from_pyx = True


setup(
    name='daffodil',
    version='0.5.0',
    author='James Robert',
    description='A Super-simple DSL for filtering datasets',
    license='MIT',
    keywords='data filtering',
    url='https://github.com/mediapredict/daffodil',
    packages=['daffodil'],
        ext_modules=cythonize(
        'daffodil/*.pyx',
        compiler_directives={
            'language_level': "3",
            'profile': True,
        }
    ),
    long_description='A Super-simple DSL for filtering datasets',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Utilities'
    ]
)
