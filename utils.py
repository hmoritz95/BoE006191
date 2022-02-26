import pandas as pd


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
    return data_general, data_underwritings