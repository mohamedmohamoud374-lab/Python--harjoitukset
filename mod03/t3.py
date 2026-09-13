sukupuoli = input("Anna biologinen sukupuoli (nainen/mies): ")
arvo =float(input("Anna hemoglobiiniarvo (g/1): "))

if sukupuoli == "nainen" and 117 <= arvo <= 175:
    print("Normaali")
elif sukupuoli == "nainen" and arvo < 117:
    print("Alhainen")
elif sukupuoli == "nainen" and arvo > 175:
    print("korkea")
elif sukupuoli == "mies" and 134 <= arvo <= 195:
    print("Normaali")
elif sukupuoli == "mies" and arvo < 134:
    print("Alhainen")
elif sukupuoli == "mies" and arvo > 195:
    print("korkea")
else: 
    print("virheellinen syöte.")
               