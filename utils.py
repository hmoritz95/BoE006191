import pandas as pd
import numpy as np


def import_data(path):
    """
    This function is intended to read in the excel file and to clean it up
    :param path: string, the filepath
    :return: pd.DataFrame, stacked with Year, Metric
    """
    data_general = pd.read_excel(path, index_col=0, header=[0, 1], sheet_name='Dataset 1 - General')
    data_general.index.names = ['Company']
    data_general.columns.names = ['Metrics', 'Year']
    data_general = data_general.unstack(level=1)
    data_general = data_general.unstack(level='Metrics')
    data_general = data_general.sort_index(level='Year')

    data_underwritings = pd.read_excel(path, index_col=0, header=[0, 1], sheet_name='Dataset 2 - Underwriting')
    data_underwritings.index.names = ['Company']
    data_underwritings.columns.names = ['Metrics', 'Year']
    data_underwritings = data_underwritings.unstack(level=1)
    data_underwritings = data_underwritings.unstack(level='Metrics')
    data_underwritings = data_underwritings.sort_index(level='Year')
    return data_general.replace(0, 0.01), data_underwritings.replace(0, 0.01)


def clean_values(data, replacing_values):
    """
    This function aims to cleanup the data based on certain conditions and returning the cleaned data afterwards
    :param data: pd.DataFrame, the original data
    :param replacing_values: dict, the dictionary with the columns as keys and the checking value as value with the first one being < | >
    :return: pd.DataFrame, returns the cleaned up data frame object
    """
    for i in replacing_values:
        correction_term = replacing_values[i] #correction_term[2:]

        if correction_term[1] == '<':
            # choosing here the "biased" mean on purpose to keep at least the directions of the all-in values
            temp = data[data[i] <= float(correction_term[1:])]
            temp[i] = np.mean(data[i])
            data.loc[temp.index, temp.columns] = temp
        else:
            # choosing here the "biased" mean on purpose to keep at least the directions of the all-in values
            temp = data[data[i] >= float(correction_term[1:])]
            temp[i] = np.mean(data[i])
            data.loc[temp.index, temp.columns] = temp
        del temp

    return data
