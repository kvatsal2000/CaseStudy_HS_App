import streamlit as st

def main():
    st.set_page_config(page_title="Introduction")

    st.sidebar.title("Introduction")

    st.header(':blue-background[Air Quality Analysis]',divider='rainbow')

    st.subheader("About the data:")

    st.write("""

    THe Dataset is the UCI Air Quality Dataset that contains instances of hourly averaged
    responses from an array of 5 metal oxide chemical sensors embedded in an Air Quality 
    Chemical Multisensor Device which was located on a field in a significantly polluted area.
    The Dataset also contains ground truth values which were recorded by a co-located reference certified analyzer. 
    The dataset also had info about the temperature, absolute humidity and relative humidity.
    """)

    st.write("""
    This App contains the EDA for the UCI Air Quality Dataset and also a prediction page that takes the input steps from the user and returns
    the predictions for that many steps in the future.
            """)
    

if __name__ == '__main__':
    main()