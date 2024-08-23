from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

def train_model(bank_df):
    # Suponha que você esteja prevendo uma coluna específica
    X = bank_df[['feature1', 'feature2']]  # Características
    y = bank_df['target']  # Alvo
    
    # Dividir dados em treino e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Definir o modelo
    model = LinearRegression()
    
    # Treinar o modelo
    model.fit(X_train, y_train)
    
    # Avaliar o modelo
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    
    print(f"Mean Squared Error: {mse}")
    
    return model
