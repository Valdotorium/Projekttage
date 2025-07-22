def multiplyNumber(number, factor): #Funktion, die eine eingegebene Zahl quadriert
    print(f"Das Ergebnis von {number} mal {factor} ist: {number * factor}")  # Ausgabe des Ergebnisses
    return number * factor

input_number = int(input("Gib eine Zahl zum multiplizieren ein: ")) 

x = 1

while x < 10:  # Solange x kleiner als 10 ist
    result = multiplyNumber(input_number, x)  # Aufruf der Funktion
    x += 1  # Erhöht x um 1