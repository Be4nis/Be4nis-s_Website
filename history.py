baroque = ["Exploration of the new world", "Absolute Monarchs", "Scientific Discoveries", "Religious Divisions"]
tempvar = 0
while True:
    p = input("What section would you liked to be quized on?\nType world for world of baroque, \nType name for meaning of baroque, \nType harmony for different types of harmony, \nType vocal for vocal music, \nType instrumental for instrumental music, \nType antonio for Vivaldi, \nType bach for Bach: \nType here: ")
    if p == "world":
        for i in range(len(baroque)):
            h = input("Type in one major thing that happend in the Baroque Period: ").strip().lower()
            if "new world" and "exploration" in h:
                print ("Correct!")
                tempvar += 1
                print (4 - tempvar, "left!")
            if "absolute monarch" in h:
                print ("Correct!")
                tempvar += 1
                print (4 - tempvar, "left!")
            if "scientific discoveries" in h:
                print ("Correct!")
                tempvar += 1
                print (4 - tempvar, "left!")
            if "religious division" in h:
                divisions = input("What divisions?: ").strip().lower().split(' ')
                tempvar = 0
                if "catholics" in divisions:
                    print ("Correct!")
                    tempvar += 1
                    print (2 - tempvar, "left!")
                if "protestants" in divisions:
                    print ("Correct!")
                    tempvar += 1
                    print (2 - tempvar, "left!")
    if p == "meaning":
        meaningofbaroque = input("What is the meaning of Baroque?: ").strip().lower()
        if "mishapen pearl" not in meaningofbaroque:
            print ("Wrong")
        else:
            print ("Yep")
        origin = input("What language did it come from?: ").strip().lower()
        if "portugese" not in origin:
            print ("Wrong")
        else:
            print ("Yep it is Portugese")
    if p == "harmony":
        for i in range(4):
            print("What are the four type of harmonies in the Baroque time period")
            harmonies = input("Name one:")
            if "figured bass" in harmonies:
                print ("Yep")
                print ("\n\n")
                t = input("What line is it known as?: ")
                if t.lower().strip() == 'continuo line':
                    print ("Correct! Musicians knew basic harmony so it was not necessary to write out every note.")
            
            elif "monody" in harmonies:
                print ("Yep")
                print ("\n\n")
                meaning = input("What does monody mean?: ")
                if "one" or "1" and "song" in meaning:
                    print ("Yep")
                variable = input("Describe what monody sounds like: ").lower().strip()
                if "shift" in variable and "interest" in variable and "independent" in variable and "single" in variable and "melody" in variable:
                    print ("Yep, it is a shift in interest from several independent parts to music with a single melody!")
                else:
                    print ("Yep, it is a shift in interest from several independent parts to music with a single melody!")
                print ("\n\n")
            
            elif "equal temperment" in harmonies:
                print ("Yep")
                print ("Bach's Fugue's")
                print ("\n\n")
            elif "major" or "minor" and "tonality" or "tonalities" in harmonies:
                print ("Yep")
                print ("\n\n")
                interest = input("What two chords were the large interests?: ").strip().lower().split(' ')
                if "tonic" in interest and "dominant" in interest:
                    print ("Correct!")
                elif "tonic" in interest and "dominant" not in interest:
                    print ("Tonic is correct! Other is dominant")
                elif "dominant" in interest and "tonic" not in interest:
                    print ("Dominant is correct! The other is Tonic")
                else:
                    print ("Nope. The large interest is in Dominant and Tonic chords!")
                shift = input("Where did interest shift to? What is the most important thing?: ")
                if "single" in shift and "note" in shift:
                    print ("Correct!")
                else:
                    print ("Music shifted to a single note being the most important!")
                print ("\n\n")
    if p == "vocal":
        for i in range(3):
            h = input("What was a type of vocal work?: ")
            if h.lower().strip() == "opera":
                print ("Correct!")
                opera = input("Name two facts about Opera: ")
                if ("dramatic" in opera) and ("sets" or "costumes" in opera):
                    print ("True, it includes performers and Orchestra, and the music served the drama")
                else:
                    print ("You were prob right. Too lazy to finish system. Opera is a dramatic work that includes actors and orchestra. \nThere are sets and Costumes and the music acompanies the drama.")
            if h.lower().strip() == "cantata":
                print ("Yep\n")
                based = input("What is the canatata based on?: ")
                if "poem" or "lyric" in based:
                    print ("Correct! It is based on a poem or Lyric")
                sacorsec = input("Is the cantata sacred or secular?: ")
                print ("The answer is that they can be both sacred and secular")
                howlongiscantata = input("What two adjectives describe the cantata?: ")
                if "short" in howlongiscantata and "intimate" in howlongiscantata:
                    print ("Correct, it is short and intimate")
                else:
                    print ("Wrong, it is short and intimate")
            if h.lower().strip() == "oratorio":
                print ("Yep\n")
                features = input("What three things did Oratorios feature? Not people performing it: ")
                if ("recitatives" in features.strip().lower()) and ("arias" in features.strip().lower()) and ("ensemble" in features.strip().lower()):
                    print ('Exactly')
                else:
                    print ("Oratorios features ensemble pieces, recitatives and arias")
                secorsac = input("Was the Bach oratorio sacred or secular?: ")
                if secorsac.lower().strip() == "sacred":
                    print ("Correct!")
                    based = input("What were they based on?: ")
                    if "bibl" in based:
                        print ("Yep, it was biblical and based on the bible")
                    else:
                        print ("It was based on the bible!")
                else:
                    print ("Bach's oratorios are sacred!")
                performers = input("What were the three types of performers?: ")
                if ("soloist" in  performers.lower().strip()) and ("chorus" in  performers.lower().strip()) and ("orchestra" in  performers.lower().strip()):
                    print ("Yep")
                else:
                    print ("Nope, soloist, orchestra and chorus")
    if p == "instrumental":
        for i in range(3):
            k = input("There are three major instrumental families during this time period. Name one: ")
            if k == "keyboard":
                print ("Yep")
                print ("\n\n")
                type = input("Which one are you talking about?: ")
                if type == "harpsichord":
                    differences = input("Name three differences between harpsichord and modern piano: ")
                    print ("Yep, differences include: \n\tStrings are plucked with a pick instead of struck with a hammer, \n\tTwo sets of keys, \n\tOften more black then white keys because white keys were made of ivory.")
                elif type == "organ":
                    print ("Yep, Bach played that very well!")
                type = input("What is the other one?: ")
                if type == "harpsichord":
                    differences = input("Name three differences between harpsichord and modern piano: ")
                    print ("Yep, differences include: \n\tStrings are plucked with a pick instead of struck with a hammer, \n\tTwo sets of keys, \n\tOften more black then white keys because white keys were made of ivory.")
                elif type == "organ":
                    print ("Yep also that!")
            if k == "strings":
                differece = input("Name three differences between modern and baroque violin: ")
                print ("Baroque violins had no chin rest, the bridges were shorter and the strings were made of animal guts")
                bow = input("Name three differences with the bows: ")
                print ("Baroque bows and pointy tips rather then the hatchet shape, clip on frogs and curved inwards rather then outwards")
            if k == "winds":
                print ("Yep, winds were a thing but we are not the band so we don't go too in depth!")
    if p == "antonio":
        print ("\n\nVivaldi time!")
        born = input("Name three facts about Vivaldi such as birth place, son of a _____, nickname, social class")
        print ("Antonio Vivaldi was born in Venice Italy and lived form 1648-1741. He was nicknamed as the Red haired Priest, he was the son of a violinist and he died impoverished")
    if p == "bach":
        section = input("What section you wanna do?\nType city for cities, \nType family for family, \nType music for his music: ")
        if section == "city":
            for i in range(3):
                city = input("Name a city he worked in: ")
                if city == "weimar":
                    dates = input("What were the dates he worked there?: ")
                    
