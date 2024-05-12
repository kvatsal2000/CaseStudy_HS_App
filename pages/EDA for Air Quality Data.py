import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px


df = pd.read_csv('clean.csv',parse_dates=['datetime'],index_col='datetime')
df.drop(columns = ['Unnamed: 0'], inplace =True)
df1 = df[['PT08.S1(CO)','PT08.S2(NMHC)','PT08.S3(NOx)','PT08.S4(NO2)','PT08.S5(O3)','T','RH','AH']]






#App


st.header(":blue-background[EDA for the UCI Air Quality Data]")
st.sidebar.markdown("# EDA for the UCI Air Quality Data")

st.markdown("## :green-background[Data Cleaning in brief:]")

st.markdown(""" 
- Merged the date and time column to form single datetime column.
- Removing missing values.
- Changing -200 values to NA. Checking for NA values again.
- Removing NMHC(GT) column as it had more than 90% NA values.
- Imputing the rest of the values with the average of the respective column.
""")


st.markdown("# :blue-background[Exploratory data Analysis:]")

st.markdown("## :green-background[ Columns of interest:]")

st.markdown("""
- **PT08.S1(CO)**
- **PT08.S2(NMHC)**
- **PT08.S3(NOx)**
- **PT08.S4(NO2)**
- **PT08.S5(O3)**
""")


# Time series plotting for the columns of interest

x = st.selectbox("Select sensor at the polluted field",
                 ('PT08.S1(CO)','PT08.S3(NOx)','PT08.S4(NO2)','PT08.S2(NMHC)','PT08.S5(O3)'),
                 key= 'sb3')

max = len(df1)-1
start, end = st.slider(
    'Select the range of data to visualize (1 unit change implies change in an hour.)',
    0,max, (0,240) 
)

if start < end:
    fig =px.line(df1[start:end], y=x, width=1200, height=500)
    st.plotly_chart(fig, use_container_width=True)
else:
    st.error("Start date is more than the end date.")



st.markdown('Using the plots above, we can visualize the time series according to required time span')
st.markdown("""

- When the whole time series is seen at once, no descernible pattern in trend or seasonality can be observed.
- When we shorten the duration to about 10 days(240 Steps) some daily pattern is visible in all the time series.
- There were NA values for all the 5 sensors, at the same time (April 9 2004) indiacting down time.
- 3 of the 4 ground truth sensors were down on April 3 2004 and the 4th was down on the 9th.
            
                     """)



# Correlation between the variables

st.markdown("## :blue-background[Correlation between the variables:]")
st.write("Using Correlation matrix to find correlation between the variables")

def plot_heatmap(correlation):
    fig_corr = plt.figure(figsize=(12, 10))
    ax = fig_corr.add_subplot(111)

    cax = ax.matshow(correlation, cmap='coolwarm')
    fig_corr.colorbar(cax)
    for (i, j), val in np.ndenumerate(correlation):
        ax.text(j, i, f'{val:.2f}', ha='center', va='center', fontsize=10, color='black')

    # Set axis labels
    ax.set_xticks(np.arange(len(correlation.columns)))
    ax.set_yticks(np.arange(len(correlation.index)))
    ax.set_xticklabels(correlation.columns, rotation=90, ha='right')
    ax.set_yticklabels(correlation.index)

    return fig_corr

correlation = df.corr()
fig2 = plot_heatmap(correlation)
st.pyplot(fig2)


st.write("""
From the above plot we can see that:       
- Temperature is only correlated with S4.(NO2),Relative and Absolute humidity.
- Every sensor value except PT08.S3(NOx) has high to moderate correlation with each other.
- PT08.S3(NOx) has high negative correlation with every other sensor variable.
""")


# Polluted field vs baseline valu comparison.

st.markdown("## :blue-background[Comparing the pollutant value at the field vs baseline:]")

def plot_graph(df, a, gt):
    sns.set(style="whitegrid") 
    fig, ax = plt.subplots(figsize=(16, 6))

    # Actual 
    ax.plot(df.index, df[a], linestyle='-', marker='o', color='dodgerblue', label=f'Value of {a} at Polluted Field', markersize=6)
    # Baseline 
    ax.plot(df.index, df[gt], linestyle='--', marker='x', color='crimson', label=f'Baseline Value of {gt}', markersize=6)
    ax.set_xlabel('Time', fontsize=12, fontweight='bold')
    ax.set_ylabel('Value', fontsize=12, fontweight='bold')
    ax.set_title(f'Baseline VS Polluted Sensor Reading for {gt}', fontsize=14, fontweight='bold')
    ax.grid(True, which='both', linestyle='--', linewidth=0.5)  
    ax.legend(frameon=True, framealpha=0.7, fancybox=True) 
    ax.tick_params(axis='both', which='major', labelsize=10)
    return fig

max2 = len(df1)-1
start2, end2 = st.slider(
    'Select the range of data to visualize (1 unit change implies change in an hour.)',
    0,max2, (0,240),key='st1' 
)


a = st.selectbox("Select sensor at the polluted field",
                 ('PT08.S1(CO)','PT08.S3(NOx)','PT08.S4(NO2)','PT08.S2(NMHC)'),
                 key= 'sb1')

gt = st.selectbox("Select reference sensor",
                 ('CO(GT)','NOx(GT)','NO2(GT)','C6H6(GT)'),
                 key= 'sb2')

figa = plot_graph(df = df[start2:end2], a= a, gt = gt)
st.pyplot(figa)


st.markdown("""
- From the above plots, we can see that the reference values for almost all the sensors have remained constant throughout
    except NOx which fluctuates a lot in the later part of the series which may be due to several factors such as seasonal changes or sensor drift.
- The NOx sensor might need some calibration due to above mentioned reasons.
""")


st.markdown('# :blue-background[Conclusion:]')
st.markdown("""

- Looking at the sensor values present at the site, the site appears to be a highly populated area with lots 
    of traffic as the values are so high compared to the ground truth values.
- These pollutants in the air might cause prolonged respiratory diseases to the people livig in the area, so
    accurate predictions of the future can help us develop preventive measures such as traffic management.
- The values in the dataset have moderate to high correlation so it'll be helpful in multivariate
    time series prediction.
""")

