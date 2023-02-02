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


# Teszt esetek
def teszt_esetek():
    jatekos_vesztett_21_nagyobb_teszt()
    jatekos_vesztett_21_kevesebb_teszt()
    jatekos_vesztett_tobbet_huzott_teszt()
    dontetlen_teszt()
    gep_vesztett_21_nagyobb_teszt()
    gep_vesztett_21_kevesebb_teszt()
    gep_vesztett_tobbet_huzott_teszt()


def jatekos_vesztett_21_nagyobb_teszt():
    jlapok = [10, 9, 4]
    glapok = [10, 9]
    vart_eredmeny = "A játékos vesztett!"
    kapott_eredmeny = eredmeny(jlapok, glapok)
    if vart_eredmeny == kapott_eredmeny:
        print("A játékos 21-nél több teszt sikeres")
    else:
        print("A játékos 21-nél több teszt megbukott")


def jatekos_vesztett_21_kevesebb_teszt():
    jlapok = [10, 9, 1]
    glapok = [10, 9, 2]
    vart_eredmeny = "A játékos vesztett!"
    kapott_eredmeny = eredmeny(jlapok, glapok)
    if vart_eredmeny == kapott_eredmeny:
        print("A játékos 21-nél kevesebb teszt sikeres")
    else:
        print("A játékos '21-nél kevesebb' teszt megbukott")

def gep_vesztett_tobbet_huzott_teszt():
    jlapok = [10, 9, 2]
    glapok = [10, 9, 1, 1]
    vart_eredmeny = "A gép vesztett!"
    kapott_eredmeny = eredmeny(jlapok, glapok)
    if vart_eredmeny == kapott_eredmeny:
        print("A gép több húzás teszt sikeres")
    else:
        print("A gép több húzás teszt megbukott")


def dontetlen_teszt():
    jatekos_lapok = [5, 8]
    gep_lapok = [8, 5]
    vart_eredmeny = "Döntetlen, osztoztok a nyereségen"
    kapott_eredmeny = eredmeny(jatekos_lapok, gep_lapok)
    if kapott_eredmeny == vart_eredmeny:
        print("A döntetlen teszt sikeres")
    else:
        print("A döntetlen teszt megbukott")

def jatekos_vesztett_tobbet_huzott_teszt():
    jlapok = [10, 9, 1, 1]
    glapok = [10, 9, 2]
    vart_eredmeny = "A játékos vesztett!"
    kapott_eredmeny = eredmeny(jlapok, glapok)
    if vart_eredmeny == kapott_eredmeny:
        print("A játékos több húzás teszt sikeres")
    else:
        print("A játékos több húzás teszt megbukott")


def gep_vesztett_21_nagyobb_teszt():
    jlapok = [10, 9]
    glapok = [10, 9, 3]
    vart_eredmeny = "A gép vesztett!"
    kapott_eredmeny = eredmeny(jlapok, glapok)
    if vart_eredmeny == kapott_eredmeny:
        print("A gép 21-nél több teszt sikeres")
    else:
        print("A gép 21-nél több teszt megbukott")


def gep_vesztett_21_kevesebb_teszt():
    jlapok = [10, 9, 2]
    glapok = [10, 9, 1]
    vart_eredmeny = "A gép vesztett!"
    kapott_eredmeny = eredmeny(jlapok, glapok)
    if vart_eredmeny == kapott_eredmeny:
        print("A gép 21-nél kevesebb teszt sikeres")
    else:
        print("A gép 21-nél kevesebb teszt megbukott")





def folyamatabra():
#    jP = ossz(jL)
#    gP = ossz(gL)

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
