import matplotlib.pyplot as plt

def pie_chart():
    # Data
    labels = ['High-Risk Sub-Fund: Early-Stage Startups', 'Medium-Risk Sub-Fund: Series A & B Tech Companies', 'Low-Risk Sub-Fund: Private Equity in Plastic Manufacturing', 'Feeder Fund: Diverse Fund Investments']
    sizes = [20, 30, 40, 10]
    colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']
    explode = (0, 0, 0.1, 0)  # explode the 1st slice

    # Plot
    fig1, ax1 = plt.subplots()
    fig1.patch.set_alpha(0)
    ax1.set_facecolor('none')
    wedges, texts, autotexts = ax1.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%',
                                       shadow=True, startangle=90, textprops=dict(color="#31333F"))
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # Add legend
    legend = ax1.legend(wedges, labels, loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), facecolor='#0E1117', framealpha=0.0)

    for text in legend.get_texts():
        text.set_fontfamily('sans-serif')
        text.set_fontsize(12)
        text.set_color("#31333F")

    # Remove title and make background black
    plt.gca().set_facecolor('#31333F')
    plt.gcf().set_facecolor('#31333F')

    return plt
