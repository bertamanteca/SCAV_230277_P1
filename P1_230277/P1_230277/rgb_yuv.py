#ex1

def rgb2yuv(r,g,b):
    y= 0.299*r + 0.587*g +0.114*b
    u=0.492*(b-y)
    v=0.877 *(r-y)
    return y, u, v

def yuv2rgb(y,u,v ):
    r= y+1.13983*v
    g= y-0.39465*u - 0.58060*v
    b= y+2.03211*u

    return r,g,b

print("Red:")
r = float(input())
print("Green:")
g = float(input())
print("Blue:")
b = float(input())

[y2, u2, v2] = rgb2yuv(r, g, b)
print("Y: ", y2)
print("U: ", u2)
print("V: ", v2)

[r2,g2,b2] = yuv2rgb(y2, u2, v2)

print("Original ones ")
print("R: ", r2)
print("G: ", g2)
print("B: ", b2)

#ex2

import subprocess

def resize_and_reduce_quality(input_image_path, output_image_path):


    cmd= f'ffmpeg -i {input_image_path} -vf scale=360:360 {output_image_path}'
    subprocess.run(cmd, shell=True)


# Example
input_image_path = "photo_alexia.jpeg"
output_image_path = "photo_alexia_360.png"
resize_and_reduce_quality(input_image_path, output_image_path)



