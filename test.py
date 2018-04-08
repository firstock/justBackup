# coding: utf-8
pp= pd.read_table('data/pypi.txt', header=None)
pp
f= lambda x: ','.join(x.split('::'))
pp.applymap(f)
