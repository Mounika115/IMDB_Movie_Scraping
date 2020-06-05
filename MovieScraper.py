# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 14:29:39 2020

@author: Pinku
"""


import pandas as pd
import numpy as nm

class Scraper:
    def __init__(self,initial_url):
        self.initial_url= initial_url
        
    def extract_all_urls(self,inital_url):
        all_urls=[]
        return all_urls
    
    def extract_movie_names(self,initial_url):
        movie_names = []
        return movie_names

    def extact_revies_users(self,all_urls):
        reviews = {}
        return reviews
    
    def extract_directros(self,all_urls):
        directros= []
        return directros
    


scraper=Scraper()
