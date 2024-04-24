import pandas as pd


spls = pd.read_excel('recommend/files/Specialist.xlsx')

y = spls.Disease

specialists = list(y.unique())
# columns = spls.columns