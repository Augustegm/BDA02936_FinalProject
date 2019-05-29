# BDA02936_FinalProject
This repository contains my work for the final project in Bayesian Data Analysis at DTU. It consists of the following files:

webscraper.py: A webscraper that downloads data from https://www.worldfootball.net/ for the Italy Series A 1991-1992. This file must be run first to generate the necessary data for process_data.ipynb. 

project.ipynb: A notebook which fits a Bayesian Hierarchical model based on https://doi.org/10.1080/02664760802684177 to the data using the probalistic programming language STAN https://mc-stan.org/. It furthermore fits two simpler variants of the Bayesian Hierarchical model and their predictive powers are compared based on predicting accumulated points throughout the season and a PSIS-LOO analysis (http://dx.doi.org/10.1007/s11222-016-9709-3). 

