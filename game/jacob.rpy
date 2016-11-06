label jacob_init(game_characters):
    define jacob = Character('Jacob')
    
    python:
        class Jacob(SchoolCharacter):
            def __init__(self):
                super(Jacob, self).__init__()
            
            def before_school(self, date):
                renpy.call('jacob_before_school_0')
        
            def during_classes(self, date):
                renpy.call('jacob_normal_talk_0')
        
            def after_school(self, date):
                pass
        
            def character_discovery(self, date):
                pass
            
            def check_availability(self, dayTime):
                return True
            
        game_characters.append(Jacob())
        
    return
        
label jacob_normal_talk_0:
    me "Cześć!"
    jacob "Hej, cześć!"
    "Rozmawiamy przez chwile"
    return
    
label jacob_before_school_0:
    "Kiedy zbliżam się do szkoły już z daleka dostrzegam znajomą postać"
    "To Jacob"
    me "Cześć!"
    jacob "Hej, cześć!"
    "Rozmawiamy przez chwile"
    return
