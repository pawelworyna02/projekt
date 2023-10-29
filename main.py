import os
import matplotlib.pyplot as plt
import numpy as np
import requests

def generuj_histogram(tekst, litery_wlasne=None):
    histogram = {}
    for znak in tekst:
        if znak.isalpha() and (not litery_wlasne or znak.lower() in litery_wlasne):
            znak = znak.lower()
            if znak in histogram:
                histogram[znak] += 1
            else:
                histogram[znak] = 1
    return histogram

def zapisz_histogram_jako_obraz(histogram, nazwa_pliku):
    litery = list(histogram.keys())
    ilosci = list(histogram.values())

    x = np.arange(len(litery))
    plt.bar(x, ilosci)
    plt.xticks(x, litery)
    plt.xlabel('Litery')
    plt.ylabel('Częstotliwość')
    plt.title('Histogram Częstotliwości Liter')
    plt.savefig(nazwa_pliku, format='png')

def generuj_histogram_z_tekstu(tekst, litery_wlasne=None, tytul="Histogram Częstotliwości Liter"):
    histogram = generuj_histogram(tekst, litery_wlasne)

    for znak, ilosc in histogram.items():
        print(f"{znak}: {ilosc}")

    zapisz_histogram_jako_obraz(histogram, f"{tytul}_histogram.png")

def pobierz_tekst_z_pliku(sciezka_pliku):
    with open(sciezka_pliku, 'r') as plik:
        return plik.read()

def pobierz_tekst_z_url(url):
    odpowiedz = requests.get(url)
    if odpowiedz.status_code == 200:
        return odpowiedz.text
    else:
        print("Nie udało się pobrać tekstu z URL.")
        return ""

def main():
    while True:
        print("Menu:")
        print("1. Generuj histogram z tekstu wprowadzonego z klawiatury.")
        print("2. Generuj histogram z pliku tekstowego.")
        print("3. Generuj histogram z tekstu pobranego z URL.")
        print("4. Wyjście")

        wybor = input("Wybierz opcję: ")


        if wybor == "1":
            litery_wlasne = input("Podaj zestaw liter oddzielonych przecinkami (opcjonalne): ")
            litery_wlasne = litery_wlasne.split(',') if litery_wlasne else None
            tekst = input("Wprowadź tekst: ")
            generuj_histogram_z_tekstu(tekst, litery_wlasne, "WejścieUżytkownika")
        elif wybor == "2":
            katalog_danych = "katalog"
            for nazwa_pliku in os.listdir(katalog_danych):
                if nazwa_pliku.endswith(".txt"):
                    sciezka_pliku = os.path.join(katalog_danych, nazwa_pliku)
                    litery_wlasne = input("Podaj zestaw liter oddzielonych przecinkami (opcjonalne): ")
                    litery_wlasne = litery_wlasne.split(',') if litery_wlasne else None
                    tekst = pobierz_tekst_z_pliku(sciezka_pliku)
                    generuj_histogram_z_tekstu(tekst, litery_wlasne, nazwa_pliku)
        elif wybor == "3":
            url = input("Podaj URL: ")
            litery_wlasne = input("Podaj zestaw liter oddzielonych przecinkami (opcjonalne): ")
            litery_wlasne = litery_wlasne.split(',') if litery_wlasne else None
            tekst = pobierz_tekst_z_url(url)
            generuj_histogram_z_tekstu(tekst, litery_wlasne, "TekstZURL")
        elif wybor == "4":
            break
        else:
            print("Nieprawidłowy wybór. Wybierz opcję od 1 do 4.")


if __name__ == "__main__":
    main()
