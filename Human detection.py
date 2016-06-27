import cv2

image = cv2.imread("example_25_1.jpg")
height , width, channels = image.shape
# convert to grayscale
gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# threshold image
_,thresh = cv2.threshold(gray_image,160,255,cv2.THRESH_BINARY_INV)
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
dilated = cv2.dilate(thresh,kernel,iterations = 10)
# get contours
contours, hierarchy = cv2.findContours(dilated,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

# draw a bounding rectangle for each contour found
for contour in contours:
    [x,y,w,h] = cv2.boundingRect(contour)

    # discard areas that are too small
    if h<height/4 or w<width/4:
        continue

    # draw rectangle around contour
    cv2.rectangle(image,(x,10),(x+w,height),(255,0,255),2)

#save the image with the bounding box on disk
cv2.imwrite("human_detected.jpg", image)