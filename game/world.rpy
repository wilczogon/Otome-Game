label world_init:
    python:
        class DayTime:
            MORNING = 0
            AFTERNOON = 1
            EVENING = 2
            NIGHT = 3
            
        class Weekday:
            PONIEDZIALEK = 0
            WTOREK = 1
            SRODA = 2
            CZWARTEK = 3
            PIATEK = 4
            SOBOTA = 5
            NIEDZIELA = 6
            
        weekday = {
            Weekday.PONIEDZIALEK: 'poniedziałek',
            Weekday.WTOREK: 'wtorek',
            Weekday.SRODA: 'środa',
            Weekday.CZWARTEK: 'czwartek',
            Weekday.PIATEK: 'piątek',
            Weekday.SOBOTA: 'sobota',
            Weekday.NIEDZIELA: 'niedziela'
        }
            
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
                
            
    call special_events_init
    call weekend_init
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
    $nazwa_dnia = weekday.get(date.weekday())
    "Dzień tygodnia: [nazwa_dnia]"
    
    $specjalny_dzien = isSpecialEventDay(date.weekday())
    $weekend = isWeekend(date.weekday())
    
    if specjalny_dzien:
        jump special_events
        
    if weekend:
        jump weekend
        
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
    
label koniec_dnia:
    
    $ date = date + datetime.timedelta(days=1)
    
    jump world_loop