def calculate_circle_area(radius): # Funktion zur Berechnung der Fläche eines Kreises
    return 3.14 * (radius ** 2)

def calculate_circumference(radius): # Funktion zur Berechnung des Umfangs eines Kreises
    return 2 * 3.14 * radius

def main():
    print("Wilkommen zum Kreisrechner!") 
    radius = float(input("Gib den Radius des Kreises ein (in cm): ")) 
    area = calculate_circle_area(radius)  
    circumference = calculate_circumference(radius) 
    
    print("Die Fläche des Kreises beträgt:", area, "cm^2")  
    print(f"Der Umfang des Kreises beträgt:", circumference, "cm") 

main()  # Aufruf der Hauptfunktion