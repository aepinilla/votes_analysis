
import pandas as pd
from settings import d, senado_files, year, corporacion


def read_data():
    senado = []
    for s in senado_files:
        # print('Leyendo registro de votaciones al Senado')
        print('Leyendo datos de ' + corporacion + str(year) + '-' + str(s))
        data = pd.read_pickle(d + '/analisis_votos/data/senado%s/senado%s-%s.pkl' % (year, year, s))
        senado.append(data)

    senado_df = pd.concat(senado)
    return senado_df


if __name__ == '__main__':
    read_data()