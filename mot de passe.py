import os
import subprocess
from concurrent.futures import ProcessPoolExecutor

caracteres = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
              "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
              "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "!", "@", "#", "$", "%", "&", "*", "(", ")", "-", "_", "+", "=", "[", "]", "{", "}",
              ";", ":", "'", '"', "<", ">", ",", ".", "?", "/"]

def extraire_dernier_mot(archive):
    """Extrait le dernier mot de passe d'une archive 7z"""
    temp_file = "temp.txt"
    try:
        subprocess.run(['7z', 'e', '-so', archive], stdout=open(temp_file, 'wb'), check=True)
        with open(temp_file, 'rb') as f:
            lines = f.read().splitlines()
            return lines[-1].decode() if lines else None
    finally:
        if os.path.exists(temp_file):
            os.remove(temp_file)

def trouver_progres(caractere):
    """Trouve le dernier mot de passe généré pour un caractère donné"""
    max_suffix = -1
    dernier_mot = None
    for fichier in os.listdir():
        if fichier.startswith(f"{caractere}_") and fichier.endswith(".7z"):
            suffix = int(fichier.split('_')[1].split('.')[0])
            if suffix > max_suffix:
                max_suffix = suffix
                dernier_mot = extraire_dernier_mot(fichier)
    return dernier_mot

def mot_to_compteur(mot):
    """Convertit un mot de passe en compteur numérique"""
    return sum(caracteres.index(c) * (len(caracteres)**i) for i, c in enumerate(reversed(mot)))

def compteur_to_mot(compteur):
    """Convertit un compteur en mot de passe"""
    mot = []
    for _ in range(5):
        mot.append(caracteres[compteur % len(caracteres)])
        compteur = compteur // len(caracteres)
    return ''.join(reversed(mot))

def generer_pour_caractere(caractere):
    dernier_mot = trouver_progres(caractere)
    debut = 0
    if dernier_mot:
        debut = mot_to_compteur(dernier_mot[1:]) + 1  # On saute le premier caractère
    
    suffixe = 0
    while True:
        nom_fichier = f"{caractere}_{suffixe:03d}.txt"
        if not os.path.exists(nom_fichier) and not os.path.exists(f"{nom_fichier}.7z"):
            break
        suffixe += 1

    try:
        with open(nom_fichier, 'ab') as f:
            for compteur in range(debut, len(caracteres)**5):
                mot_partiel = compteur_to_mot(compteur)
                mot_complet = caractere + mot_partiel
                f.write(mot_complet.encode() + b'\n')
                
                if f.tell() >= 10 * 1024**3:  # 10 Go
                    f.close()
                    subprocess.run(['7z', 'a', '-t7z', f"{nom_fichier}.7z", nom_fichier], check=True)
                    os.remove(nom_fichier)
                    suffixe += 1
                    nom_fichier = f"{caractere}_{suffixe:03d}.txt"
                    f = open(nom_fichier, 'ab')
    finally:
        if os.path.exists(nom_fichier):
            os.remove(nom_fichier)

if __name__ == "__main__":
    with ProcessPoolExecutor() as executor:
        executor.map(generer_pour_caractere, caracteres)