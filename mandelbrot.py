from tkinter import Tk, Canvas

class Mand:
    def __init__(self, resolution=1000, left=-2, right=1, low=-1, high=1):

        self.left = left
        self.right = right
        self.low = low
        self.high = high
        self.resolution = ((right-left)*(right-left)+(high-low)*(high-low))/resolution
        self.points = {} #fill this with data points that look like a + bi:c+di, where a + bi is a complex number
        self.populate()

    def populate(self):
        for i in range(int((self.high-self.low)//self.resolution)):
            for j in range(int((self.right-self.left)//self.resolution)):
                com = Complex(j*self.resolution+self.left, i*self.resolution+self.low)
                self.points[com] = (Complex(),True)

    def iterate(self):
        for point in self.points:
            com, ismand = self.points[point]
            if com.mag > 4:
                self.points[point] = com, False
            else:
                self.points[point] = (com*com + point, ismand)

    def generate(self, steps):
        for i in range(steps):
            print("generating step {0} out of {1}".format(i+1, steps), end="\r")
            self.iterate()
        print("generated {} steps".format(steps))

class MandDisplay(Mand):
    ytics = 20
    xtics = 20
    def __init__(self, resolution=1/256, left=-2, right=1, low=-1, high=1):
        Mand.__init__(self, resolution, left, right, low, high)
        self.root = Tk()
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        self.scal = min(screenheight/(self.high-self.low),
            screenwidth/(self.right-self.left))
        self.screenwidth = int(self.scal*(self.right-self.left))
        self.screenheight = int(self.scal*(self.high-self.low))
        self.can = Canvas(self.root, width=self.screenwidth, height=self.screenheight)
        self.can.pack()
        self.xpix = max(self.scal*self.resolution, 1)
        self.ypix = max(self.scal*self.resolution, 1)
        self.xticspace = (self.right - self.left)/self.xtics
        self.yticspace = (self.high - self.low)/self.ytics

    def place_dot(self, com, ismand):
        """com is a complex number"""
        x = self.scal*(com.re - self.left)
        y = self.scal*(self.high - com.im)
        #print(x,y)
        color = "blue"
        if ismand:
            color = "black"
        self.can.create_rectangle(int(x), int(y), int(x+self.xpix),
            int(y+self.ypix), outline=color, fill=color)

    def display(self):
        print("Displaying...")
        for point in self.points:
            com, ismand = self.points[point]
            self.place_dot(point, ismand)
        for i in range(0, self.screenheight, int(self.scal*self.yticspace)):
            self.can.create_line(0, i, 10, i, fill="green")
            self.can.create_text(15, i, fill="green", text=str(round(self.high - i/self.scal, 2)), anchor="w")

        for j in range(0, self.screenwidth, int(self.scal*self.xticspace)):
            self.can.create_line(j, 10, j, 20, fill="green")
            self.can.create_text(j, 45, fill="green", text=str(round(j/self.scal + self.left, 2)), anchor="s")

        self.root.mainloop()

class Complex:
    def __init__(self, a=0, b=0):
        self.re = a
        self.im = b
        self.mag = a*a + b*b

    def __add__(self, other):
        if type(other) is int:
            return Complex(self.re + other, self.im)
        return Complex(self.re + other.re, self.im + other.im)

    def __mul__(self, other):
        return Complex(self.re*other.re - self.im*other.im,
            self.re*other.im + self.im*other.re)

    def __str__(self):
        if self.im == 0:
            return str(self.re)
        if self.re == 0:
            if self.im == 1:
                return "i"
            return str(self.im) + "i"
        if self.im == 1:
            return "{0} + i".format(self.re)
        return "{0} + {1}i".format(self.re, self.im)

def main():
    M = MandDisplay(5000, -2, 1, -1, 1)
    #inputs are in order: resolution, left screen limit, right limit, lower, upper
    M.generate(30)


    M.display()

if __name__ == '__main__':
    main()
