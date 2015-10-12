from PIL import Image

im=Image.open("cave.jpg")

width=im.size[0]
height=im.size[1]

even=Image.new(im.mode, (width/2,height/2))
odd=Image.new(im.mode, tuple([x/2 for x in im.size]))

for x in range(width):
    for y in range(height):
        pixel=im.getpixel((x,y))
        if x%2^y%2:
            odd.putpixel(((x-1)/2, y/2) if x%2 else (x/2, (y-1)/2) , pixel)
        else:
            even.putpixel((x/2, y/2), pixel)  
            
even.save('cave_even.jpg')
odd.save('cave_odd.jpg')
