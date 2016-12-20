label special_events_init:
    python:
        def isSpecialEventDay(weekday):
            return False
                
    return

label special_events:
    "Cos sie dzieje"
    jump koniec_dnia
