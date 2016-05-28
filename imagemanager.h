#include <iostream>
#include <complex>
#include <vector>
#include <algorithm>
#include <boost/python/list.hpp>
#include <boost/python/tuple.hpp>
#include <boost/python/to_python_converter.hpp>

// don't clutter the global namespace
namespace bp=boost::python;
  //image manager classpython wrapper for Mandelbrot and Julia classes
class ImageManager
{
  public:
    //constructor
    ImageManager(int px_w, int px_h, const std::string& ty);
    //default constructor


    //publicly exposed python wrappers
    bp::list update(double new_x_min, double new_x_max, double new_y_min, double new_y_max,int iter);
    //python exposed members
    std::string type;
    int height;
    int width;


  private:
    int escape_it_mandelbrot(std::complex<double>& z0, int& max);
    /* int escapte_it_julia(std::complex<double> &z0); */
    void compute_mandelbrot(double x_min, double x_max, double y_min, double y_max, int iter);
    /* void compute_julia(double x_min, double x_max, double y_min, double y_max, int iter); */

    //private (c++ only )members
    std::vector<int> priv_data;

};
