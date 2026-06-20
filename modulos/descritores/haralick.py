import cv2
import mahotas as mt
import numpy as np

def extrair_haralick(imagens):
  """
    Extrai características de textura utilizando o descritor Haralick.

    Parâmetros:
        imagens (list): Lista contendo as imagens carregadas.

    Retorno:
        numpy.ndarray: Matriz contendo os vetores de características
        extraídos de cada imagem.
    """

  # Lista que armazenará os vetores de características
  caracteristicas = []

  # Percorre todas as imagens do conjunto
  for imagem in imagens:
    # Verifica se a imagem está em RGB
    if len(imagem.shape) == 3:
      # Converte a imagem para escala de cinza
      imagem = cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY)
      
      # Extrai os atributos de Haralick. O método retorna uma matriz com características calculadas em diferentes direções
      vetor = mt.features.haralick(imagem).flatten()

      # Adiciona o vetor de características à lista
      caracteristicas.append(vetor)

  # Converte a lista para um array NumPy
  return np.array(caracteristicas)