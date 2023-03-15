# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 14:05:43 2023

@author: Leo Feng
"""

import pandas as pd
import json



def read_adult():
    # Define the column names for the dataset
    column_names = [
        "age", "workclass", "fnlwgt", "education", "education-num", "marital-status",
        "occupation", "relationship", "race", "sex", "capital-gain", "capital-loss",
        "hours-per-week", "native-country", "income"
    ]

    # Read the training dataset
    train_data = pd.read_csv("../dataset/adult/adult.data", names=column_names, sep=",\s", na_values="?", engine="python")

    # Read the test dataset
    test_data = pd.read_csv("../dataset/adult/adult.test", names=column_names, sep=",\s", na_values="?", engine="python", skiprows=1)
    
    with open("../dataset/adult/adult_metadata.json", "r") as f:
        metadata = json.load(f)
    # Display the first few records of the training dataset
    return train_data,test_data,metadata

