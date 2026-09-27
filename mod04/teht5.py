oikea_tunnus = "mohamed"
oikea_salasana = "python123"
tunnus = input("käyttäjätunnus: ")
salasana = input ("Salasana: ")
yritykset =1
while (tunnus != oikea_tunnus or salasana != oikea_salasana) and yritykset < 5:
    print("väärä tunnus tai salasana.")
    tunnus =input("käyttäjätunnus: ")
    salasana = input("salasana:")
    yritykset = yritykset + 1
if tunnus == oikea_tunnus and salasana == oikea_salasana:
    print("tervetuloa")
else:
    print("pääsy estetty. liian monta yritystä.")
