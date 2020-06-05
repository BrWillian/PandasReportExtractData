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
from datetime import date


class Relatorio:
    def __init__(self, path):
        self.__path = path

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

        arquivo = open('Relatorio-' + str(date.today()) + '.txt', 'a')

        arquivo.write('{titulo}\t|{t}\t\t\t|{p} ({p_p}%)\t\t|{np} ({np_p}%)\t\t|{c} ({c_p}%)\t\t'
                      '| {nc} ({nc_p}%)\t\t|{tp} ({tp_p}%)\t\t\t\t|{fn} ({fn_p}%)\t\t|{tn} ({tn_p}%)\t\t\t\t|{fp} '
                      '({fp_p}%)\t\t|{acc}%\n'.format(titulo=titulo, t=t, p=p, p_p=p_p, np=sp, np_p=sp_p, c=c,
                                                      c_p=c_p,
                                                      nc=nc, nc_p=nc_p,
                                                      tp=tp, tp_p=tp_p, fn=fn, fn_p=fn_p, tn=tn, tn_p=tn_p,
                                                      fp=fp, fp_p=fp_p, acc=acc))
        arquivo.close()

    @staticmethod
    def __escrevertitulo(titulo):
        string = '#################################################################################################\n'
        relatorio = open('Relatorio-' + str(date.today()) + '.txt', 'a')
        relatorio.write(string)
        relatorio.write(titulo + '\n')
        relatorio.write(string)
        relatorio.close()

    @staticmethod
    def __head():
        arquivo = open('Relatorio-' + str(date.today()) + '.txt', 'a')
        arquivo.write('REDE\t\t\t|IMAGENS\t\t|COM PROBLEMA\t\t|SEM PROBLEMA\t\t|CLASSIFICADOS\t\t|NÃO CLASSIFICADOS'
                      '\t\t|VERDADEIRO POSITIVO\t\t|FALSO NEGATIVO\t\t|VERDADEIRO NEGATIVO\t\t|FALSO POSITIVO\t\t'
                      '|ACURÁCIA\n')
        arquivo.close()

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

        arquivo = open('Relatorio-' + str(date.today()) + '.txt', 'a')

        arquivo.write('{titulo}\t\t|{t}\t\t\t|{p} ({p_p}%)\t\t|{np} ({np_p}%)\t\t|{c} ({c_p}%)\t\t'
                      '| {nc} ({nc_p}%)\t\t\t|{tp} ({tp_p}%)\t\t\t\t|{fn} ({fn_p}%)\t\t|{tn} ({tn_p}%)\t\t\t\t|{fp} '
                      '({fp_p}%) \t\t|{acc}%\n'.format(titulo=titulo, t=t, p=p, p_p=p_p, np=sp, np_p=sp_p, c=c,
                                                      c_p=c_p,
                                                      nc=nc, nc_p=nc_p,
                                                      tp=tp, tp_p=tp_p, fn=fn, fn_p=fn_p, tn=tn, tn_p=tn_p,
                                                      fp=fp, fp_p=fp_p, acc=acc))
        arquivo.close()

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

        arquivo = open('Relatorio-' + str(date.today()) + '.txt', 'a')

        arquivo.write('{titulo}\t|{t}\t\t\t|{p} ({p_p}%)\t\t\t|{np} ({np_p}%)\t\t|{c} ({c_p}%) \t\t'
                      '|{nc} ({nc_p}%)\t\t\t|{tp} ({tp_p}%)\t\t\t\t\t|{fn} ({fn_p}%) \t\t|{tn} ({tn_p}%)\t\t\t\t|{fp} '
                      '({fp_p}%)  \t\t|{acc}%\n'.format(titulo=titulo, t=t, p=p, p_p=p_p, np=sp, np_p=sp_p, c=c,
                                                       c_p=c_p,
                                                       nc=nc, nc_p=nc_p,
                                                       tp=tp, tp_p=tp_p, fn=fn, fn_p=fn_p, tn=tn, tn_p=tn_p,
                                                       fp=fp, fp_p=fp_p, acc=acc))
        arquivo.close()

    def geral(self):
        self.__escrevertitulo('GERAL')

        self.__head()

        self.__escreverlinhas_g('REFLETIVA\t', refletiva)
        self.__escreverlinhas_g('FLASH\t\t', flash)
        self.__escreverlinhas_g('ENTREPISTA\t', entrepista)
        self.__escreverlinhas_g('CHUVA/NEBLINA', chuv_nebli)
        self.__escreverlinhas_g('IMAGEM FOSCA', fosca)

    def entrepista_veiculo(self):
        self.__escrevertitulo('ENTREPISTA POR VEICULO')
        self.__head()
        self.__escreverlinhas_v('Moto\t', entrepista, 'V moto')
        self.__escreverlinhas_v('Carro\t', entrepista, 'V car')
        self.__escreverlinhas_v('Caminhão', entrepista, 'V cami')
        self.__escreverlinhas_v('Ônibus\t', entrepista, 'V oni')
        self.__escreverlinhas_v('Outro Tipo', entrepista, 'V outro')

    def entrepista_problema(self):
        self.__escrevertitulo('ENTREPISTA POR PROBLEMA')
        self.__head()
        self.__escreverlinhas_p('Chuva/Neblina', entrepista, 'L chu neb')
        self.__escreverlinhas_p('Imagem Fosca', entrepista, 'L Fosca')
        self.__escreverlinhas_p('Flash Problema', entrepista, 'L flash n')
        self.__escreverlinhas_p('Refletiva Sol', entrepista, 'L refle sol')
        self.__escreverlinhas_p('Refletiva Flash', entrepista, 'L refle flash')
        self.__escreverlinhas_p('Autuadas\t', entrepista, 'L sem')




