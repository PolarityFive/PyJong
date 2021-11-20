from PIL import ImageGrab
import cv2
import glob
import win32api
import win32con
import win32gui
import pygame
import os
import keyboard
running = True


#Window setup

pygame.init()
screen = pygame.display.set_mode((1920, 1080),pygame.NOFRAME)
fuchsia = (0, 0, 0)  # Transparency color
color = (255, 255, 255)

# Create layered window
hwnd = pygame.display.get_wm_info()["window"]

# Set window transparency color
l_ex_style = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
l_ex_style |= win32con.WS_EX_TRANSPARENT | win32con.WS_EX_LAYERED
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, l_ex_style)

# Set the window to be transparent and appear always on top
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*fuchsia), 150, win32con.LWA_ALPHA)  # transparent
win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 1920, 1080, 0) #Always on top

font = pygame.font.SysFont('Arial', 25)

tileNames = [os.path.basename(x) for x in glob.glob('C:\\Users\\Jim\\Desktop\\PyjongIMG\\tiles\\*.png')]
templates = [cv2.imread(file) for file in glob.glob("C:\\Users\\Jim\\Desktop\\PyjongIMG\\tiles\\*.png")]


threshold = 0.85
method = cv2.TM_CCOEFF_NORMED


while running:
    
    
    cImage = ImageGrab.grab()
    cImage.save('C:\\Users\\Jim\\Desktop\\PyjongIMG\\cImage.png')
    img = cv2.imread('C:\\Users\\Jim\\Desktop\\PyjongIMG\\save1.png',cv2.IMREAD_COLOR)

    i = 0

    for template in templates: 

        res = cv2.matchTemplate(img, template, method)
        doubleCount = 0
        singleCount = 2
        max_val = 1
        
        isDrawnFlag = False
        while max_val > threshold:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
            if (max_val > threshold):
                isDrawnFlag = True
                res[max_loc[1]-30//2:max_loc[1]+30//2+1, max_loc[0]-30//2:max_loc[0]+30//2+1] = 0
                pygame.draw.rect(screen, color, pygame.Rect(max_loc[0], max_loc[1],50 ,80),3)
                screen.blit(font.render(tileNames[i], True, (255,255,255)), (max_loc[0]-30, max_loc[1]-30))
                pygame.display.update()
                doubleCount+=1

        print("Max Val: ", max_val)
        print ("Max Loc: ", max_loc)
        i += 1 
        if (isDrawnFlag == True):
            while(True):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                if (keyboard.is_pressed('q')):
                    screen.fill(fuchsia)
                    pygame.display.update()
                    isDrawnFlag = False
                    break
    
