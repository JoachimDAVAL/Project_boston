# analysis.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from etl.models.user import analyse  # importe la fonction analyse depuis user.py

# ---------------------------------------------------
# Exemple de données pour tester (remplace par ton df réel si tu l'as)
# ---------------------------------------------------
data_example = {
    "department": ["Finance", "Finance", "IT", "IT", "HR", "HR"],
    "total_earnings": [50000, 60000, 70000, 65000, 40000, 45000]
}

df_clean = pd.DataFrame(data_example)

# ---------------------------------------------------
# Lancer l'analyse statistique
# ---------------------------------------------------
stats_par_dept = analyse(df_clean)

# Affichage des résultats
print("Statistiques des salaires par département :")
print(stats_par_dept)

# ---------------------------------------------------
# Visualisation simple (boxplot)
# ---------------------------------------------------
plt.figure(figsize=(8,5))
sns.boxplot(x='department', y='total_earnings', data=df_clean)
plt.xticks(rotation=45)
plt.title("Écarts de salaires par département - Boston")
plt.show()

# ---------------------------------------------------
# Fin du script
# ---------------------------------------------------