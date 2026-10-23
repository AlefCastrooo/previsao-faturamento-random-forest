import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

rng = np.random.default_rng(42)

datas = pd.date_range(
    start="2025-01-01",
    periods=365,
    freq="D"
)

df = pd.DataFrame({"data": datas})

df["dia_semana"] = df["data"].dt.dayofweek
df["mes"] = df["data"].dt.month

df["promocao"] = rng.integers(0, 2, len(df))

df["clientes"] = (
    40
    + df["promocao"] * 15
    + (df["dia_semana"] >= 5) * 10
    + rng.integers(-10, 11, len(df))
)

df["faturamento"] = (
    df["clientes"] * 55
    + df["promocao"] * 250
    + rng.normal(0, 200, len(df))
).round(2)

print("\n=== BASE DE DADOS ===")
print(df.head())

print("\nDimensões:", df.shape)
print("\nValores nulos:")
print(df.isnull().sum())

X = df[
    ["clientes", "promocao", "dia_semana", "mes"]
]

y = df["faturamento"]


divisao = int(len(df) * 0.8)

X_treino = X.iloc[:divisao]
X_teste = X.iloc[divisao:]

y_treino = y.iloc[:divisao]
y_teste = y.iloc[divisao:]

print("\n=== DIVISÃO DOS DADOS ===")
print("Registros de treinamento:", len(X_treino))
print("Registros de teste:", len(X_teste))



modelo = RandomForestRegressor(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

modelo.fit(X_treino, y_treino)

print("\nModelo treinado com sucesso!")


previsoes = modelo.predict(X_teste)

resultado = pd.DataFrame({
    "Data": df["data"].iloc[divisao:].values,
    "Real": y_teste.values,
    "Previsto": previsoes

resultado["Erro_Absoluto"] = abs(
    resultado["Real"] - resultado["Previsto"]
)

print("\n=== PREVISÕES ===")
print(resultado.head(10).round(2))


mae = mean_absolute_error(y_teste, previsoes)
r2 = r2_score(y_teste, previsoes)

print("\n=== DESEMPENHO DO MODELO ===")
print(f"MAE: R$ {mae:.2f}")
print(f"R²: {r2:.4f}")


plt.figure(figsize=(12, 5))

plt.plot(
    resultado["Data"],
    resultado["Real"],
    label="Faturamento real"
)

plt.plot(
    resultado["Data"],
    resultado["Previsto"],
    label="Faturamento previsto"
)

plt.title("Previsão de Vendas - Random Forest")
plt.xlabel("Data")
plt.ylabel("Faturamento (R$)")
plt.legend()
plt.grid(alpha=0.3)
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()


importancia = pd.DataFrame({
    "Variavel": X.columns,
    "Importancia": modelo.feature_importances_
})

importancia = importancia.sort_values(
    by="Importancia",
    ascending=False
)

print("\n=== IMPORTÂNCIA DAS VARIÁVEIS ===")
print(importancia)

plt.figure(figsize=(9, 5))

plt.barh(
    importancia["Variavel"],
    importancia["Importancia"]
)

plt.title("Importância das Variáveis - Random Forest")
plt.xlabel("Importância")
plt.gca().invert_yaxis()
plt.tight_layout()

plt.show()


resultado.to_csv(
    "previsoes_vendas.csv",
    index=False,
    encoding="utf-8-sig"
)

print("\nArquivo previsoes_vendas.csv gerado!")
print("\nProjeto finalizado!")
