from PIL import Image 
import time


starttime  = time.time()

filename = input('name file(without file extension): ')

# Преобразование картинки под размеры блокнота
img = Image.open(filename+".jpg")
img = img.resize((1024,332), Image.ANTIALIAS)

fpic = open(filename+".txt", "a")


def openfile(pixheight, pixwidth):

    pixel = pix[pixwidth,pixheight]
    bwpixel = (int(pixel[0]) + int(pixel[1]) + int(pixel[2]) )//3
    #определение яркости пикселя делением суммы rgb
    return bwpixel


def openfilepic(fpic,sumbol):
    fpic.write(sumbol)


def findimgsize(image):

    width = image.size[0]
    height = image.size[1] 
    pix = image.load()

    return(width,height,pix)


def finalresult(brightness,fpic):

    sumbols = [' ', ':', ',','r', 'B','W','@']#

    if(brightness > (220)):
        openfilepic(fpic,sumbols[0])
    elif(brightness > 190):
        openfilepic(fpic,sumbols[1])
    elif(brightness > 160):
        openfilepic(fpic,sumbols[2])
    elif(brightness > 130):
        openfilepic(fpic,sumbols[3])
    elif(brightness > 90):
        openfilepic(fpic,sumbols[4])
    elif(brightness > 50):
        openfilepic(fpic,sumbols[5])
    else:
        openfilepic(fpic,sumbols[6])


def count(startheight,height,wigth,fpic):
    
    for one in range(startheight,height):

        fpic.write('\n')
        for two in range(0,width):

            brightness = openfile(one,two)
            finalresult(brightness,fpic)


width,height,pix = findimgsize(img)
count(0,height,width,fpic)


print("--- %s секунд ---"% (time.time()-starttime))




