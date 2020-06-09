"""
@ Author Willian Antunes
@ Built at Vizentec SA
@ 29/05/2020
"""
import pandas as pd
import warnings

warnings.simplefilter(action="ignore", category=RuntimeWarning)


class master:
    def __init__(self, data):
        self._data = pd.read_csv(data)
        self._data = pd.DataFrame(self._data)

    @staticmethod
    def merge_or(data, new_column_name='new_column', *column):
        data_problem = pd.DataFrame(data)
        data_problem[new_column_name] = (data_problem[column[0]] | data_problem[column[1]])
        return data

    @staticmethod
    def merge_and(data, new_column_name='new_column', *column):
        data_problem = pd.DataFrame(data)
        data_problem[new_column_name] = (data_problem[column[0]] & data_problem[column[1]])
        return data

    def total_images(self, data=None):
        try:
            total = len(data['Nome do Arquivo'])
        except:
            total = len(self._data['Nome do Arquivo'])

        result = {
            'total': total
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

    def with_problem(self, data):
        return {}

    def classification(self, data):
        return {}

    def confusion_matrix(self, data):
        return {}