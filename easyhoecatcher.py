import pygame
import random

green=(50,100,50)
black=(0,0,0)
red=(255,0,0)
white=(255,255,255)
blockSize=60
width=1200
height=900

def program():
    x = 600
    y = 600
    counts=1
    points=0
    xHoe=random.randrange(blockSize,width,blockSize)
    yHoe=random.randrange(blockSize,height,blockSize)
    lead_x=0
    lead_y=0
    h=0
    w=0
    fps=7
    snakeList=[]
    snakeLenght=1
    dtc="up"
    icon=pygame.image.load('images/iconn.png')
    macHead= pygame.image.load('images/macHead1.jpg')
    corpse=pygame.image.load('images/corpse.jpg')
    wallpaper=pygame.image.load('images/wallpaper.jpg')
    endwall=pygame.image.load('images/endgame.jpg')

    hoes=[]
    for i in range(15):
        hoes.append(pygame.image.load('images/hoe'+str(i)+'.jpg'))

    hoe = random.choice(hoes)

    def hoeAppear():
        screen.blit(hoe,[xHoe,yHoe,blockSize,blockSize] )

    def snake(snakeList):
        if dtc=="left":
            head=pygame.transform.rotate(macHead,90)
        if dtc=="right":
            head=pygame.transform.rotate(macHead,270)
        if dtc == "up":
            head = pygame.transform.rotate(macHead, 0)
        if dtc=="down":
            head=pygame.transform.rotate(macHead,180)

        screen.blit(head,(snakeList[-1][0],snakeList[-1][1]))
        for part in snakeList[:-1]:
            screen.blit(corpse,[part[0], part[1], blockSize, blockSize])

    screen = pygame.display.set_mode((width, height))

    pygame.font.init()
    font = pygame.font.SysFont("monotypecorsiva",70)
    font1=pygame.font.SysFont(None,30)
    def message(text, color,xcor,ycor):
        mtext = font.render(text,True,color)
        screen.blit(mtext, [xcor, ycor])
    def score(text, color,xcor,ycor):
        mtext = font1.render(text,True,color)
        screen.blit(mtext, [xcor,ycor])

    pygame.display.set_caption('Easy Hoes Catcher')
    pygame.display.set_icon(icon)
    clock = pygame.time.Clock()

    running=True
    notOver=True
    startingWin = True

    while running:
      for event in pygame.event.get():
        if event.type==pygame.QUIT:
          running=False
        if startingWin==True:
            # StartScreen
            screen.blit(wallpaper,[-100,-20])
            s = pygame.Surface((800, 300))
            s.set_alpha(128)
            s.fill(white)
            screen.blit(s, (200, 400))
            message("Easy Hoes Catcher", black, 400, 420)
            message("Catch as many hoes as possible!", black, 210, 520)
            message("Press 'w' to start", black, 400, 620)
            pygame.display.update()
            if event.type ==pygame.KEYDOWN:
                if event.key==pygame.K_w:
                    startingWin=False

        elif notOver==True:
            if event.type ==pygame.KEYDOWN:
                if event.key==pygame.K_a:
                    if h==0 or h==2:
                        dtc = "left"
                        lead_x=-blockSize
                        lead_y = 0
                        h=2
                        w=0
                elif event.key==pygame.K_d:
                    if h == 0 or h == 1:
                        dtc = "right"
                        lead_x=+blockSize
                        lead_y = 0
                        h=1
                        w=0
                elif event.key==pygame.K_w:
                    if w == 0 or w == 1:
                        dtc = "up"
                        lead_y=-blockSize
                        lead_x=0
                        w=1
                        h=0
                elif event.key==pygame.K_s:
                    if w == 0 or w == 2:
                        dtc = "down"
                        lead_y=+blockSize
                        lead_x=0
                        w=2
                        h=0

      x+=lead_x
      y+=lead_y

        #EXIT
      if x<=-15 or x>=width or y<=-15 or y>=height:
        screen.blit(endwall,[-40,0])
        s.fill(black)
        s.set_alpha(100)
        screen.blit(s, (180, 350))
        message("Game over noob", white,350,400)
        score("Hoes: "+str(points), black,20,20)
        message("Press 'w' to play again", white, 300, 500)
        pygame.display.update()
        notOver=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                notOver=True
                x=600
                y=600
                snakeList = []
                snakeLenght = 1
                lead_x=0
                lead_y=0
                points=0

        #displaying
      if notOver==True and startingWin==False:
        screen.fill(black)
        snakeHead=[]
        snakeHead.append(x)
        snakeHead.append(y)
        snakeList.append(snakeHead)
        if len(snakeList)>snakeLenght:
            del snakeList[0]

        snake(snakeList)
        for part in snakeList[:-1]:
            if part==snakeHead:
                notOver = False

        hoeAppear()

        score("Hoes: " +str(points), red,20,20)
        pygame.display.update()
        if x==xHoe and y==yHoe:
            snakeLenght+=1
            #fps+=0.5
            points+=1
            counts+=1
            hoe=random.choice(hoes)
            xHoe=random.randrange(blockSize,width,blockSize)
            yHoe=random.randrange(blockSize,height,blockSize)
            for part in snakeList[:-1]:
                if part[0]==xHoe and part[1]==yHoe:
                    xHoe = random.randrange(blockSize, width, blockSize)
                    yHoe = random.randrange(blockSize, height, blockSize)


        clock.tick(fps)
    pygame.quit()

program()
