import random
rare_table=["X Max Immelmann","X Thunderer","X Marceau","X Hayate","X Småland",
            "X Salem","X Napoli","X Yoshino","X Moskva","X Smolensk","IX Missouri",
            "IX Georgia","IX Jean Bart","IX Musashi","IX Benham","IX Neustrashimy",
            "IX Friesland","IX Alaska","IX Kronshtadt","VIII Enterprise",
            "VIII Massachusetts","VIII Lenin","VIII Asashio","VIII Mikhail Kutuzov","VII Z-39",
            "VII Haida","VII Nelson","VII Flint","VII Belfast","VI Erich Loewenhardt",
            "VI Admiral Graf Spee","VI T-61"]


t8t9_table=["IX Pommern","IX Marco,Polo","IX Ägir","IX Azuma","IX Z-44",
            "IX Groningen","VIII Saipan","VIII Indomitable","VIII Graf Zeppelin",
            "VIII Kaga","VIII Alabama","VIII Constellation","VIII Vanguard","VIII Gascogne",
            "VIII Champagne","VIII Flandre","VIII Tirpitz","VIII Roma","VIII Kii","VIII Borodino",
            "VIII Congress","VIII Wichita","VIII Cheshire","VIII Tiger '59","VIII Belfast'43",
            "VIII Bayard","VIII Prinz Eugen","VIII Mainz","VIII Atago","VIII Tone","VIII Ochakov",
            "VIII Pyotr Bagration","VIII Irian","VIII Kidd","VIII Cossack","VIII Le Terrible",
            "VIII Z-35","VIII Orkan","VIII Loyang","VIII Fenyang","VIII Siliwangi"]

t5t6t7_table=["VII Florida","VII California","VII Hood","VII Duke of York","VII Strasbourg",
              "VII Scharnhorst","VII Ashitaka","VII Hyūga","VII Poltava","VII Atlanta","VII Indianapolis",
              "VII Boise","VII München","VII Weimar","VII Duca degli Abruzzi","VII Gorizia","VII Lazo",
              "VII Nueve de Julio","VII Yukon","VII Sims","VII Yūdachi","VII Leningrad","VII Błyskawica",
              "VI Ark Royal","VI W.Virginia 1941","VI Arizona","VI Warspite","VI Dunkerque",
              "VI Prinz Eitel Friedrich","VI Mutsu","VI London","VI De Grasse","VI Duca d'Aosta",
              "VI Molotov","VI Admiral Makarov","VI Perth","VI Mysore","VI Huanghe","VI Ise","VI Monaghan",
              "VI Gallant","VI Aigle","VI Leone","VI Juruá","VI Anshan","V Texas","V Agincourt","V Oktyabrskaya Revolutsiya",
              "V Viribus Unitis","V Marblehead","V Marblehead Lima","V Exeter","V Genova","V Yahagi","V Murmansk",
              "V Krasny Krym","V Mikoyan","V Kirov","V Hill","V Siroco","V Okhotnik"]

specialsig=["30x Dragon","30x Red Dragon","30x Wyvern","30x Hydra",
            "30x Ouroboros","30x Basilisk","30x Scylla","30x Leviathan"]

camo=["20x Winter Strands Camo","20x Frosty Fir Tree Camo","20x New Year Streamer Camo"]
skycamo=["20x New Year Sky Camo"]
rarecamo=["25x New Year Camo","25x Type - 3 New Year Camo"]
ssrcamo=["5x Spring Sky","5x Asian Lantern","5x Mosaic"]

roll=-1
def gamble(x):
    pity=0
    camo_count = 0
    flag_count = 0
    t5t6t7_count = 0
    t8t9_count = 0
    t10rare_count = 0
    totaldubs = 0
    totalcoal = 0
    premiumdays = 0
    while x > 0:
        x-=1
        roll = random.randint(1,100)
        print("Pity Count: ",pity,"Rolls left",x)
        if pity == 14:
            pity = 0
            pity_roll = random.randrange(1,16)
            if pity_roll == 1:
                print("PITY ROLL",random.choice(rare_table))
                
                
            elif 2 <= pity_roll <= 4:
                print("PITY ROLL",random.choice(t8t9_table))
                
            else:
                print("PITY ROLL",random.choice(t5t6t7_table))
            
        elif 1 <= roll <= 40:
            print(random.choice(specialsig))
            flag_count+=30
            pity+=1
        
        elif 41 <= roll <= 49:
            print(random.choice(camo))
            camo_count+=20
            pity+=1

        elif 50 <= roll <= 59:
            print(random.choice(skycamo))
            camo_count+=20
            pity+=1
            
        elif 60 <= roll <= 65:
            print(random.choice(rarecamo))
            camo_count+=25
            pity+=1
            
        elif 66 <= roll <= 71:
            print(random.choice(ssrcamo))
            camo_count+=5
            pity+=1
        
        elif roll == 72:
            print("180 days of Warships Premium Account")
            premiumdays+=180
            pity+=1
            
        elif 73 <= roll <= 79:
            print("12,500 Coal")
            totalcoal+=12500
            pity+=1
        
        elif 80 <= roll <= 84:
            print("2,500 Doubloons")
            totaldubs+=2500
            pity+=1
            
        elif 85 <= roll <= 96:
            print(random.choice(t5t6t7_table))
            t5t6t7_count+=1
            pity = 0
        
        elif 97 <= roll <= 99:
            print(random.choice(t8t9_table))
            t8t9_count+=1
            pity = 0 
        
        elif roll == 100:
            print(random.choice(rare_table))
            t10rare_count+=1
            pity = 0
        
    print("\nSpecial Signal Count = ", flag_count)
    print("Total Camos = ", camo_count)
    print("Total Coal = ", totalcoal)
    print("Total Doubloons = ", totaldubs)
    print("Premium Days = ", premiumdays)
    print("Ships of t5-t7 = ", t5t6t7_count)
    print("Ships of t8-t9 = ", t8t9_count)
    print("Ships of t10 or rare = ", t10rare_count)


running=True
while running !=False:
    box_count= int(input("How many boxes are you purchasing? Type 0 to exit\n"))
    if 1 <= box_count <= 100:
        gamble(box_count)
    elif box_count == 0:
        break;
    else:
        print("try again LUL")
