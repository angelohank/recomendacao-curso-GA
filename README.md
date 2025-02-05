# Algoritmo genético para recomendação de cursos para alunos

#### O objetivo desse algortimo é indicar qual o melhor curso, para qual aluno.
#### Os dados de avaliação dos alunos para os cursos foram retirados do dataset [ITM-Rec](https://www.kaggle.com/datasets/irecsys/itmrec)


## Funcionamento

Baseado na quantidade de gerações, definida na variável `QT_GERACOES`, o algoritmo: <br>
**1 - seleciona os melhores indivíduos da população, baseando-se no fitness**

```O *fitness* é calculado para calcular a qualidade da recomendação passada, da seguinte forma:
1 - filtra as avaliações do estudante para o curso
2 - calcula a média das avaliações nos diferentes critérios do dataset
```

**2 - seleciona os filhos usando a função de mutação e realizando o crossover**
Nessa etapa considera-se a taxa de mutação, definida na variável `TAXA_MUTACAO`

**3 - forma uma nova população com os pais e filhos criados**


## Requerimentos
Pandas - para leitura de arquivos .csv <br>
`pip install pandas`
`pip install tensorflow`
`pipinstall sklearn`

Python instalado (qualquer versao)
```
caso use a versão 3, no passo seguinte utilize Python3 ao invés de Python
```


## Execução
Para executar esse algoritmo, siga os seguintes passos:

1 - clone o repositório <br>
2 - no terminal digite <br> `python /caminho-do-repositorio-clonado/recomendacao-curso/src/main.py`

<br><br>
Por hora é preciso alterar em código qual função de fitness será usada, em breve poderá ser passada como parâmetro na execução
- #### Função de fitness sem redes neurais
tudo que estiver com `fitness_with_tensor_flow` deve ser substituido por `fitness`

- #### Função de fitness com redes neurais
tudo que estiver com `fitness` deve ser substituido por `fitness_with_tensor_flow`

### Após 100 execuções, a acurácia sem o uso de redes neurais ficou em média 0.75% durante as execuções, enquanto que, com use de redes neurais, ficou com média 0.99

Com redes neurais: <br> ![image](https://github.com/user-attachments/assets/b0b13a17-a040-42cd-ab30-d103a721c6d4) <br>
Sem redes neurais: <br> ![image](https://github.com/user-attachments/assets/15c0210b-0209-4eaa-8c7d-b039ca50c8a2) <br>



<!--#### Exemplo de saída
<!--![image](https://github.com/user-attachments/assets/720dafe4-29f3-47d7-9d8f-692e111e03ec)
