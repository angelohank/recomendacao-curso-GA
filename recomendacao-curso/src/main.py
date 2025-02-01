import pandas as pd

usuarios_dataset = pd.read_csv('../resources/datasets/users.csv')
classificacoes_dataset = pd.read_csv('../resources/datasets/ratings.csv')

students = usuarios_dataset['UserID'].unique().tolist()
courses = classificacoes_dataset['Item'].unique().tolist()

TAMANHO_POPULACAO = 10
QT_GERACOES = 50
TAXA_MUTACAO = 0.1 #TODO esses valores podem ser alterados para serem recebidos dinamicamente na execucao
