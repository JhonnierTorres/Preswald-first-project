import pandas as pd
import plotly.express as px
from preswald import connect, get_df, query, text, table, plotly

connect()
df = pd.read_csv('data/titanic.csv')

# Filter passengers older than 50 who survived
filtered_df = df[(df["Age"] > 50) & (df["Survived"] == 1)]

text("# Titanic Dashboard 🚢")
text("My Data Analysis App")
# Display table
table(filtered_df, title="Filtered Data (Age > 50 & Survived)")

fig = px.scatter(
    df,
    x="Age",
    y="Fare",
    color="Survived",
    hover_name="Name",
    title="Fare vs Age (Colored by Survival)",
    labels={
        "Age": "Passenger Age",
        "Fare": "Ticket Fare",
        "Survived": "Survived?"
    }
)

plotly(fig)
