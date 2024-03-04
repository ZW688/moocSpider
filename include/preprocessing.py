import pandas as pd

def school_data_preprocessing(df):
    """
    :param df: pandas
    985\211标签提取
    @param df:
    @return:
    """
    df['is_985'] = None
    df['is_211'] = None
    df['create_time'] = '2024-02-02 00:00:00'
    df['update_time'] = '2024-03-02 00:00:00'
    df['deleted'] = False
    df['is_985'] = df['text'].apply(lambda x : True if '985' in x else False)
    df['is_211'] = df['text'].apply(lambda x : True if '211' in x else False)
    df.reindex(columns=['is_985', 'is_211'])