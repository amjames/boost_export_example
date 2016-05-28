PYTHON = python
GCC5 = g++
CP = /bin/cp
FRACTSOSRC= ./build/lib.*/fractal.so
FRACTSOTGT= ./fractal.so
RM = /bin/rm

all: fractal.so

fractal.so: mandelbrot.cc boost.cc setup.py
	$(PYTHON) setup.py build
	$(CP) $(FRACTSOSRC) $(FRACTSOTGT)


clean:
	$(RM) -rf build *.o *.so
