"""
generate_mock_data.py
---------------------
Gera um histórico fictício de vendas diárias para uma loja de moda
com 5 categorias de produto, cobrindo o período de 2022 a 2024.

Os dados simulam padrões realistas do setor:
- Picos em novembro/dezembro (Black Friday + Natal)
- Alta em maio (Dia das Mães)
- Alta em junho (Dia dos Namorados)
- Queda em fevereiro e agosto (meses historicamente fracos no varejo)
- Tendência de crescimento gradual ao longo dos 3 anos
- Ruído aleatório diário para simular variação natural

Saída: data/raw/vendas.csv
"""

import pandas as pd
import numpy as np
import os

# ── Configurações gerais ──────────────────────────────────────────────────────

SEED = 42  # garante que os dados gerados são sempre iguais ao rodar de novo
np.random.seed(SEED)

INICIO = "2022-01-01"
FIM    = "2024-12-31"

CATEGORIAS = {
    "Camisetas":    {"base": 120, "ticket_medio": 79.90},
    "Calças":       {"base": 80,  "ticket_medio": 159.90},
    "Vestidos":     {"base": 90,  "ticket_medio": 189.90},
    "Acessórios":   {"base": 150, "ticket_medio": 49.90},
    "Calçados":     {"base": 60,  "ticket_medio": 219.90},
}

OUTPUT_DIR  = "data/raw"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "vendas.csv")

# ── Funções auxiliares ────────────────────────────────────────────────────────

def sazonalidade_mensal(mes: int) -> float:
    """
    Retorna um multiplicador de sazonalidade para cada mês.
    Baseado em padrões reais do varejo de moda brasileiro.
    """
    multiplicadores = {
        1:  0.85,   # Janeiro  — pós-festas, queda
        2:  0.70,   # Fevereiro — mês mais fraco do ano
        3:  0.90,   # Março    — leve recuperação
        4:  0.95,   # Abril    — Páscoa ajuda um pouco
        5:  1.30,   # Maio     — Dia das Mães (pico)
        6:  1.15,   # Junho    — Dia dos Namorados
        7:  0.95,   # Julho    — férias escolares, movimento misto
        8:  0.80,   # Agosto   — mês fraco no varejo
        9:  0.95,   # Setembro — volta às aulas, leve alta
        10: 1.05,   # Outubro  — aquecimento para Black Friday
        11: 1.45,   # Novembro — Black Friday (maior pico)
        12: 1.50,   # Dezembro — Natal (maior pico junto com novembro)
    }
    return multiplicadores[mes]


def tendencia_anual(ano: int) -> float:
    """
    Crescimento gradual ao longo dos anos.
    Simula uma loja que está expandindo.
    """
    tendencias = {
        2022: 1.00,
        2023: 1.12,  # crescimento de 12% no segundo ano
        2024: 1.25,  # crescimento de 25% em relação ao ano base
    }
    return tendencias.get(ano, 1.0)


def gerar_vendas_categoria(datas: pd.DatetimeIndex, config: dict) -> np.ndarray:
    """
    Gera a série de vendas diárias para uma categoria.

    Combina:
    - Volume base de unidades vendidas por dia
    - Multiplicador de sazonalidade mensal
    - Multiplicador de tendência anual
    - Ruído aleatório (distribuição normal)
    - Picos pontuais em datas comemorativas
    """
    vendas = []

    for data in datas:
        base       = config["base"]
        sazonal    = sazonalidade_mensal(data.month)
        tendencia  = tendencia_anual(data.year)

        # Ruído diário: variação de ±20% em torno da média
        ruido = np.random.normal(loc=1.0, scale=0.20)
        ruido = max(ruido, 0.3)  # garante que nunca seja negativo ou perto de zero

        # Picos pontuais — dias específicos com volume muito maior
        pico = 1.0
        if data.month == 11 and data.day >= 24:  # semana da Black Friday
            pico = 2.8
        elif data.month == 12 and 20 <= data.day <= 24:  # véspera de Natal
            pico = 2.2
        elif data.month == 5 and 8 <= data.day <= 12:   # semana do Dia das Mães
            pico = 1.8
        elif data.month == 6 and 10 <= data.day <= 12:  # Dia dos Namorados
            pico = 1.5

        # Final de semana tem ~30% mais vendas online
        if data.weekday() >= 5:
            pico *= 1.30

        unidades = base * sazonal * tendencia * ruido * pico
        unidades = max(int(round(unidades)), 1)  # mínimo de 1 venda por dia

        receita = round(unidades * config["ticket_medio"], 2)
        vendas.append({"unidades": unidades, "receita": receita})

    return vendas


# ── Geração do dataset ────────────────────────────────────────────────────────

def gerar_dataset() -> pd.DataFrame:
    """
    Monta o DataFrame completo com todas as categorias e datas.
    """
    datas = pd.date_range(start=INICIO, end=FIM, freq="D")
    registros = []

    for categoria, config in CATEGORIAS.items():
        print(f"  Gerando dados: {categoria}...")
        vendas = gerar_vendas_categoria(datas, config)

        for data, venda in zip(datas, vendas):
            registros.append({
                "data":       data.strftime("%Y-%m-%d"),
                "categoria":  categoria,
                "unidades":   venda["unidades"],
                "receita":    venda["receita"],
                # colunas no formato Prophet para uso direto no modelo
                "ds":         data.strftime("%Y-%m-%d"),
                "y":          venda["receita"],
            })

    df = pd.DataFrame(registros)
    df["data"] = pd.to_datetime(df["data"])
    df["ds"]   = pd.to_datetime(df["ds"])

    return df


def salvar_dataset(df: pd.DataFrame) -> None:
    """
    Salva o CSV na pasta correta e exibe um resumo do que foi gerado.
    """
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    df.to_csv(OUTPUT_FILE, index=False)

    print(f"\n✓ Arquivo salvo em: {OUTPUT_FILE}")
    print(f"  Total de registros : {len(df):,}")
    print(f"  Período            : {df['data'].min().date()} → {df['data'].max().date()}")
    print(f"  Categorias         : {df['categoria'].nunique()}")
    print(f"  Receita total      : R$ {df['receita'].sum():,.2f}")
    print(f"\nResumo por categoria:")
    print(
        df.groupby("categoria")
          .agg(
              total_unidades=("unidades", "sum"),
              receita_total=("receita", "sum"),
              media_diaria=("receita", "mean"),
          )
          .round(2)
          .to_string()
    )


# ── Execução ──────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("Gerando dados mockados — Loja de Moda (2022–2024)\n")
    df = gerar_dataset()
    salvar_dataset(df)
    print("\nPronto! Execute o notebook para a análise exploratória.")
