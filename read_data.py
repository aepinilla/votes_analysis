
import os
import pandas as pd

senado_files = list(range(1,7))
d = os.path.dirname(os.getcwd())

def read_data():
    for s in senado_files:
        print('Reading senado ' + str(s))
        file = d + '/votes_analysis/data/excel/senado/senado%s.xlsx' % (s)
        data = pd.read_excel(file, index_col=0, engine="openpyxl")
        data.to_pickle(d + '/votes_analysis/data/pickle/senado/senado1.pkl')
        # unpickled_df = pd.read_pickle(d + '/votes_analysis/data/pickle/senado/senado1.pkl')


if __name__ == '__main__':
    read_data()