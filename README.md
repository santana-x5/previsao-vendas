# 📈 Sistema de Previsão de Vendas

> Aplicação de previsão de séries temporais de vendas com Prophet, FastAPI e Streamlit.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Prophet](https://img.shields.io/badge/Prophet-1.1-orange)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110-green)
![Streamlit](https://img.shields.io/badge/Streamlit-1.33-red)
![Docker](https://img.shields.io/badge/Docker-Compose-blue)
![Status](https://img.shields.io/badge/Status-Em%20desenvolvimento-yellow)

---

## 📌 Sobre o projeto

Este sistema analisa o histórico de vendas de uma empresa fictícia, identifica tendências e sazonalidades, e gera projeções futuras com intervalos de confiança. O resultado é apresentado em um dashboard interativo com gráficos, KPIs e exportação de dados.

Projeto desenvolvido como **portfólio técnico**, com arquitetura desenhada para permitir evolução para um produto SaaS.

---

## 🖥️ Preview

[visualização do DASHBOARD — indisponível por enquanto]

```
Insirir aqui: screenshot do dashboard Streamlit rodando
assets/dashboard_preview.png
![Dashboard Preview](assets/dashboard_preview.png)
```

---

## 🧱 Arquitetura

```


dados_mockados.csv
       │
       ▼
  Pandas (ETL)
       │
       ▼
   SQLite DB
       │
       ▼
  Prophet (modelo)
       │
    ┌──┴──┐
    │     │
FastAPI  Jupyter
(API)  (notebook)
    │
    ▼
Streamlit (dashboard)
    │
    ▼
 Plotly (gráficos)
```

---

## 🗂️ Estrutura do repositório

```


sales-forecast/
├── data/
│   ├── raw/                  # CSV gerado com dados mockados
│   └── processed/            # Dados limpos prontos para o modelo
├── notebooks/
│   └── exploratory.ipynb     # EDA + treinamento do modelo Prophet
├── api/
│   ├── main.py               # FastAPI — endpoints /predict e /retrain
│   ├── model.pkl             # Modelo serializado com joblib
│   └── requirements.txt
├── dashboard/
│   ├── app.py                # Interface Streamlit
│   └── requirements.txt
├── docker-compose.yml
├── .env.example
├── assets/
│   └── dashboard_preview.png
└── README.md
```

---

## ⚙️ Tecnologias utilizadas

| Tecnologia | Versão | Função |
|---|---|---|
| Python | 3.11 | Linguagem base |
| Pandas | [?] | Geração e limpeza dos dados |
| Prophet | [?] | Modelo de previsão de séries temporais |
| Plotly | [?] | Visualização interativa |
| FastAPI | [?] | API REST para servir o modelo |
| Streamlit | [?] | Dashboard e interface do usuário |
| SQLite | — | Armazenamento local dos dados |
| Joblib | [?] | Serialização do modelo treinado |
| Docker Compose | [?] | Orquestração dos serviços |

---

## 🚀 Como rodar o projeto

### Pré-requisitos

- Docker e Docker Compose instalados
- Git

### Passo a passo

```bash
# 1. Clone o repositório
git clone https://github.com/santana-x5/previsao-vendas.git
cd previsao-vendas

# 2. Copie o arquivo de variáveis de ambiente
cp .env.example .env

# 3. Suba os serviços
docker-compose up --build
```

Após subir, acesse:

| Serviço | URL |
|---|---|
| Dashboard | http://localhost:[PORTA_STREAMLIT] |
| API (Swagger) | http://localhost:[PORTA_FASTAPI]/docs |

---

## 📊 Como os dados foram gerados

Os dados utilizados neste projeto são **inteiramente fictícios**, gerados via script Python com as seguintes características:

- **Período:**  Janeiro/2022 a janeiro/2025
- **Frequência:** Diária
- **Categorias simuladas:**  Vestuário
- **Sazonalidade embutida:** Picos em Jan/Dez/jun/Jul, baixas em meses de verão
- **Ruído:** Distribuição normal com desvio padrão de [PREENCHA]

Para gerar os dados novamente:

```bash
python data/generate_mock_data.py
```

---

## 🔌 Endpoints da API

### `POST /predict`

Retorna a previsão de vendas para o horizonte informado.

**Body:**
```json
{
  "horizon_days": 90,
  "category": "casacos"
}
```

**Response:**
```json
{
  "forecast": [
    {
      "ds": "2025-01-01",
      "yhat": 1523.40,
      "yhat_lower": 1201.10,
      "yhat_upper": 1845.70
    }
  ]
}
```

### `POST /retrain`

[DESCREVA O COMPORTAMENTO — ex: "Re-treina o modelo com os dados mais recentes do banco e salva o novo modelo serializado."]

---

## 📓 Notebook

O notebook `notebooks/exploratory.ipynb` documenta:

1. Análise exploratória dos dados (EDA)
2. Decomposição de tendência e sazonalidade
3. Treinamento do modelo Prophet com configurações de feriados BR
4. Avaliação com métricas MAE e MAPE
5. Geração do gráfico final de projeção

[ADICIONAR O LINK DO NOTEBOOK RENDERIZADO NO NBVIEWER  — : https://nbviewer.org/github/...]

---

## 📈 Resultados

[PREENCHER APÓS CONCLUIR O MODELO]

| Métrica | Valor |
|---|---|
| MAE | [PREENCHA] |
| MAPE | [PREENCHA] |
| Horizonte testado | [PREENCHA — ex: 90 dias] |
| Período de teste | [PREENCHA] |

---

## 🗺️ Roadmap

- [ ] Geração de dados mockados
- [ ] Pipeline de limpeza com Pandas
- [ ] Modelo Prophet treinado e avaliado
- [ ] API FastAPI com endpoint /predict
- [ ] Dashboard Streamlit
- [ ] Docker Compose
- [ ] Migração para PostgreSQL + TimescaleDB
- [ ] n8n para automação de pipeline
- [ ] Integração com IA generativa para narrativa das previsões
- [ ] Autenticação e multi-tenant (fase SaaS)

---

## 🤝 Contribuindo

Pull requests são bem-vindos. Para mudanças maiores, abra uma issue primeiro descrevendo o que deseja alterar.

---

## 📄 Licença

[ESCOLHA E PREENCHA — sugestões: MIT para portfólio aberto, ou remova se preferir sem licença explícita]

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---

## 👤 Autor

**[Klinger F. X. Santana]**

- GitHub: [@santana-x5](https://github.com/santana-x5)
- LinkedIn: [linkedin.com/in/klinger-santana](https://linkedin.com/in/klinger-santana-8357723a8)

---

*Projeto desenvolvido como portfólio técnico em [04/2026].*
