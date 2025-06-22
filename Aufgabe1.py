import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("umsatz.csv")

umsatz_pro_abteilung = df.groupby("Abteilung")["Umsatz"].sum().sort_values(ascending=False)

top5 = umsatz_pro_abteilung.head(5)

top5.plot(kind="bar", title="Top 5 Abteilungen nach Umsatz", ylabel="Umsatz (€)", xlabel="Abteilung", color="skyblue")
plt.tight_layout()
plt.show()

top5.to_csv("auswertung.csv")
