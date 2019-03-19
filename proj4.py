#project4-linhanning-auto52-2150504042
import cv2 as cv
import numpy as np
#OOP create class Pic
class Pic:
    def __init__(self, name, path):
         self.name=name
         self.path=path
         self.img=cv.imread(path,0)
         self.target_img=self.img
         print("[LOG]:Object {} created successfully!".format(self.name))
    def lowpass(self):
        temp_img=cv.GaussianBlur(self.img,(3,3),0)
        cv.imwrite('1-3x3_gaussin_lowpass_of_{}.bmp'.format(self.name),temp_img)
        print("[LOG]:1-3x3_gaussin_lowpass_of_{}.bmp created sucessfully!".format(self.name))
        temp_img=cv.GaussianBlur(self.img,(5,5),0)
        cv.imwrite('1-5x5_gaussin_lowpass_of_{}.bmp'.format(self.name),temp_img)
        print("[LOG]:1-5x5_gaussin_lowpass_of_{}.bmp created sucessfully!".format(self.name))
        temp_img=cv.GaussianBlur(self.img,(7,7),0)
        cv.imwrite('1-7x7_gaussin_lowpass_of_{}.bmp'.format(self.name),temp_img)
        print("[LOG]:1-7x7_gaussin_lowpass_of_{}.bmp created sucessfully!".format(self.name))
        temp_img = cv.medianBlur(self.img,3)
        cv.imwrite('1-3x3_mid_lowpass_of_{}.bmp'.format(self.name),temp_img)
        print("[LOG]:1-3x3_mid_lowpass_of_{}.bmp created sucessfully!".format(self.name))
        temp_img = cv.medianBlur(self.img,5)
        cv.imwrite('1-5x5_mid_lowpass_of_{}.bmp'.format(self.name),temp_img)
        print("[LOG]:1-5x5_mid_lowpass_of_{}.bmp created sucessfully!".format(self.name))
        temp_img = cv.medianBlur(self.img,5)
        cv.imwrite('1-7x7_mid_lowpass_of_{}.bmp'.format(self.name),temp_img)
        print("[LOG]:1-7x7_mid_lowpass_of_{}.bmp created sucessfully!".format(self.name))
    def gaussian(self):
        gaussian1_5 = cv.GaussianBlur(self.img,(5,5),1.5)
        cv.imwrite('2-5x5_gaussin_sigma1p5_lowpass_of_{}.bmp'.format(self.name),gaussian1_5)
        print("[LOG]:2-5x5_gaussin_sigma1p5_lowpass_of_{}.bmp created sucessfully!".format(self.name))
    
    
    def unsharpHighpass(self):
        height, width = self.img.shape
        temp = np.zeros([height, width], np.uint8)
        diff = np.zeros([height, width], np.int16)
        unsharp = cv.GaussianBlur(self.img, (3, 3), 0)
        for i in range(height):
            for j in range(width):
                diff[i][j] = self.img[i][j] - unsharp[i][j]
        for i in range(height):
            for j in range(width):
                if 0.2*diff[i][j] + self.img[i][j] <= 255:
                    temp[i][j] = 0.2*diff[i][j] + self.img[i][j]
                else:
                    temp[i][j] = 255
        cv.imwrite('3-unsharp_highpass_of_{}.bmp'.format(self.name),temp)
        print("[LOG]:3-unsharp_highpass_of_{}.bmp created sucessfully!".format(self.name))
    def sobelHighpass(self):
        temp1 = cv.Sobel(self.img,cv.CV_16S,1,0)
        temp2 = cv.Sobel(self.img,cv.CV_16S,0,1)
        temp1 = cv.convertScaleAbs(temp1)
        temp2 = cv.convertScaleAbs(temp2)
        temp = cv.addWeighted(temp1,0.5,temp2,0.5,0)
        cv.imwrite('3-sobel_highpass_of_{}.bmp'.format(self.name),temp)
        print("[LOG]:3-sobel_highpass_of_{}.bmp created sucessfully!".format(self.name))
    def laplaceHighpass(self):
        temp=cv.Laplacian(self.img,cv.CV_16S)
        temp=cv.convertScaleAbs(temp)
        cv.imwrite('3-laplace_highpass_of_{}.bmp'.format(self.name),temp)
        print("[LOG]:3-laplace_highpass_of_{}.bmp created sucessfully!".format(self.name))
    def cannyHighpass(self,min,max):
        temp=cv.GaussianBlur(self.img,(7,7),0)
        temp=cv.Canny(temp,min,max)
        cv.imwrite('3-canny_highpass_of_{}.bmp'.format(self.name),temp)
        print("[LOG]:3-canny_highpass_of_{}.bmp created sucessfully!".format(self.name))



test1=Pic("test1","/home/hanninglin/Documents/CV/PROJECT/hw4/4th/test1.pgm")
test2=Pic("test2","/home/hanninglin/Documents/CV/PROJECT/hw4/4th/test2.tif")
test3=Pic("test3_corrupt","/home/hanninglin/Documents/CV/PROJECT/hw4/4th/test3_corrupt.pgm")
test4=Pic("test4","/home/hanninglin/Documents/CV/PROJECT/hw4/4th/test4.tif")
test4_copy=Pic("test4","/home/hanninglin/Documents/CV/PROJECT/hw4/4th/test4 copy.bmp")
#4-1
print("-------------------------------------")
print("#ANS:4-1 Lowpass\n")
# test1.lowpass()
# test2.lowpass()
#4-2
print("-------------------------------------")
print("#ANS:4-2 Gaussian\n")
test1.gaussian()
test2.gaussian()
#4-3
print("-------------------------------------")
print("#ANS:4-3 Highpass\n")
# test3.unsharpHighpass()
# test3.sobelHighpass()
# test3.laplaceHighpass()
# test3.cannyHighpass(50,150)
# test4.unsharpHighpass()
# test4.sobelHighpass()
# test4.laplaceHighpass()
# test4.cannyHighpass(50,150)
