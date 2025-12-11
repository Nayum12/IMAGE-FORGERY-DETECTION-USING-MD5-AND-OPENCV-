import cv2
from md5hash import scan

def similar(first, second):    
# test image
    image = cv2.imread(first)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    histogram = cv2.calcHist([gray_image], [0],
                            None, [256], [0, 256])
    
    
    # data2 image
    image = cv2.imread(second)
    gray_image2 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    histogram2 = cv2.calcHist([gray_image2], [0],
                            None, [256], [0, 256])
    
    
    c1, c2 = 0, 0
    
    # Euclidean Distance between data1 and test
    i = 0
    while i<len(histogram) and i<len(histogram2):
        c1+=(histogram[i]-histogram2[i])**2
        i+= 1
    c1 = c1**(1 / 2)
    
    print(c1)
    if c1 < 20:
        return True
    return False


def createHash(first, second):
    h1 = scan(first)
    h2 = scan(second)

    print("HI",h1)
    print("HI2",h2)

    if h1 == h2:
        return True
    return False

