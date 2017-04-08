import unittest
from pyUFbr.baseuf import ufbr, Municipio

LISTA_AP16 = ['SERRA DO NAVIO', 'AMAPÁ', 'PEDRA BRANCA DO AMAPARI', 'CALÇOENE', 'CUTIAS', 'FERREIRA GOMES', 'ITAUBAL',
              'LARANJAL DO JARI', 'MACAPÁ', 'MAZAGÃO', 'OIAPOQUE', 'PORTO GRANDE', 'PRACUÚBA', 'SANTANA',
              'TARTARUGALZINHO', 'VITÓRIA DO JARI']

LISTA_AC12 = ['ACRELÂNDIA', 'ASSIS BRASIL', 'BRASILÉIA', 'BUJARI', 'CAPIXABA', 'CRUZEIRO DO SUL', 'EPITACIOLÂNDIA',
              'FEIJÓ', 'JORDÃO', 'MÂNCIO LIMA', 'MANOEL URBANO', 'MARECHAL THAUMATURGO', 'PLÁCIDO DE CASTRO',
              'PORTO WALTER', 'RIO BRANCO', 'RODRIGUES ALVES', 'SANTA ROSA DO PURUS', 'SENADOR GUIOMARD',
              'SENA MADUREIRA', 'TARAUACÁ', 'XAPURI', 'PORTO ACRE']

NTUPLE_AP16 = [Municipio(codigo='1600055.0', nome='SERRA DO NAVIO'), Municipio(codigo='1600105.0', nome='AMAPÁ'),
               Municipio(codigo='1600154.0', nome='PEDRA BRANCA DO AMAPARI'),
               Municipio(codigo='1600204.0', nome='CALÇOENE'), Municipio(codigo='1600212.0', nome='CUTIAS'),
               Municipio(codigo='1600238.0', nome='FERREIRA GOMES'), Municipio(codigo='1600253.0', nome='ITAUBAL'),
               Municipio(codigo='1600279.0', nome='LARANJAL DO JARI'), Municipio(codigo='1600303.0', nome='MACAPÁ'),
               Municipio(codigo='1600402.0', nome='MAZAGÃO'), Municipio(codigo='1600501.0', nome='OIAPOQUE'),
               Municipio(codigo='1600535.0', nome='PORTO GRANDE'), Municipio(codigo='1600550.0', nome='PRACUÚBA'),
               Municipio(codigo='1600600.0', nome='SANTANA'), Municipio(codigo='1600709.0', nome='TARTARUGALZINHO'),
               Municipio(codigo='1600808.0', nome='VITÓRIA DO JARI')]

NTUPLE_AC12 = [Municipio(codigo='1200013.0', nome='ACRELÂNDIA'), Municipio(codigo='1200054.0', nome='ASSIS BRASIL'),
               Municipio(codigo='1200104.0', nome='BRASILÉIA'), Municipio(codigo='1200138.0', nome='BUJARI'),
               Municipio(codigo='1200179.0', nome='CAPIXABA'), Municipio(codigo='1200203.0', nome='CRUZEIRO DO SUL'),
               Municipio(codigo='1200252.0', nome='EPITACIOLÂNDIA'), Municipio(codigo='1200302.0', nome='FEIJÓ'),
               Municipio(codigo='1200328.0', nome='JORDÃO'), Municipio(codigo='1200336.0', nome='MÂNCIO LIMA'),
               Municipio(codigo='1200344.0', nome='MANOEL URBANO'),
               Municipio(codigo='1200351.0', nome='MARECHAL THAUMATURGO'),
               Municipio(codigo='1200385.0', nome='PLÁCIDO DE CASTRO'),
               Municipio(codigo='1200393.0', nome='PORTO WALTER'),
               Municipio(codigo='1200401.0', nome='RIO BRANCO'), Municipio(codigo='1200427.0', nome='RODRIGUES ALVES'),
               Municipio(codigo='1200435.0', nome='SANTA ROSA DO PURUS'),
               Municipio(codigo='1200450.0', nome='SENADOR GUIOMARD'),
               Municipio(codigo='1200500.0', nome='SENA MADUREIRA'), Municipio(codigo='1200609.0', nome='TARAUACÁ'),
               Municipio(codigo='1200708.0', nome='XAPURI'), Municipio(codigo='1200807.0', nome='PORTO ACRE')]

UFS = ['AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MG', 'MS', 'MT', 'PA', 'PB', 'PE', 'PI', 'PR', 'RJ',
       'RN', 'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO']

class test_nt_cidade(unittest.TestCase):
    def test_codigo(self):
        self.assertEqual(ufbr.nt_cidades(codigo='16'), NTUPLE_AP16)
        self.assertEqual(ufbr.nt_cidades(codigo='12'), NTUPLE_AC12)

    def test_sigla(self):
        self.assertEqual(ufbr.nt_cidades('AP'), NTUPLE_AP16)
        self.assertEqual(ufbr.nt_cidades(sigla='AP'), NTUPLE_AP16)
        self.assertEqual(ufbr.nt_cidades('AC'), NTUPLE_AC12)
        self.assertEqual(ufbr.nt_cidades(sigla='AC'), NTUPLE_AC12)

    def test_Inexistente(self):
        self.assertEqual(ufbr.nt_cidades(codigo='999'), 'Inexistente')
        self.assertEqual(ufbr.nt_cidades(), None)


class test_list_cidades(unittest.TestCase):

    def test_None(self):
        self.assertEqual(ufbr.list_cidades(), None)
        self.assertEqual(ufbr.list_cidades(codigo='3412'), 'Inexistente')

    def test_codigo(self):
        self.assertEqual(ufbr.list_cidades(codigo='12'), LISTA_AC12)
        self.assertEqual(ufbr.list_cidades(codigo='16'), LISTA_AP16)

    def test_sigla(self):
        self.assertEqual(ufbr.list_cidades('AC'), LISTA_AC12)
        self.assertEqual(ufbr.list_cidades(sigla='AP'), LISTA_AP16)


class  test_list_UFs(unittest.TestCase):
    def test_list(self):
        self.assertEqual(ufbr.list_uf, UFS)

class  test_UF_dict(unittest.TestCase):
    def test_list(self):
        self.assertEqual(ufbr.dict_uf['AP'], {'codigo': '16', 'nome': 'Amapá'})
        self.assertEqual(ufbr.dict_uf['SP'], {'codigo': '35', 'nome': 'São Paulo'})

class  test_find_cidade(unittest.TestCase):
    def test_None(self):
        self.assertEqual(ufbr.get_cidade(), None)
        self.assertEqual(ufbr.get_cidade('New York'), None)

    def test_sigla(self):
        self.assertEqual(ufbr.get_cidade('São Paulo'), Municipio(codigo='3550308.0', nome='SÃO PAULO'))
        self.assertEqual(ufbr.get_cidade('RIANÁPOLIS'), Municipio(codigo='5218706.0', nome='RIANÁPOLIS'))


unittest.main()

