MANDELBROT SET GENERATION AND VIEWING SOFTWARE

The mandelbrot set is a famous and beautiful fractal. It is based on the simple function f(z) = z*z + c, but the image this function generates has infinite depth and complexity. See numberphile's video for more info: https://www.youtube.com/watch?v=NGMRB4O922I

HOW TO USE

To run in linux, open a terminal in the same folder as the mandelbrot.py file and type

	python3 mandelbrot.py

 into the terminal. You should be able to run it with other operating systems or with an IDE as well. However you run it, make sure you have tkinter installed.

If you want to custom zoom in on the image, you can edit the main function on line 106. The inputs to the method MandDisplay define the zoom window and the resolution. It looks like this:

	M = MandDisplay(resolution, leftlimit, rightlimit, lowerlimit, upperlimit)

resolution is the number of data points across the diagonal, kind of like a tv screen. So a higher resolution means more definition and more pixels, but will also take longer to load.

Also on line 18 is 

	M.generate(50)

This tells the program to generate 50 iterations of the mandelbrot set. More iterations takes longer but is more accurate.

