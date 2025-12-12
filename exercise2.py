"""
Ejercicio 2 - Applied Statistics Project
Chi-square: Type of Accident × Type of Road
Using official microdata from DGT (Accidentes 2024).
"""

import pandas as pd
from scipy.stats import chi2_contingency


def main():

    # 1. Load Excel file
    file_path = "TABLA_ACCIDENTES_24.XLSX" 
    df = pd.read_excel(file_path)

    # 2. Select relevant columns
    col_via = "TIPO_VIA"
    col_acc = "TIPO_ACCIDENTE"

    sub = df[[col_via, col_acc]].copy()

    # 3. Map road types into Urban / Interurban
    map_via = {
        1: "Interurban",
        2: "Interurban",
        3: "Interurban",
        4: "Interurban",
        5: "Interurban",
        6: "Interurban",
        7: "Interurban",
        8: "Interurban",
        9: "Urban",
        10: "Urban",
        11: "Urban",
        12: "Urban",
        13: "Urban",
        14: "Interurban"  # "Otro" → lo clasifico neutralmente como interurbana
    }

    # 4. Map accident types (choose 3 categories)
    map_acc = {
        3: "Lateral",
        4: "Rear-end",
        11: "Run-off-road",
        # Puedes añadir más si quieres
    }

    # Convert to numeric just in case
    sub[col_via] = pd.to_numeric(sub[col_via], errors="coerce")
    sub[col_acc] = pd.to_numeric(sub[col_acc], errors="coerce")

    sub["road_type"] = sub[col_via].map(map_via)
    sub["accident_type"] = sub[col_acc].map(map_acc)

    # Keep only mapped values
    sub = sub.dropna(subset=["road_type", "accident_type"])

    # 5. Contingency table
    table = pd.crosstab(sub["accident_type"], sub["road_type"])
    print("\nContingency Table:")
    print(table)

    # 6. Chi-square test
    chi2, p, dof, expected = chi2_contingency(table)

    print("\nChi-square test results:")
    print(f"Chi2: {chi2:.3f}")
    print(f"Degrees of freedom: {dof}")
    print(f"p-value: {p:.6f}")

    print("\nExpected frequencies under independence:")
    print(pd.DataFrame(expected, index=table.index, columns=table.columns))

    # 7. Interpretation
    print("\nInterpretation:")
    if p < 0.05:
        print("There is a statistically significant association between type of accident and type of road.")
    else:
        print("No significant association was found between type of accident and type of road.")


if __name__ == "__main__":
    main()