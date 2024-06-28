import pyodbc as dbc


dados_conexao = (
    'Divrer={SQL Server};'
    'Server=Bruno;'
    'Database=Biblioteca_CG;'
    'UID=Bruno_codigos;'
    'PWD=Concreto.19'
)

conexao = dbc.connect(dados_conexao)

print('Conexão sucedida')


#print(dbc.drivers())
#['SQL Server', 'ODBC Driver 17 for SQL Server', 'SQL Server Native Client RDA 11.0']