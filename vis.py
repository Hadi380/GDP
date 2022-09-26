import streamlit as st
st.title("GDP and GDP per Capita in Countries")
import pandas as pd
gdp = pd.read_csv(r"C:\Users\hadik\OneDrive\Desktop\Assignment streamlit\GPD by Country.csv")
gdp.head()
import plotly.express as px
gdp_USA = gdp[ gdp["Country Name"]== "United States"]
fig = px.bar(gdp_USA, x='Year', y='GDP', title="GDP variation in USA")
st.plotly_chart(fig)
col1, col2, col3 = st.columns(3)
col1.metric("GDP 2021", "23 T", "Top 1")
col2.metric("GDP 2019", "21.3 T", "Top 2")
col3.metric("GDP 2020", "20.8 T", "Top 3")
gdp_2021 = gdp.loc[gdp['Year'] == 2021]
gdp_2021.head()
pop = pd.read_csv(r"C:\Users\hadik\OneDrive\Desktop\Assignment streamlit\pop_csv.csv",skiprows=4)
pop.head()
pop_21= pop[['Country Name','2021']]
pop_21.head()
gdp_merge = gdp_2021.merge(pop_21[['Country Name', '2021']])
gdp_merge.head()
gdp_merge.rename(columns = {'2021':'population'}, inplace = True)
gdp_merge.head()

fig = px.scatter(gdp_merge, x="GDP", y="GDP per Capita", color="Country Name",
                 size='population', hover_data=['Country Name'], title = "GDP and GDP per Capita in countries over the year 2021")
st.plotly_chart(fig)

gdp_mean = gdp.groupby(["Country Name"], as_index = False)["GDP per Capita"].mean()
gdp_mean.head()
gdp_big = gdp_mean.nlargest(5, "GDP per Capita")
fig = px.pie(gdp_big, values='GDP per Capita', names='Country Name', title='Top 5 Average GDP per Capita countries')

st.plotly_chart(fig)
fig = px.bar(gdp_mean, x='Country Name', y='GDP per Capita', title="Average GDP per Capita in countries")
st.plotly_chart(fig)
options = st.multiselect(
    'Highest 3 Average GDP per Capita countries',
    ['Monaco', 'Qatar', 'Bermuda', 'Netherlands', 'Luxembourg'],
    ['Monaco', 'Luxembourg', 'Bermuda'])
gdp_china = gdp[ gdp["Country Name"]== "China"]
gdp_china.head()
gdp_china = gdp_china.sort_values(by='Year',ascending=True)
gdp_china.head()
fig = px.line(gdp_china, x= ["2017","2018","2019","2020","2021"], y="GDP per Capita", title = "GDP per Capita variation in China over time")
fig.update_xaxes(title="Year")
st.plotly_chart(fig)
china = st.radio(
    "Did China's GDP increase from years 2017-2021 ?",
    ('Yes', 'No', 'Cannot tell'))

if china == 'Yes':
    st.write('correct.')
else:
    st.write("wrong answer")

@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

csv = convert_df(gdp)

st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='large_df.csv',
    mime='text/csv',
)
st.sidebar.title('Figures')
st.sidebar.title('Fig 1: GDP variation in USA')
st.sidebar.title('Fig 2: GDP and GDP per Capita in Countries over the Year 2021 ')
st.sidebar.title('Fig 3: Top 5 Average GDP per Capita Countries')
st.sidebar.title('Fig 4: Average GDP per Capita in Countries')
st.sidebar.title('Fig 5: GDP per Capita Variation in China Over Time')