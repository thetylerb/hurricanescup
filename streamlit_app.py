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

def load_playoff_data():
    # Load the playoff skater data from the CSV file
    playoff_data = pd.read_csv("playoff_stats.csv")
    return playoff_data

def load_goalie_playoff_data():
    # Load the goalie playoff data
    goalie_playoff_data = pd.read_csv("goalie_playoff_stats.csv")
    return goalie_playoff_data

def main():
    st.title("Carolina Hurricanes 2006 Stanley Cup Winning Season Statistics")
    
    # Load team data
    team_data = load_team_data()
    
    # Load player data
    player_data = load_player_data()

    # Load Playoff Data
    playoff_data = load_playoff_data()

    # Load Goalie Playoff stats
    goalie_playoff_data = load_goalie_playoff_data()

    st.markdown(
        """
        <style>
        body {
            background-color: #f0f2f6;
            color: #333;
            font-family: Arial, sans-serif;
        }
        h1 {
            color: #ff5733;
        }
        table.dataframe {
            font-size: 14px;
            border-collapse: collapse;
            margin: 20px 0;
            width: 100%;
        }
        th {
            background-color: #333;
            color: #fff;
            font-weight: bold;
            padding: 8px;
            text-align: left;
            border: 1px solid #ddd;
        }
        td {
            background-color: #fff;
            color: #333;
            padding: 8px;
            border: 1px solid #ddd;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # Display team statistics
    st.write("## Team Statistics")
    st.write(team_data)
    
    # Display individual player statistics
    st.write("## Individual Player Statistics")
    st.write(player_data)

    # Display playoff statistics
    st.write("## Skater Playoff Statistics")
    st.write(playoff_data)

    # Display goalie Playoff data
    st.write("## Goalie Playoff Data")
    st.write(goalie_playoff_data)

if __name__ == "__main__":
    main()
