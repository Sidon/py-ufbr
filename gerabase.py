import xlrd
import os
import sys
from collections import namedtuple

f = open("base.py", "w")

estados = {'11': {'sigla': 'RO', 'nome': 'Rondonia'},
           '12': {'sigla': 'AC', 'nome': 'Acre'},
           '13': {'sigla': 'AM', 'nome': 'Amazonas'},
           '14': {'sigla': 'RR', 'nome': 'Roraima'},
           '15': {'sigla': 'PA', 'nome': 'Pará'},
           '16': {'sigla': 'AP', 'nome': 'Amapá'},
           '17': {'sigla': 'TO', 'nome': 'Tocantis'},
           '21': {'sigla': 'MA', 'nome': 'Maranão'},
           '22': {'sigla': 'PI', 'nome': 'Piaui'},
           '23': {'sigla': 'CE', 'nome': 'Ceará'},
           '24': {'sigla': 'RN', 'nome': 'Rio Grande do Norte'},
           '25': {'sigla': 'PB', 'nome': 'Paraiba'},
           '26': {'sigla': 'PE', 'nome': 'Pernanbuco'},
           '27': {'sigla': 'AL', 'nome': 'Alagoas'},
           '28': {'sigla': 'SE', 'nome': 'Sergipe'},
           '29': {'sigla': 'BA', 'nome': 'Bahia'},
           '31': {'sigla': 'MG', 'nome': 'Minas Gerais'},
           '32': {'sigla': 'ES', 'nome': 'Espirito Santo'},
           '33': {'sigla': 'RJ', 'nome': 'Rio de Janeiro'},
           '35': {'sigla': 'SP', 'nome': 'São Paulo'},
           '41': {'sigla': 'PR', 'nome': 'Paraná'},
           '42': {'sigla': 'SC', 'nome': 'Santa Catarina'},
           '43': {'sigla': 'RS', 'nome': 'Rio Grande do Sul'},
           '50': {'sigla': 'MS', 'nome': 'Mato Grosso do Sul'},
           '51': {'sigla': 'MT', 'nome': 'Mato Grosso'},
           '52': {'sigla': 'GO', 'nome': 'Goiás'},
           '53': {'sigla': 'DF', 'nome': 'Distrito Federal'}}

book = xlrd.open_workbook('base.xls')
first_sheet = book.sheet_by_index(0)

municipios = []
Municipio = namedtuple('municipio', 'codigo nome')

cod_uf = first_sheet.cell(1, 1).value

for n in range(1, first_sheet.nrows):

    m = Municipio(codigo=str(first_sheet.cell(n, 2).value), nome=first_sheet.cell(n, 4).value)

    if first_sheet.cell(n, 1).value == cod_uf:
        municipios.append(m)
    else:
        estados[cod_uf]['municipios'] = municipios
        municipios = [m]
        cod_uf = first_sheet.cell(n, 1).value

orig_stdout = sys.stdout
sys.stdout = f

print('from collections import namedtuple\n\n')
print ('class UF:')
print ('    def __init__(self):')
print ('        self._ufs = OrderedDict()')
print ('        self._ufs =  estados')
print ('    def municipios(self, codigo=None, nome=None):')
print ("        return self._ufs[codigo]['municipios']")

sys.stdout = orig_stdout
f.close()
