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

    def __escrevertitulo(self, titulo):
        string = '#################################################################################################\n'
        relatorio = open('Relatorio-' + str(date.today()) + '.txt', 'a')
        relatorio.write(string)
        relatorio.write(titulo + '\n')
        relatorio.write(string)
        relatorio.close()

    def __head(self):
        arquivo = open('Relatorio-' + str(date.today()) + '.txt', 'a')
        arquivo.write('REDE\t\t\t|IMAGENS\t\t|COM PROBLEMA\t\t|SEM PROBLEMA\t\t|CLASSIFICADOS\t\t|NÃO CLASSIFICADOS'
                      '\t\t|VERDADEIRO POSITIVO\t\t|FALSO NEGATIVO\t\t|VERDADEIRO NEGATIVO\t\t|FALSO POSITIVO\t\t'
                      '|ACURÁCIA\n')
        arquivo.close()

    def geral(self):
        self.__escrevertitulo('GERAL')

        self.__head()

        self.__escreverlinhas_g('REFLETIVA\t', refletiva)
        self.__escreverlinhas_g('FLASH\t\t', flash)
        self.__escreverlinhas_g('ENTREPISTA\t', entrepista)
        self.__escreverlinhas_g('CHUVA/NEBLINA', chuv_nebli)
        self.__escreverlinhas_g('IMAGEM FOSCA', fosca)

