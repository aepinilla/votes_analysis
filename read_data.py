
import pandas as pd
from settings import d, senado_files


def read_data():
    senado = []
    for s in senado_files:
        print('Reading senado ' + str(s))
        file = d + '/votes_analysis/data/excel/senado/senado%s.xlsx' % (s)
        data = pd.read_pickle(d + '/votes_analysis/data/pickle/senado/senado%s.pkl' % (s))
        senado.append(data)

    senado_df = pd.concat(senado)
    return senado_df


if __name__ == '__main__':
    read_data()