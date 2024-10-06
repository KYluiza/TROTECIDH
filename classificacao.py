import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import GridSearchCV
from matplotlib import use

# Configurar o matplotlib para usar um backend que não precise de interface gráfica
use('Agg')

# Passo 1: Abrir o arquivo CSV
df = pd.read_csv('NOTÍCIAS - MANCHETES.csv')

# Adicionar a coluna de classificação com base nas regras definidas anteriormente
def categorize_headline_updated(manchete):
    positive_keywords = ['sucesso', 'aprovação', 'conquista', 'crescimento', 'vitória',  'melhora', 'ganho', 'avanço', 'lei proíbe', "proíbe", "proibid"]
    negative_keywords = ["nega", 'absurdo', 'agredid', 'racismo', "racista", 'denúncia', 'fracasso', 'queda', 'erro', 'morte', 'tóxico', 'expulso', 'crime', 'perda', 'violência', "estupro", "errado", "morre", "abandon"]
    
    manchete_lower = manchete.lower()  # Converter a manchete para minúsculas

    if any(word in manchete_lower for word in positive_keywords):
        return 'Positiva'
    elif any(word in manchete_lower for word in negative_keywords):
        return 'Negativa'
    else:
        return 'Neutra'

df['Classificação'] = df['Manchete'].apply(categorize_headline_updated)

# Verificar os nomes das colunas
print(df.columns)

# Assumindo que a coluna de classificação agora é 'Classificação'
manchetes = df['Manchete']
classificacao = df['Classificação']  # Coluna já criada acima

# Função para padronizar palavras (normalização simples)
def normalize_text(text):
    text = text.replace('trotes', 'trote')
    text = text.replace('universidades', 'universidade')
    text = text.replace('universitários', 'universitário')
    return text

# Aplicar a função de normalização a todas as manchetes
manchetes_normalizadas = manchetes.apply(normalize_text)

# Passo 2: Criar a lista de palavras a serem removidas (stop words)
stop_words = ["a", "e", "i", "o", "u", "de", "da", "di", "do", "em", "na", "no", "com", "que", "por", "para", "são", "após", "diz", "durante", "como", "dos", "sobre", "não", "os", "tem", "ser", "mais", "se", "bem"]

# Passo 3: Criar o vetorizador para contar a frequência de palavras, incluindo Unigramas e Bigramas
vectorizer = CountVectorizer(stop_words=stop_words, ngram_range=(1, 2))

# Ajustar e transformar o texto normalizado para uma matriz de contagem de Unigramas e Bigramas
X = vectorizer.fit_transform(manchetes_normalizadas)

# Passo 4: Divisão dos dados em treino e teste (70% treino, 30% teste)
X_train, X_test, y_train, y_test = train_test_split(X, classificacao, test_size=0.3, random_state=42)

# Definir uma função para treinar, avaliar diferentes classificadores e realizar Cross-Validation
def train_and_evaluate_model(model, model_name, param_grid=None):
    if param_grid:
        grid_search = GridSearchCV(model, param_grid, cv=5)
        grid_search.fit(X_train, y_train)
        best_model = grid_search.best_estimator_
        print(f"Melhores hiperparâmetros para {model_name}: {grid_search.best_params_}")
    else:
        best_model = model
        best_model.fit(X_train, y_train)
    
    # Previsão no conjunto de teste
    y_pred = best_model.predict(X_test)
    
    # Avaliação com cross-validation
    scores = cross_val_score(best_model, X_train, y_train, cv=5)
    print(f"\nResultados para: {model_name}")
    print(f"Acurácia (Validação Cruzada): {scores.mean():.4f}")
    print("Acurácia no Teste:", accuracy_score(y_test, y_pred))
    print("Relatório de Classificação:\n", classification_report(y_test, y_pred))

# Passo 5: Testar diferentes classificadores com tuning de hiperparâmetros

# 1. Naive Bayes (sem ajuste de hiperparâmetros)
nb_model = MultinomialNB()
train_and_evaluate_model(nb_model, "Naive Bayes")

# 2. Árvore de Decisão (com tuning de hiperparâmetros)
tree_param_grid = {
    'max_depth': [5, 10, 15, None],
    'min_samples_split': [2, 10, 20],
    'min_samples_leaf': [1, 5, 10]
}
tree_model = DecisionTreeClassifier(random_state=42)
train_and_evaluate_model(tree_model, "Árvore de Decisão", tree_param_grid)

# 3. Regressão Logística (com tuning de hiperparâmetros)
lr_param_grid = {
    'C': [0.01, 0.1, 1, 10, 100],
    'penalty': ['l2']
}
lr_model = LogisticRegression(max_iter=1000, random_state=42)
train_and_evaluate_model(lr_model, "Regressão Logística", lr_param_grid)

# 4. Random Forest (com tuning de hiperparâmetros)
rf_param_grid = {
    'n_estimators': [10, 50, 100, 200],
    'max_depth': [5, 10, 15, None],
    'min_samples_split': [2, 10, 20],
    'min_samples_leaf': [1, 5, 10]
}
rf_model = RandomForestClassifier(random_state=42)
train_and_evaluate_model(rf_model, "Random Forest", rf_param_grid)

# 5. SVM (com tuning de hiperparâmetros)
svm_param_grid = {
    'C': [0.01, 0.1, 1, 10, 100],
    'kernel': ['linear', 'rbf', 'poly']
}
svm_model = SVC(random_state=42)
train_and_evaluate_model(svm_model, "SVM (Support Vector Machines)", svm_param_grid)
