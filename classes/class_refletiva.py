"""
@ Author Willian Antunes
@ Built at Vizentec SA
@ 29/05/2020
"""
from sklearn.metrics import confusion_matrix
from classes.functions import merge_or
from classes.class_master import master


class refletiva(master):
    def __init__(self, data):
        super().__init__(data)

    def with_problem(self, data=None):
        data_problem = data

        try:
            data_problem = merge_or(data_problem, 'L refle', 'L refle flash', 'L refle sol')
            label = data_problem['L refle']
        except:
            data = merge_or(self._data, 'L refle', 'L refle flash', 'L refle sol')
            label = self._data['L refle']

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
            label = data_classification['M REFLE']
        except:
            label = self._data['M REFLE']

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
        data_problem = data

        try:
            data_problem = merge_or(data_problem, 'L refle', 'L refle flash', 'L refle sol')
            data = data_problem[['M REFLE', 'L refle']]
        except:
            data_problem = merge_or(self._data, 'L refle', 'L refle flash', 'L refle sol')
            data = data_problem[['M REFLE', 'L refle']]

        y_true = list(data['M REFLE'])
        y_pred = list(data['L refle'])
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