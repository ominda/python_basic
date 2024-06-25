from d3blocks import D3Blocks 
import pandas as pd
d3 = D3Blocks()

df = pd.read_csv("Index2018.csv")
d3.movingbubbles(df, 
                 datetime='datetime',
                 sample_id= 'sample_id',
                 state='state',
                 filepath='./movingbubbles.html' )