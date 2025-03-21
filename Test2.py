# Import Necessary Libraries
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


st.title('This Imad Test File')
st.write('## The Graph will embeded here')
df = pd.read_csv('cleaned_df.csv', index_col= 0)


# Home Page



country_count = df.Country.value_counts()
st.plotly_chart(px.bar(country_count, x= country_count.index, y= country_count.values, title= 'Number of Transactions per Country', 
                                                                       labels= {'Country' : 'All Countries', 'y' : 'No of Transactions'}))
minor_count = df['Minor Category'].value_counts()
st.plotly_chart(px.bar(minor_count, x= minor_count.index, y= minor_count.values, title= 'Number of Orders per Minor Category',
                                                                 color_discrete_sequence= ['#ed7953'],
                                                                 labels= {'y' : 'No of Orders'}))

df_sorted = df.sort_values(by= 'InvoiceDateTime')
st.write('### Order Values According the Date')
st.plotly_chart(px.line(df_sorted, x= 'InvoiceDateTime', y= 'OrderValue'))

##### How to design to TABS ممكن تخصصها لكل بند من بنود التقرير

tab1, tab2 = st.tabs(['Tab1', 'Tab2'])
tab1.title ('The Title  of Tab1 ###')
tab1.image('ecommerce.jpg')
tab1.write('### Data Sample')
tab1.dataframe(df.head())

tab1.write("##### Test Tab1")
##### Columns of Tab1
col1, col2 = tab1.columns(2)
col1.write('Draw Graph of correlation Heat Map for all nummeric vRIbles')
col2.plotly_chart(px.imshow(df.corr(numeric_only= True), text_auto= True))

##### Columns of Tab2
tab2.title ('The Title  of Tab2')
tab2.write("### Test Tab2")
tab2.dataframe(df.info())
tab2.dataframe(df.describe())
col3, col4 = tab2.columns(2)
col3.write('test for any graph')
col4.plotly_chart(px.pie(df, names= 'Country', title= 'Number of orders per Country'))

