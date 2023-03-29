import cv2
import numpy as np

def cartoonify(image):
    # 회색이미지로 바꾸기
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 블러적용하기
    gray = cv2.medianBlur(gray, 10)

    # adaptiveThreshold를 이용해 엣지 찾기
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

    # 이미지의 색상을 부드럽게 만들기 위해 사용
    color = cv2.bilateralFilter(image, 9, 250, 250)

    # 색상 정보와 엣지 정보를 결합
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    
    return cartoon

def pencilcartoon(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(25,25),0)
    pentoon = cv2.divide(gray,blur,scale = 250.0)
    
    return pentoon
    
def pencilcartoon2(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.medianBlur(gray, 5)
    laplace = cv2.Laplacian(blur, -1, ksize=3)
    invert = 255-laplace
    pencil_edge_img = cv2.threshold(invert,225,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY)
    
    return pencil_edge_img 

image = cv2.imread('image2cartoon.jpg')
cartoon = cartoonify(image)
pencilcartoon = pencilcartoon(image)
pencilcartoon2 = pencilcartoon2(image)

cv2.imwrite('cartoonfromimage.jpg', cartoon)
cv2.imwrite('pencilcartoon1.jpg', cartoon)
cv2.imwrite('pencilcartoon2.jpg', cartoon)