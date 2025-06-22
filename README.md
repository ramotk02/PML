# 📁 Python-Projekt – CSV-Daten auswerten & Diagramme erstellen

Dieses Projekt zeigt, wie man mit Python CSV-Dateien liest, Daten mit **pandas** analysiert und mit **matplotlib** anschauliche Diagramme erstellt.

---

## 📌 Das Projekt enthält 3 Aufgaben:

---

## 🔶 Aufgabe 1 – Umsatzanalyse

### ➤ Was ist das?

Ein Skript, das die Umsätze verschiedener Abteilungen aus einer CSV-Datei einliest und analysiert.

### ➤ Was macht es genau?

1. Liest die Datei `umsatz.csv`.
2. Summiert die Umsätze je Abteilung.
3. Sortiert die Abteilungen nach Umsatz (von hoch nach niedrig).
4. Zeigt die Top 5 Abteilungen in einem **Balkendiagramm** an.
5. (Optional) Speichert die Ergebnisse in `auswertung.csv`.

### ➤ Warum ist das nützlich?

So sieht man auf einen Blick, welche Abteilungen am meisten Umsatz machen.

---

## 🟦 Aufgabe 2 – Schritte zählen (Fitness)

### ➤ Was ist das?

Ein Skript, das die täglichen Schrittzahlen einer Person namens **Lina** analysiert.

### ➤ Was macht es?

1. Liest die Datei `schritte.csv`.
2. Filtert alle Daten nur für Lina.
3. Wandelt die Datumswerte in ein richtiges Datumsformat um.
4. Berechnet den Durchschnitt der Schritte pro Woche.
5. Zeichnet ein **Liniendiagramm** mit den täglichen Schritten.
6. (Optional) Speichert die Tage mit mehr als 10.000 Schritten in `aktiv.csv`.

### ➤ Warum ist das nützlich?

Man kann sehen, wie aktiv Lina über die Zeit war und an welchen Tagen sie besonders viel gegangen ist.

---

## 🟩 Aufgabe 3 – Ernährungsauswertung

### ➤ Was ist das?

Ein Skript, das Gerichte nach ihrem Proteingehalt und Kalorien analysiert.

### ➤ Was macht es?

1. Liest die Datei `ernaehrung.csv`.
2. Filtert alle Gerichte mit mehr als 20g Protein.
3. Zeigt die 3 kalorienärmsten Gerichte an.
4. Erstellt ein **Kreisdiagramm (Pie Chart)**, das den Proteingehalt der gefilterten Gerichte zeigt.

### ➤ Warum ist das nützlich?

So erkennt man, welche Gerichte besonders proteinreich und welche besonders kalorienarm sind – wichtig z.B. beim Sport oder gesunder Ernährung.

---

## ⚙️ Installation

Installiere vor dem Ausführen die benötigten Bibliotheken:

```bash
pip install pandas matplotlib
