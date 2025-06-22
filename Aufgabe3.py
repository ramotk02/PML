
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("ernaehrung.csv")

proteinreiche_gerichte = df[df["Protein"] > 20]

kalorienarm = proteinreiche_gerichte.sort_values("Kalorien").head(3)
print("Drei kalorienärmste proteinreiche Gerichte:")
print(kalorienarm)

proteinreiche_gerichte.set_index("Gericht")["Protein"].plot(kind="pie", autopct="%1.1f%%", title="Proteinanteil pro Gericht")
plt.ylabel("")
plt.tight_layout()
plt.show()
