# Bankautomat (ATM) Simulation
kontostand = 1000.0

pin = "12345"
versuche = 3

while versuche > 0:
    eingabe_pin = input("Bitte geben Sie Ihre PIN ein: ")

    if eingabe_pin == pin:
        print("\nPin korrekt! Wilkommen.")
        break
    else:
        versuche -= 1
        if versuche > 0:
            print(f"Falsche PIN! Bitte versuchen Sie es erneut. (Verbleibende Versuche: {versuche})" )
        else:
            print("Zu viele falsche Eingaben! Karte wurde gesperrt.")
            exit()

while True:
    print("1. Kontostand prüfen")
    print("2. Geld einzahlen")
    print("3. Geld abheben")
    print("4. Beenden")
    
    auswahl = input("Bitte wählen Sie eine Option (1-4): ")

    if auswahl == "1":
        print(f"\nIhr aktueller Kontostand beträgt: {kontostand:.2f} €")

    elif auswahl == "2":
        try:
            einzahlung = float(input("\nGeben Sie den Einzahlungsbetrag ein: €"))
            if einzahlung > 0:
                kontostand += einzahlung
                print(f"Erfolgreich eingezahlt! Neuer Kontostand: {kontostand:.2f} €")
            else:
                print("Bitte geben Sie einen gültigen Betrag ein.")
        except ValueError:
            print("Ungültige Eingabe! Bitte nur Zahlen eingeben.")

    elif auswahl == "3":
        try:
            auszahlung = float(input("\nGeben Sie den Auszahlungsbetrag ein: €"))
            if auszahlung <= 0:
                print("Bitte geben Sie einen gültigen Betrag ein.")
            elif auszahlung <= kontostand:
                kontostand -= auszahlung
                print(f"Erfolgreich abgehoben! Neuer Kontostand: {kontostand:.2f} €")
            else:
                print("Fehler: Unzureichendes Guthaben auf Ihrem Konto!")
        except ValueError:
            print("Ungültige Eingabe! Bitte nur Zahlen eingeben.")

    elif auswahl == "4":
        print("\nVielen Dank für Ihre Nutzung. Auf Wiedersehen!")
        break

    else:
        print("\nUngültige Auswahl! Bitte wählen Sie eine Zahl von 1 bis 4.")