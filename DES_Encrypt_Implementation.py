#  Copyright (c) 2021 - Marc Bourbonnot - 22001994
#  Desc : implementation du chiffrement pour le DES

from FonctionsEtDonnees import calcul_PC1, shift, calcul_PC2, calcul_E, xor, calculSBoxes, calcul_P, calcul_IP, \
    calcul_Inverse_IP, Vi, Sboxes, from_hex_to_bin


#  Fonction permettant de generer les 16 sous-cles a partir de K
def key_scheduler(k):
    PC1_K = calcul_PC1(k)

    c0 = PC1_K[:28]
    d0 = PC1_K[28:]

    ci_di = []
    for shiftValue in Vi:
        c0 = shift(c0, shiftValue)
        d0 = shift(d0, shiftValue)
        ci_di.append((c0, d0))

    keys = []
    for ci, di in ci_di:
        tmp = ci + di
        keys.append(calcul_PC2(tmp))

    return keys


#  Fonction permettant de faire le calcul de F
def fonction_F(ri, key):
    E_ri = calcul_E(ri)

    E_riXorKi = xor(E_ri, key)

    SBoxOut = ""
    for i in range(0, 48, 6):
        SBoxOut += calculSBoxes(E_riXorKi[i:i + 6], Sboxes[i // 6])

    P_SBoxOut = calcul_P(SBoxOut)

    return P_SBoxOut


#  Fonction retournant le message chiffre par le DES
def des(hexMsg, hexK):
    msg = from_hex_to_bin(hexMsg)
    k = from_hex_to_bin(hexK)

    keys = key_scheduler(k)

    IP_msg = calcul_IP(msg)

    l0 = IP_msg[:32]
    r0 = IP_msg[32:]

    li_old = l0
    ri_old = r0
    for i in range(16):
        li = ri_old
        ri = xor(li_old, fonction_F(ri_old, keys[i]))

        li_old = li
        ri_old = ri

    cipher = calcul_Inverse_IP(ri + li)

    return hex(int(cipher, 2)).replace('0x', '').zfill(16)
