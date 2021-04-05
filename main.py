#  Copyright (c) 2021. Marc Bourbonnot 22001994


#  Mes donnees :
#  Message chiffre juste :
hexaChiffrJuste = "EF 3F BB 0D 09 61 CF 24"

#  Messages chiffres faux :
hexaChiffrFaux = ["ED 3A BB 49 09 61 CF 30",
                  "EF 2D BB 4D 09 60 CF 24",
                  "EF 2F B9 49 09 61 CF 24",
                  "EE 6F BB 4F 09 61 CF 24",
                  "EE 7F BF 49 0B 61 CF 24",
                  "EF 7F BB 0D 19 63 CF 24",
                  "EE 3F BF 0D 09 61 CD 24",
                  "EE 7F BB 0C 49 65 CF 26",
                  "E6 7F BF 0C 49 61 CF 24",
                  "EF 37 BB 0D 49 65 CF 24",
                  "EF 3F B3 0C 09 75 CF 24",
                  "AF 3F AB 04 49 25 CF 24",
                  "EF 3F BB 0C 41 35 CF 25",
                  "EF 3F AB 0D 09 69 CF 25",
                  "AF 3F AB 0D 09 61 C7 24",
                  "AF 3F AB 0D 0D 61 CF 6D",
                  "8F 3F BB 0D 0D 21 CE 64",
                  "EF 1F BB 0D 0D 61 DE 64",
                  "EF 3F 9B 0D 09 61 DF 64",
                  "EB 3F FA 2D 09 61 DE 64",
                  "EF 3F FA 0D 29 61 DF 64",
                  "EB 3F FA 0D 09 41 CF 24",
                  "FF 3F FA 0D 09 61 EF 24",
                  "FB 3F FB 0D 08 61 8F 04",
                  "7B 3F BB 0D 08 61 CB 24",
                  "EF BF BB 1D 08 61 CF 24",
                  "EF 3F 3B 0D 09 61 8B 24",
                  "EF 3E BB 9D 09 61 8F 34",
                  "EF 3A BB 1D 88 61 CF 34",
                  "EF 3A BB 0D 09 E1 CF 30",
                  "EF 3E BB 0D 09 61 4F 34",
                  "EF 3B BB 4D 09 60 CF B0"]

#  Permutations necessaires :
#  IP :
IP = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

#  E :
E = [32, 1, 2, 3, 4, 5,
     4, 5, 6, 7, 8, 9,
     8, 9, 10, 11, 12, 13,
     12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21,
     20, 21, 22, 23, 24, 25,
     24, 25, 26, 27, 28, 29,
     28, 29, 30, 31, 32, 1]

#  P :
P = [16, 7, 20, 21,
     29, 12, 28, 17,
     1, 15, 23, 26,
     5, 18, 31, 10,
     2, 8, 24, 14,
     32, 27, 3, 9,
     19, 13, 30, 6,
     22, 11, 4, 25]

#  S-Boxes :
Sboxes = [
    [
        14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
        0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
        4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
        15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13
    ],
    [
        15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
        3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
        0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
        13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9
    ],
    [
        10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
        13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
        13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
        1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12
    ],
    [
        7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
        13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
        10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
        3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14
    ],
    [
        2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
        14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
        4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
        11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3
    ],
    [
        12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
        10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
        9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
        4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13
    ],
    [
        4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
        13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
        1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
        6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12
    ],
    [
        13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
        1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
        7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
        2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11
    ]
]


#  Fonctions :
#  Fonction permettant de passer de la notation hexadecimal a la notation binaire
def from_hex_to_bin(hex):
    # Suppression des espaces potentiellement presents qui sont non necessaires a la convertion
    hex = hex.replace(" ", "")
    res = ""
    for i in hex:
        # zfill(6) : 4 bit pour l'hexa + 2 bit pour "0b" (enlever ensuite)
        res += bin(int(i, 16)).zfill(6).replace("0b", "")
    return res


#  Fonction permettant de calculer la permutation IP a partir d'une notation bianire sur 64 bits du message
def calcul_IP(bin):
    res = ""
    for i in range(0, 64):
        res += bin[IP[i] - 1]
    return res


#  Fonction permettant de calculer l'expansion E de la fonction F du DES a partir de la notation permutés sur 64 bits
def calcul_E(permutedBin):
    res = ""
    for i in range(48):
        res += permutedBin[E[i] - 1]
    return res


#  Fonction permettant de calculer la permutation P (pour tester calcul_Inverse_P)
def calcul_P(value):
    res = ""
    for i in range(len(P)):
        res += value[P[i] - 1]

    return res


#  Fonction permettant de calculer l'inverse de la permutation P
def calcul_Inverse_P(value):
    tmp = [0 for i in range(32)]
    for i in range(len(P)):
        tmp[P[i] - 1] = value[i]

    res = ""
    for i in tmp:
        res += str(i)

    return res


#  Fonction permettant de calculer le xor entre deux varaibles de meme taille
def xor(a, b):
    if len(a) != len(b):
        exit("erreur de calcul sur le xor : len(a) != len(b)")

    res = ""
    for i in range(len(a)):
        res += str((int(a[i]) + int(b[i])) % 2)
    return res


#  Fonction retournant la valeur de sortie de la sbox pour la valeur entree
def calculSBoxes(value, tabSbox):
    if len(value) != 6:
        exit("erreur calcul des sbox len(entree) != 6")

    ligne = value[0] + value[5]
    colonne = value[1:5]

    indice_ligne = int(ligne, 2)
    indice_colonne = int(colonne, 2)

    return tabSbox[indice_ligne * 16 + indice_colonne]


#  Fonction de test permettant de représenter visuellement la différence entre une valeur et un tableau de valeur
def testAffichageDifferenceEntreVraiEtLesFaux(val, tab):
    for i in range(len(tab)):
        printable = ""
        fautChiffr = tab[i]
        for j in range(len(val)):
            if val[j] == fautChiffr[j]:
                printable += "-"
            else:
                printable += "*"
        print(printable)


#  Fonction permettant le calcul de K16
def calculK16():
    #  Passage des chiffres de la notation hexa en notation binaire (64bits)
    binChiffrJuste = from_hex_to_bin(hexaChiffrJuste)

    binChiffrFaux = []
    for i in range(len(hexaChiffrFaux)):
        binChiffrFaux.append(from_hex_to_bin(hexaChiffrFaux[i]))

    #  On applique IP pour obtenir R16 L16 (64bits)
    IPBinChiffrJuste = calcul_IP(binChiffrJuste)

    IPBinChiffrFaux = []
    for i in range(len(binChiffrFaux)):
        IPBinChiffrFaux.append(calcul_IP(binChiffrFaux[i]))

    # On divise en 2 * 32 bits pour représenter L16 et R16
    L16 = IPBinChiffrJuste[32:]
    R16 = IPBinChiffrJuste[:32]

    L16Faux = []
    R16Faux = []

    for i in IPBinChiffrFaux:
        L16Faux.append(i[32:])
        R16Faux.append(i[:32])

    #  On calcul E(L16) = E(R15) (32 bits (L16) -> 48 bits(E(L16)))
    E_L16 = calcul_E(L16)

    E_L16Faute = []
    for i in L16Faux:
        E_L16Faute.append(calcul_E(i))

    #  Calcul des differences entre E(L16) = E(R15) et toutes les valeurs possibles de E(L16) faute
    diff_EL16_EL16Faux = []
    for i in E_L16Faute:
        diff_EL16_EL16Faux.append(xor(E_L16, i))
        print(xor(E_L16, i))


calculK16()
