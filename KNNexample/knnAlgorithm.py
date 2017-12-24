import csv
import math
import matplotlib.pyplot as plt

def udaljenost(prosjeci: object, godineStudija: object, praksa: object, prosjek: object, gS: object) -> object:
    #funkcija za mjerenje udaljenosti
    #između trening skupa i ulaznog primjerka
    udaljenost = []
    a=[]
    b=[]
    novi = []
    for i in range(0,len(prosjeci)):
        a = pow((float(prosjeci[i]) - float(prosjek)), 2)
        b = pow((float(godineStudija[i]) - gS), 2)
        d=a+b
        udaljenost.append(math.sqrt(d))
        a=0
        b=0
        novi.append(list([prosjeci[i], godineStudija[i], math.sqrt(d), praksa[i]]))
    return novi


def vizualizacija(studenti, b, a):
    a = int(a)
    b = float(b)
    i=0
    xY = []
    yY = []
    xN = []
    yN = []
    #Razdvajanje na dvije liste studenata: one koji su primljeni
    #i one koji nisu primljeni na praksu
    for i in range(0,len(studenti)):
        if(studenti[i][2] == "Y;"):
            xY.append(studenti[i][0])
            yY.append(studenti[i][1])
        if (studenti[i][2] == "N;"):
            xN.append(studenti[i][0])
            yN.append(studenti[i][1])
    #Prikaz na grafiku
    plt.scatter(a, b, c='b')
    plt.scatter(xN,yN, c='r')
    plt.scatter(xY, yY, c='g')
    plt.xlabel("Godina studija")
    plt.ylabel("Prosjek ocjena")
    plt.show()

def main():
    studenti=[]
    prosjeci=[]
    primljen=[]
    godineStudija=[]

    #otvaranje baze podataka

    with open('praksa.csv') as csvfile:
        studenti1 = csv.reader(csvfile, delimiter=',')
        studenti = list(studenti1)

    #razdvajanje liste sačinjene od liste studenata na 3 liste
    for i in range(0, len(studenti)):
        for j in range(0, len(studenti[0])):
            if (j == 0):
                godineStudija.append(studenti[i][j])
            if (j==1):
                prosjeci.append(studenti[i][j])
            if (j==2):
                primljen.append(studenti[i][j])
    goStud = input("Unesite godinu studija: ")
    proOcj = input("Unesite prosjek ocjena: ")
    #validacija ulaza
    if (int(goStud) > 5 or float(proOcj) >10 or int(goStud) < 1 or float(proOcj) < 6):
        return

    #mjerenje udaljenosti ulaza

    novi = udaljenost(prosjeci, godineStudija, primljen, float(proOcj), int(goStud))

    vizualizacija(studenti, proOcj, goStud)
    #sortiranje
    novi = sorted(novi, key=lambda novi:novi[2])
    K = input("Unesite parametar K: ")
    #validacija ulaza
    if (int(K) < 1):
        return
    jes=0
    no = 0

    #brojanje glasova
    for i in range(0, int(K)):
        if (novi[i][3]=="Y;"):
            jes+=1
        else:
            no+=1
    if (jes >= no):
        print("Kandidat je primljen na praksu, čestitamo!")
    else:
        print("Nažalost, kandidat nije primljen na praksu.")

main()
