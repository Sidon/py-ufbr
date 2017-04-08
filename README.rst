``pyUFbr`` - Estados e Municípios Brasileiros em python
#######################################################


Description
***********

Data set dos estados e suas respectivas cidades do Brasil, com seus códigos IBGE.


Requirements
************

::

    Python 3


Environment:
************

::

    linux


Install:
########

::

    pip install pyufbr


Usage
#####


>>> from pyUFbr.baseuf import ufbr


list_uf (Propriedade)
*********************
Retorna uma lista com todos os estados em ordem alfabética (siglas)

|

Sintaxe:

- ufbr.list_uf

|

*Exemplo:*

>>> print (ufbr.list_uf)
['AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MG', 'MS', 'MT',
 'PA', 'PB', 'PE', 'PI', 'PR', 'RJ', 'RN', 'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO']

----

list_cidades (Método)
*********************
Retorna lista com todas as cidades de um estado.

|

sintaxe:

- ufbr.list_cidades('XX'),
- ufbr.list_cidades(sigla='XX'),
- ufbr.list_cidades(codigo='NN')

|

onde:


sigla  = Sigla do estado, por exemplo: São Paulo = SP, Rio de Janeiro = RJ

codigo = Codigo do estado no IBGE, por exemplo: Amapá = 12,  Acre = 16


|

*Exemplo:*

>>> print(ufbr.list_cidades('AC'))
['ACRELÂNDIA', 'ASSIS BRASIL', 'BRASILÉIA', 'BUJARI', 'CAPIXABA', 'CRUZEIRO DO SUL',
  'EPITACIOLÂNDIA', 'FEIJÓ', 'JORDÃO', 'MÂNCIO LIMA', 'MANOEL URBANO',
  'MARECHAL THAUMATURGO', 'PLÁCIDO DE CASTRO', 'PORTO WALTER', 'RIO BRANCO',
  'RODRIGUES ALVES', 'SANTA ROSA DO PURUS', 'SENADOR GUIOMARD', 'SENA MADUREIRA',
  'TARAUACÁ', 'XAPURI', 'PORTO ACRE']

------

get_cidade (Método)
*******************
Retorna uma tupla (namedtupla) com o nome e o código da cidade

|

sintaxe:

- ufbr.get_cidade('São Paulo')

|

*Exemplos:*

>>> ufbr.get_cidade('São Paulo')
Municipio(codigo='3550308.0', nome='SÃO PAULO')

>>> ufbr.get_cidade('São Paulo').codigo
'3550308.0'


:Authors:
    Sidon Duarte,
    Yan Duarte

:Version: 0.1.0 of 2017/04/08
