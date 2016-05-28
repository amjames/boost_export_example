
#include <iostream>
#include <complex>
#include <vector>
#include <utility>

#include "imagemanager.h"


ImageManager::ImageManager(
    int px_w,
    int px_h,
    const std::string& ty)
{
  height = px_h;
  width  = px_w;
  type=ty;

}
/*
 * private member escape_it_mandelbrot(z0)
 * Given a complex number z0
 * determine z is candidate for the Mandelbrot set for a
 * given fixed number of iterations.
 *
 * if norm(z) is within radius compute next step
 * if norm (z) is outside of radius the return the iteration
 * at which it escapes
*/
int ImageManager::escape_it_mandelbrot(std::complex<double>& z0, int& max)
{
  std::complex<double> z=z0;
  for(int i=0; i<max; i++){
    if(norm(z)>=4) return i;
    z= z*z +z0;
  }
  return max;
}

/*
 * ImageManager private member compute_mendelbrot
 * input parameters x_max, x_min, y_max, y_min --> window limits for the image
 * each entry (n,m) corresponds to a pixel with coordinates  in the image the integer value is computed
 * private function m(z0) with z0 being a complex valued number compuetd:
 *  z0 = x_min +(n*(x_max-x_min)/width) + (i*(y_min+m*((y_max-y_min)/height)))
 */
void ImageManager::compute_mandelbrot(double x_min, double x_max, double y_min, double y_max, int iter)
{
  double dx = (x_max-x_min)/width;
  double dy = (y_max-y_min)/height;
  std::vector<int>  results(height*width);
  #pragma omp parallel for
  for(int i=0; i<height*width; i++){
    double row = i/height;
    double col = i%width;
    /* in this parallel a team of threads is created and each
     * is assigned an i value to work on in turn, each thread then
     * works on all j values for that i
     */
    // the results that this thread is working on is private to the thread (implicitly)
    double y = y_min + row*dy;
    double x = x_min + col*dx;
    //declare complex z0 x is re(z0), y im(z0)
    std::complex<double> z0(x,y);
    //compute integer value for this pixel
    // and store in this threads running result
    results[i] = escape_it_mandelbrot(z0,iter);
    //assign the threads y results to the outer vector
  }//this thread now picks up the next available i value
  //store in object
  priv_data=results;
}

#include <boost/python.hpp>
#include <boost/python/module.hpp>
#include <boost/python/def.hpp>
#include <boost/python/list.hpp>

boost::python::list ImageManager::update(double new_x_min, double new_x_max, double new_y_min, double new_y_max, int iter)
{
  boost::python::list py_result;
  //if we are to resample set the max itter to the original value + whatever value is in the center of the plot
  if (type=="mandelbrot") {
    compute_mandelbrot(new_x_min, new_x_max,new_y_min,new_y_max,iter);
  }else if (type =="julia"){
    std::cout << " not implemented error " <<std::endl;
    /* compute_julia(new_x_min,new_x_max,new_y_min,new_y_max, nitter); */
  }
  for(const auto &it1: priv_data){
    py_result.append(it1);
  }
  //set python exposed list of lists
  //return to caller
  return py_result;
}

