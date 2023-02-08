# megoldás
def pontszamitas(lapok):
    pontok = 0
    for i in range(len(lapok)):
        pontok += lapok[i]

    return pontok


def eredmeny(jatekos_lapok, gep_lapok):
    eredmenyki = ""
    geppontok = pontszamitas(gep_lapok)
    jatekospontok = pontszamitas(jatekos_lapok)
    if geppontok <= 21 and jatekospontok <= 21:
        if jatekospontok > geppontok:
            eredmenyki = "A játékos nyert"
        elif geppontok > jatekospontok:
            eredmenyki = "A gép nyert"
        elif jatekospontok == geppontok:
            if len(jatekos_lapok) < len(gep_lapok):
                eredmenyki = "A játékos nyert"
            elif len(jatekos_lapok) > len(gep_lapok):
                eredmenyki = "A gép nyert"
            else:
                eredmenyki = "Döntetlen"
    if jatekospontok > 21:
        eredmenyki = "A játékos vesztett"
    if geppontok > 21:
        eredmenyki = "A gép vesztett"
    if jatekospontok > 21 and geppontok > 21:
        eredmenyki = "Döntetlen, a Ház nyert"
    return eredmenyki


# tesztesetek

def teszt_esetek():
    jatekosvesztett_tobb_ponttal_teszt()
    jatekosvesztett_kevesebb_ponttal_teszt()
    jatekosvesztett_kevesebb_lappal_teszt()
    gepvesztett_tobb_ponttal_teszt()
    gepvesztett_kevesebb_ponttal_teszt()
    gepvesztett_kevesebb_lappal_teszt()
    dontetlen()
    dontetlen_max_pont()
    gepvesztett_tobb_lappal()
    jatekosvesztett_tobb_lappal()
    jatekosvesztett_19p_tobb_lap()


def jatekosvesztett_tobb_ponttal_teszt():
    jatekos_lapok = [10, 10, 5, ]
    gep_lapok = [5, 10]
    varteredmeny = "A játékos vesztett"
    kapotteredmeny = eredmeny(jatekos_lapok, gep_lapok)
    print("A játékos vesztett teszt(több ponttal): ", end="")
    if kapotteredmeny == varteredmeny:
        print("A teszt sikeres")
    else:
        print("A teszt megbukott")





def jatekosvesztett_kevesebb_lappal_teszt():
    jatekos_lapok = [10, 5, 5]
    gep_lapok = [10, 10]
    varteredmeny = "A gép nyert"
    kapotteredmeny = eredmeny(jatekos_lapok, gep_lapok)
    print("A játékos vesztett teszt (kevesebb lappal): ", end="")
    if kapotteredmeny == varteredmeny:
        print("A teszt sikeres")
    else:
        print("A teszt megbukott")


def gepvesztett_tobb_ponttal_teszt():
    jatekos_lapok = [10, 10, ]
    gep_lapok = [5, 10, 10]
    varteredmeny = "A gép vesztett"
    kapotteredmeny = eredmeny(jatekos_lapok, gep_lapok)
    print("A gép vesztett teszt(több ponttal): ", end="")
    if kapotteredmeny == varteredmeny:
        print("A teszt sikeres")
    else:
        print("A teszt megbukott")

def jatekosvesztett_kevesebb_ponttal_teszt():
    jatekos_lapok = [10, 5]
    gep_lapok = [10, 10]
    varteredmeny = "A gép nyert"
    kapotteredmeny = eredmeny(jatekos_lapok, gep_lapok)
    print("A játékos vesztett teszt (kevesebb ponttal): ", end="")
    if kapotteredmeny == varteredmeny:
        print("A teszt sikeres")
    else:
        print("A teszt megbukott")

def gepvesztett_kevesebb_lappal_teszt():
    jatekos_lapok = [10, 10]
    gep_lapok = [10, 5, 5]
    varteredmeny = "A játékos nyert"
    kapotteredmeny = eredmeny(jatekos_lapok, gep_lapok)
    print("A gép vesztett teszt (kevesebb lappal): ", end="")
    if kapotteredmeny == varteredmeny:
        print("A teszt sikeres")
    else:
        print("A teszt megbukott")



def gepvesztett_kevesebb_ponttal_teszt():
    jatekos_lapok = [10, 10]
    gep_lapok = [10, 5]
    varteredmeny = "A játékos nyert"
    kapotteredmeny = eredmeny(jatekos_lapok, gep_lapok)
    print("A gép vesztett teszt (kevesebb ponttal): ", end="")
    if kapotteredmeny == varteredmeny:
        print("A teszt sikeres")
    else:
        print("A teszt megbukott")


def dontetlen():
    jatekos_lapok = [10, 10]
    gep_lapok = [10, 10]
    varteredmeny = "Döntetlen"
    kapotteredmeny = eredmeny(jatekos_lapok, gep_lapok)
    print("Döntetlen (kevesebb lappal): ", end="")
    if kapotteredmeny == varteredmeny:
        print("A teszt sikeres")
    else:
        print("A teszt megbukott")


def dontetlen_max_pont():
    jatekos_lapok = [12, 10]
    gep_lapok = [12, 10]
    varteredmeny = "Döntetlen, a Ház nyert"
    kapotteredmeny = eredmeny(jatekos_lapok, gep_lapok)
    print("Döntetlen (több ponttal mint 21): ", end="")
    if kapotteredmeny == varteredmeny:
        print("A teszt sikeres")
    else:
        print("A teszt megbukott")


def gepvesztett_tobb_lappal():
    jatekos_lapok = [10, 9, 2]
    gep_lapok = [10, 9, 1, 1]
    varteredmeny = "A gép vesztett"
    kapotteredmeny = eredmeny(jatekos_lapok, gep_lapok)
    print("A gép többet húzott teszt: ", end="")
    if varteredmeny == kapotteredmeny:
        print("A teszt sikeres")
    else:
        print("A teszt megbukott")

def jatekosvesztett_tobb_lappal():
    jatekos_lapok = [10, 9, 1, 1]
    gep_lapok = [10, 9, 2]
    varteredmeny = "A játékos vesztett"
    kapotteredmeny = eredmeny(jatekos_lapok, gep_lapok)
    print("A játékos többet húzott teszt: ", end="")
    if varteredmeny == kapotteredmeny:
        print("A teszt sikeres")
    else:
        print("A teszt megbukott")

def jatekosvesztett_19p_tobb_lap():
    jatekos_lapok = [9, 9, 1]
    gep_lapok = [10, 9]
    varteredmeny = "A játékos vesztett"
    kapotteredmeny = eredmeny(jatekos_lapok, gep_lapok)
    print("A játékos vesztett teszt (több lappal mint a gép): ", end="")
    if kapotteredmeny == varteredmeny:
        print("A teszt sikeres")
    else:
        print("A teszt megbukott")


teszt_esetek()


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
