label weekend_init:
    python:
        def isWeekend(weekday):
            if weekday == 5 or weekday == 6:
                return True
            else:
                return False
                
    return

label weekend:
    "Jak spędzę dzień wolny?"
    menu:
        "Poucz się":
            "Uczę się przez cały dzień."
            "Wydaje mi się, że nauczyłam się trochę na lekcje."
            
        "Zadzwoń do znajomego":
            "Zadzwonię do znajomego..."
            "Moment, ja nie mam żadnego numeru..."
            jump weekend
            
        "Zaproponuj wyjście ze znajomym":
            "Wyjdę na miasto z jakimś znajomym..."
            "Moment, ja nie mam żadnego numeru..."
            jump weekend
            
        "Zjedz coś i idź spać":
            "Zjadłam coś i poszłam spać."
            "Grunt to wiedzieć czego się chce."
            
    jump koniec_dnia
    
