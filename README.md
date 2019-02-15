# Python ppm Image Processor 
This program performs a range of functions that edit ppm images. 

### Main Functions 
read_file(file): 
  returns a dictionary of file attributes (ppm encoding, # of columns and rows, max color value, and the pixels)
 
object_filter(file1, file2, file3): 
  finds differences in images and replaces unique pixels that are not shared among all three with the majority pixel value 
 
flip_horizontal(file): 
  returns the mirror image of the input file 
 
shades_of_grey(file): 
  averages the rgb values of every pixel to convert the whole image to grayscale 
  
negate(file, color): 
  replaces every pixel's specified color value with the difference between max color value and the color value, effectively inverting the color in the image

