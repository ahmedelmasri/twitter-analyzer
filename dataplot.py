#!/usr/bin/env python
# coding: utf-8


import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


def plot_hist(centrality, data, num_bins):

    num_bins = 20
    # the histogram of the data
    n, bins, patches = plt.hist(data, num_bins, facecolor='navy', alpha=0.5)
    plt.xlabel('Sentiment')
    plt.ylabel(centrality + ' Centrality')
    plt.title(r'Histogram of Cancer Sentiments')

    # Tweak spacing to prevent clipping of ylabel
    plt.subplots_adjust(left=0.15)
    plt.show()