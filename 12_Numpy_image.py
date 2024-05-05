import numpy
 import skimage.io, skimage.color
 import matplotlib.pyplot
 
 raspberry = skimage.io.imread(fname="raspberry.jpg", as_grey=False)
 apple = skimage.io.imread(fname="apple.jpg", as_grey=False)
 mango = skimage.io.imread(fname="mango.jpg", as_grey=False)
 lemon = skimage.io.imread(fname="lemon.jpg", as_grey=False)
 
 apple_hsv = skimage.color.rgb2hsv(rgb=apple)
 mango_hsv = skimage.color.rgb2hsv(rgb=mango)
 raspberry_hsv = skimage.color.rgb2hsv(rgb=raspberry)
 lemon_hsv = skimage.color.rgb2hsv(rgb=lemon)
 
 fruits = ["apple", "raspberry", "mango", "lemon"]
 hsv_fruits_data = [apple_hsv, raspberry_hsv, mango_hsv, lemon_hsv]
 idx = 0
 for hsv_fruit_data in hsv_fruits_data:
     fruit = fruits[idx]
     hist = numpy.histogram(a=hsv_fruit_data[:, :, 0], bins=360)
     matplotlib.pyplot.bar(left=numpy.arange(360), height=hist[0])
     matplotlib.pyplot.savefig(fruit+"-hue-histogram.jpg", bbox_inches="tight")
     matplotlib.pyplot.close("all")
     idx = idx + 1