import os
import sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set()


def plota_pivot_table(df, value, index, func, ylabel, xlabel, opcao='nada'):
    if opcao == 'nada':
        pd.pivot_table(df, values=value, index=index, aggfunc=func).plot(figsize=[15, 5])
    elif opcao == 'unstack':
        pd.pivot_table(df, values=value, index=index, aggfunc=func).unstack().plot(figsize=[15, 5])
    elif opcao == 'sort':
        pd.pivot_table(df, values=value, index=index, aggfunc=func).sort_values(value).plot(figsize=[15, 5])
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    return None


meses = sys.argv
del meses[0]
for mes in meses:
    sinasc = pd.read_csv('./input/SINASC_RO_2019_' + mes + '.csv')
    max_data = sinasc.DTNASC.max()[:7]
    os.makedirs('./output/figs/' + max_data, exist_ok=True)
    plota_pivot_table(sinasc, 'IDADEMAE', 'DTNASC', 'mean', 'idade media da mae por data', 'data de nascimento')
    plt.savefig('./output/figs/' + max_data + '/idade media mae por data.png')
    plota_pivot_table(sinasc, 'IDADEMAE', ['DTNASC', 'SEXO'], 'mean', 'idade media da mae', 'data de nascimento',
                      'unstack')
    plt.savefig('./output/figs/' + max_data + '/idade media mae por sexo.png')
    plota_pivot_table(sinasc, 'PESO', ['DTNASC', 'SEXO'], 'mean', 'media peso bebe', 'data de nascimento', 'unstack')
    plt.savefig('./output/figs/' + max_data + '/media peso bebe.png')
    plota_pivot_table(sinasc, 'PESO', 'ESCMAE', 'median', 'Peso mediano', 'Escolaridade mae', 'sort')
    plt.savefig('./output/figs/' + max_data + '/eso mediano por escolaridade mae.png')
    plota_pivot_table(sinasc, 'APGAR1', 'GESTACAO', 'mean', 'apgar1 medio', 'gestacao', 'sort')
    plt.savefig('./output/figs/' + max_data + '/apgar1 medio por gestacao.png')
    plota_pivot_table(sinasc, 'APGAR5', 'GESTACAO', 'mean', 'apgar5 medio', 'gestacao', 'sort')
    plt.savefig('./output/figs/' + max_data + '/apgar5 medio por gestacao.png')
