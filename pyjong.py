from PIL import ImageGrab
import cv2
import numpy as np
import glob


#image = ImageGrab.grab()
#image.save('C:\\Users\\Jim\\Desktop\\PyjongIMG\\image.png')

#cImage = ImageGrab.grab()
#cImage.save('C:\\Users\\Jim\\Desktop\\PyjongIMG\\cImage.png')

img = cv2.imread('C:\\Users\\Jim\\Desktop\\PyjongIMG\\save1.png',cv2.IMREAD_COLOR)
tImg = cv2.imread('C:\\Users\\Jim\\Desktop\\PyjongIMG\\tiles\\kefala.png',cv2.IMREAD_COLOR)



templates = [cv2.imread(file) for file in glob.glob("C:\\Users\\Jim\\Desktop\\PyjongIMG\\tiles\\*.png")]
threshold = 0.90
w, h = templates[0].shape[:2]
method = cv2.TM_CCOEFF_NORMED
i = len(templates) * 2

max_val = 1

for template in templates: 

    res = cv2.matchTemplate(img, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    print(max_val)
    if max_val > threshold:
        res[max_loc[1]-h//2:max_loc[1]+h//2+1, max_loc[0]-w//2:max_loc[0]+w//2+1] = 0   
        img = cv2.rectangle(img,(max_loc[0],max_loc[1]), (max_loc[0]+w+1, max_loc[1]+h+1), (255,0,0) )

cv2.imwrite('C:\\Users\\Jim\\Desktop\\PyjongIMG\\output.png', img)