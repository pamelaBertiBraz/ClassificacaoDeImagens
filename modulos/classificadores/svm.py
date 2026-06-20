import time

from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


def treinar_svm(caracteristicas, rotulos):

    print('Treinando o modelo SVM...')

    modelo_svm = make_pipeline(
        StandardScaler(),
        SVC(
            kernel='rbf',
            C=10,
            gamma='scale',
            random_state=42
        )
    )

    startTime = time.time()

    modelo_svm.fit(caracteristicas, rotulos)

    elapsedTime = round(time.time() - startTime, 2)

    print(f'Treinamento encerrado em {elapsedTime}s')

    return modelo_svm


def testar_svm(modelo_svm, caracteristicas):

    print('Iniciando previsão...')

    startTime = time.time()

    rotulos_previstos = modelo_svm.predict(caracteristicas)

    elapsedTime = round(time.time() - startTime, 2)

    print(f'Previsão encerrada em {elapsedTime}s')

    return rotulos_previstos