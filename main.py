import os
import matplotlib.pyplot as plt
import numpy as np

def generuj_histogram(tekst):
    histogram = {}
    for znak in tekst:
        if znak.isalpha():
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

def generuj_histogram_z_pliku_tekstowego(sciezka_pliku):
    with open(sciezka_pliku, 'r') as plik:
        tekst = plik.read()
        histogram = generuj_histogram(tekst)

        print(f"Histogram dla pliku {sciezka_pliku}:")
        for znak, ilosc in histogram.items():
            print(f"{znak}: {ilosc}")

        zapisz_histogram_jako_obraz(histogram, f"{sciezka_pliku.split('.')[0]}_histogram.png")

def main():
    katalog_danych = "katalog"

    for nazwa_pliku in os.listdir(katalog_danych):
        if nazwa_pliku.endswith(".txt"):
            sciezka_pliku = os.path.join(katalog_danych, nazwa_pliku)
            generuj_histogram_z_pliku_tekstowego(sciezka_pliku)

if __name__ == "__main__":
    main()
