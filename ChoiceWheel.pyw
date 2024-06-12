import pygame
from pygame import gfxdraw
import time
import sys
import random
import math
import tkinter as tk
from data import ieraksta, dabut_datus

def quit():
    for event in pygame.event.get():                    
        if event.type == pygame.QUIT:                     
            pygame.quit(); sys.exit();                  


#Function to display large result text
# def displayresult(result):
#     fanfare = pygame.mixer.Sound("fanfare.wav")
#     font = pygame.font.SysFont(None, 48)            

#     #cheer.play() 
#     fanfare.play()
#     textsurface = font.render(result, True, (0, 255, 0))
#     textrect = textsurface.get_rect()
#     textrect.centerx = screen.get_rect().centerx
#     textrect.centery = screen.get_rect().centery
#     screen.blit(textsurface,textrect)
#     pygame.display.update()

##INPUT DECISION LIST HERE
##
#decisionlist = ['Choice 1','Choice 2','Choice 3','Choice 4','Choice 5','Choice 6','Choice 7','Choice 8'] # šeit no db jādabū saraksts ar elementiem
##
##INPUT DECISION LIST ABOVE



def palaist_speli():
    decisionlist = dabut_datus()
    pygame.init() #Initializing pygame
    font2 = pygame.font.SysFont(None, 28)             
    screen = pygame.display.set_mode((400,400))
    spin1 = pygame.mixer.Sound("spin1.wav")
    spin2 = pygame.mixer.Sound("spin2.wav")
    spin3 = pygame.mixer.Sound("spin3.wav")
         
    degree = 0                                          
    elapsedtime = 1                                    
    end = random.randint(200,560)                      
    x = 1                                               
    resultlist = []                                     
    cx = cy = r = 200
    dividers = len(decisionlist)
    radconvert = math.pi/180
    divvies = int(360/dividers)

    for i in range(len(decisionlist)):                 
        resultlist.append(random.choice(decisionlist))  
        decisionlist.remove(resultlist[i])              

    print(resultlist)

    while x == 1:  
        pygame.display.flip()
        screen.fill([255, 255, 255])                   
        
        surf = pygame.Surface((100,100))               
        surf.fill((255, 255, 255))                    

        surf.set_colorkey((255,255,255))               

        surf = pygame.image.load('cool.png').convert_alpha()    
        where = 180, 10                               

        blittedRect = screen.blit(surf, where)        
        screen.fill([255, 255, 255])                
        pygame.draw.circle(screen, (0,0,0), (cx, cy), r, 3)
        for i in range(dividers):
            gfxdraw.pie(screen, cx, cy, r, i*divvies, divvies, (0,0,0))
        i = 1
        iters = range(1,dividers*2,2)
        for i in iters:
            textChoice = font2.render(resultlist[iters.index(i)],False,(0,0,0))
            textwidth = textChoice.get_rect().width
            textheight = textChoice.get_rect().height
            textChoice = pygame.transform.rotate(textChoice,(i-(2*i))*(360/(dividers*2)))
            textwidth = textChoice.get_rect().width
            textheight = textChoice.get_rect().height
            screen.blit(textChoice,(
                                    (cx-(textwidth/2))
                                    +((r-100)*math.cos(((i*(360/(dividers*2))))*radconvert)),
                                    (cy-(textheight/2))
                                    +((r-100)*math.sin(((i*(360/(dividers*2))))*radconvert))
                                    )
                                )
            textChoice = ''
        oldCenter = blittedRect.center                 

        rotatedSurf = pygame.transform.rotate(surf, degree)  
        
        rotRect = rotatedSurf.get_rect()              
        rotRect.center = oldCenter                     

        screen.blit(rotatedSurf, rotRect)             

        degree -= 2                                    
        if degree == -360:                             
            degree = 0
        
        pygame.display.flip()
        
        quit()                                         
    
        
        if elapsedtime == 1:
            spin1.play(-1)
            elapsedtime += 1
        elif elapsedtime < end/6:
            pygame.time.wait(2)
            elapsedtime += 1
        elif elapsedtime < end/4:
            pygame.time.wait(5)
            elapsedtime += 1
        elif elapsedtime < end/2:
            pygame.time.wait(10)
            elapsedtime += 1
        elif elapsedtime < end/1.5:
            pygame.time.wait(15)
            elapsedtime += 1
        elif elapsedtime < end/1.2:
            spin3.stop()
            spin3.play()
            pygame.time.wait(30)
            elapsedtime += 1
        elif elapsedtime < end/1.1:
            spin3.stop()
            spin3.play()
            pygame.time.wait(70)
            elapsedtime += 1
        elif elapsedtime < end/1.05:
            spin1.fadeout(1000)
            spin3.stop()
            spin3.play()
            pygame.time.wait(150)
            elapsedtime += 1
        elif elapsedtime < end:
            spin1.stop()
            spin3.stop()
            spin3.play()
            pygame.time.wait(200)
            elapsedtime += 1    
        elif elapsedtime == end:                      
            spin1.stop()
            print('raw degree: ' + str(degree))
            degCheck = degree#+6
            degCheck = (-1*degCheck)-90
            if degCheck < 0:
                degCheck = degCheck + 360
            print('degCheck: ' + str(degCheck))
            x = 2                                     
            while x == 2:   
                screen.blit(rotatedSurf, rotRect)                    
                for i in range(len(resultlist)):
                    if degCheck > i*(360/len(resultlist)) and degCheck < (i+1)*(360/len(resultlist)):
                        x = 3
                        print(i)
                        result = resultlist[i]
                        #displayresult(result)
                        fanfare = pygame.mixer.Sound("fanfare.wav")
                        font = pygame.font.SysFont(None, 48)            

                        #cheer.play() 
                        fanfare.play()
                        textsurface = font.render(result, True, (0, 255, 0))
                        textrect = textsurface.get_rect()
                        textrect.centerx = screen.get_rect().centerx
                        textrect.centery = screen.get_rect().centery
                        screen.blit(textsurface,textrect)
                        pygame.display.update()


                        while x == 3:
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    x = 1
                                    elapsedtime = 1
                                    end = random.randint(200,560)
                                    break
                            quit()
                    elif degCheck%(360/len(resultlist)) == 0:
                        x = 3
                        displayresult('Spinning Again')
                        print('on the line')
                        pygame.time.wait(1)
                        x = 1
                        elapsedtime = 1
                        end = random.randint(200,560)
                        while x == 3:
                            quit()   
                quit()

def submit_poga():
    dati = entry.get()
    ieraksta(dati)




window = tk.Tk()
window.config(width=400, height=400)
entry = tk.Entry(window)
button1 = tk.Button(window, text="Submit", command=submit_poga)
label2 = tk.Label(window, text="")
entry.pack()
button1.pack()
label2.pack()
button_spele = tk.Button(window, text = "Griezt ratu!", command=palaist_speli)
button_spele.place(x=100, y=100)
button_spele.pack()


window.mainloop()
