"""
@ Author Willian Antunes
@ Built at Vizentec SA
@ 29/05/2020
"""
import pandas as pd
from sklearn.metrics import confusion_matrix


class entrepista:
    def __init__(self, data):
        self._data = pd.read_csv(data)
        self._data = pd.DataFrame(self._data)

    def total_images(self, data=None):
        try:
            total = len(data['Nome do Arquivo'])
        except:
            total = len(self._data['Nome do Arquivo'])

        result = {
            'total': total
        }

        return result

    def with_problem(self, data=None):
        data_problem = data

        try:
            label = data_problem['L entre']
        except:
            label = self._data['L entre']

        list_no_prob = list(filter(lambda x: not x, label))
        list_prob = list(filter(lambda x: x, label))

        percent_prob = round(len(list_prob) * 100 / len(label), 2)
        percent_not_prob = round(len(list_no_prob) * 100 / len(label), 2)

        result = {
            'problm': [len(list_prob), percent_prob],
            'noproblm': [len(list_no_prob), percent_not_prob]
        }

        return result

    def classification(self, data=None):

        data_classification = data

        try:
            label = data_classification['M ENTRE']
        except:
            label = self._data['M ENTRE']

        list_no_prob = list(filter(lambda x: not x, label))
        list_prob = list(filter(lambda x: x, label))

        percent_prob = round(len(list_prob) * 100 / len(label), 2)
        percent_not_prob = round(len(list_no_prob) * 100 / len(label), 2)

        result = {
            'classified': [len(list_prob), percent_prob],
            'noclassified': [len(list_no_prob), percent_not_prob]
        }

        return result

    def confusion_matrix(self, data=None):

        try:
            data = data[['M ENTRE', 'L entre']]
        except:
            data = self._data[['M ENTRE', 'L entre']]

        y_true = list(data['M ENTRE'])
        y_pred = list(data['L entre'])
        tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()

        total = len(data)

        result = {
            'tn': [tn, round(tn * 100 / total, 2)],
            'fp': [fp, round(fp * 100 / total, 2)],
            'fn': [fn, round(fn * 100 / total, 2)],
            'tp': [tp, round(tp * 100 / total, 2)],
            'acc': round((tp + tn) / total * 100, 2)
        }

        return result

    def general(self, *columns):
        data = self._data
        if len(columns) < 2:
            data = data[(data[columns[0]] == True)]
        else:
            data = data[(data[columns[0]] == True) & (data[columns[1]] == True)]

        total = self.total_images(data)

        with_problem = self.with_problem(data)

        classification = self.classification(data)

        confusion_matrix = self.confusion_matrix(data)

        result = dict()

        result.update(total.items())
        result.update(with_problem.items())
        result.update(classification.items())
        result.update(confusion_matrix.items())

        return result
