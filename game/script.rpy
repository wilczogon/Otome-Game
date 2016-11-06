# in-game characters
define me = Character('[alicja]')
define alicja = 'Ja'
define pan_kruk = Character('???')

# background images
image black = "#000"
image outside_school = im.FactorScale(Image("outside_school.jpg"), width=2.5)
image corridor = im.FactorScale(Image("corridor.jpg"), width=1)
image room = im.FactorScale(Image("room.jpg"), width=2)
image classroom = im.FactorScale(Image("classroom.jpg"), width=5)

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
