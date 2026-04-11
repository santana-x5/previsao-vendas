# 📈 Sistema de Previsão de Vendas

> [DESCRIÇÃO CURTA — ex: "Aplicação de previsão de séries temporais de vendas com Prophet, FastAPI e Streamlit."]

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Prophet](https://img.shields.io/badge/Prophet-1.1-orange)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110-green)
![Streamlit](https://img.shields.io/badge/Streamlit-1.33-red)
![Docker](https://img.shields.io/badge/Docker-Compose-blue)
![Status](https://img.shields.io/badge/Status-Em%20desenvolvimento-yellow)

---

## 📌 Sobre o projeto

[PARÁGRAFO DESCRITIVO — descreva o que o sistema faz, qual problema resolve e qual o contexto de uso. Ex: "Este sistema analisa o histórico de vendas de uma empresa fictícia, identifica tendências e sazonalidades, e gera projeções futuras com intervalos de confiança. O resultado é apresentado em um dashboard interativo com gráficos, KPIs e exportação de dados."]

Projeto desenvolvido como **portfólio técnico**, com arquitetura desenhada para evoluir para um produto SaaS.

---

## 🖥️ Preview

[PRINT OU GIF DO DASHBOARD — substitua pela imagem após concluir a interface]

```
Insira aqui: screenshot do dashboard Streamlit rodando
Sugestão de nome do arquivo: assets/dashboard_preview.png
Markdown para inserir: ![Dashboard Preview](assets/dashboard_preview.png)
```

---

## 🧱 Arquitetura

```
[DIAGRAMA OPCIONAL — pode ser uma imagem ou o texto abaixo adaptado]

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
[PREENCHA CONFORME A ESTRUTURA FINAL DO PROJETO]

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
| Pandas | [PREENCHA] | Geração e limpeza dos dados |
| Prophet | [PREENCHA] | Modelo de previsão de séries temporais |
| Plotly | [PREENCHA] | Visualização interativa |
| FastAPI | [PREENCHA] | API REST para servir o modelo |
| Streamlit | [PREENCHA] | Dashboard e interface do usuário |
| SQLite | — | Armazenamento local dos dados |
| Joblib | [PREENCHA] | Serialização do modelo treinado |
| Docker Compose | [PREENCHA] | Orquestração dos serviços |

---

## 🚀 Como rodar o projeto

### Pré-requisitos

- Docker e Docker Compose instalados
- Git

### Passo a passo

```bash
# 1. Clone o repositório
git clone https://github.com/[SEU_USUARIO]/[NOME_DO_REPOSITORIO].git
cd [NOME_DO_REPOSITORIO]

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

- **Período:** [PREENCHA — ex: Janeiro/2022 a Dezembro/2024]
- **Frequência:** Diária
- **Categorias simuladas:** [PREENCHA — ex: Eletrônicos, Vestuário, Alimentos]
- **Sazonalidade embutida:** Picos em dezembro/janeiro, queda em [PREENCHA]
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
  "category": "[PREENCHA — ex: 'Eletrônicos' ou 'all']"
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

[ADICIONE O LINK DO NOTEBOOK RENDERIZADO NO NBVIEWER SE QUISER — ex: https://nbviewer.org/github/...]

---

## 📈 Resultados

[PREENCHA APÓS CONCLUIR O MODELO]

| Métrica | Valor |
|---|---|
| MAE | [PREENCHA] |
| MAPE | [PREENCHA] |
| Horizonte testado | [PREENCHA — ex: 90 dias] |
| Período de teste | [PREENCHA] |

---

## 🗺️ Roadmap

- [x] Geração de dados mockados
- [x] Pipeline de limpeza com Pandas
- [x] Modelo Prophet treinado e avaliado
- [x] API FastAPI com endpoint /predict
- [x] Dashboard Streamlit
- [x] Docker Compose
- [ ] Migração para PostgreSQL + TimescaleDB
- [ ] n8n para automação de pipeline
- [ ] Integração com IA generativa para narrativa das previsões
- [ ] Autenticação e multi-tenant (fase SaaS)

---

## 🤝 Contribuindo

[PREENCHA SE QUISER ACEITAR CONTRIBUIÇÕES — caso contrário, remova esta seção]

Pull requests são bem-vindos. Para mudanças maiores, abra uma issue primeiro descrevendo o que deseja alterar.

---

## 📄 Licença

[ESCOLHA E PREENCHA — sugestões: MIT para portfólio aberto, ou remova se preferir sem licença explícita]

Este projeto está sob a licença [NOME DA LICENÇA]. Veja o arquivo `LICENSE` para mais detalhes.

---

## 👤 Autor

**[SEU NOME]**

- GitHub: [@[SEU_USUARIO]](https://github.com/[SEU_USUARIO])
- LinkedIn: [linkedin.com/in/[SEU_PERFIL]](https://linkedin.com/in/[SEU_PERFIL])
- [OUTRO CONTATO OPCIONAL — portfólio, e-mail, etc.]

---

*Projeto desenvolvido como portfólio técnico em [MÊS/ANO DE INÍCIO].*
