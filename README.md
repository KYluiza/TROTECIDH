# Análise das Manchetes sobre Trote Universitário

## Descrição do Projeto
Este projeto tem como objetivo analisar manchetes de notícias relacionadas ao trote universitário, com foco em universidades como USP, UNICAMP, UNESP e outras instituições. Utilizamos técnicas de web scraping para coletar manchetes de notícias, que são então classificadas como Positivas, Negativas ou Neutras com base em palavras-chave. Posteriormente, aplicamos modelos de aprendizado de máquina para prever a polaridade das manchetes.

## Objetivos
- Coletar manchetes de notícias sobre trote universitário.
- Classificar as manchetes como Positivas, Negativas ou Neutras com base em palavras-chave.
- Utilizar diferentes modelos de aprendizado de máquina para refinar a análise e prever a polaridade das manchetes.
- Avaliar a performance dos modelos utilizando validação cruzada e ajuste de hiperparâmetros.

## Tecnologias Utilizadas
- **Linguagem de Programação**: Python
- **Automação de Navegação e Coleta de Dados**: PyAutoGUI, Pyperclip, Webbrowser
- **Bibliotecas de Machine Learning**: Scikit-learn
- **Manipulação de Dados**: Pandas
- **Visualização de Dados**: Matplotlib (sem interface gráfica)
- **Processamento de Texto**: CountVectorizer para unigramas e bigramas
- **Modelos de Classificação**:
  - Naive Bayes
  - Árvore de Decisão
  - Regressão Logística
  - Random Forest
  - Support Vector Machines (SVM)

## Estrutura do Projeto
- `scripts/`: Scripts Python para raspagem de notícias e análise das manchetes.
- `data/`: Arquivos CSV contendo as manchetes e classificações coletadas.
- `results/`: Resultados das avaliações dos modelos, incluindo relatórios de classificação e métricas de performance.

## Fluxo do Projeto

### 1. Coleta de Manchetes
Utilizamos web scraping para coletar manchetes de diferentes fontes de notícias online, incluindo pesquisas específicas no Google News para universidades como USP, UNICAMP, UNESP e notícias gerais sobre trote universitário.

URLs utilizadas para coleta:
- **USP**: [Notícias sobre trote na USP](https://www.google.com/search?q=trote+universit%C3%A1rio+USP&sca_esv=cd8f201e94c2caf3&rlz=1C1GCEA_enBR1125BR1125&tbm=nws&ei=YakBZ_CSNKzO1sQPpIm_yQc&start={start_value}&sa=N&ved=2ahUKEwiwx8XWkfiIAxUsp5UCHaTEL3k4KBDy0wN6BAgCEAQ&biw=1280&bih=585&dpr=1.5)
- **UNICAMP**: [Notícias sobre trote na UNICAMP](https://www.google.com/search?q=trote+universit%C3%A1rio+UNICAMP&sca_esv=cd8f201e94c2caf3&rlz=1C1GCEA_enBR1125BR1125&tbm=nws&ei=YakBZ_CSNKzO1sQPpIm_yQc&start={start_value}&sa=N&ved=2ahUKEwiwx8XWkfiIAxUsp5UCHaTEL3k4KBDy0wN6BAgCEAQ&biw=1280&bih=585&dpr=1.5)
- **UNESP**: [Notícias sobre trote na UNESP](https://www.google.com/search?q=trote+universit%C3%A1rio+UNESP&sca_esv=cd8f201e94c2caf3&rlz=1C1GCEA_enBR1125BR1125&tbm=nws&ei=YakBZ_CSNKzO1sQPpIm_yQc&start={start_value}&sa=N&ved=2ahUKEwiwx8XWkfiIAxUsp5UCHaTEL3k4KBDy0wN6BAgCEAQ&biw=1280&bih=585&dpr=1.5)
- **Trote Universitário Geral**: [Notícias sobre trote universitário](https://www.google.com/search?q=trote+universit%C3%A1rio&sca_esv=cd8f201e94c2caf3&rlz=1C1GCEA_enBR1125BR1125&tbm=nws&ei=YakBZ_CSNKzO1sQPpIm_yQc&start={start_value}&sa=N&ved=2ahUKEwiwx8XWkfiIAxUsp5UCHaTEL3k4KBDy0wN6BAgCEAQ&biw=1280&bih=585&dpr=1.5)

O script de raspagem abre as páginas, copia o conteúdo das manchetes e as salva em um arquivo CSV para posterior análise.

### 2. Limpeza e Classificação das Manchetes
As manchetes são limpas para remover inconsistências e normalizar termos como "universidades" para "universidade" e "trotes" para "trote". Em seguida, são classificadas automaticamente com base em palavras-chave que indicam uma polaridade positiva ou negativa. Se nenhuma palavra-chave for encontrada, a manchete é classificada como "Neutra".

Palavras-chave utilizadas:
- **Positivas**: "sucesso", "aprovação", "conquista", "crescimento", "vitória", "melhora", "lei proíbe", "proíbe", "proibid"
- **Negativas**: "nega", 'absurdo', 'agredid', 'racismo', "racista", 'denúncia', 'fracasso', 'queda', 'erro', 'morte', 'tóxico', 'expulso', 'crime', 'perda', 'violência', "estupro", "errado", "morre", "abandon"

### 3. Análise de Sentimentos com Modelos de Machine Learning
Utilizamos diferentes modelos de aprendizado de máquina para prever a classificação das manchetes. Os modelos incluem Naive Bayes, Árvore de Decisão, Regressão Logística, Random Forest e Support Vector Machines (SVM). Os dados são divididos em conjuntos de treino e teste (70% teste e 30% treino), e aplicamos validação cruzada e ajuste de hiperparâmetros para otimizar os modelos.

## Modelos de Aprendizado de Máquina

### 1. **Naive Bayes**
O Naive Bayes é um classificador probabilístico que assume a independência condicional entre as características. Ele é particularmente eficiente para problemas de classificação de texto, como a análise de sentimentos. Este modelo é rápido e simples, mas a suposição de independência pode limitar seu desempenho em certos casos.

### 2. **Árvore de Decisão**
As árvores de decisão criam um modelo em formato de árvore, onde cada nó representa uma decisão baseada em uma característica. Elas são fáceis de interpretar, mas podem ser propensas ao overfitting (ajustar demais aos dados de treino) se não forem podadas adequadamente.

### 3. **Regressão Logística**
A regressão logística é um classificador linear que calcula a probabilidade de uma instância pertencer a uma determinada classe. É eficaz para problemas binários ou multiclasses, e seu desempenho pode ser ajustado com o hiperparâmetro `C`, que controla a regularização.

### 4. **Random Forest**
O Random Forest é um método de ensemble que utiliza várias árvores de decisão para melhorar a generalização do modelo. Ele é robusto e reduz o risco de overfitting, proporcionando bons resultados em muitas aplicações.

### 5. **SVM (Support Vector Machines)**
As máquinas de vetores de suporte (SVM) tentam encontrar um hiperplano que melhor separe as classes de dados. SVM é eficaz em espaços de alta dimensionalidade e pode ser ajustado com diferentes tipos de kernel, como linear, radial ou polinomial.

## Validação Cruzada
A validação cruzada é uma técnica que divide o conjunto de dados em vários subconjuntos (folds) e avalia o modelo em diferentes combinações de treino e teste. Isso ajuda a garantir que o modelo generalize bem para dados desconhecidos, evitando overfitting. Uma validação cruzada com 5 folds foi utilizada neste projeto.

## Métricas de Avaliação

Ao avaliar os modelos de aprendizado de máquina, utilizamos quatro principais métricas: **Precisão (Precision)**, **Recall**, **F1-score** e **Acurácia**. Essas métricas fornecem uma visão detalhada sobre o desempenho do modelo, especialmente em problemas de classificação com múltiplas classes.

### **Precisão (Precision)**

A **Precisão** mede a proporção de previsões corretas para uma classe específica entre todas as previsões feitas para essa classe. Ela é útil quando o foco está em minimizar o número de falsos positivos (previsões incorretas como pertencentes a uma classe).

$\text{Precisão} = \frac{\text{Verdadeiros Positivos (TP)}}{\text{Verdadeiros Positivos (TP)} + \text{Falsos Positivos (FP)}}$

- **Verdadeiros Positivos (TP)**: Instâncias que pertencem a uma classe e foram corretamente classificadas como tal.
- **Falsos Positivos (FP)**: Instâncias que não pertencem a uma classe, mas foram incorretamente classificadas como pertencendo a ela.

**Exemplo de Cálculo**:
Se o modelo previu corretamente 80 manchetes negativas como "Negativa" (TP) e previu incorretamente 20 manchetes neutras como "Negativa" (FP), a precisão para a classe "Negativa" seria:

$\text{Precisão} = \frac{80}{80 + 20} = 0.80 \, (80\%)$

---

### **Recall**

O **Recall** mede a capacidade do modelo de identificar corretamente todas as instâncias relevantes de uma classe específica. Ele é útil quando o objetivo é minimizar os falsos negativos, ou seja, instâncias que pertencem a uma classe, mas que o modelo falhou em identificar.

$\text{Recall} = \frac{\text{Verdadeiros Positivos (TP)}}{\text{Verdadeiros Positivos (TP)} + \text{Falsos Negativos (FN)}}$

- **Falsos Negativos (FN)**: Instâncias que pertencem a uma classe, mas foram classificadas incorretamente como pertencendo a outra classe.

**Exemplo de Cálculo**:
Se de 100 manchetes negativas, o modelo classificou corretamente 80 como "Negativa" (TP), mas classificou 20 incorretamente como neutras ou positivas (FN), o recall seria:

$\text{Recall} = \frac{80}{80 + 20} = 0.80 \, (80\%)$

---

### **F1-score**

O **F1-score** é a média harmônica entre a precisão e o recall. Ele é particularmente útil quando há um desequilíbrio entre as classes, pois equilibra o impacto de ambas as métricas.

$F1 = 2 \times \frac{\text{Precisão} \times \text{Recall}}{\text{Precisão} + \text{Recall}}$

**Exemplo de Cálculo**:
Se a precisão e o recall de um modelo para uma classe são ambos 0.80, o F1-score será:

$F1 = 2 \times \frac{0.80 \times 0.80}{0.80 + 0.80} = 0.80$

---

### **Acurácia**

A **Acurácia** mede a proporção de previsões corretas em relação ao total de previsões feitas. Ela é uma métrica geral que considera todas as classes, mas pode ser enganosa em casos de classes desbalanceadas.

$\text{Acurácia} = \frac{\text{Verdadeiros Positivos (TP)} + \text{Verdadeiros Negativos (TN)}}{\text{Total de Instâncias}}$

**Exemplo de Cálculo**:
Se o modelo classificou corretamente 150 de 200 manchetes, a acurácia será:

$\text{Acurácia} = \frac{150}{200} = 0.75 \, (75\%)$

---

Essas métricas foram utilizadas para avaliar a performance dos modelos de aprendizado de máquina neste projeto, proporcionando uma visão detalhada do desempenho em diferentes aspectos.


## Análise dos Resultados

### 0. **Resultados descritivos abertos**
- **Dashboard trote universitário**: [Dashboard aberto]([https://app.powerbi.com/view?r=eyJrIjoiZTZjZTY1MzktZjE3Mi00NTcyLTkyNDYtZmQ4MjE0ZDYzYTQ4IiwidCI6ImViZjIyYzg0LThiNzAtNGMyNy05NGYzLTRhMWNjNjRlYThhNCJ9])

### 1. **Naive Bayes**
- **Acurácia (Validação Cruzada)**: 0.7730
- **Acurácia no Teste**: 0.7191
- **Relatório de Classificação**:
  - **Precisão**: A precisão para classes como "Neutra" é alta (0.90), mas para "Negativa", a precisão é de apenas 0.38, sugerindo que o modelo tem dificuldade em identificar corretamente manchetes negativas.
  - **Recall**: O recall para manchetes negativas é alto (0.72), mas a precisão é baixa, indicando que muitas previsões negativas são incorretas.

**Análise**: O Naive Bayes é um modelo simples, e sua principal limitação é a suposição de independência condicional entre as características, o que pode explicar a performance mediana, especialmente em classes como "Negativa".

### 2. **Árvore de Decisão**
- **Acurácia (Validação Cruzada)**: 0.9565
- **Acurácia no Teste**: 0.9326
- **Relatório de Classificação**:
  - **Precisão**: A árvore de decisão obteve 1.00 de precisão para manchetes negativas e positivas, o que pode indicar que o modelo está superajustado.
  - **Recall**: O recall da classe "Positiva" é baixo (0.58), sugerindo que o modelo não identifica bem todas as manchetes positivas.

**Análise**: Embora a acurácia seja alta, o modelo pode estar sofrendo de overfitting, ajustando-se demais aos dados de treino e não generalizando bem para o conjunto de teste.

### 3. **Regressão Logística**
- **Acurácia (Validação Cruzada)**: 0.9010
- **Acurácia no Teste**: 0.8708
- **Relatório de Classificação**:
  - **Precisão**: A precisão para manchetes negativas é alta (1.00), mas o recall é baixo (0.48), o que sugere que o modelo classifica muitas manchetes como "Negativas" de forma equivocada.
  - **Recall**: A regressão logística tem bom recall para manchetes neutras (1.00).

**Análise**: A regressão logística tem um desempenho sólido, especialmente para a classe neutra. No entanto, a baixa sensibilidade para manchetes negativas é um ponto fraco.

### 4. **Random Forest**
- **Acurácia (Validação Cruzada)**: 0.8865
- **Acurácia no Teste**: 0.8708
- **Relatório de Classificação**:
  - **Precisão e Recall**: O Random Forest tem desempenho semelhante ao da regressão logística, com boa precisão para manchetes neutras e positivas, mas problemas ao identificar manchetes negativas.

**Análise**: O Random Forest oferece uma boa combinação de precisão e recall, mas tem dificuldades nas classes menores, como "Positiva".

### 5. **SVM (Support Vector Machines)**
- **Acurácia (Validação Cruzada)**: 0.9058
- **Acurácia no Teste**: 0.8933
- **Relatório de Classificação**:
  - **Precisão e Recall**: A SVM teve bom desempenho geral, com uma precisão de 1.00 para manchetes negativas e positivas. No entanto, o recall da classe "Positiva" foi relativamente baixo (0.58).

**Análise**: O SVM apresentou um desempenho equilibrado, sendo um dos melhores modelos em termos de acurácia e F1-score, embora tenha enfrentado algumas dificuldades com a classe "Positiva".

## Conclusão
Com base nos resultados obtidos:
- O **SVM** e a **Árvore de Decisão** tiveram as melhores acurácias e desempenho geral, embora ambos tenham sofrido com um recall relativamente baixo para manchetes positivas.
- O **Naive Bayes** é eficiente, mas teve um desempenho inferior em comparação com os outros modelos.
- O **Random Forest** e a **Regressão Logística** tiveram desempenho sólido, mas com problemas em prever corretamente manchetes negativas.

O próximo passo seria ajustar ainda mais os hiperparâmetros ou combinar modelos (ensemble) para melhorar a performance geral, especialmente em classes menores como "Positiva".

