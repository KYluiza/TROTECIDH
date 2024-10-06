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
- **USP**: [Google News - USP](https://www.google.com/search?q=trote+universit%C3%A1rio+USP)
- **UNICAMP**: [Google News - UNICAMP](https://www.google.com/search?q=trote+universit%C3%A1rio+UNICAMP)
- **UNESP**: [Google News - UNESP](https://www.google.com/search?q=trote+universit%C3%A1rio+UNESP)
- **Trote Universitário Geral**: [Google News - Geral](https://www.google.com/search?q=trote+universit%C3%A1rio)

O script de raspagem abre as páginas, copia o conteúdo das manchetes e as salva em um arquivo CSV para posterior análise.

### 2. Limpeza e Classificação das Manchetes
As manchetes são limpas para remover inconsistências e normalizar termos como "universidades" para "universidade" e "trotes" para "trote". Em seguida, são classificadas automaticamente com base em palavras-chave que indicam uma polaridade positiva ou negativa. Se nenhuma palavra-chave for encontrada, a manchete é classificada como "Neutra".

Palavras-chave utilizadas:
- **Positivas**: "sucesso", "aprovação", "conquista", "crescimento", "vitória", "melhora", "lei proíbe", "proíbe", "proibid"
- **Negativas**: "nega", 'absurdo', 'agredid', 'racismo', "racista", 'denúncia', 'fracasso', 'queda', 'erro', 'morte', 'tóxico', 'expulso', 'crime', 'perda', 'violência', "estupro", "errado", "morre", "abandon"

### 3. Análise de Sentimentos com Modelos de Machine Learning
Utilizamos diferentes modelos de aprendizado de máquina para prever a classificação das manchetes. Os modelos incluem Naive Bayes, Árvore de Decisão, Regressão Logística, Random Forest e Support Vector Machines (SVM). Os dados são divididos em conjuntos de treino e teste (70% treino e 30% teste), e aplicamos validação cruzada e ajuste de hiperparâmetros para otimizar os modelos.

#### Modelos Testados:
- **Naive Bayes**: Modelo simples e eficiente para a classificação de texto.
- **Árvore de Decisão**: Testamos diferentes profundidades e critérios de divisão.
- **Regressão Logística**: Ajustamos o parâmetro `C` para melhorar a precisão do modelo.
- **Random Forest**: Utilizamos múltiplas árvores de decisão para melhorar a generalização do modelo.
- **Support Vector Machines (SVM)**: Testamos diferentes kernels e valores de `C` para encontrar a melhor performance.

#### Avaliação dos Modelos:
Para cada modelo, medimos a acurácia e geramos um relatório de classificação que inclui precisão, recall e F1-score. Um exemplo de saída para o modelo Naive Bayes é:


