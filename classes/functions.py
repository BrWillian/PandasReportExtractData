"""
@ Author Willian Antunes
@ Built at Vizentec SA
@ 29/05/2020
"""
import pandas as pd


def merge_or(data, new_column_name='new_column', *column):
	data_problem = pd.DataFrame(data)
	data_problem[new_column_name] = (data_problem[column[0]] | data_problem[column[1]])
	return data


def merge_and(data, new_column_name='new_column', *column):
	data_problem = pd.DataFrame(data)
	data_problem[new_column_name] = (data_problem[column[0]] & data_problem[column[1]])
	return data