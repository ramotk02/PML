import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("schritte.csv")

df["Datum"] = pd.to_datetime(df["Datum"])

lina_df = df[df["Name"] == "Lina"]

lina_df.plot(x="Datum", y="Schritte", kind="line", marker="o", title="Linas Schritte")
plt.tight_layout()
plt.show()

wochen_durchschnitt = lina_df["Schritte"].mean()
print(f"Wochendurchschnitt: {wochen_durchschnitt:.2f} Schritte")

aktiv = lina_df[lina_df["Schritte"] > 10000]
aktiv.to_csv("aktiv.csv", index=False)
