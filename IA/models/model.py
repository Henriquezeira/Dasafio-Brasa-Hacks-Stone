import pandas as pd
from sklearn.linear_model import LinearRegression

def train_model(predial_df, impostos_df, produtos_df, funcionarios_df, prolabore_df):
    # Combine os DataFrames conforme necessário
    combined_df = pd.concat([predial_df, impostos_df, produtos_df, funcionarios_df, prolabore_df], axis=1)

    # Exemplo de como selecionar características e rótulo (ajuste conforme necessário)
    X = combined_df[['feature1', 'feature2']]  # Substitua 'feature1', 'feature2' pelos nomes reais das colunas
    y = combined_df['target']  # Substitua 'target' pelo nome da coluna que você deseja prever

    # Treine o modelo
    model = LinearRegression()
    model.fit(X, y)

    return model
