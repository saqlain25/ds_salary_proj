# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 09:57:18 2020

@author: User
"""

import glassdoor_scraper as gs
import pandas as pd
path = "C:/Users/User/Documents/ds_salary_proj/chromedriver.exe"

df = gs.get_jobs('data scientist', 15, False, path, 15)

df
