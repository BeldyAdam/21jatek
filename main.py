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

