
from strategy import myStratygy as st 
import pandas as pd
data = pd.read_csv('data/1h/AGLDUSDT.csv',index_col=0)
df= data


#new edite 
import plotly.graph_objects as go


fig = go.Figure( data=[go.Candlestick(x=df.index,
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'])])
fig.update_layout(xaxis_rangeslider_visible=False)
box = 1
candls = []
for index,row in data.iterrows():
        if index == len(data)-1 or index  <3 :
            continue
        #if data.loc[index-1,"Open"] < data.loc[index-1,"Close"] and row.Close < row.Open and data.loc[index+1,"Close"] > data.loc[index+1,"Open"] and( row.Open >  data.loc[index+1,"Open"] and row.Close < data.loc[index+1,"Close"] and row.Open < data.loc[index+1,"Close"] and data.loc[index+1,"Close"] < data.loc[index+2,"Close"] ) :
        #if data.loc[index-1,"Low"] > row.Low and data.loc[index-1,"Close"] < data.loc[index-1,"Open"] and row.Close > row.Open and data.loc[index+1,"Close"] > data.loc[index+1,"Open"] and( data.loc[index-1,"Open"] < data.loc[index-2,"Close"] ) :
        #if data.loc[index-1,"Low"] > row.Low and data.loc[index-1,"Close"] < data.loc[index-1,"Open"] and row.Close < row.Open and data.loc[index+1,"Close"] > data.loc[index+1,"Open"] and( data.loc[index-1,"Open"] < data.loc[index-2,"Close"] and data.loc[index-2,"Close"] < data.loc[index-2,"Open"] ):
        if data.loc[index+1,"Low"] > row.Low and data.loc[index-1,"Close"] < data.loc[index-1,"Open"] and row.Close < row.Open and data.loc[index+1,"Close"] > data.loc[index+1,"Open"] and( data.loc[index-1,"Open"] < data.loc[index-2,"Close"] and data.loc[index-2,"Close"] < data.loc[index-2,"Open"] ):
            candls.append(row)
            #for i in candls:
                #if (i.Open < row.Open and i.Close > row.Close)  :
            i = 0
            drw = []
            dw = False
            for x in range(1,5):
                
                if  row.Low > data.loc[index+x,"Low"] and  data.loc[index+i,"Low"] > data.loc[index+x,"Low"]:
                    drw.append(True)
                    i+=1
                else:
                    drw.append(False)
            for i in range(-len(drw),-1):
                if drw[i] == True:   
                    dw = True
                    fig.add_shape(type="rect",x0=index+1,y0=data.loc[index+(-1*i),"Close"],
                    x1=index+index, y1= data.loc[index+(-1*i),"Low"],
                    line=dict(color='red', width=2),
                    fillcolor='blue', opacity=0.3,name="s")
                    break
            if not dw:
                    fig.add_shape(type="rect",x0=index,y0=data.loc[index,"Close"],
                    x1=index+index, y1= data.loc[index,"Low"],
                    line=dict(color='red', width=2),
                    fillcolor='blue', opacity=0.3,name="s")

        #    
        #   
        #        fig.add_shape(type="rect",x0=index,y0=row.Close,
        #            x1=index+index, y1= row.Low,
        #            line=dict(color='red', width=2),
        #            fillcolor='blue', opacity=0.3,name="s")
                   
fig.show()
