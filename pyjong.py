from PIL import ImageGrab
import cv2
import numpy as np
import glob


#image = ImageGrab.grab()
#image.save('C:\\Users\\Jim\\Desktop\\PyjongIMG\\image.png')

#cImage = ImageGrab.grab()
#cImage.save('C:\\Users\\Jim\\Desktop\\PyjongIMG\\cImage.png')

img = cv2.imread('C:\\Users\\Jim\\Desktop\\PyjongIMG\\save1.png',cv2.IMREAD_COLOR)



templates = [cv2.imread(file) for file in glob.glob("C:\\Users\\Jim\\Desktop\\PyjongIMG\\tiles\\*.png")]
threshold = 0.90
w, h = templates[0].shape[:2]
method = cv2.TM_CCOEFF_NORMED



for template in templates: 

    res = cv2.matchTemplate(img, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    img = cv2.rectangle(img,(max_loc[0],max_loc[1]), (max_loc[0]+w+1, max_loc[1]+h+1), (255,0,0) )

    resDup = cv2.matchTemplate(img, template, method)
    min_valDup, max_valDup, min_locDup, max_locDup = cv2.minMaxLoc(resDup)
    if max_valDup > threshold:
        img = cv2.rectangle(img,(max_locDup[0],max_locDup[1]), (max_locDup[0]+w+1, max_locDup[1]+h+1), (255,0,0) )
    print("Max Val: ", max_val)
    print("Max ValDup: ", max_valDup)
    print ("Max Loc: ", max_loc)
    print ("Max LocDup: ", max_locDup)    



cv2.imwrite('C:\\Users\\Jim\\Desktop\\PyjongIMG\\output.png', img)