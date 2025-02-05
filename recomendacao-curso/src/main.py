import pandas as pd
import random
from sklearn.model_selection import train_test_split
from previsao_recomendacao import prever

usuarios_dataset = pd.read_csv('../resources/datasets/users.csv')
classificacoes_dataset = pd.read_csv('../resources/datasets/ratings.csv')

students = usuarios_dataset['UserID'].unique().tolist()
courses = classificacoes_dataset['Item'].unique().tolist()

treino, teste = train_test_split(classificacoes_dataset, test_size=0.2, random_state=42)

TAMANHO_POPULACAO = 10
QT_GERACOES = 50
TAXA_MUTACAO = 0.1 #TODO esses valores podem ser alterados para serem recebidos dinamicamente na execucao


def fitness_with_tensor_flow(recomendacao):
    estudante, curso = recomendacao
    return prever(estudante, curso)


def fitness(recomendacao):
    student, course = recomendacao

    classificacao_estudante = classificacoes_dataset[(classificacoes_dataset['UserID'] == student) & (classificacoes_dataset['Item'] == course)]
    if not classificacao_estudante.empty:
        score = classificacao_estudante['Rating'].mean().mean()
        return score
    else:
        return 0

def gerar_populacao():
    return [(random.choice(students), random.choice(courses)) for _ in range(TAMANHO_POPULACAO)]

def seleciona_individuos(populacao):
    populacao_ordenada = sorted(populacao, key=fitness_with_tensor_flow, reverse=True)
    return populacao_ordenada[:2]

def crossover(individuo1, individuo2):
    estudante = individuo1[0]
    curso = individuo2[1]
    return (estudante, curso)


def mutate(recomendacao):
    if random.random() < TAXA_MUTACAO:
        return (recomendacao[0], random.choice(courses))
    return recomendacao

def calc_acuracia(cursos_recomendados, testes):
    hits = 0
    total = 0

    for student in testes['UserID'].unique():
        real_courses = set(testes[testes['UserID'] == student]['Item'])
        if student in cursos_recomendados:
            recommended = {cursos_recomendados[student]}
            if len(real_courses & recommended) > 0:
                hits += 1
        total += 1

    return hits / total if total > 0 else 0

def exec_process():
    populacao = gerar_populacao()

    for geracao in range(QT_GERACOES):
        individuos = seleciona_individuos(populacao)
        filhos = [mutate(crossover(*individuos)) for _ in range(TAMANHO_POPULACAO)]
        populacao = individuos + filhos

    best_recommendation = max(populacao, key=fitness_with_tensor_flow)
    return best_recommendation

recomendacoes = [exec_process() for _ in range(10)]
cursos_recomendados = {student: course for student, course in recomendacoes}

qt_execucoes = 100
soma_acuracia = 0.0

for i in range(qt_execucoes):
    melhor_recomendacao = exec_process()
    print(f"melhor recomendação: Estudante: {melhor_recomendacao[0]} -> curso: {melhor_recomendacao[1]}")

    acuracia = calc_acuracia(cursos_recomendados, teste)

    soma_acuracia += acuracia

print(f"Acurácia média do algoritmo: {(soma_acuracia/qt_execucoes):.2%}")

