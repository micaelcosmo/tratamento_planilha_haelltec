import pandas as pd
from keys.secret_keys import CURRENT_SHEET_PATH


class CollectData:
    def __init__(self):
        self.df = pd.read_excel(CURRENT_SHEET_PATH)
        print(self.df)


if __name__ == '__main__':
    CollectData()
