#  Copyright (c) 2021 - Marc Bourbonnot - 22001994
#  Desc : programme principal

from CalculK import calculKFromK16
from CalculK16 import calculK16
from DES_Encrypt_Implementation import des


#  Mes donnees :
#  Message clair :
msgClair = "E5 D0 3E 8A 4C E5 13 2F"

#  Message chiffre juste :
chiffreJuste = "EF 3F BB 0D 09 61 CF 24"

#  Messages chiffres faux :
chiffresFaux = ["ED 3A BB 49 09 61 CF 30",
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


if __name__ == '__main__':
    K16 = calculK16(chiffreJuste, chiffresFaux)
    K = calculKFromK16(K16, msgClair, chiffreJuste)

    print("La cle K16 est : " + K16)
    print("La cle K est : " + K)
    print("Verification en chiffrant le message clair avec la clé trouvée : " + str(des(msgClair, K) == chiffreJuste.lower().replace(' ', '')))
