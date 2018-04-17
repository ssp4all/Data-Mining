def gini_of(df, y, unique_classes):
    gini_y = 1
    total = len(df)
    for class_d in unique_classes[y]:
        val = len(df[df[y] == class_d])
        gini_y -= (val/total) ** 2
    return gini_y

def calc_gini(df, y):
    unique_classes = {}
    total = len(df)
    for col in df.columns:
        unique_classes[col] = list(df[col].unique())
    df_x = df.drop([y], axis=1)
    gini_y = gini_of(df, y, unique_classes)
    ginis = {}
    for column in df_x.columns:
        ginis[column] = {'value': 1, 'combination': []}
        for combination in combinations(unique_classes[column], len(unique_classes[column]) - 1):
            missing_label = list(set(unique_classes[column]) - set(combination))[0]
            total_df = [df[df[column] == class_] for class_ in list(combination)]
            total_df = pd.concat(total_df)
            missing_df = df[df[column] == missing_label]
            final_gini = 0
            for dfs in [total_df, missing_df]:
                count_len = len(dfs)
                final_gini += (count_len / total) * gini_of(dfs, y, unique_classes)
            if ginis[column]['value'] > final_gini:
                comb = [list(combination)]
                comb.append([missing_label])
                ginis[column] = {'value': final_gini, 'combination': comb}
    ret_val = (df_x.columns[0], ginis[df_x.columns[0]]['combination'], ginis[df_x.columns[0]]['value'])
    for gin in ginis:
        if ret_val[2] > ginis[gin]['value']:
            ret_val = (gin, ginis[gin]['combination'], ginis[gin]['value'])
    return ret_val