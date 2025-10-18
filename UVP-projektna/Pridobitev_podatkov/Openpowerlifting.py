import re
import requests
import csv
import os

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
}

def poberi_podatke():
    '''
    to je funkcija ki iz spletne strani vzame html in izlusci podatke, ki jih zelimo
    '''
    # ker je stran taka da je v html zapisanih le prvih 100 podatkov, moramo podatke pobirati po 100
    vsebina = []

    for x in range(0, 1000, 100):
        start = x
        end = x + 99
        url = f"https://www.openpowerlifting.org/api/rankings/raw/75/ipf/men/by-total?start={start}&end={end}&lang=sl&units=kg"
        
        r = requests.get(url)
        html = r.text

        html3 = re.findall(r'\[\s*\d+,\d+.*?\]',html, re.DOTALL)

        for tekmovalec in html3:

            # decimalne vejice moramo zamenjati s pikami saj bomo "," uporabljali za deljenje podatkov
            tekmovalec = re.sub(r'(\d),(\d)', r'\1.\2', tekmovalec)

            uporabno = '' # ne bomo uporabili vseh podatkov
            podatki = tekmovalec.split(',')

            for i, podatek in enumerate(podatki):
                if i in [1, 8, 9, 14, 16, 18, 19, 20, 21]:
                    uporabno += podatek + ','

            uporabno = uporabno.rstrip(',') # znebimo se zadnje vejice

            # poskrbimo da se podatki ne ponavljajo
            if uporabno not in vsebina: 
                vsebina.append(uporabno)

        # za preverjanje da se nalagojo novi podatki in da se vidi kje je prislo do napake
        print(len(vsebina))

    return vsebina

def slovar(vsebina):
    '''
    ta funkcija bo iz podatkov ki jih prejme kot list naredila slovar da bomo lazje napisali csv
    '''
    slovar_imen = {}

    for vrstica in vsebina:
        podatki = vrstica.split(',')
        
        podatki[3] = podatki[3].replace('~','') # nekateri tekmovalci imajo pri starosti vijugo, ki pomeni oceno

        for i, podatek in enumerate(podatki):
            podatki[i] = podatki[i].strip('"')

            if not podatki[i]:
                podatki[i] = 0 # na koncu seznama pri nekaterih manjka kaksen podatek

        ime = podatki[0]

        slovar_imen[ime] ={
            "datum": podatki[1],
            "drzava": podatki[2],
            "starost": podatki[3],
            "teza": podatki[4],
            "pocep": podatki[5],
            "bench": podatki[6],
            "deadlift": podatki[7],
            "skupaj": podatki[8]
            }              
    return slovar_imen

def ustvari_csv(slovar_imen):
    absolutna_pot = os.path.dirname(os.path.abspath(__file__))
    pot_csv = os.path.join(absolutna_pot, "podatki.csv")
    with open(pot_csv, "w", newline='', encoding="utf-8") as d:
        pisatelj = csv.writer(d)
        pisatelj.writerow([
            "ime",
            "datum",
            "drzava",
            "starost",
            "teza",
            "pocep",
            "bench",
            "deadlift",
            "skupaj"
        ])
        for ime, info in slovar_imen.items():
            pisatelj.writerow([
                ime,
                info["datum"],
                info["drzava"],
                info["starost"],
                info["teza"],
                info["pocep"],
                info["bench"],
                info["deadlift"],
                info["skupaj"]
            ])

    return slovar_imen

def podatki():
    a = slovar(poberi_podatke())
    return ustvari_csv(a)