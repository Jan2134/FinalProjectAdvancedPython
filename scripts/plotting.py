"""
Scripts to plot
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

def StressfactorAnalysis(df):

    #Separate the mental factor columns
    mental_pos = df[["anxiety_level", "depression", "self_esteem", "mental_health_history"]]

    mental_pos_count = {}
    for column,row in mental_pos.items():
        #If it is anxiety or depression we count the people who are in the upper 40%
        if column == "anxiety_level" or column == "depression":
            count = (row > np.percentile(mental_pos[column],60))
            mental_pos_count[column] = count
        elif column == "mental_health_history":
            count = row == 1
            mental_pos_count[column] = count
        else:
            count = (row < np.percentile(mental_pos[column],40))
            mental_pos_count[column] = count

    mental_pos_df = pd.DataFrame(mental_pos_count)
    mental_number = len((mental_pos_df[(mental_pos_df >= 1).sum(axis=1) >= 1]))

    #Separate the pyhsical factor columns
    physical = df[["headache", "blood_pressure", "sleep_quality", "breathing_problem"]]

    physical_dict = {}
    for column,row in physical.items():
        #People in the upper 40% for headache, breathing problems or blood pressure get counted
        if column == "headache" or column == "breathing problem" or column == "blood_pressure":
            count = (row > np.percentile(physical[column],60))
            physical_dict[column] = count
        else:
            count = (row < np.percentile(physical[column],40))
            physical_dict[column] = count

    physical_df = pd.DataFrame(physical_dict)
    physical_number = len((physical_df[(physical_df >= 1).sum(axis=1) >= 1]))

    #Separate the environmental factor columns
    env = df[["living_conditions", "safety", "basic_needs", "noise_level"]]

    env_dict = {}
    for column,row in env.items():
        #People in the upper 40% for noise level get counted
        if column == "noise_level":
            count = (row > np.percentile(env[column],60))
            env_dict[column] = count
        else:
            count = (row < np.percentile(env[column],40))
            env_dict[column] = count

    env_df = pd.DataFrame(env_dict)
    env_number = len((env_df[(env_df >= 1).sum(axis=1) >= 1]))

    #Separate the academic factor columns
    acad = df[["academic_performance", "study_load", "teacher_student_relationship", "future_career_concerns"]]

    acad_dict = {}
    for column,row in acad.items():
        #People in the upper 40% for study load and future career concners get counted
        if column == "study_load" or column == "future_career_concerns":
            count = (row > np.percentile(acad[column],60))
            acad_dict[column] = count
        else:
            count = (row < np.percentile(acad[column],40))
            acad_dict[column] = count

    acad_df = pd.DataFrame(acad_dict)
    acad_number = len((acad_df[(acad_df >= 1).sum(axis=1) >= 1]))

    #Separate the social factor columns
    social = df.iloc[:, 16:20]

    social_dict = {}
    for column,row in social.items():
        #People in the upper 40% for peer pressure, extracurricular activities and bullying get counted
        if column == "peer_pressure" or column == "extracurricular_activities" or column == "bullying":
            count = (row > np.percentile(social[column],60))
            social_dict[column] = count
        else:
            count = (row < np.percentile(social[column],40))
            social_dict[column] = count

    social_df = pd.DataFrame(social_dict)
    social_number = len((social_df[(social_df >= 1).sum(axis=1) >= 1]))

    #Create a pandas series from the numbers
    neg = pd.Series([mental_number, physical_number, env_number, acad_number, social_number])
    col_names = ["Mental", "Physical", "Environmental", "Academic", "Social"]
    ax = sns.barplot(x = col_names, y = neg.values)
    ax.set(title="Number of students with negative experiences in the different fields")
    ax.bar_label(ax.containers[0])
    ax.set_ylabel("Number of students")
    plt.savefig(os.path.join("outputs", "negative_experiences_plot.png"))

    #Choose which factor has the biggest impact on stress level within each variable subgroup.
    correl = df.corr()
    print("Graph in output folder")
    print("In mental variables", round(correl.iloc[-1:,0:4].abs().max(),2).index.max().replace("_", " "), "has the biggest impact.")
    print("In physical variables", round(correl.iloc[-1:,4:8].abs().max(),2).index.max().replace("_", " "), "has the biggest impact.")
    print("In environmental variables", round(correl.iloc[-1:,8:12].abs().max(),2).index.max()), "has the biggest impact."
    print("In academic variables", round(correl.iloc[-1:,12:16].abs().max(),2).index.max().replace("_", " "), "has the biggest impact.")
    print("In social variables", round(correl.iloc[-1:,16:20].abs().max(),2).index.max().replace("_", " "), "has the biggest impact.")
