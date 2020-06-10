"""
@ Author Willian Antunes
@ Built at Vizentec SA
@ 29/05/2020
"""
from sklearn.metrics import confusion_matrix
from classes.class_master import master


class chuv_nebli(master):
    def __init__(self, data):
        super().__init__(data)

    def with_problem(self, data=None):
        data_problem = data

        try:
            data_problem = self.merge_or(data_problem, 'M CHUV NEB', 'M CHUVA', 'M NEBLI')
            label = data_problem['M CHUV NEB']
        except:
            data_problem = self.merge_or(self._data, 'M CHUV NEB', 'M CHUVA', 'M NEBLI')
            label = data_problem['M CHUV NEB']

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
            label = data_problem['L chu neb']
        except:
            label = self._data['L chu neb']

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
            data_problem = self.merge_or(data_problem, 'M CHUV NEB', 'M CHUVA', 'M NEBLI')
            data = data_problem[['M CHUV NEB', 'L chu neb']]
        except:
            data_problem = self.merge_or(self._data, 'M CHUV NEB', 'M CHUVA', 'M NEBLI')
            data = data_problem[['M CHUV NEB', 'L chu neb']]

        y_true = list(data['M CHUV NEB'])
        y_pred = list(data['L chu neb'])
        tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()

        positivos = data[data['L chu neb'] == True]
        negativos = data[data['L chu neb'] == False]

        total = len(data)
        totalp = len(positivos)
        totaln = len(negativos)

        if totalp == 0:
            fp_p = 0.0
            tp_p = 0.0
        else:
            fp_p = round(fp * 100 / totalp, 2)
            tp_p = round(tp * 100 / totalp, 2)

        if totaln == 0:
            fn_p = 0.0
            tn_p = 0.0
        else:
            fn_p = round(fn * 100 / totaln, 2)
            tn_p = round(tn * 100 / totaln, 2)
        result = {
            'tn': [tn, tn_p],
            'fp': [fp, fp_p],
            'fn': [fn, fn_p],
            'tp': [tp, tp_p],
            'acc': round((tp + tn) / total * 100, 2)
        }

        return result