"""
@ Author Willian Antunes
@ Built at Vizentec SA
@ 29/05/2020
"""
from classes.class_flash import flash
from classes.class_chuva_neblina import chuv_nebli
from classes.class_refletiva import refletiva
from classes.class_entrepista import entrepista
from classes.class_fosca import fosca
from datetime import date, datetime
from prettytable import PrettyTable
from os import remove
from getpass import getuser


class Relatorio:
    def __init__(self, path):
        self.__path = path
        self.__table = PrettyTable()

        with open('Relatorio-' + str(date.today()) + '.txt', 'w') as relatorio:
            relatorio.write('DATA: ' + str(datetime.now().strftime('%d/%m/%Y')) + '\nRELATÓRIO GERADO AS: '
                            + str(datetime.now().strftime('%H:%M:%S')) + '\nPOR: ' + str(getuser()).upper())

    @staticmethod
    def __escrevertitulo(titulo):
        string = '\n\n------------------------------------------------------------------------------------------------' \
                 '------------------------------------------------------------------------------------------\n'
        with open('Relatorio-' + str(date.today()) + '.txt', 'a') as relatorio:
            relatorio.write(string)
            relatorio.write('# ' + titulo + '\n')

    def __head(self, titulo):
        self.__table.field_names = [titulo, 'IMAGENS', 'COM PROBLEMA', 'SEM PROBLEMA', 'CLASSIFICADOS',
                                    'NÃO CLASSIFICADOS', 'VERDADEIRO POSITIVO', 'FALSO NEGATIVO', 'VERDADEIRO NEGATIVO',
                                    'FALSO POSITIVO', 'ACURÁCIA']

    def __escreverlinhas_g(self, titulo, problema):
        pblm = problema(self.__path)
        t = str(pblm.total_images()['total'])
        p, p_p = pblm.with_problem()['problm']
        sp, sp_p = pblm.with_problem()['noproblm']
        c, c_p = pblm.classification()['classified']
        nc, nc_p = pblm.classification()['noclassified']
        tn, tn_p = pblm.confusion_matrix()['tn']
        fp, fp_p = pblm.confusion_matrix()['fp']
        fn, fn_p = pblm.confusion_matrix()['fn']
        tp, tp_p = pblm.confusion_matrix()['tp']
        acc = pblm.confusion_matrix()['acc']

        self.__table.add_row([titulo, t, str(p) + ' (' + str(p_p) + '%)', str(sp) + ' (' + str(sp_p) + '%)',
                              str(c) + ' (' + str(c_p) + '%)', str(nc) + ' (' + str(nc_p) + '%)',
                              str(tp) + ' (' + str(tp_p) + '%)',
                              str(fn) + ' (' + str(fn_p) + '%)', str(tn) + ' (' + str(tn_p) + '%)',
                              str(fp) + ' (' + str(fp_p) + '%)', str(acc) + '%'])

    def __escreverlinhas_v(self, titulo, problema, coluna):
        pblm = problema(self.__path)
        t = str(pblm.general(coluna)['total'])
        p, p_p = pblm.general(coluna)['problm']
        sp, sp_p = pblm.general(coluna)['noproblm']
        c, c_p = pblm.general(coluna)['classified']
        nc, nc_p = pblm.general(coluna)['noclassified']
        tn, tn_p = pblm.general(coluna)['tn']
        fp, fp_p = pblm.general(coluna)['fp']
        fn, fn_p = pblm.general(coluna)['fn']
        tp, tp_p = pblm.general(coluna)['tp']
        acc = pblm.general(coluna)['acc']

        self.__table.add_row([titulo, t, str(p) + ' (' + str(p_p) + '%)', str(sp) + ' (' + str(sp_p) + '%)',
                              str(c) + ' (' + str(c_p) + '%)', str(nc) + ' (' + str(nc_p) + '%)',
                              str(tp) + ' (' + str(tp_p) + '%)',
                              str(fn) + ' (' + str(fn_p) + '%)', str(tn) + ' (' + str(tn_p) + '%)',
                              str(fp) + ' (' + str(fp_p) + '%)', str(acc) + '%'])

    def __escreverlinhas_p(self, titulo, problema, coluna):
        pblm = problema(self.__path)
        t = str(pblm.general(coluna)['total'])
        p, p_p = pblm.general(coluna)['problm']
        sp, sp_p = pblm.general(coluna)['noproblm']
        c, c_p = pblm.general(coluna)['classified']
        nc, nc_p = pblm.general(coluna)['noclassified']
        tn, tn_p = pblm.general(coluna)['tn']
        fp, fp_p = pblm.general(coluna)['fp']
        fn, fn_p = pblm.general(coluna)['fn']
        tp, tp_p = pblm.general(coluna)['tp']
        acc = pblm.general(coluna)['acc']

        self.__table.add_row([titulo, t, str(p) + ' (' + str(p_p) + '%)', str(sp) + ' (' + str(sp_p) + '%)',
                              str(c) + ' (' + str(c_p) + '%)', str(nc) + ' (' + str(nc_p) + '%)',
                              str(tp) + ' (' + str(tp_p) + '%)',
                              str(fn) + ' (' + str(fn_p) + '%)', str(tn) + ' (' + str(tn_p) + '%)',
                              str(fp) + ' (' + str(fp_p) + '%)', str(acc) + '%'])

    def __escreverlinhas_vp(self, titulo, problema, *colunas):
        coluna1 = colunas[0]
        coluna2 = colunas[1]
        pblm = problema(self.__path)
        t = str(pblm.general(coluna1, coluna2)['total'])
        p, p_p = pblm.general(coluna1, coluna2)['problm']
        sp, sp_p = pblm.general(coluna1, coluna2)['noproblm']
        c, c_p = pblm.general(coluna1, coluna2)['classified']
        nc, nc_p = pblm.general(coluna1, coluna2)['noclassified']
        tn, tn_p = pblm.general(coluna1, coluna2)['tn']
        fp, fp_p = pblm.general(coluna1, coluna2)['fp']
        fn, fn_p = pblm.general(coluna1, coluna2)['fn']
        tp, tp_p = pblm.general(coluna1, coluna2)['tp']
        acc = pblm.general(coluna1)['acc']

        self.__table.add_row([titulo, t, str(p) + ' (' + str(p_p) + '%)', str(sp) + ' (' + str(sp_p) + '%)',
                              str(c) + ' (' + str(c_p) + '%)', str(nc) + ' (' + str(nc_p) + '%)',
                              str(tp) + ' (' + str(tp_p) + '%)',
                              str(fn) + ' (' + str(fn_p) + '%)', str(tn) + ' (' + str(tn_p) + '%)',
                              str(fp) + ' (' + str(fp_p) + '%)', str(acc) + '%'])

    def __geral(self):
        self.__escrevertitulo('GERAL')
        self.__table.clear_rows()
        self.__head('REDE')

        self.__escreverlinhas_g('REFLETIVA', refletiva)
        self.__escreverlinhas_g('FLASH', flash)
        self.__escreverlinhas_g('ENTREPISTA', entrepista)
        self.__escreverlinhas_g('CHUVA / NEBLINA', chuv_nebli)
        self.__escreverlinhas_g('IMAGEM FOSCA', fosca)

        with open('Relatorio-' + str(date.today()) + '.txt', 'a') as arquivo:
            arquivo.write(str(self.__table))

    def __prob_veic(self, *args):
        self.__escrevertitulo(args[0])
        self.__table.clear_rows()
        self.__head(args[1])
        self.__escreverlinhas_v('Moto', args[2], 'V moto')
        self.__escreverlinhas_v('Carro', args[2], 'V car')
        self.__escreverlinhas_v('Caminhão', args[2], 'V cami')
        self.__escreverlinhas_v('Ônibus', args[2], 'V oni')
        self.__escreverlinhas_v('Outro Tipo', args[2], 'V outro')
        with open('Relatorio-' + str(date.today()) + '.txt', 'a') as arquivo:
            arquivo.write(str(self.__table))

    def __prob_prob(self, *args):
        self.__escrevertitulo(args[0])
        self.__table.clear_rows()
        self.__head(args[1])
        self.__escreverlinhas_p('Chuva / Neblina', args[2], 'L chu neb')
        self.__escreverlinhas_p('Imagem Fosca', args[2], 'L Fosca')
        self.__escreverlinhas_p('Flash / Problema', args[2], 'L flash n')
        self.__escreverlinhas_p('Refletiva / Sol', args[2], 'L refle sol')
        self.__escreverlinhas_p('Refletiva / Flash', args[2], 'L refle flash')
        self.__escreverlinhas_p('Autuadas', args[2], 'L sem')
        with open('Relatorio-' + str(date.today()) + '.txt', 'a') as arquivo:
            arquivo.write(str(self.__table))

    def __prob_veic_prob(self, *args):
        self.__escrevertitulo(args[0])
        self.__table.clear_rows()
        self.__head(args[1])
        self.__escreverlinhas_vp('Chuva / Neblina - Moto', args[2], 'V moto', 'L chu neb')
        self.__escreverlinhas_vp('Chuva / Neblina - Carro', args[2], 'V car', 'L chu neb')
        self.__escreverlinhas_vp('Chuva / Neblina - Caminhão', args[2], 'V cami', 'L chu neb')
        self.__escreverlinhas_vp('Chuva / Neblina - Onibus', args[2], 'V oni', 'L chu neb')
        self.__escreverlinhas_vp('Chuva / Neblina - Outro', args[2], 'V outro', 'L chu neb')
        # Imagem fosca
        self.__escreverlinhas_vp('Imagem Fosca - Moto', args[2], 'V moto', 'L Fosca')
        self.__escreverlinhas_vp('Imagem Fosca - Carro', args[2], 'V car', 'L Fosca')
        self.__escreverlinhas_vp('Imagem Fosca - Caminhão', args[2], 'V cami', 'L Fosca')
        self.__escreverlinhas_vp('Imagem Fosca - Onibus', args[2], 'V oni', 'L Fosca')
        self.__escreverlinhas_vp('Imagem Fosca - Outro', args[2], 'V outro', 'L Fosca')
        # Flash / Problema
        self.__escreverlinhas_vp('Flash / Problema - Moto', args[2], 'V moto', 'L flash n')
        self.__escreverlinhas_vp('Flash / Problema - Carro', args[2], 'V car', 'L flash n')
        self.__escreverlinhas_vp('Flash / Problema - Caminhão', args[2], 'V cami', 'L flash n')
        self.__escreverlinhas_vp('Flash / Problema - Onibus', args[2], 'V oni', 'L flash n')
        self.__escreverlinhas_vp('Flash / Problema -  Outro', args[2], 'V outro', 'L flash n')
        # Refletiva / Sol
        self.__escreverlinhas_vp('Refletiva / Sol - Moto', args[2], 'V moto', 'L refle sol')
        self.__escreverlinhas_vp('Refletiva / Sol - Carro', args[2], 'V car', 'L refle sol')
        self.__escreverlinhas_vp('Refletiva / Sol - Caminhão', args[2], 'V cami', 'L refle sol')
        self.__escreverlinhas_vp('Refletiva / Sol - Onibus', args[2], 'V oni', 'L refle sol')
        self.__escreverlinhas_vp('Refletiva / Sol - Outro', args[2], 'V outro', 'L refle sol')
        # Refletiva / Flash
        self.__escreverlinhas_vp('Refletiva / Flash - Moto', args[2], 'V moto', 'L refle sol')
        self.__escreverlinhas_vp('Refletiva / Flash - Carro', args[2], 'V car', 'L refle sol')
        self.__escreverlinhas_vp('Refletiva / Flash - Caminhão', args[2], 'V cami', 'L refle sol')
        self.__escreverlinhas_vp('Refletiva / Flash - Onibus', args[2], 'V oni', 'L refle sol')
        self.__escreverlinhas_vp('Refletiva / Flash - Outro', args[2], 'V outro', 'L refle sol')
        # Autuadas
        self.__escreverlinhas_vp('Autuada - Moto', args[2], 'V moto', 'L sem')
        self.__escreverlinhas_vp('Autuada - Carro', args[2], 'V car', 'L sem')
        self.__escreverlinhas_vp('Autuada - Caminhão', args[2], 'V cami', 'L sem')
        self.__escreverlinhas_vp('Autuada - Onibus', args[2], 'V oni', 'L sem')
        self.__escreverlinhas_vp('Autuada - Outro', args[2], 'V outro', 'L sem')

        with open('Relatorio-' + str(date.today()) + '.txt', 'a') as arquivo:
            arquivo.write(str(self.__table))

    def relatorio_completo(self):

            self.__geral()
            self.__prob_veic('ENTREPISTA POR VEICULO', 'VEICULO', entrepista)
            self.__prob_prob('ENTREPISTA POR PROBLEMA', 'PROBLEMA', entrepista)
            self.__prob_veic_prob('ENTREPISTA POR VEÍCULO E PROBLEMA', 'PROBLEMA / VEICULO', entrepista)

            self.__prob_veic('FLASH POR VEICULO', 'VEICULO', flash)
            self.__prob_prob('FLASH POR PROBLEMA', 'PROBLEMA', flash)
            self.__prob_veic_prob('FLASH POR VEÍCULO E PROBLEMA', 'PROBLEMA / VEICULO', flash)

            self.__prob_veic('FLASH POR VEICULO', 'VEICULO', fosca)
            self.__prob_prob('FLASH POR PROBLEMA', 'PROBLEMA', flash)
            self.__prob_veic_prob('FLASH POR VEÍCULO E PROBLEMA', 'PROBLEMA / VEICULO', fosca)

            self.__prob_veic('FLASH POR VEICULO', 'VEICULO', refletiva)
            self.__prob_prob('FLASH POR PROBLEMA', 'PROBLEMA', refletiva)
            self.__prob_veic_prob('FLASH POR VEÍCULO E PROBLEMA', 'PROBLEMA / VEICULO', refletiva)

            self.__prob_veic('FLASH POR VEICULO', 'VEICULO', chuv_nebli)
            self.__prob_prob('FLASH POR PROBLEMA', 'PROBLEMA', chuv_nebli)
            self.__prob_veic_prob('FLASH POR VEÍCULO E PROBLEMA', 'PROBLEMA / VEICULO', chuv_nebli)
