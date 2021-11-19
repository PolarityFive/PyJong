from PIL import ImageGrab
import cv2
import numpy as np
import glob
import win32api
import win32con
import win32gui
import pygame

#Window setup

pygame.init()
screen = pygame.display.set_mode((1920, 1080),pygame.NOFRAME)
done = False
fuchsia = (255, 0, 128)  # Transparency color
dark_red = (0, 0, 255)

# Create layered window
hwnd = pygame.display.get_wm_info()["window"]

# Set window transparency color
l_ex_style = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
l_ex_style |= win32con.WS_EX_TRANSPARENT | win32con.WS_EX_LAYERED
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, l_ex_style)

# Set the window to be transparent and appear always on top
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*fuchsia), 50, win32con.LWA_ALPHA)  # transparent
win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 1920, 1080, 0) #Always on top



while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    img = cv2.imread('C:\\Users\\Jim\\Desktop\\PyjongIMG\\save1.png',cv2.IMREAD_COLOR)



    templates = [cv2.imread(file) for file in glob.glob("C:\\Users\\Jim\\Desktop\\PyjongIMG\\tiles\\*.png")]
    threshold = 0.80
    method = cv2.TM_CCOEFF_NORMED



    for template in templates: 

        res = cv2.matchTemplate(img, template, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
       
        pygame.draw.rect(screen, dark_red, pygame.Rect(max_loc[0], max_loc[1],50 ,50),3)
        pygame.display.update()

        resDup = cv2.matchTemplate(img, template, method)
        min_valDup, max_valDup, min_locDup, max_locDup = cv2.minMaxLoc(resDup)
        
            
        
        
        print("Max Val: ", max_val)
        print("Max ValDup: ", max_valDup)
        print ("Max Loc: ", max_loc)
        print ("Max LocDup: ", max_locDup)




    #screen.fill(fuchsia)  # Transparent background
    



#img = cv2.rectangle(img,(max_loc[0],max_loc[1]), (max_loc[0]+w+1, max_loc[1]+h+1), (255,0,0) )
#img = cv2.rectangle(img,(max_locDup[0],max_locDup[1]), (max_locDup[0]+w+1, max_locDup[1]+h+1), (255,0,0) )
#image = ImageGrab.grab()
#image.save('C:\\Users\\Jim\\Desktop\\PyjongIMG\\image.png')

#cImage = ImageGrab.grab()
#cImage.save('C:\\Users\\Jim\\Desktop\\PyjongIMG\\cImage.png')

