# -*- coding: utf-8 -*-


import pandas as pd


def import_csv(path, data, headers):
    """
    import csv file
    """
    df = pd.DataFrame(data)
    df.to_csv(path, mode='w', header=headers, index=False)


if __name__ == '__main__':
    data = [
        ['2021-02-01', 'donny', '23', 'login'],
        ['2021-02-01', 'donny', '23', 'coupon'],
        ['2021-02-01', 'donny', '23', 'login_out'],
    ]
    headers = ['date', 'name', 'age', 'action']
    #
    # data_frame = pd.DataFrame(data, columns=headers)
    #
    # print data_frame.to_json(orient='index')

    path = './test.csv'
    import_csv(path, data, headers)