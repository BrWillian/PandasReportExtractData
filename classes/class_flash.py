"""
@ Author Willian Antunes
@ Built at Vizentec SA
@ 29/05/2020
"""
from sklearn.metrics import confusion_matrix
from classes.class_master import master


class flash(master):
    def __init__(self, data):
        super().__init__(data)

    def with_problem(self, data=None):
        data_problem = data

        try:
            label = data_problem['M FLASH']
        except:
            label = self._data['M FLASH']

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

        data_problem = data

        try:
            label = data_problem['L flash n']
        except:
            label = self._data['L flash n']

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
            data = data[['M FLASH', 'L flash n']]
        except:
            data = self._data[['M FLASH', 'L flash n']]

        y_true = list(data['M FLASH'])
        y_pred = list(data['L flash n'])
        tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()

        positivos = data[data['L flash n'] == True]
        negativos = data[data['L flash n'] == False]

        total = len(data)
        totalp = len(positivos)
        totaln = len(negativos)

        result = {
            'tn': [tn, round(tn * 100 / totaln, 2)],
            'fp': [fp, round(fp * 100 / totalp, 2)],
            'fn': [fn, round(fn * 100 / totaln, 2)],
            'tp': [tp, round(tp * 100 / totalp, 2)],
            'acc': round((tp + tn) / total * 100, 2)
        }

        return result
