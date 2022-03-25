
import pandas as pd
from settings import d, senado_files


def xls2pkl():
    for s in senado_files:
        print('Reading senado ' + str(s))
        file = d + '/votes_analysis/data/excel/senado/senado%s.xlsx' % (s)
        data = pd.read_excel(file, index_col=0, engine="openpyxl")
        data.to_pickle(d + '/votes_analysis/data/pickle/senado/senado%s.pkl' % (s))


if __name__ == '__main__':
    xls2pkl()