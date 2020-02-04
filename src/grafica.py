import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
import os


def graph(year_start, year_end):
    all_data = pd.read_csv('../output/all_data.csv',encoding='utf-8')
    grouped = all_data.groupby(['year'])
    res_1 = grouped['tempo'].mean()
    res_2 = grouped['loudness'].mean()
    res_3 = grouped['energy'].mean()
    res_4 = grouped['danceability'].mean()

    data = pd.DataFrame({'Year':res_1.index, 'Median Tempo':res_1.values, 'Median Loudness': res_2.values, 'Median Energy': res_3.values, 'Median Danceability': res_4.values})
    data = data.loc[(data.Year>=year_start)&(data.Year<=year_end)]

    plot_1 = data.plot(x ='Year', y='Median Loudness', title='Loudness')
    fig_1 = plot_1.get_figure()
    fig_1.savefig("../output/grafica_1.png")

    plot_2 = data.plot(x ='Year', y='Median Tempo', title ='Tempo')
    fig_2 = plot_2.get_figure()
    fig_2.savefig("../output/grafica_2.png")

    plot_3 = data.plot(x ='Year', y='Median Energy', title ='Energy')
    fig_3 = plot_3.get_figure()
    fig_3.savefig("../output/grafica_3.png")

    plot_4 = data.plot(x ='Year', y='Median Danceability', title ='Danceability')
    fig_4 = plot_4.get_figure()
    fig_4.savefig("../output/grafica_4.png")

    #return fig.savefig("grafica.png")
    