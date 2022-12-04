import pandas as pd
from keys.secret_keys import CURRENT_SHEET_SECRETS as CSS


class CollectData:
    def __init__(self):
        data = pd.read_excel(CSS['path'])
        self.df = pd.DataFrame(data)

    def column_1(self):
        print(self.df[CSS['column_1']][0])

    def column_2(self):
        print(self.df[CSS['column_2']][0])


if __name__ == '__main__':
    CollectData().column_1()
    CollectData().column_2()
