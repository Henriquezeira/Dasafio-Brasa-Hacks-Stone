import pandas as pd

def load_data():
    # Caminho para o arquivo carregado
    excel_path = r'C:\Users\chhen\OneDrive\Documentos\Desafio-Brasa-hacks-Stone\IA\app\data\dados_stone.xlsx'
    
    # Leia todas as planilhas do arquivo
    all_sheets = pd.read_excel(excel_path, sheet_name=None)

    # Extraia cada planilha em um DataFrame separado
    predial_df = all_sheets.get('Predial')
    impostos_df = all_sheets.get('Impostos')
    produtos_df = all_sheets.get('Produtos')
    funcionarios_df = all_sheets.get('Funcionarios')
    prolabore_df = all_sheets.get('Prolabore')

    return predial_df, impostos_df, produtos_df, funcionarios_df, prolabore_df

# Carregar os dados
predial_df, impostos_df, produtos_df, funcionarios_df, prolabore_df = load_data()

# Exemplo de como você pode usar os dados carregados
def process_request(request_type):
    if request_type == 'predial':
        return predial_df
    elif request_type == 'impostos':
        return impostos_df
    elif request_type == 'produtos':
        return produtos_df
    elif request_type == 'funcionarios':
        return funcionarios_df
    elif request_type == 'prolabore':
        return prolabore_df
    else:
        return "Tipo de solicitação desconhecido."

# Exemplo de uso: Solicitar dados de uma planilha específica
request_type = 'produtos'  # Exemplo de solicitação
result = process_request(request_type)

# Exibir o resultado
print(result)
