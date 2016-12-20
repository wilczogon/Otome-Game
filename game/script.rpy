# in-game characters
define me = Character('[alicja]')
define alicja = 'Ja'
define pan_kruk = Character('???')

# background images
image black = "#000"
image outside_school = im.Scale("outside_school.jpg", 1280, 720)
image corridor = im.Scale("corridor.jpg", 1280, 720)
image room = im.Scale("room.jpg", 1280, 720)
image classroom = im.Scale("classroom.jpg", 1280, 720)

# character images
image pan kruk = im.FactorScale(Image("pan kruk.png"), width=1.3)

init python:
    import datetime
    import random
    
    random.seed()

label start:
    call world_init
    
    call introduction
    
    jump world_loop

    return
