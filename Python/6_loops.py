x = 0
while x < 10:  # Solange x kleiner als 10 ist
    print(x)  # Gibt den aktuellen Wert von x aus
    x += 1  # Erhöht x um 1

while True:  # Endlosschleife, da Bedingung immer erfüllt
    user_input = input("Gib etwas ein (oder 'x' zum Beenden)")
    if user_input.lower() == 'x':  # Überprüft, ob die Eingabe 'exit' ist
        print("Beende die Schleife.")
        break # Beendet die Schleife


