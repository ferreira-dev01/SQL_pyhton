from sqlite3 import connect
import pandas as pd

# Cria um banco de dados em memória
engine = connect(':memory:')

# Cria os DataFrames a partir das planilhas de vitimas
df1 = pd.read_excel('vitimasA20003.xlsx')
df2 = pd.read_excel('vitimasU33004.xlsx')

# Salva os DataFrames como tabelas no banco de dados na memoria
df1.to_sql('tabela1', con=engine, index=False)
df2.to_sql('tabela2', con=engine, index=False)

# Realiza a consulta
query = pd.read_sql_query('''
SELECT nome1 as 'Nome vitima reincidente'
FROM
tabela1 AS t1
INNER JOIN
tabela2 AS t2
ON t1.nome1 = t2.nome2
WHERE t1.data_fato1 < t2.data_fato2
''', engine)

# Imprime o resultado
print(query)