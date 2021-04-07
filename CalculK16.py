#  Copyright (c) 2021 - Marc Bourbonnot - 22001994
#  Desc : contient la fonction permettant de calculer la valeur de K16

import FonctionsEtDonnees


#  Fonction permettant le calcul de K16
def calculK16(hexaChiffrJuste, hexaChiffrFaux):
    #  Passage des chiffres de la notation hexa en notation binaire (64bits)
    binChiffrJuste = FonctionsEtDonnees.from_hex_to_bin(hexaChiffrJuste)

    binChiffrFaux = []
    for i in range(len(hexaChiffrFaux)):
        binChiffrFaux.append(FonctionsEtDonnees.from_hex_to_bin(hexaChiffrFaux[i]))

    #  On applique IP pour obtenir R16 L16 (64bits)
    IPBinChiffrJuste = FonctionsEtDonnees.calcul_IP(binChiffrJuste)

    IPBinChiffrFaux = []
    for i in range(len(binChiffrFaux)):
        IPBinChiffrFaux.append(FonctionsEtDonnees.calcul_IP(binChiffrFaux[i]))

    # On divise en 2 * 32 bits pour représenter L16 et R16
    L16 = IPBinChiffrJuste[32:]
    R16 = IPBinChiffrJuste[:32]

    L16Faux = []
    R16Faux = []

    for i in IPBinChiffrFaux:
        L16Faux.append(i[32:])
        R16Faux.append(i[:32])

    #  Calcul des differences entre L16 et toutes les valeurs possibles de L16 faute
    diffs_L16_L16Faux = []
    for i in L16Faux:
        diffs_L16_L16Faux.append(FonctionsEtDonnees.xor(L16, i))

    #  On calcul E(L16) = E(R15) (32 bits (L16) -> 48 bits(E(L16)))
    E_L16 = FonctionsEtDonnees.calcul_E(L16)

    E_L16Faute = []
    for i in L16Faux:
        E_L16Faute.append(FonctionsEtDonnees.calcul_E(i))

    #  Calcul des differences entre E(L16) = E(R15) et toutes les valeurs possibles de E(L16) faute
    diffs_SBoxIn_SBoxInFaux = []
    for i in E_L16Faute:
        diffs_SBoxIn_SBoxInFaux.append(FonctionsEtDonnees.xor(E_L16, i))

    #  Calcul des differences entre F(R16) et toutes les valeurs possibles de F(R16) faute
    diffs_FR16_FR16Faux = []
    for i in R16Faux:
        diffs_FR16_FR16Faux.append(FonctionsEtDonnees.xor(R16, i))

    #  Calcul des differences en sortie des Sboxs entre la valeur juste et les valeurs faussees
    diffs_SBoxOut_SboxOutFaux = []
    for i in diffs_FR16_FR16Faux:
        diffs_SBoxOut_SboxOutFaux.append(FonctionsEtDonnees.calcul_Inverse_P(i))

    # on determine les entrees a etudier (les sbox dont au moins un bit de diff en entre = 1) pour trouver les
    # couples de valeurs possibles pour entre de SBox valide et entree faute
    clePossible = [[] for _ in range(8)]
    for h in range(len(diffs_SBoxIn_SBoxInFaux)):
        diff_In = diffs_SBoxIn_SBoxInFaux[h]
        diff_Out = diffs_SBoxOut_SboxOutFaux[h]

        for i in range(len(diff_In)):
            if diff_In[i] == "1":
                value_In = diff_In[i // 6 * 6:i // 6 * 6 + 6]
                value_Out = diff_Out[i // 6 * 4:i // 6 * 4 + 4]

                couplesSboxIn = FonctionsEtDonnees.calculCoupleInput(value_In)
                numSBox = i // 6
                for couple in couplesSboxIn:
                    val1 = FonctionsEtDonnees.calculSBoxes(couple[0], FonctionsEtDonnees.Sboxes[numSBox])
                    val2 = FonctionsEtDonnees.calculSBoxes(couple[1], FonctionsEtDonnees.Sboxes[numSBox])
                    if FonctionsEtDonnees.xor(val1, val2) == value_Out:
                        clePossibleCouple = FonctionsEtDonnees.xor(E_L16[i // 6 * 6:i // 6 * 6 + 6], couple[
                            0])  # ici je ne fais pas avec couple[1], car la methode calculCoupleInput me donnera le couple (couple[1], couple[0])
                        clePossible[numSBox].append(clePossibleCouple)

    #  On retrouve le fragment de K16 correct en comptant le nombre d'occurrence de chaque fragment dans la liste des fragments possible
    #  et on sélectionne celui qui à 6 occurrences, car cela est en lien avec les 6 bits d'entré de chaque sbox.
    K16 = ''
    for SBox in range(8):
        for fragment in clePossible[SBox]:
            nombreOccurence = clePossible[SBox].count(fragment)
            if nombreOccurence == 6:
                K16 += fragment
                break

    print(K16)

    #  Verifications
    for j in range(32):
        FK16XorEL16 = FonctionsEtDonnees.xor(K16, E_L16)
        FK16XorEL16F = FonctionsEtDonnees.xor(K16, E_L16Faute[j])

        sbox = ''
        for i in range(0, len(FK16XorEL16), 6):
            sbox += FonctionsEtDonnees.calculSBoxes(FK16XorEL16[i: i + 6], FonctionsEtDonnees.Sboxes[i // 6])

        permSbox = FonctionsEtDonnees.calcul_P(sbox)

        sboxF = ''
        for i in range(0, len(FK16XorEL16F), 6):
            sboxF += FonctionsEtDonnees.calculSBoxes(FK16XorEL16F[i: i + 6], FonctionsEtDonnees.Sboxes[i // 6])

        permSboxF = FonctionsEtDonnees.calcul_P(sboxF)

        if FonctionsEtDonnees.xor(permSbox, permSboxF) != FonctionsEtDonnees.xor(R16, R16Faux[j]):
            exit('erreur sur K16')

    return K16
