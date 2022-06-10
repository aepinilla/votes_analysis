import functools
import numpy as np
import pandas as pd

from settings import incomplete_columns, base_columns


def non_nan_columns(x):
    number_nans = {}
    for col in x.columns:
        nnan = x[col].isna().sum()
        number_nans[col] = nnan

    # Columns without missing values
    no_nan = []
    for k in number_nans:
        if number_nans[k] == 0:
            no_nan.append(k)

    return no_nan


def filter_relevant_columns(df, repeated_cols_dict, feature=''):
    # To increase processing speed, drop all repeated columns, except the ones that are relevant for the selected feature
    all_repeated_columns = sum(repeated_cols_dict.values(), [])
    for col in repeated_cols_dict[feature]:
        all_repeated_columns.remove(col)
    df = df.drop(all_repeated_columns, axis=1)
    df = df.drop(incomplete_columns, axis=1)
    df = df.drop(base_columns, axis=1)
    df['entry_code'] = list(range(len(df)))
    filtered_df = df.reset_index(drop=True)

    return filtered_df


def build_masks(df, repeated_cols_dict, feature=''):
    masks_list = []
    masks_dict = {}
    df = df.reset_index(drop=True)
    df_index = list(range(len(df)))
    for col in repeated_cols_dict[feature]:
        this_col = df[col]
        missing_values = np.where(this_col.isna())
        is_missing_mask = np.isin(df_index, missing_values)
        masks_list.append(is_missing_mask)
        masks_dict[col]=is_missing_mask

    # If mask value is equal in all masks, then it is missing in all columns, because values exist in only one column at a time
    if len(masks_list) == 2:
        a = masks_list[0]
        b = masks_list[1]
        mask_all_nans = np.where((a == b))
    if len(masks_list) == 3:
        a = masks_list[0]
        b = masks_list[1]
        c = masks_list[2]
        mask_all_nans = np.where((a == b) & (b == c))
    if len(masks_list) == 4:
        a = masks_list[0]
        b = masks_list[1]
        c = masks_list[2]
        d = masks_list[3]
        mask_all_nans = np.where((a == b) & (b == c) & (c == d))
    if len(masks_list) == 5:
        a = masks_list[0]
        b = masks_list[1]
        c = masks_list[2]
        d = masks_list[3]
        e = masks_list[4]
        mask_all_nans = np.where((a == b) & (b == c) & (c == d) & (d == e))
        mask_all_nans = mask_all_nans[0]

    return masks_dict, mask_all_nans


def join_repeated_columns(df, new_names_dict, repeated_cols_dict, feature=''):
    relevant_data = filter_relevant_columns(df, repeated_cols_dict, feature)
    masks_dict, mask_all_nans = build_masks(df, repeated_cols_dict, feature)

    nonans_df_list = []
    for col in repeated_cols_dict[feature]:
        # Subset rows WITHOUT nans
        nonans_df = relevant_data[~masks_dict[col]]
        nonans_df = nonans_df.rename(columns={col: new_names_dict[feature]})
        nonans_df_list.append(nonans_df)
    existing_values_df = pd.concat(nonans_df_list)

    # Subset rows WITH nan values
    absent_values_df = relevant_data.iloc[mask_all_nans]

    for col in repeated_cols_dict[feature]:
        absent_values_df = absent_values_df.drop(col, axis=1)
        existing_values_df = existing_values_df.drop(col, axis=1)

    absent_values_df[new_names_dict[feature]] = np.nan

    # Join nan and no-nan values
    joined_columns = pd.concat([existing_values_df, absent_values_df])

    return joined_columns