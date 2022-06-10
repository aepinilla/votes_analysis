from functools import reduce
import pandas as pd

from read_data import read_data
from helper import join_repeated_columns, filter_relevant_columns
from settings import base_columns, d, new_names_dict, repeated_cols_dict, year


def clean_data():
    senado_df = read_data()
    base_data = senado_df[base_columns]
    base_data['entry_code'] =  list(range(len(senado_df)))

    clean_dfs = []
    for feature in repeated_cols_dict:
        print('Consolidando %s' % (feature))
        df = join_repeated_columns(senado_df, new_names_dict=new_names_dict, repeated_cols_dict=repeated_cols_dict, feature=feature)
        clean_dfs.append(df)

    features = reduce(lambda left, right: pd.merge(left, right, on=['entry_code'], how='outer'), clean_dfs)
    all_data = base_data.merge(features, on=['entry_code'], how='outer')
    all_data.to_pickle(d + '/analisis_votos/data/senado%s/all_data_senado.pkl' % (year))


if __name__ == '__main__':
    clean_data()