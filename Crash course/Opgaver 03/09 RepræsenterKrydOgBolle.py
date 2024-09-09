def move():
    Optagetfelter = {3, 4, 7}
    while True:
        try:
            position = int(input(f"Spiller, hvad er dit træk (1-9)?: "))
            if position < 1 or position > 9:
                print("Du har valgt en ugyldig værdi, venligst vælg et tal mellem 1 og 9.")
            elif position in Optagetfelter:
                print(f"Position {position} er optaget. Vælg venligst et andet felt!")
            else:
                print(f"Du har valgt feltet: {position}")
                break  
        except ValueError:
            print("Du skal indtaste et gyldigt tal mellem 1 og 9.")
            
move()