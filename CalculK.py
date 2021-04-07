#  Copyright (c) 2021 - Marc Bourbonnot - 22001994
#  Desc : contient la fonction permettant de calculer la valeur de K à partir de K16

from DES_Encrypt_Implementation import des
from FonctionsEtDonnees import calcul_Inverse_PC2, calcul_Inverse_PC1, from_hex_to_bin


#  Fonction permettant de retrouver la cle K a partir de la sous-cle K16
def calculKFromK16(K16, msgClair, chiffreJuste):
    C16D16s = calcul_Inverse_PC2(K16)

    keysWithoutSignByte = []
    for C0D0 in C16D16s:
        keysWithoutSignByte.append(calcul_Inverse_PC1(C0D0))

    keys = []
    for j in keysWithoutSignByte:
        key = ""
        for i in range(0, len(j), 8):
            octet = j[i:i + 8]
            count = octet.count("1")
            if count % 2 == 0:
                octet = octet.replace("2", "1")
            else:
                octet = octet.replace("2", "0")
            key += octet
        keys.append(hex(int(key, 2)).replace('0x', '').zfill(16))

    for key in keys:
        c = des(msgClair, key)
        if c == chiffreJuste.lower().replace(' ', ''):
            trueKey = key

    return trueKey
