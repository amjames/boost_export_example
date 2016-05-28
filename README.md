# boost_export_example
Example of python module written in c++ using boost-python 


##Files
  - imagemanager.h 
    - defines the class which we will export to python
  - mandelbrot.cc
    - implementation of the imagemanager class
    - also defines wrapper function for boost export 
  - boost.cc
    - defines the actual exported class
    - note that only one function (the wrapper ImageManager::update) is exported to python
  - setup.py 
    - builds the python module as a shared library using python distutils 
  
