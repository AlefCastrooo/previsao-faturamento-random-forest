# Previsão de Faturamento com Machine Learning 

## Sobre o projeto

Este projeto surgiu de uma ideia que venho explorando: utilizar Machine Learning para ajudar empresas a compreender seus dados comerciais e, futuramente, antecipar resultados de faturamento.

Como primeiro passo, desenvolvi um modelo de regressão utilizando **Python e Random Forest Regressor**, com uma base de vendas simulada.

O objetivo inicial é compreender o funcionamento do algoritmo, desde a preparação dos dados até a avaliação das estimativas, criando uma base para futuras aplicações com dados reais.

## Tecnologias utilizadas

- **Python:** desenvolvimento do projeto
- **Pandas:** manipulação e organização dos dados
- **NumPy:** geração dos dados simulados
- **Scikit-learn:** treinamento e avaliação do modelo
- **Matplotlib:** visualização dos resultados

## Metodologia

O projeto foi desenvolvido em cinco etapas:

1. Geração de uma base simulada com 365 dias de vendas.
2. Preparação das variáveis comerciais e de calendário.
3. Separação cronológica dos dados em treinamento (80%) e teste (20%).
4. Treinamento do algoritmo Random Forest Regressor.
5. Avaliação das estimativas utilizando MAE e R².

## Resultados

O modelo foi treinado utilizando uma base simulada de 365 dias de vendas, com divisão cronológica de 80% para treinamento e 20% para teste.

**Métricas obtidas:**

- MAE (Erro Absoluto Médio): R$ 182,12
- R² (Coeficiente de Determinação): 0,8883

O modelo conseguiu explicar aproximadamente 88,83% da variação do faturamento no conjunto de teste.

A análise de importância das variáveis demonstrou que a quantidade de clientes foi o principal fator utilizado pelo algoritmo.

**Limitações:** os resultados foram obtidos com dados simulados e utilizando informações do próprio dia. Portanto, representam a capacidade de estimativa do modelo nesse cenário, não uma validação de previsão antecipada de faturamento.

O próximo objetivo é evoluir o projeto para realizar previsões futuras com informações disponíveis antes do período previsto.

As métricas de desempenho são calculadas durante a execução do código.

## Limitações e melhorias futuras

Esta primeira versão utiliza dados simulados e considera a quantidade de clientes do próprio dia para estimar o faturamento.

Por isso, ainda não representa uma solução capaz de prever antecipadamente o faturamento futuro de uma empresa.

As próximas evoluções previstas incluem:

- Utilização de históricos reais de vendas.
- Criação de variáveis baseadas em vendas anteriores.
- Desenvolvimento de previsões para períodos futuros.
- Comparação com modelos de referência.
- Avaliação da aplicação em diferentes negócios.

## Objetivo futuro

Evoluir o projeto para desenvolver soluções que apoiem empresas no planejamento comercial e na tomada de decisões orientadas por dados.

Este repositório representa a primeira etapa desse desenvolvimento.
