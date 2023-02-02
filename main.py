#Megoldas
def eredmeny(g_lapok:[int],j_lapok:[int]):
    allapot = ""
    j_pontok = lapok_osszege(j_lapok)
    g_pontok = lapok_osszege(g_lapok)
    if j_pontok > 21:
        allapot ="Játékos vesztett"
    elif g_pontok > 21:
        allapot = "Gép vesztett"
    return allapot

def lapok_osszege(lapok:[int]):
    pontok: int = 0
    for i in range(len(lapok)):
        pontok += lapok[i]
    return pontok


#Teszt esetek
def teszt_esetek():
    jatekos_vesztett()
    teszt_esetek()

def jatekos_vesztett():
    jatekos = [10,9,3]
    gep = [10,9]
    vart_eredmeny ="Játékos vesztett"
    kapott_eredmeny = eredmeny(gep,jatekos)
    if kapott_eredmeny == vart_eredmeny:
        print("A teszt sikerült")
    else:
        print("A teszt nem sikerült")

def jatekos_tobb_21(allapot):
    jatekos_vesztett()

def jatekos_kevesebb_gep():
    jatekos_vesztett()


def jatekos_vesztett_21_nagyobb_teszt():
    j_lapok = [10, 9, 3]
    g_lapok = [10, 9]
    vart_eredmeny = "A játékos vesztett!"
    kapott_eredmeny = eredmeny(j_lapok, g_lapok)
    if vart_eredmeny == kapott_eredmeny:
        print("A játékos 21-nél több, a teszt sikeres")
    else:
        print("A játékos 21-nél több, a teszt megbukott")


def jatekos_vesztett_21_kevesebb_teszt():
    j_lapok = [10, 9, 1]
    g_lapok = [10, 9, 2]
    vart_eredmeny = "A játékos vesztett!"
    kapott_eredmeny = eredmeny(j_lapok, g_lapok)
    if vart_eredmeny == kapott_eredmeny:
        print("A játékos 21-nél kevesebb, a teszt sikeres")
    else:
        print("A játékos 21-nél kevesebb, a teszt megbukott")


def jatekos_vesztett_tobbet_huzott_teszt():
    jlapok = [10, 9, 1, 1]
    glapok = [10, 9, 2]
    vart_eredmeny = "A játékos vesztett!"
    kapott_eredmeny = eredmeny(jlapok, glapok)
    if vart_eredmeny == kapott_eredmeny:
        print("A játékos többet húzott teszt sikeres")
    else:
        print("A játékos többet húzott teszt megbukott")

def folyamatabra():
#    jP = ossz(jL)
#   gP = ossz(gL)

#    jDb = lapDb(jL)
#    gDb = lapDb(gL)
    jP = 0
    gP = 0
    jDb = 0
    gDb = 0

    if jP <= 21 and gP <= 21:
        if jP > 21:
            print("Játékos vesztett")
            exit()
        elif gP > 21:
            print("Gép vesztett")
            exit()
        else:
            print("Döntetlen a ház nyert")
            exit()

        if jP > gP:
            print("Játékos nyert")
            exit()
        elif gP > jP:
            print("Gép nyert")
            exit()
        else:
            if gP == jP:
                if  jDb < gDb:
                    print("Játékos nyert")
                    exit()
                elif jDb > gDb:
                    print("Gép nyert")
                    exit()
                else:
                    print("Döntetlen, osztoztok a nyereségen")
                    exit()
