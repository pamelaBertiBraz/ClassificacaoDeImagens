# 😺​🐶​ Classificação de Imagens de Gatos e Cachorros utilizando Haralick e SVM
---

## 👤​ Equipe
- Pamela Berti Braz

---

## 🖋️​ Descrição da abordagem utilizada

Foi utilizada uma abordagem clássica de classificação de imagens baseada em extração de características e aprendizado de máquina.

---

### 💾​ Dataset

O dataset utilizado foi uma amostra do conjunto PetImages (Cats vs Dogs), contendo 2000 imagens, sendo 1000 imagens da classe Cat (gatos) e 1000 imagens da classe Dog (cachorros).

As imagens foram divididas em dois conjuntos:

- Treinamento: 1600 imagens
- Teste: 400 imagens

O dataset original está disponível em:

<https://www.kaggle.com/datasets/shaunthesheep/microsoft-catsvsdogs-dataset>

---

### 🔍 Haralick

Para a extração de características foi utilizado o descritor Haralick, implementado por meio da biblioteca Mahotas.

O método Haralick é baseado na Matriz de Coocorrência dos Níveis de Cinza (GLCM), uma técnica utilizada para analisar padrões de textura presentes em uma imagem. A partir dessa matriz são calculadas diversas medidas estatísticas capazes de representar características visuais como contraste, correlação, homogeneidade e energia.

No projeto, cada imagem foi inicialmente convertida para escala de cinza utilizando a biblioteca OpenCV. Em seguida, foram extraídas as características de Haralick por meio da função ```mt.features.haralick()```. Os vetores gerados foram utilizados como entrada para o processo de classificação.

---

### 🤖 SVM

Após a extração das características, foi utilizado um classificador SVM (Support Vector Machine).

O SVM é um algoritmo de aprendizado supervisionado que busca encontrar uma fronteira de decisão capaz de separar amostras pertencentes a diferentes classes. Esse método é amplamente utilizado em problemas de classificação devido à sua capacidade de lidar com dados de alta dimensionalidade.

Neste projeto foi utilizada uma configuração composta por:
- Normalização dos atributos utilizando StandardScaler;
- Kernel RBF (Radial Basis Function);
- Parâmetro C = 10;
- random_state = 42.

A utilização do kernel RBF permite que o modelo encontre fronteiras de decisão não lineares, tornando a classificação mais flexível em relação aos padrões encontrados nas características extraídas pelo descritor Haralick.

---

### 📊 Resultados Obtidos

O modelo foi avaliado utilizando o conjunto de teste composto por 400 imagens, sendo 200 imagens de gatos e 200 imagens de cachorros.

A classificação foi realizada utilizando o descritor de textura Haralick para extração de características e o classificador SVM com kernel RBF.

#### Matriz de Confusão

![Matriz de Confusão](https://imgur.com/cghW7f8.png)

A matriz de confusão demonstra que o modelo apresentou melhor desempenho na identificação de gatos do que de cachorros. Das 200 imagens de gatos, 138 foram classificadas corretamente, enquanto 62 foram classificadas incorretamente como cachorros. Já para a classe cachorro, 110 imagens foram classificadas corretamente e 90 incorretamente como gatos.

#### Métricas de Classificação

![Métricas de Classificação](https://imgur.com/VnVA2Zz.png)

As métricas obtidas indicam um desempenho moderado do classificador. A classe Cat apresentou maior recall (0,69), indicando que o modelo conseguiu identificar corretamente a maior parte das imagens de gatos. Já a classe Dog apresentou maior precisão (0,64), porém com recall inferior (0,55), demonstrando maior dificuldade na identificação correta dos cachorros.

O F1-Score, que representa o equilíbrio entre precisão e recall, foi de 0,64 para gatos e 0,59 para cachorros. A acurácia geral obtida foi de 62%, indicando que o modelo classificou corretamente 248 das 400 imagens do conjunto de teste.

#### Análise dos Resultados

Os resultados obtidos indicam que a combinação do descritor Haralick com o classificador SVM foi capaz de distinguir parcialmente as duas classes presentes no dataset. A acurácia geral de 62% demonstra que as características de textura extraídas pelo Haralick fornecem informações úteis para a classificação, porém insuficientes para capturar completamente as diferenças entre gatos e cachorros.

Isso ocorre porque o descritor Haralick foi desenvolvido para representar padrões de textura da imagem, enquanto a distinção entre gatos e cachorros depende também de características relacionadas à forma, contorno, posição do animal e contexto da cena. Dessa forma, imagens com texturas semelhantes podem gerar vetores de características parecidos, dificultando a separação das classes pelo classificador.

Mesmo com essa limitação, o objetivo do projeto foi atingido, pois foi possível aplicar uma abordagem clássica de visão computacional utilizando um descritor diferente dos apresentados em aula, realizar o treinamento de um modelo SVM e avaliar seu desempenho por meio de matriz de confusão, precisão, recall, F1-score e acurácia.

---

## 📎​ Links importantes

- Repositório Google Drive: <https://drive.google.com/drive/folders/1wD2rUkinDMPRkEAvQTkUmnAmLoyYCDa8?usp=drive_link>
- Repositório GitHub: <https://github.com/pamelaBertiBraz/ClassificacaoDeImagens>
- Vídeo Google Drive: <https://drive.google.com/file/d/1WPhei666_EI92xmOhUxh93qp9O7_RcDt/view?usp=drive_link>
- Dataset utilizado: <https://www.kaggle.com/datasets/shaunthesheep/microsoft-catsvsdogs-dataset>

--- 

## 📄​ Instruções de Uso

### 1. Obter os arquivos do projeto

Baixe todos os arquivos disponibilizados no repositório Google Drive ou GitHub.

### 2. Baixar o dataset

Realize o download do dataset PetImages disponível em:

https://www.kaggle.com/datasets/shaunthesheep/microsoft-catsvsdogs-dataset

Após o download, organize as imagens em pastas separadas para treinamento e teste, contendo as classes:

- Cat
- Dog

### 3. Configurar os caminhos do projeto

Nos arquivos de configuração, altere:

- `caminho_modulos`
- `caminho_base`

para os diretórios correspondentes ao seu ambiente.

### 4. Configurar o ambiente no Google Colab

Execute a célula responsável pela montagem do Google Drive:

```python
from google.colab import drive
drive.mount('/content/drive')
```

### 5. Instalar dependências

Execute a célula responsável pela biblioteca Mahotas:

```
!pip install mahotas
```

As principais bibliotecas utilizadas foram:

- OpenCV
- NumPy
- Mahotas
- Scikit-Learn
- Matplotlib
- Seaborn

### 6. Executar o sistema

Após a configuração do ambiente:

1. Execute a célula principal do projeto;
2. Acesse a interface inicial;
3. Extraia as características Haralick das imagens;
4. Treine o classificador SVM;
5. Realize a classificação das imagens de teste;
6. Visualize as métricas de avaliação geradas pelo sistema.

### 7. Resultados

Ao final da execução serão gerados:

- Modelo treinado SVM;
- Matriz de confusão;
- Relatório de classificação;
- Precisão (Precision);
- Recall;
- F1-Score;
- Acurácia.


