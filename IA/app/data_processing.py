import pandas as pd

def load_data():
    # Caminhos para os arquivos .parquet
    bank_path = 'data/hackathon_stone_brasa_banking_data'
    sales_path = 'data/hackathon_stone_brasa_sales_data'
    mcc_path = 'data/mcc.parquet'
    
    # Carregar os dados
    bank_df = pd.read_parquet(bank_path)
    sales_df = pd.read_parquet(sales_path)
    mcc_df = pd.read_parquet(mcc_path)
    
    return bank_df, sales_df, mcc_df

def preprocess_data(bank_df, sales_df):
    # Exemplo de pré-processamento
    bank_df = bank_df.dropna()
    sales_df = sales_df.dropna()
    
    # Adicione mais etapas de pré-processamento conforme necessário
    
    return bank_df, sales_df

