import streamlit as st
import pandas as pd
import plotly.graph_objects as go


def load_data():
    df = pd.read_csv('funnel_data.csv')
    return df


def create_funnel_requests(df, stages, title):
    fig = go.Figure(go.Funnel(
        y=df["funnel's stage"].loc[stages:].str.replace("_", " "),
        x=df['value'].loc[stages:],
        textposition="inside",
        textinfo="value + percent previous+text",
        opacity=0.65, marker={"color": ["deepskyblue", "lightsalmon", "tan", "teal", "silver"],
                              "line": {"width": [4, 2, 2, 3, 1, 1], "color": ["wheat", "wheat", "blue", "wheat", "wheat"]}},
        connector={"line": {"color": "royalblue", "dash": "dot", "width": 3}})
    )

    fig.update_layout(
        autosize=False,
        width=700,
        height=800,
        title=title,
        font=dict(
            family="Courier New, monospace",  # You can choose a different font here
            size=18,  # You can adjust the size to make it larger or smaller
            color="RebeccaPurple",  # You can choose a different color here

        ),
        yaxis=dict(
            title_font=dict(
                size=24,
                family='Courier New, monospace',
                color='RebeccaPurple',

            ),
            tickfont=dict(
                size=18,
                family='Courier New, monospace',
                color='RebeccaPurple',

            ),
        ),
    )
    return fig


def create_funnel_users(df, stages, title):
    fig = go.Figure(go.Funnel(
        y=df["funnel's stage"].loc[:stages].str.replace("_", " "),
        x=df['value'].loc[:stages],
        textposition="inside",
        textinfo="value+percent initial",
        opacity=0.65, marker={"color": ["deepskyblue", "lightsalmon", "tan", "teal", "silver"],
                              "line": {"width": [4, 2, 2, 3, 1, 1], "color": ["wheat", "wheat", "blue", "wheat", "wheat"]}},
        connector={"line": {"color": "royalblue", "dash": "dot", "width": 3}})
    )

    fig.update_layout(
        autosize=False,
        width=700,
        height=800,
        title=title,
        font=dict(
            family="Courier New, monospace",  # You can choose a different font here
            size=18,  # You can adjust the size to make it larger or smaller
            color="RebeccaPurple",  # You can choose a different color here


        ),
        yaxis=dict(
            title_font=dict(
                size=24,
                family='Courier New, monospace',
                color='RebeccaPurple',

            ),
            tickfont=dict(
                size=18,
                family='Courier New, monospace',
                color='RebeccaPurple',

            ),
        ),
    )

    return fig


def main():
    df = load_data()

    st.header("Funnel Analysis")

    st.plotly_chart(create_funnel_requests(
        df, 3, 'Requests Funnel with Percent Previous'))
    st.plotly_chart(create_funnel_users(
        df, 2, 'Users Funnel with Percent Previous'))


if __name__ == "__main__":
    main()
