# -*- coding: utf-8 -*-


import pandas as pd


if __name__ == '__main__':
    data = [
        ['2021-02-01', 'donny', '23', 'login'],
        ['2021-02-01', 'donny', '23', 'coupon'],
        ['2021-02-01', 'donny', '23', 'login_out'],
    ]
    headers = ['date', 'name', 'age', 'action']
    data_frame = pd.DataFrame(data, columns=headers)

    print data_frame.to_json(orient='index')
