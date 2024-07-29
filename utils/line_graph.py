import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def pe_vc_vs_sp500():
    # Initial investment
    initial_investment = 1000000

    # Years
    years = np.arange(1996, 2022)

    # Annualized returns
    pe_return = 14.29 / 100
    vc_return = 28.66 / 100
    sp500_return = 10.3 / 100

    # Calculate the final amount for each year
    pe_growth = initial_investment * (1 + pe_return) ** (years - 1996)
    vc_growth = initial_investment * (1 + vc_return) ** (years - 1996)
    sp500_growth = initial_investment * (1 + sp500_return) ** (years - 1996)

    # Convert the values to millions
    pe_growth_m = pe_growth / 1e6
    vc_growth_m = vc_growth / 1e6
    sp500_growth_m = sp500_growth / 1e6

    # Create a DataFrame for plotting
    data = {
        'Year': years,
        'Private Equity': pe_growth_m,
        'Venture Capital': vc_growth_m,
        'S&P 500': sp500_growth_m
    }
    df = pd.DataFrame(data)
    df.set_index('Year', inplace=True)

    # Plot using Matplotlib
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(df.index, df['Venture Capital'], label="Venture Capital", color='#2ca02c', linewidth=2)
    ax.plot(df.index, df['Private Equity'], label="Private Equity", color='#1f77b4', linewidth=2)
    ax.plot(df.index, df['S&P 500'], label="S&P 500", color='#ff7f0e', linewidth=2)

    # Adding titles and labels with improved formatting
    plt.title("Growth of $1,000,000 Investment over 25 Years", fontsize=8, fontweight='bold', color='white')
    plt.xlabel("Year", fontsize=6, fontweight='bold', color='white')
    plt.ylabel("Investment Value", fontsize=6, fontweight='bold', color='white')

    # Removing grid and borders, adding legend
    plt.legend(loc='upper left', fontsize=6)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Setting ticks color and format
    plt.tick_params(axis='x', colors='#31333F')
    plt.tick_params(axis='y', colors='#31333F')

    # Formatter for y-axis to show values in millions with '$' prefix and 'm' suffix without decimal points
    formatter = ticker.FuncFormatter(lambda x, pos: f'${int(x)}m')
    ax.yaxis.set_major_formatter(formatter)

    # Set the background color to transparent
    fig.patch.set_alpha(0)
    ax.set_facecolor('none')

    # Show plot in Streamlit
    st.pyplot(fig)