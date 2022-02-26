import pandas as pd


def import_data(path):
    """
    This function is intended to read in the excel file and to clean it up
    :param path: string, the filepath
    :return: pd.DataFrame, stacked with Year, Metric
    """
    data = pd.read_excel(path, index_col=0, header=[0, 1])
    data.index.names = ['Company']
    data.columns.names = ['Metrics', 'Year']
    data = data.unstack(level=1)
    data = data.unstack(level='Metrics')
    data = data.sort_index(level='Year')
    return data