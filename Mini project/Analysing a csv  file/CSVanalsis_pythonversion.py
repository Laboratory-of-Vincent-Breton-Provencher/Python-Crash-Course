import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import os

def identify_files(path, keywords=None, exclude=None):
    items = os.listdir(path)
    if keywords is None:
        keywords = []
    if exclude is None:
        exclude = []
    files = []
    for item in items:
        if all(keyword in item for keyword in keywords):
            if any(excluded in item for excluded in exclude):
                pass
            else:
                files.append(item)
    files.sort()
    return files

folder = r'C:\Users\pouli\Desktop\Python Crash Course\Python-Crash-Course\Mini project\Project 4'

files = identify_files(folder, keywords=['ProbCond'])
print(files)

averages = []

for i in range(len(files)):

    # 1. Load the file
    
    directory = folder + '/' + files[i]# To do: aller chercher le bon directory 
    dataframe = pd.read_csv(directory) # To do: loader le DF

    # 2. Extract the relevant columns 

    tone_id = dataframe.iloc[:,1] # To do 
    anticip_lickrate = dataframe.iloc[:,8] # To do 

    # 3. Find columns where tone_id is equal to 2 and the associated values for anticip_lickrate

    equal_to_2 = tone_id == 2# To do 
    anticip_lrs = anticip_lickrate[equal_to_2]# To do 
    ave = np.mean(anticip_lrs)# To do

    # 4. store the values in a list

    averages.append(ave)

dictionary = {'filename': files, 'average anticip_lickrate' : averages}
to_save = pd.DataFrame(dictionary)
to_save.to_csv('results.csv')
