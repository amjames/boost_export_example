# Creates two identical panels.  Zooming in on the right panel will show
# a rectangle in the first panel, denoting the zoomed region.
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.widgets import Slider
import fractal
import time


# We just subclass Rectangle so that it can be called with an Axes
# instance, causing the rectangle to update its shape to match the
# bounds of the Axes
class UpdatingRect(Rectangle):
    def __call__(self, ax):
        self.set_bounds(*ax.viewLim.bounds)
        ax.figure.canvas.draw_idle()


# A class that will regenerate a fractal set as we zoom in, so that you
# can actually see the increasing detail.  A box in the left panel will show
# the area to which we are zoomed.
class Mandlebrot(object):
    def __init__(self, h=100, w=100,n=50):
        self.manager = fractal.ImageManager(h,w,'mandelbrot')
        self.niter=n
        self.xmin=-.7950
        self.xmax=-.7960
        self.ymin=0.1600
        self.ymax=0.1610
        raw_data=self.manager.update(self.xmin,self.xmax,self.ymin,self.ymax,self.niter)
        self.data=np.array(raw_data).reshape(self.manager.height,self.manager.width)

    def ext(self):
        return self.xmin,self.xmax,self.ymin,self.ymax


    def update_data(self):
        tstart=time.time()
        raw_data=self.manager.update(self.xmin,self.xmax,self.ymin,self.ymax,self.niter)
        self.data= np.array(raw_data).reshape(self.manager.height,self.manager.width)
        tend=time.time()
        print " update rendered in {}".format(abs(tstart-tend))

    def ax_update(self, ax):
        ax.set_autoscale_on(False)  # Otherwise, infinite loop


        # Get the range for the new area
        self.xmin, self.ymin, xdelta, ydelta = ax.viewLim.bounds
        self.xmax = self.xmin + xdelta
        self.ymax = self.ymin + ydelta


        # Update the image object with our new data and extent
        im = ax.images[-1]
        self.update_data()
        im.set_data(self.data)
        im.set_extent(self.ext())
        ax.figure.canvas.draw_idle()




md = Mandlebrot(h=2000,w=2000,n=200)
Z=md.data
fig1, (ax1,ax2) = plt.subplots(1, 2)
plt.subplots_adjust(left=0.15, bottom=0.25)
ax1.imshow(Z, origin='lower', extent=(md.ext()))
ax2.imshow(Z, origin='lower', extent=(md.ext()))

rect = UpdatingRect([0, 0], 0, 0, facecolor='None', edgecolor='black')
rect.set_bounds(*ax2.viewLim.bounds)
ax1.add_patch(rect)

# Connect for changing the view limits
ax2.callbacks.connect('xlim_changed', rect)
ax2.callbacks.connect('ylim_changed', rect)

ax2.callbacks.connect('xlim_changed', md.ax_update)
ax2.callbacks.connect('ylim_changed', md.ax_update)

def slider_update(val):
    newiter=int(val)
    im2 = ax2.images[-1]
    md.niter=newiter
    print "new iter_max is {}".format(md.niter)
    md.update_data()
    im2.set_data(md.data)
    ax2.figure.canvas.draw_idle()

slider_ax = plt.axes([0.15,0.01,0.5,0.10])
slider = Slider(slider_ax, ' nitter', valmin=100,valmax=10000,valinit=200)
slider.on_changed(slider_update)

plt.show()
