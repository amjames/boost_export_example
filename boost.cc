
#include <iostream>
#include <complex>
#include <vector>
#include <utility>

#include "imagemanager.h"


#include <boost/python.hpp>
#include <boost/python/module.hpp>
#include <boost/python/def.hpp>
#include <boost/python/list.hpp>

namespace bp = boost::python;
BOOST_PYTHON_MODULE(fractal)
{
  bp::class_<ImageManager>("ImageManager",bp::init<int,int,std::string>())
    .def("update",&ImageManager::update)
    .def_readwrite("type",&ImageManager::type)
    .def_readwrite("height",&ImageManager::height)
    .def_readwrite("width",&ImageManager::width);

}









