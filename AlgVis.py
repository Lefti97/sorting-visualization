import pygame
import random

BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

pygame.display.set_caption('Algorithm Visualization')
clock = pygame.time.Clock()

FPS = 100

arrSize = 100

xSize = arrSize
ySize = xSize

dispMult = 7
xDisplay = xSize * dispMult
yDisplay = ySize * dispMult + 100
display = pygame.display.set_mode((xDisplay,yDisplay))

arr = []

pygame.init()

font = pygame.font.SysFont(None, 25)
botText = font.render('SPACE: Pause, 1: Shuffle, 2: Asc Sort, 3: Desc Sort, Q: Insertion Sort', True, WHITE)
topText = [font.render('Choose Algorithm', True, WHITE)]

STOP = [True]

def initArr(size):
    arr.clear()
    for i in range(size):
        arr.append(size - i)

    random.shuffle(arr)

def draw(x = None, y = None):

    if STOP[0] == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_SPACE):
                        STOP[0] = True

    display.fill(BLACK)
    for i in range(arrSize):
        if i == x or i == y:
            pygame.draw.rect(display, RED, [i * dispMult , (arrSize - arr[i]) * dispMult + 50, dispMult, arr[i] * dispMult])
        else:
            pygame.draw.rect(display, YELLOW, [i * dispMult , (arrSize - arr[i]) * dispMult + 50, dispMult, arr[i] * dispMult]) 
    display.blit(botText, (10 , yDisplay - 50))
    display.blit(topText[0], (50, 10)) 
    clock.tick(FPS) 
    pygame.display.update()


def insertionSort():
    STOP[0] = False
    topText[0] = font.render('Insertion Sort    Comparisons: 0    Swaps: 0', True, WHITE)
    comps = 0
    swaps = 0

    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and STOP[0] == False:
            comps += 1
            if key < arr[j]:
                arr[j+1] = arr[j]
                j -= 1
                swaps += 1
    
                topText[0] = font.render('Insertion Sort    Comparisons: '+ str(comps) +'    Swaps: ' + str(swaps), True, WHITE)
                draw(i, j)
            else:
                break

        arr[j+1] = key

        if STOP[0] == True:
            break
        
    STOP[0] = True


def main():
    LOOP = True
    initArr(arrSize)

    while LOOP == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_q):
                    insertionSort()
                if (event.key == pygame.K_1):
                    random.shuffle(arr)
                if (event.key == pygame.K_2):
                    arr.sort()
                if (event.key == pygame.K_3):
                    arr.sort(reverse=True)

        draw()
        

if __name__ == "__main__":
    main()