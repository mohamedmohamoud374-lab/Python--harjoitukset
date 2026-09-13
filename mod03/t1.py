pituus = float(input("Anna kuhan pituus (cm): "))
if pituus < 37:
    puuttuu = 37- pituus
    print(f"laske kuha takaisin järveen. Alimittaa puuttuu {puuttuu} cm.")
else:
    print("kuha on riittävän pitkä, voit pitää sen.")
    
