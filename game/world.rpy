label world_init:
    python:
        class DayTime:
            MORNING = 0
            AFTERNOON = 1
            EVENING = 2
            NIGHT = 3
            
        date = datetime.date(2016, 9, 1)
        day_time = DayTime.MORNING
        game_characters = []
        
        def dayTimeSceneRouter (functionName, probabilityOfInterruptScene):
            enableDiscovery = True
            if probabilityOfInterruptScene > random.random():
                random.shuffle(game_characters)
                for character in game_characters:
                    if character.check_availability(day_time):
                        getattr(character, functionName)(date)
                        enableDiscovery = False
                        break
                        
            if enableDiscovery:
                pass # TODO - enable discovery
                
            
        
    call school_character_init
    call jacob_init(game_characters)
    call grzegorz_init(game_characters)
    return

label world_loop:
    scene black
    show text "[date]" at truecenter
    pause 3
    hide text with dissolve
    scene room with dissolve
    pause 1
    
    "Kolejny poranek."
    "Dzisiaj mamy wtorek."
    "Zbieram się i idę do szkoły."
    
    scene outside_school with dissolve
    
    "Dotarłam do szkoły."
    
    $ dayTimeSceneRouter ("before_school", 1)
    
    scene corridor with dissolve
    
    "Dzwoni dzwonek."
    "Rozpoczynają się lekcje."
    
    scene classroom with dissolve
    
    $ dayTimeSceneRouter ("during_classes", 1)
    
    "Jeszcze przez jakiś czas trwają lekcje."
    "W końcu..."
    "<dźwięk dzwonka>"
    "Pakuję książki do plecaka."
    
    scene corridor with dissolve
    
    $ dayTimeSceneRouter ("after_school", 1)
    scene room with dissolve
    pause 1
    
    scene outside_school with dissolve
    
    "Wracam do domu."
    
    scene room with dissolve
    
    "Kolejny dzień chyli się ku wieczorowi."
    "Odrabiam lekcje, odpoczywam i w końcu zasypiam."
    
    $ date = date + datetime.timedelta(days=1)
    
    jump world_loop