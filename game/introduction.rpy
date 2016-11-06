label introduction:
    scene black
    
    "Nasza historia zaczyna się w zwyczajnym liceum"
    "A dokładnie, przed zwyczajnym liceum..."
    "... na ulicy"
    play sound "music/237375__squareal__car-crash.mp3"
    pause 4
    me "..."
    me "... aauu..."
    pan_kruk "Czy wszystko w porządku?"
    me "...c..co?"
    
    scene outside_school with dissolve
    show pan kruk with dissolve
    
    pan_kruk "Pytałem się czy wszystko w porządku..."
    me "AAA...!!! Kruk!!!!"
    pan_kruk "Dla ciebie PAN Kruk"
    
    $ pan_kruk = Character('Pan Kruk')
    
    me "Pan ma głowę kruka!"
    pan_kruk "... I?"
    me "..."
    me "To... dziwne..?"
    pan_kruk "..."
    pan_kruk "Niesądzę."
    pan_kruk "Ale ty chyba nieźle dostałaś w głowę..."
    pan_kruk "Żeby sprawdzić czy wszystko z tobą w porządku, zadam ci teraz parę pytań..."
    $ alicja = renpy.input("A więc, jak się nazywasz?")
    pan_kruk "Hmm, dobrze... A teraz spróbujmy odmienić twoje imię..."
    $ alicji = renpy.input("Jak brzmi twoje imię w Dopełniaczu? (Podpowiem: Kogo? Czego?)")
    pan_kruk "Dobrze, dobrze..."
    $ alicjol = renpy.input("Jak brzmi twoje imię w Narzędniku? (Kim? Czym? To proste)")
    pan_kruk "Yhm..."
    $ alicjo = renpy.input("Jak brzmi twoje imię w Wołaczu? (Wiesz, \"O!\" i tak dalej)")
    pan_kruk "Hmm... Chyba z tobą wszystko w porządku, [alicjo]..."
    pan_kruk "To szczęście, że nic ci się nie stało, uderzenie wyglądało groźnie..."
    pan_kruk "No dobrze, nie zatrzymuję cię dłużej, biegnij do szkoły"
    me "Proszę Pana..."
    pan_kruk "Tak..?"
    me "A, nie ważne..."
    pan_kruk "Hmm... dobrze zatem..."
    
    hide pan kruk with dissolve
    
    "[alicja] odwróciła się na pięcie i pobiegła do szkoły."
    
    scene black with dissolve
    
    return
