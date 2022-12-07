#Authoren = Paul Sadlowski s0569617 u. Nils Petersen s0569718
#Gruppe 7

import random

#Variablen
spiel_check = True
spieler = 'X'

# Feld als Liste
feld = ["",
        "1","2","3",
        "4","5","6",
        "7","8","9"]

# Feld ausgeben
def feld_ausgeben():
    print (feld[1] + "|" + feld[2] + "|" + feld[3] )
    print (feld[4] + "|" + feld[5] + "|" + feld[6] )
    print (feld[7] + "|" + feld[8] + "|" + feld[9] )
feld_ausgeben()


#Eingabe vom Spieler und Kontrolle des Spielzugs
def spieler_eingabe():
    global spiel_check
    while True:
        spielzug = input("Bitte Feld eingeben: oder exit eingeben für beenden")
        #Falls man das Spiel vorzeitig beenden möchte
        if spielzug == 'exit':
            spiel_check = False
            return
        try:
            spielzug = int(spielzug)
        except ValueError:
            print("Bitte Zahl von 1 bis 9 eingeben")
        else:
            if spielzug >= 1 and spielzug <= 9:
                #Spielereingabe Kontrolle Eingabe
                if feld[spielzug] == 'X' or feld[spielzug] == 'O':
                    print("Das Feld ist bereits belegt - ein anderes wählen!")
                else: 
                    return spielzug
            else:
                print("Zahl muss zwischen 1 und 9 liegen")
      
# Der jeweilige Wechsel der Spieler
def spieler_wechseln():
    global spieler
    if spieler == 'X':
        spieler = 'O'
    else:
        spieler = 'X'

# Kontrolle ob es einen Gewinner gibt
def kontrolle_gewonnen():
    # wenn alle 3 Felder gleich sind, hat der entsprechende Spieler gewonnen
    # Kontrolle auf Reihen
    if feld[1] == feld[2] == feld[3]:
        return feld[1]
    if feld[4] == feld[5] == feld[6]:
        return feld[4]
    if feld[7] == feld[8] == feld[9]:
        return feld[7]
    # Kontrolle auf Spalten
    if feld[1] == feld[4] == feld[7]:
        return feld[1]
    if feld[2] == feld[5] == feld[8]:
        return feld[2]
    if feld[3] == feld[6] == feld[9]:
        return feld[3]
    # Kontrolle auf Diagonalen
    if feld[1] == feld[5] == feld[9]:
        return feld[5]
    if feld[7] == feld[5] == feld[3]:
        return feld[5]        

# Kontrolle ob es zu einem Unentschieden kam
def kontrolle_auf_unentschieden():
    if (feld[1] == 'X' or feld[1] == 'O') \
      and (feld[2] == 'X' or feld[2] == 'O') \
      and (feld[3] == 'X' or feld[3] == 'O') \
      and (feld[4] == 'X' or feld[4] == 'O') \
      and (feld[5] == 'X' or feld[5] == 'O') \
      and (feld[6] == 'X' or feld[6] == 'O') \
      and (feld[7] == 'X' or feld[7] == 'O') \
      and (feld[8] == 'X' or feld[8] == 'O') \
      and (feld[9] == 'X' or feld[9] == 'O'):
        return ('unentschieden')

# aktuelles Spielfeld ausgeben
feld_ausgeben()

#While-Schleif zur überprüfung Spiel noch aktiv
while spiel_check:
    # Eingabe des Spielers
    print("Spieler " + spieler + " am Zug")
    
    # aus der Liste spielfeld alle X und O und leere Felder entfernen
    spielfeld_KI = []
    for moegliche_felder in feld:
        if moegliche_felder != 'X' and moegliche_felder != 'O' and moegliche_felder != ' ':
            spielfeld_KI += moegliche_felder
        
    # wenn Computergegner am Zug ist, ein freies zufälliges Feld belegen
    if spieler == 'O':
        spielzug = int(random.choice(spielfeld_KI))
    else:
        spielzug = spieler_eingabe()
    
    if spielzug:
        # spielfeld[spielzug] = 'X'
        feld[spielzug] = spieler
        # aktuelles Spielfeld ausgeben
        feld_ausgeben()
        # Kontrolle, ob jemand gewonnen hat
        gewonnen = kontrolle_gewonnen()
        if gewonnen:
            print ("Spieler " + gewonnen + " hat gewonnen!")
            spiel_check = False
            break
        # Kontrolle, ob unentschieden
        unentschieden = kontrolle_auf_unentschieden()
        if unentschieden:
            print ("Spiel ist unentschieden ausgegangen")
            spiel_check = False
        # Spieler wechseln
        spieler_wechseln()