import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Pridobitev_podatkov')))

from Openpowerlifting import podatki

def main():
    rekorderji = podatki()

if __name__ == "__main__":
    main()