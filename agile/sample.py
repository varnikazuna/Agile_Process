import sys, pygame
from pygame.locals import *
import threading
import random
import time
from time import sleep
from os import path
from datetime import datetime
solution=[]
threadLock = threading.Lock()
results = [[]for _ in range(4)]
class myThread (threading.Thread):
   
   def __init__(self, threadID, name, counter,x):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
      self.x=x
   def run(self):
      print ("Starting " + self.name)
      # Get lock to synchronize threads
      threadLock.acquire()
      print(self.threadID)
      results[(self.threadID)-1] = results[(self.threadID)-1]+ [''.join(self.x)]
      print (results)
      solution.append(eval(self.x))
      c=eval(self.x)
      # Free lock to release next thread
      threadLock.release()
      #return(c)

pygame.init()
pygame.font.init() 
myfont = pygame.font.SysFont(None, 29)
titlefont = pygame.font.SysFont(None, 50)

display_width = 1400
display_height = 800

black = (0,0,0)
white = (255,255,255)
lime = (0,255,0) #lime
yellow = (255,255,0) #yellow

z1=x1 = x3=(0.05*display_width)
z2=y1 = y2 =(0.05*display_height)
z3=x2 = x4=(0.85*display_width)
z4=y3 = y4=(0.35*display_height)
x5=(0.45*display_width)
y5=(0.2*display_height)

gamebackground = pygame.image.load("cover.jpg")
scrum=pygame.image.load("scrum.jpg")
m1=pygame.image.load("m1.png")
m2=pygame.image.load("m2.png")
m3=pygame.image.load("m3.jpg")
m4=pygame.image.load("m4.jpg")
prompt=pygame.image.load("prompt.png")

scrum=pygame.transform.scale(scrum,(200,200))
m1=pygame.transform.scale(m1,(100,100))
m2=pygame.transform.scale(m2,(100,100))
m3=pygame.transform.scale(m3,(100,100))
m4=pygame.transform.scale(m4,(100,100))

gamedisplay = pygame.display.set_mode((display_width,display_height), RESIZABLE)
pygame.display.set_caption("My Game")
def call(x):
   gamedisplay.fill([255, 255, 255])
   gamedisplay.blit(scrum,(x5,y5))
   gamedisplay.blit(m1,(x1,y1))
   gamedisplay.blit(m2,(x2,y2))
   gamedisplay.blit(m3,(x3,y3))
   gamedisplay.blit(m4,(x4,y4))
   return x

def display_window(message,x,y):
   x3=x1=x
   x2=x4=y  
   gamedisplay.fill([255, 255, 255])
   gamedisplay.blit(scrum,(x5,y5))
   gamedisplay.blit(m1,(x1,y1))
   gamedisplay.blit(m2,(x2,y2))
   gamedisplay.blit(m3,(x3,y3))
   gamedisplay.blit(m4,(x4,y4))
   showMessage(message,(gamedisplay.get_width() / 2) - 120,
                    (gamedisplay.get_height() / 2) -10)
   if (message == "Team Members work on their respective Tasks" ):
     showMessage(str(results[0]),z1,z2+102)
     showMessage(str(results[1]),z3,z2+102)
     showMessage(str(results[2]),z1,z4+102)
     showMessage(str(results[3]),z3,z4+102)
   if (message == "Product Delivered"):
          showMessage(str(solution),((gamedisplay.get_width() / 2)-102),((gamedisplay.get_height() / 2) +100))
   pygame.display.flip()
   pygame.time.delay(5000)
  

def showMessage(message, x, y):
  textsurface = myfont.render(message, True, lime)
  gamedisplay.blit(textsurface,(x,y))
def get_key():
  while 1:
    event = pygame.event.poll()
    if event.type == KEYDOWN:
      return event.key
    else:
      pass

def display_box(gamedisplay, message):
  "Print a message in a box in the middle of the gamedisplay"
  fontobject = pygame.font.Font(None,18)
  pygame.draw.rect(gamedisplay, (0,0,0),
                   ((gamedisplay.get_width() / 2) - 80,
                    (gamedisplay.get_height() / 2) -10,
                    200,20), 0)
  pygame.draw.rect(gamedisplay, (255,255,255),
                   ((gamedisplay.get_width() / 2) - 82,
                    (gamedisplay.get_height() / 2) - 12,
                    204,24), 1)
  if len(message) != 0:
    gamedisplay.blit(fontobject.render(message, 1, (255,255,255)),
                ((gamedisplay.get_width() / 2) - 80, (gamedisplay.get_height() / 2) - 10))
  pygame.display.flip()


def ask(gamedisplay, question):
  print ("ask(gamedisplay, question) -> answer")
  pygame.font.init()
  current_string = [[] for _ in range(8)]
  string = []
  display_box(gamedisplay, question + ": " + str(current_string))
  x=0
  for x in range(8):
    while 1:
      inkey = get_key()
      if inkey == K_BACKSPACE:
        current_string[x] = current_string[x][0:-1]
      elif inkey == K_RETURN: 
        break
      elif inkey ==K_a:
        current_string[x].append("+")
      elif inkey == K_m:
        current_string[x].append("*")
      elif inkey <= 57:
        current_string[x].append(chr(inkey))
      display_box(gamedisplay, question + ": " + (''.join(current_string[x])))
    string = string + [''.join(current_string[x])]  
    x=x+1
    print (string)
  return (string)



def print_time(threadName, delay, counter):
   while counter:
      time.sleep(delay)
      print ("%s: %s" % (threadName, time.ctime(time.time())))
      counter -= 1

gamedisplay.blit(gamebackground,(0,0))
gamedisplay.blit(prompt,(135,50))
def main():
  
  pygame.display.update()
  done = False
  threads = []
  i=0
  delay=0
  while not done:
    for event in pygame.event.get():
      pygame.display.update()
      if event.type == pygame.QUIT:
        done = True
      if event.type == KEYDOWN and event.key == K_RETURN:
         call(0)
         print(6)
         showMessage("press i to enter the requirements:",(gamedisplay.get_width() / 2)+100,(gamedisplay.get_height() / 2)+100)
      if event.type == KEYDOWN and event.key == K_i:
        #result = []
        call(0)
        a = ask(gamedisplay, "Input")
        print(a)
        

        # Create new threads

        while(i<len(a)-1):
            delay=delay+1
            
            thread1 = myThread(1, "Thread-1", delay,a[i])
            i=i+1
            thread2 = myThread(2, "Thread-2", delay,a[i])
            i=i+1
            thread3 = myThread(3, "Thread-3", delay,a[i])
            i=i+1
            thread4 = myThread(4, "Thread-4", delay,a[i])
            i=i+1

        # Start new Threads
            thread1.start()
            thread2.start()
            thread3.start()
            thread4.start()

            # Add threads to thread list
            threads.append(thread1)
            threads.append(thread2)
            threads.append(thread3)
            threads.append(thread4)
            
        # Wait for all threads to complete
            for t in threads:
                t.join()

        display_window("Scrum Master called for meeting",x5 - 120, x5 + 120)
        display_window("Team Members work on their respective Tasks",0.05*display_width, 0.85*display_width)
        display_window("Product Delivered",0.05*display_width, 0.85*display_width)
    
if __name__ == '__main__': main()
pygame.quit()
