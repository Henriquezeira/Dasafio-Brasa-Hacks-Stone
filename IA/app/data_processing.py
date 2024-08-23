import pandas as pd

def load_data():
    # Substitua 'caminho/para/dados_stone.xlsx' pelo caminho real do seu arquivo
    excel_path = 'caminho/para/dados_stone.xlsx'
    # Leia todas as planilhas do arquivo
    all_sheets = pd.read_excel(excel_path, sheet_name=None)

    # Extraia cada planilha em um DataFrame separado
    predial_df = all_sheets.get('Predial')
    impostos_df = all_sheets.get('Impostos')
    produtos_df = all_sheets.get('Produtos')
    funcionarios_df = all_sheets.get('Funcionarios')
    prolabore_df = all_sheets.get('Prolabore')

    return predial_df, impostos_df, produtos_df, funcionarios_df, prolabore_df
