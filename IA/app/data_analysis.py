# App/data_analysis.py

def analyze_data(data):
    df_bank = data['bank']
    df_sales = data['sales']

    # Exemplo de análise: calcular média de transações e dar uma dica
    summary_bank = df_bank.groupby('document_id')['value'].agg(['max', 'mean'])
    summary_sales = df_sales.groupby('document_id')['value'].agg(['max', 'mean'])

    # Dicas com base na análise
    tips = []
    if summary_sales['mean'].mean() < 500:
        tips.append("Considere aumentar as vendas com promoções.")
    
    return summary_bank, summary_sales, tips
