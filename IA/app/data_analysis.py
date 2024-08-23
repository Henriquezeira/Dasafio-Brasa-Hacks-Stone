def analyze_data(data):
    # Extraindo os DataFrames dos dados
    df_bank = data.get('bank')
    df_sales = data.get('sales')

    # Verificar se os DataFrames foram corretamente extraídos
    if df_bank is None or df_sales is None:
        raise ValueError("Os dados 'bank' ou 'sales' não foram encontrados.")

    # Verificar se as colunas esperadas estão presentes
    if 'document_id' not in df_bank.columns or 'value' not in df_bank.columns:
        raise ValueError("O DataFrame 'bank' não contém as colunas esperadas.")

    if 'document_id' not in df_sales.columns or 'value' not in df_sales.columns:
        raise ValueError("O DataFrame 'sales' não contém as colunas esperadas.")

    # Exemplo de análise: calcular máxima e média de transações por documento
    summary_bank = df_bank.groupby('document_id')['value'].agg(['max', 'mean'])
    summary_sales = df_sales.groupby('document_id')['value'].agg(['max', 'mean'])

    # Dicas com base na análise
    tips = []
    if summary_sales['mean'].mean() < 500:
        tips.append("Considere aumentar as vendas com promoções.")
    
    return summary_bank, summary_sales, tips
