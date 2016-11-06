label grzegorz_init(game_characters):
    define grzegorz = Character('Grzegorz')
    
    python:
        class Grzegorz(SchoolCharacter):
            def __init__(self):
                super(Grzegorz, self).__init__()
            
            def before_school(self, date):
                pass
        
            def during_classes(self, date):
                renpy.call('grzegorz_during_classes_0')
        
            def after_school(self, date):
                pass
        
            def character_discovery(self, date):
                pass
            
            def check_availability(self, dayTime):
                return True
            
        game_characters.append(Grzegorz())
        
    return
        
label grzegorz_during_classes_0:
    me "Cześć!"
    jacob "Hej, cześć!"
    "Rozmawiacie przez chwile"
    return
