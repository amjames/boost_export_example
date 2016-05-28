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
  - main.py
    - main python program to generate mandelbrot plots
    - arguments are documented in the source code, will run with defualts `python viewlims.py` 
    - requires module has already been built
  - runtest.py
    - test memory usage by generating several data sets. 
    - @profile directive in souce code requires this script be run using mprof 
  - runtest.sh
    - runs the memory profiling test 
    - qsub this script to request a compute node for testing (to memory intensive for the head node) 
  
## build instructions 
  - Requirements:
    - Open MP
    - Boost library (tested with v. 1.58.0)
    - boost python (tested with v. 1.58.0)
    - gnu make
    - python interpeter and headers 
  - Suggested modules (blueridge/newriver @ VT): `module purge` then `module load` the folowing
    - `gcc/4.7.2` (required for anaconda)
    - `Anaconda`
    - `Anaconda-boost/1.58.0`
  - To build and run main.py run:
    - `make` in the top source directory 
    - `python main.py (optional arguments)`
    - Note: an error will occur unless you have logged with X11 forwarding 
  - To run memory tests
    - create a local anaconda environment 
      - `conda create -n myenv --clone/opt/apps/Anaconda/2.3.0`
      - `source activate myenv` 
    - Install the python memory profiler
      - `conda install mprof`
    - if you have not named the environement myenv then edit the runtes.sh script accordingly 
    - `qsub runtest.sh`
    - you can see the mprof documentation for viewing the profile results 

      - 
  
