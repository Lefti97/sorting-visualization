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
botText = font.render('SPACE: Pause, 1: Shuffle, 2: Asc Sort, 3: Desc Sort, Check README for more', True, WHITE)
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
    topText[0] = font.render('Insertion Sort    Comparisons: 0    Swaps: 0', True, WHITE)
    comps = 0
    swaps = 0

    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and STOP[0] == False:
            comps += 1
            topText[0] = font.render('Insertion Sort    Comparisons: '+ str(comps) +'    Swaps: ' + str(swaps), True, WHITE)
            draw(i, j)

            if key < arr[j]:
                arr[j+1] = arr[j]
                j -= 1
                swaps += 1
            else:
                break
            
        topText[0] = font.render('Insertion Sort    Comparisons: '+ str(comps) +'    Swaps: ' + str(swaps), True, WHITE)
        draw(i, j)
        arr[j+1] = key

        if STOP[0] == True:
            break


def bubbleSort():
    topText[0] = font.render('Bubble Sort    Comparisons: 0    Swaps: 0', True, WHITE)
    comps = 0
    swaps = 0

    for i in range(len(arr) - 1):
        for j in range(0, len(arr) - i - 1):
            comps += 1
            topText[0] = font.render('Bubble Sort    Comparisons: '+ str(comps) +'    Swaps: ' + str(swaps), True, WHITE)
            draw(j, j+1)
            
            if arr[j] > arr[j + 1]:
                swaps += 1
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

            if STOP[0] == True:
                break
        if STOP[0] == True:
                break



def partition(arr, low, high, comps, swaps):
    i = (low-1)
    pivot = arr[high]
  
    for j in range(low, high):
        comps[0] += 1
        topText[0] = font.render('Quick Sort    Comparisons: '+ str(comps[0]) +'    Swaps: ' + str(swaps[0]), True, WHITE)
        draw(high, j)

        if arr[j] <= pivot:
            swaps[0] += 1
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
        if STOP[0] == True:
                break
    
    if STOP[0] == False:
        topText[0] = font.render('Quick Sort    Comparisons: '+ str(comps[0]) +'    Swaps: ' + str(swaps[0]), True, WHITE)
        draw(high, i+1)
        arr[i+1], arr[high] = arr[high], arr[i+1]
    
    return (i+1)
  

def quickSort(arr, low, high, comps, swaps):
    if STOP[0] == True:
        return
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high, comps, swaps)
        quickSort(arr, low, pi-1, comps, swaps)
        quickSort(arr, pi+1, high, comps, swaps)


def main():
    LOOP = True
    initArr(arrSize)

    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:

                STOP[0] = False

                if (event.key == pygame.K_q):
                    insertionSort()
                if (event.key == pygame.K_w):
                    bubbleSort()
                if (event.key == pygame.K_e):
                    comps = [0]
                    swaps = [0]
                    quickSort(arr, 0, arrSize-1, comps, swaps)
                if (event.key == pygame.K_1):
                    random.shuffle(arr)
                if (event.key == pygame.K_2):
                    arr.sort()
                if (event.key == pygame.K_3):
                    arr.sort(reverse=True)

                STOP[0] = True

        draw()
        

if __name__ == "__main__":
    main()
