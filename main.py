import os
import matplotlib.pyplot as plt
import numpy as np
import requests


def gEnErUj_hIsToGrAm(tekst, lItErY_wLaSnE=None):
    hIsToGrAm = {}
    for znAk in tekst:
        if znAk.isalpha() and (not lItErY_wLaSnE or znAk.lower() in lItErY_wLaSnE):
            znAk = znAk.lower()
            if znAk in hIsToGrAm:
                hIsToGrAm[znAk] += 1

            else:
                hIsToGrAm[znAk] = 1
    return hIsToGrAm

def zApIsZ_hIsToGrAm_jAkO_oBrAz(hIsToGrAm, nAzWa_PlIkU):
    lItErY = list(hIsToGrAm.keys())
    iLoScI = list(hIsToGrAm.values())

    x = np.arange(len(lItErY))
    plt.bar(x, iLoScI)
    plt.xticks(x, lItErY)
    plt.xlabel('Litery')
    plt.ylabel('Częstotliwość')
    plt.title('Histogram Częstotliwości Liter')
    plt.savefig(nAzWa_PlIkU, format='png')

def gEnErUj_hIsToGrAm_z_tEkStU(tekst, lItErY_wLaSnE=None, tYtUl="Histogram Częstotliwości Liter"):
    hIsToGrAm = gEnErUj_hIsToGrAm(tekst, lItErY_wLaSnE)

    for znAk, iLoSc in hIsToGrAm.items():
        print(f"{znAk}: {iLoSc}")

    zApIsZ_hIsToGrAm_jAkO_oBrAz(hIsToGrAm, f"{tYtUl}_histogram.png")

def pObIeRz_tEkSt_z_PlIkU(sCiEzKa_PlIkU):
    with open(sCiEzKa_PlIkU, 'r') as pLiK:
        return pLiK.read()

def pObIeRz_tEkSt_z_UrL(url):
    rEsPoNdSe = requests.get(url)
    if rEsPoNdSe.status_code == 200:
        return rEsPoNdSe.text
    else:
        print("Nie udało się pobrać tekstu z URL.")
        return ""

def mAiN():
    while True:
        print("Menu:")
        print("1. Generuj histogram z tekstu wprowadzonego z klawiatury.")
        print("2. Generuj histogram z pliku tekstowego.")
        print("3. Generuj histogram z tekstu pobranego z URL.")
        print("4. Wyjście")

        wYbOr = input("Wybierz opcję: ")

        if wYbOr == "1":
            lItErY_wLaSnE = input("Podaj zestaw liter oddzielonych przecinkami (opcjonalne): ")
            lItErY_wLaSnE = lItErY_wLaSnE.split(',') if lItErY_wLaSnE else None
            tekst = input("Wprowadź tekst: ")
            gEnErUj_hIsToGrAm_z_tEkStU(tekst, lItErY_wLaSnE, "WejścieUżytkownika")
        elif wYbOr == "2":
            kAtAlOg_dAnYcH = "katalog"
            for nAzWa_PlIkU in os.listdir(kAtAlOg_dAnYcH):
                if nAzWa_PlIkU.endswith(".txt"):
                    sCiEzKa_PlIkU = os.path.join(kAtAlOg_dAnYcH, nAzWa_PlIkU)
                    lItErY_wLaSnE = input("Podaj zestaw liter oddzielonych przecinkami (opcjonalne): ")
                    lItErY_wLaSnE = lItErY_wLaSnE.split(',') if lItErY_wLaSnE else None
                    tekst = pObIeRz_tEkSt_z_PlIkU(sCiEzKa_PlIkU)
                    gEnErUj_hIsToGrAm_z_tEkStU(tekst, lItErY_wLaSnE, nAzWa_PlIkU)
        elif wYbOr == "3":
            url = input("Podaj URL: ")
            lItErY_wLaSnE = input("Podaj zestaw liter oddzielonych przecinkami (opcjonalne): ")
            lItErY_wLaSnE = lItErY_wLaSnE.split(',') if lItErY_wLaSnE else None
            tekst = pObIeRz_tEkSt_z_UrL(url)
            gEnErUj_hIsToGrAm_z_tEkStU(tekst, lItErY_wLaSnE, "TekstZURL")
        elif wYbOr == "4":
            break
        else:
            print("Nieprawidłowy wybór. Wybierz opcję od 1 do 4.")


if __name__ == "__main__":
    mAiN()
