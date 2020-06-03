"""
@ Author Willian Antunes
@ Built at Vizentec SA
@ 29/05/2020
"""
import pandas as pd
from sklearn.metrics import confusion_matrix
from classes.functions import merge_and, merge_or


class chuv_nebli:
    def __init__(self, data):
        self._data = pd.read_csv(data)
        self._data = pd.DataFrame(self._data)
        self._keys = self._data.keys()
        self._total = 0

        """
        self._keys
            0: 'Nome do Arquivo', 1: 'M CHUVA', 2: 'M FLASH', 3: 'M ENTRE', 4: 'M REFLE',
            5: 'M NEBLI', 6: 'M FOSCA', 7: 'L chu neb', 8: 'L entre', 9: 'L erro detec',
            10: 'L flash n', 11: 'L Fosca', 12: 'L encob', 13: 'L refle flash', 14: 'L refle sol',
            15: 'L sem', 16: 'P dia', 17: 'P noite', 18: 'C front', 19: 'C lat', 20: 'C tras', 21: 'V cami',
            22: 'V car', 23: 'V moto', 24: 'V outro', 25: 'V oni', 26: 'O amb', 27: 'O bomb', 28: 'O pol',
            29: 'L descart', 30: 'L duvida', 31: 'ANTT', 32: 'GOINFRA'
        """

    def total_images(self, key=0):
        self._total = len(self._data[self._keys[key]])
        return self._total

    def with_problem(self):
        data = self._data

        label = data['L chu neb']
        list_no_prob = list(filter(lambda x: not x, label))
        list_prob = list(filter(lambda x: x, label))

        percent_prob = round(len(list_prob) * 100 / len(label), 2)
        percent_not_prob = round(len(list_no_prob) * 100 / len(label), 2)

        result = {
            'problm': [len(list_prob), percent_prob],
            'noproblm': [len(list_no_prob), percent_not_prob]
        }

        return result

    def classification(self):
        data = merge_or(self._data, 'M CHUV NEB', 'M CHUVA', 'M NEBLI')
        label = self._data['M CHUV NEB']

        list_no_prob = list(filter(lambda x: not x, label))
        list_prob = list(filter(lambda x: x, label))

        percent_prob = round(len(list_prob) * 100 / len(label), 2)
        percent_not_prob = round(len(list_no_prob) * 100 / len(label), 2)

        result = {
            'classicfied': [len(list_prob), percent_prob],
            'noclassified': [len(list_no_prob), percent_not_prob]
        }

        return result

    def confusion_matrix(self):

        data = merge_or(self._data, 'M CHUV NEB', 'M CHUVA', 'M NEBLI')
        data = data[['M CHUV NEB', 'L chu neb']]
        y_true = list(data['M CHUV NEB'])
        y_pred = list(data['L chu neb'])
        tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()

        result = {
            'tn': [tn, round(tn * 100 / self.total_images(), 2)],
            'fp': [fp, round(fp * 100 / self.total_images(), 2)],
            'fn': [fn, round(fn * 100 / self.total_images(), 2)],
            'tp': [tp, round(tp * 100 / self.total_images(), 2)],
            'acc': round((tp + tn) / self.total_images() * 100, 2)
        }

        return result
