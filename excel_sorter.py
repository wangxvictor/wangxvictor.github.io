#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 13:27:46 2022

@author: victorwang
"""

#this sorter uses pandas and its dataframes infrastructure

import pandas as pd

df = pd.read_excel('CaPS Broken Links.xlsx')

sorted_file = df.sort_values(['source url', 'new link'])

sorted_file.to_excel('new_file_name_here.xlsx')