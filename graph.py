import pandas as pd
import plotly_express as px

df=pd.read_csv("data.csv")
fig1=px.line(df,x="date", y="cases", color="country", title="Covid cases by country (Line)")
fig2=px.bar(df,x="date", y="cases", color="country", title="Covid cases by country (Bar)")
fig3=px.scatter(df,x="date", y="cases", color="country", size_max=60, title="Covid cases by country (Scatter)")

print("Would you like to see your data in a scatter plot, a bar graph, or a line graph?")
see=input("Please enter in lowercase with no extra characters: ")

if(see=="line"):
    fig1.show()
if(see=="line graph"):
    fig1.show()
if(see=="bar"):
    fig2.show()
if(see=="bar graph"):
    fig2.show()
if(see=="scatter"):
    fig3.show()
if(see=="scatter plot"):
    fig3.show()
else:
    print("Graph not recognized. Please enter: scatter/scatter plot; bar/bar graph; or line/line graph")