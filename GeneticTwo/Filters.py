import math
import numpy as np
import PIL
from PIL import Image

class Filters:

    def __init__(self):
        pass

    def kernel(self,matrix,pos,form='+',kernel_size=1):
        vector = [matrix[pos[0]][pos[1]]]
        if(form=='+'):
            for x in range(1,kernel_size+1):
                vector.append(matrix[pos[0]-x][pos[1]])
                vector.append(matrix[pos[0]][pos[1]+x])
                vector.append(matrix[pos[0]+x][pos[1]])
                vector.append(matrix[pos[0]][pos[1]-x])
        if(form=='o'):
            for x in range(1,kernel_size+1):
                vector.append(matrix[pos[0]-x][pos[1]])
                vector.append(matrix[pos[0]][pos[1]+x])
                vector.append(matrix[pos[0]+x][pos[1]])
                vector.append(matrix[pos[0]][pos[1]-x])
                vector.append(matrix[pos[0]-x][pos[1]+x])
                vector.append(matrix[pos[0]+x][pos[1]+x])
                vector.append(matrix[pos[0]+x][pos[1]-x])
                vector.append(matrix[pos[0]-x][pos[1]-x])
        if(form=='x'):
            for x in range(1,kernel_size+1):
                vector.append(matrix[pos[0]-x][pos[1]+x])
                vector.append(matrix[pos[0]+x][pos[1]+x])
                vector.append(matrix[pos[0]+x][pos[1]-x])
                vector.append(matrix[pos[0]-x][pos[1]-x])
        if(form=='/'):
            for x in range(1,kernel_size+1):
                vector.append(matrix[pos[0]-x][pos[1]+x])
                vector.append(matrix[pos[0]+x][pos[1]-x])
        if(form=='\\'):
            for x in range(1,kernel_size+1):
                vector.append(matrix[pos[0]+x][pos[1]+x])
                vector.append(matrix[pos[0]-x][pos[1]-x])
        return vector


    def mediana(self, matrix, window, form='+', kernel_size=1,threshold=50):
        mat = matrix
        for x in range(kernel_size, len(matrix)-kernel_size, window):
            for y in range(kernel_size, len(matrix[0])-kernel_size, window):
                sample = self.kernel(matrix,(x,y),form,kernel_size)
                sample.sort()
                if(sample[math.floor(len(sample)/2)]>threshold):
                    mat[x][y] = 255
                else:
                    mat[x][y] = 0
        return mat

    def binary(self,matrix,trashold):
        mat = matrix
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                if(mat[x][y]>trashold):
                    mat[x][y] = 255
                else:
                    mat[x][y] = 0
        return mat

    def histograma(self, array):
        histogram = []
        for x in range(255):
            histogram.append(array.count(x))
        return histogram

    def sobel(self, img):
        width = img.size[0]
        height = img.size[1]
        newimg = Image.new("RGB", (width, height), "white")
        for x in range(1,width-1):
            for y in range(1, height-1):
                Gx = 0
                Gy = 0

                p = img.getpixel((x-1, y-1))
                r = p[0]
                g = p[1]
                b = p[2]

                intensity = r + g + b

                # accumulate the value into Gx, and Gy
                Gx += -intensity
                Gy += -intensity

                # remaining left column
                p = img.getpixel((x-1, y))
                r = p[0]
                g = p[1]
                b = p[2]

                Gx += -2 * (r + g + b)

                p = img.getpixel((x-1, y+1))
                r = p[0]
                g = p[1]
                b = p[2]

                Gx += -(r + g + b)
                Gy += (r + g + b)

                # middle pixels
                p = img.getpixel((x, y-1))
                r = p[0]
                g = p[1]
                b = p[2]

                Gy += -2 * (r + g + b)

                p = img.getpixel((x, y+1))
                r = p[0]
                g = p[1]
                b = p[2]

                Gy += 2 * (r + g + b)

                # right column
                p = img.getpixel((x+1, y-1))
                r = p[0]
                g = p[1]
                b = p[2]

                Gx += (r + g + b)
                Gy += -(r + g + b)

                p = img.getpixel((x+1, y))
                r = p[0]
                g = p[1]
                b = p[2]

                Gx += 2 * (r + g + b)

                p = img.getpixel((x+1, y+1))
                r = p[0]
                g = p[1]
                b = p[2]

                Gx += (r + g + b)
                Gy += (r + g + b)

                # calculate the length of the gradient (Pythagorean theorem)
                length = math.sqrt((Gx * Gx) + (Gy * Gy))

                # normalise the length of gradient to the range 0 to 255
                length = length / 4328 * 255

                length = int(length)

                # draw the length in the edge image
                #newpixel = img.putpixel((length,length,length))
                newimg.putpixel((x, y), (length, length, length))
        return newimg
