# pandastask.py
# This program 
# Author: Fatima Zeino

import pandas as pd
import re
import matplotlib.pyplot as plt


logFilename = 'access.log'

colNames= ('ip',
'dash1',
'userId',
'time',
'url',
'status code',
'size of response',
'referer',
'user agent',
'dunno'
)

df = pd.read_csv(logFilename, sep=' ', header=None, names=colNames)
print(df)

df['time'] = df['time'].apply(lambda x: re.search('[\w:/]+', x).group())
df['time'] = pd.to_datetime(df['time'], format='%d/%b/%Y:%H:%M:%S')
print(df['time'])

#dfSessionId = df['url'].apply(lambda x: re.search('f\?p=101:1:(\d+):', x))
df.insert(2, 'Session Id', df['url'].apply(lambda x: re.search('f\?p=101:1:(\d+):', x)) , False)
#print(df['Session Id'])

#print(df)
#print(colNames)
#downloadSamples = df['size of response'].mean()
downloadSamples = df.groupby(by='Session Id', dropna=False).sum()
#print(downloadSamples) 

#print(df)

df.plot(kind = 'hist')
plt.show() 