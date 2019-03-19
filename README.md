# 数字图像处理HW4
- 林汉宁  自动化52 2150504042
- 提交日期：2019-03-18
## 摘要
本次作业使用python3.67面向对象方式编程，使用了opencv与numpy等库。
## 技术讨论
### 1. 低通滤波
#### 源代码片段
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
#### 思路与结果
使用cv2.GaussianBlur与cv2.MedianBlur对图像进行滤波。
#### 结果展示
![Alt text](https://github.com/HanningLin/hw4/blob/master/img/1-7x7_mid_lowpass_of_test1.bmp)
![Alt text](https://github.com/HanningLin/hw4/blob/master/img/1-5x5_mid_lowpass_of_test1.bmp)
![Alt text](https://github.com/HanningLin/hw4/blob/master/img/1-3x3_mid_lowpass_of_test1.bmp)
![Alt text](https://github.com/HanningLin/hw4/blob/master/img/1-7x7_gaussin_lowpass_of_test1.bmp)
![Alt text](https://github.com/HanningLin/hw4/blob/master/img/1-5x5_gaussin_lowpass_of_test1.bmp)
![Alt text](https://github.com/HanningLin/hw4/blob/master/img/1-3x3_gaussin_lowpass_of_test1.bmp)
![Alt text](https://github.com/HanningLin/hw4/blob/master/img/1-7x7_mid_lowpass_of_test2.bmp)
![Alt text](https://github.com/HanningLin/hw4/blob/master/img/1-5x5_mid_lowpass_of_test2.bmp)
![Alt text](https://github.com/HanningLin/hw4/blob/master/img/1-7x7_gaussin_lowpass_of_test2.bmp)
![Alt text](https://github.com/HanningLin/hw4/blob/master/img/1-3x3_mid_lowpass_of_test2.bmp)
![Alt text](https://github.com/HanningLin/hw4/blob/master/img/1-5x5_gaussin_lowpass_of_test2.bmp)
![Alt text](https://github.com/HanningLin/hw4/blob/master/img/1-3x3_gaussin_lowpass_of_test2.bmp)
#### 结果分析：
由结果可看出，核的尺寸增大图像变得模糊。同尺度下高斯滤波与中值滤波效果类似

### 2.  固定方差高斯滤波器 
#### 源代码片段
	def gaussian(self):
        gaussian1_5 = cv.GaussianBlur(self.img,(5,5),1.5)
        cv.imwrite('2-5x5_gaussin_sigma1p5_lowpass_of_{}.bmp'.format(self.name),gaussian1_5)
        print("[LOG]:2-5x5_gaussin_sigma1p5_lowpass_of_{}.bmp created sucessfully!".format(self.name))
#### 代码思路
通过调整opencv库函数GaussianBlur第三个参数可实现指定方差高斯滤波
#### 结果展示
![Alt text](https://github.com/HanningLin/hw4/blob/master/img/2-5x5_gaussin_sigma1p5_lowpass_of_test2.bmp)
![Alt text](https://github.com/HanningLin/hw4/blob/master/img/2-5x5_gaussin_sigma1p5_lowpass_of_test1.bmp)




### 3.高通滤波
#### 源代码片段
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
#### 代码思路
使用cv2.sobel,cv2.gaussianblur,cv2.canny等函数实现
#### 最终结果
![Alt text](https://github.com/HanningLin/hw4/blob/master/img/3-unsharp_highpass_of_test3_corrupt.bmp)
![Alt text](https://github.com/HanningLin/hw4/blob/master/img/3-canny_highpass_of_test3_corrupt.bmp)
![Alt text](https://github.com/HanningLin/hw4/blob/master/img/3-canny_highpass_of_test4.bmp)
![Alt text](https://github.com/HanningLin/hw4/blob/master/img/3-laplace_highpass_of_test4.bmp)
![Alt text](https://github.com/HanningLin/hw4/blob/master/img/3-sobel_highpass_of_test4.bmp)
![Alt text](https://github.com/HanningLin/hw4/blob/master/img/3-unsharp_highpass_of_test4.bmp)
![Alt text](https://github.com/HanningLin/hw4/blob/master/img/3-laplace_highpass_of_test3_corrupt.bmp)
![Alt text](https://github.com/HanningLin/hw4/blob/master/img/3-sobel_highpass_of_test3_corrupt.bmp)



