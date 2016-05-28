#! /usr/bin/env python

import os
os.environ["CC"] = "gcc"
os.environ["CXX"]= "g++"
# print os.environ["ANACONDA_INC"]
# print os.environ["ANACONDA_LIB"]
# print os.environ["BOOST_LIB"]
# print os.environ["BOOST_INC"]

from distutils.core import setup
from distutils.extension import Extension

setup(name="fractalcreatorPkg",
        ext_modules=[
            Extension("fractal",["mandelbrot.cc","boost.cc"],
                extra_compile_args=['-fopenmp','-O3','-std=c++11'],
                extra_link_args=['-lgomp'],
                libraries=["boost_python"])
            ])


