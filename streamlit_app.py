import streamlit as st
import pandas as pd

def load_data():
    # Load the data from CSV file
    data = pd.read_csv("teamstats.csv")
    return data

def main():
    st.title("Carolina Hurricanes 2006 Stanley Cup Winning Season Statistics")
    
    # Load data
    data = load_data()
    
    # Display the data
    st.write("## Team Stats vs League Average")
    st.write(data)

if __name__ == "__main__":
    main()
