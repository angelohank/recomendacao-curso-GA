import pandas as pd
import random
usuarios_dataset = pd.read_csv('../resources/datasets/users.csv')
classificacoes_dataset = pd.read_csv('../resources/datasets/ratings.csv')

students = usuarios_dataset['UserID'].unique().tolist()
courses = classificacoes_dataset['Item'].unique().tolist()

TAMANHO_POPULACAO = 10
QT_GERACOES = 50
TAXA_MUTACAO = 0.1 #TODO esses valores podem ser alterados para serem recebidos dinamicamente na execucao

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
    populacao_ordenada = sorted(populacao, key=fitness, reverse=True)
    return populacao_ordenada[:2]

def crossover(individuo1, individuo2):
    estudante = individuo1[0]
    curso = individuo2[1]
    return (estudante, curso)


def mutate(recomendacao):
    if random.random() < TAXA_MUTACAO:
        return (recomendacao[0], random.choice(courses))
    return recomendacao


def exec_process():
    populacao = gerar_populacao()

    for geracao in range(QT_GERACOES):
        individuos = seleciona_individuos(populacao)
        filhos = [mutate(crossover(*individuos)) for _ in range(TAMANHO_POPULACAO)]
        population = individuos + filhos

    best_recommendation = max(populacao, key=fitness)
    return best_recommendation

melhor_recomendacao = exec_process()
print(f"melhor recomendação: Estudante: {melhor_recomendacao[0]} -> curso: {melhor_recomendacao[1]}")
