import cv2
import numpy as np
from matplotlib import pyplot as plt
import time

# Create a VideoCapture object to access the camera
cap = cv2.VideoCapture(0)  # 0 means use the default camera

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Unable to access camera")
else:
    # Start a timer for 5 seconds
    start_time = time.time()
    while (time.time() - start_time) < 5:
        # Read a frame from the camera
        ret, frame = cap.read()

        # Check if the frame was read successfully
        if not ret:
            print("Unable to capture frame")
            break

        # Display the captured frame in a window
        cv2.imshow("Camera Interface", frame)
        cv2.imwrite("sample.jpeg",frame)

        # Wait for a key press and check if it's the 'q' key
        if cv2.waitKey(1) == ord("q"):
            break

    # Release the VideoCapture object and close the window
    cap.release()
    cv2.destroyAllWindows()

global grk,brk
grk=0
brk=0
def get_classificaton(ratio):
    ratio =round(ratio,1)
    
    toret=""
    if(ratio>1):
        toret="Broken Rice"
    else:
                toret="Good Quality"
    toret="("+toret+")"
    return toret
#rnjn
#print ("Starting")
img = cv2.imread('sample.jpeg',0)#load in greyscale mode

#convert into binary
ret,binary = cv2.threshold(img,160,255,cv2.THRESH_BINARY)# 160 - threshold, 255 - value to assign, THRESH_BINARY_INV - Inverse binary

#averaging filter
kernel = np.ones((5,5),np.float32)/9
dst = cv2.filter2D(binary,-1,kernel)# -1 : depth of the destination image


kernel2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))

#erosion
erosion = cv2.erode(dst,kernel2,iterations = 1)

#dilation 
dilation = cv2.dilate(erosion,kernel2,iterations = 1)

#edge detection
edges = cv2.Canny(dilation,100,200)

### Size detection
contours,hierarchy = cv2.findContours(erosion, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print( "Total no. of rice grains present=",len(contours))
total_ar=0
for cnt in contours:
    x,y,w,h = cv2.boundingRect(cnt)
    aspect_ratio = float(w)/h
    if(aspect_ratio>2):
        aspect_ratio=1/aspect_ratio
        brk+=1
        #print (round(aspect_ratio,2),get_classificaton(aspect_ratio))
    else:
        aspect_ratio=1/aspect_ratio
        grk+=1
        #print (round(aspect_ratio,2),get_classificaton(aspect_ratio))
    total_ar+=aspect_ratio
avg_ar=total_ar/len(contours)
#print ("Average Aspect Ratio=",round(avg_ar,2),get_classificaton(avg_ar))
print("Broken rice grain =",brk)
print("Whole rice grain =",grk)
pgrk=(grk/(brk+grk))*100
print("percentage of whole rice",round(pgrk,2),"%")
if(brk<grk):
    print("The quality of rice is good")
else:
    print("The quality of rice is bad")
#plot the images
imgs_row=2
imgs_col=3
plt.subplot(imgs_row,imgs_col,1),plt.imshow(img,'gray')
plt.title("Original image")

plt.subplot(imgs_row,imgs_col,2),plt.imshow(binary,'gray')
plt.title("Binary image")

plt.subplot(imgs_row,imgs_col,3),plt.imshow(dst,'gray')
plt.title("Filtered image")

plt.subplot(imgs_row,imgs_col,4),plt.imshow(erosion,'gray')
plt.title("Eroded image")

plt.subplot(imgs_row,imgs_col,5),plt.imshow(dilation,'gray')
plt.title("Dialated image")

plt.subplot(imgs_row,imgs_col,6),plt.imshow(edges,'gray')
plt.title("Edge detect")

plt.show()