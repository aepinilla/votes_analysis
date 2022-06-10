
import pandas as pd
from settings import d, senado_files, year, corporacion



def xls2pkl(corporacion):
    for s in senado_files:
        print('Convirtiendo datos a formato PKL: ' + corporacion + str(year) + '-' + str(s))
        file = d + '/analisis_votos/data/senado%s/senado%s-%s.xlsx' % (year, year, s)
        data = pd.read_excel(file, index_col=0, engine="openpyxl")
        data.to_pickle(d + '/analisis_votos/data/senado%s/senado%s-%s.pkl' % (year, year, s))


if __name__ == '__main__':
    xls2pkl()