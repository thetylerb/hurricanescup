import streamlit as st
import pandas as pd

def load_team_data():
    # Load the team data from CSV file
    team_data = pd.read_csv("team_stats.csv")
    return team_data

def load_player_data():
    # Load the individual player data from CSV file
    player_data = pd.read_csv("player_stats.csv", encoding="utf-8")
    return player_data

def main():
    st.title("Carolina Hurricanes 2006 Stanley Cup Winning Season Statistics")
    
    # Load team data
    team_data = load_team_data()
    
    # Load player data
    player_data = load_player_data()
    
    # Display team statistics
    st.write("## Team Statistics")
    st.write(team_data)
    
    # Display individual player statistics
    st.write("## Individual Player Statistics")
    st.write(player_data)

if __name__ == "__main__":
    main()
