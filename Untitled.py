#!/usr/bin/env python
# coding: utf-8

# In[9]:



import pandas as pd
import dash
import numpy as np
import dash_html_components as html
import webbrowser
import pandas as pd
from dash.dependencies import Input,Output
import dash_core_components as dcc
import plotly.express as px
import sqlite3 as sql
import matplotlib.pyplot as plt


# In[10]:


def visualize(m,n):
  df=pd.DataFrame()
  df["UserId"]=list(range(1,m+1))
  for j in range(1,n+1):
    df["Channel"+str(j)]=np.random.randint(-1,2,df.shape[0])

  print(df.shape)
  print(type(df.iloc[:,0]))
  print(type(df))
  print(df.isnull().any(axis=0))
  print(df.isnull().any(axis=1))
  df.to_csv("Voting Data.csv",index=False)
  conn=sql.connect("voting_data.db")

  df.to_sql("ChannelVotingTable50",conn,index=False)

  conn = sql.connect('voting_data.db')
  df = pd.read_sql_query("SELECT * from ChannelVotingTable50", conn)
  print(df)
  global total_votes
  total_votes=[]
  global channels
  channels=[]
  for j in range(1,n+1):

    tvc=df['Channel'+str(j)].value_counts()[1]

    total_votes.append(tvc)
    channels.append(j)
  plt.plot(total_votes,marker="o")
  plt.xlabel("Channel Numbers")
  plt.ylabel("Total Votes for Each Channel")
  plt.show()
  plt.scatter(channels,total_votes)

  plt.xlabel("Channel Numbers")
  plt.ylabel("Total Votes for Each Channel")
  plt.legend()
  plt.show()

  plt.pie(total_votes,labels=channels)

  plt.show()
  plt.bar(channels,total_votes)
  plt.xlabel("Channel Number")
  plt.ylabel("Total Votes for each Channel")
  plt.legend()
  plt.show()


# In[11]:


def main():
  m=int(input("Enter the Number of Users "))
  n=int(input("Enter the number of categories "))
  visualize(m,n)

main()


# In[ ]:


import pandas as pd
import webbrowser
# !pip install dash
import dash
import dash_html_components as html


# Declaring Global variables
# A variable declared outside a function is a global variable by default.
app = dash.Dash()
project_name = None

# Defining My Functions


def open_browser():
    # Open the default web browser
    webbrowser.open_new('http://127.0.0.1:8050/')

def create_app_ui():
    # Create the UI of the Webpage here
    main_layout=html.Div(
        [
        html.H1(id='Main_title',children=app.title,style={"text-align":"center","font-size":"300%"}),

        dcc.Graph(id="pie-chart",figure=None),
        html.H1(id="chart"),
        dcc.Graph(id="scatter-plot",figure=None),
        html.H1(id="scatter"),
        dcc.Graph(id="bar-graph",figure=None),
        html.H1(id="bars"),
        

        ])
    return main_layout
@app.callback(
    Output("pie-chart","figure"),
    [
     Input("chart","value"),

     ])
def pie_chart(value):

    df4=px.data.tips()
    fig=px.pie(df4,values=total_votes,names=channels)
    return fig
@app.callback(
    Output("scatter-plot","figure"),
    [
     Input("scatter","value"),

     ])
def scatter_plot(value):
    df4=px.data.tips()
    fig=px.scatter(df4,channels,total_votes)
    return fig

@app.callback(
    Output("bar-graph","figure"),
    [
     Input("bars","value"),

     ])
def bar_graph(value):
    df4=px.data.tips()
    fig=px.bar(df4,channels,total_votes)
    return fig


# Main Function to control the Flow of your Project
def main():


    open_browser()

    global project_name
    project_name = 'Sentiments Analysis with Insights'

    global app
    app.title = project_name
    app.layout = create_app_ui()
    app.run_server() # debug=True

    print("This would be executed only after the script is closed")
    app = None
    project_name = None

# Calling the main function
if __name__ == '__main__':
    main()


# In[ ]:




