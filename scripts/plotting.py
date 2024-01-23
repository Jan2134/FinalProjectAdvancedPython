"""
Scripts to plot
"""
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def stress_factor_analysis(df):
    """
    Function to plot the overview graph of all Stressfactors and print the most
    common ones. Differntiation of mental, physical, environmental, academic and social
    factors.
    """

    # Separate the mental factor columns
    mental_pos = df[
        ["anxiety_level", "depression", "self_esteem", "mental_health_history"]
    ]

    mental_pos_count = {}
    for column, row in mental_pos.items():
        # If it is anxiety or depression we count the people who are in the upper 40%
        if column in {"anxiety_level", "depression"}:
            count = row > np.percentile(mental_pos[column], 60)
            mental_pos_count[column] = count
        elif column == "mental_health_history":
            count = row == 1
            mental_pos_count[column] = count
        else:
            count = row < np.percentile(mental_pos[column], 40)
            mental_pos_count[column] = count

    mental_pos_df = pd.DataFrame(mental_pos_count)
    mental_number = len((mental_pos_df[(mental_pos_df >= 1).sum(axis=1) >= 1]))

    # Separate the pyhsical factor columns
    physical = df[["headache", "blood_pressure", "sleep_quality", "breathing_problem"]]

    physical_dict = {}
    for column, row in physical.items():
        # People in the upper 40% for headache, breathing problems or blood pressure get counted
        if column in {"headache", "breathing problem", "blood_pressure"}:
            count = row > np.percentile(physical[column], 60)
            physical_dict[column] = count
        else:
            count = row < np.percentile(physical[column], 40)
            physical_dict[column] = count

    physical_df = pd.DataFrame(physical_dict)
    physical_number = len((physical_df[(physical_df >= 1).sum(axis=1) >= 1]))

    # Separate the environmental factor columns
    env = df[["living_conditions", "safety", "basic_needs", "noise_level"]]

    env_dict = {}
    for column, row in env.items():
        # People in the upper 40% for noise level get counted
        if column == "noise_level":
            count = row > np.percentile(env[column], 60)
            env_dict[column] = count
        else:
            count = row < np.percentile(env[column], 40)
            env_dict[column] = count

    env_df = pd.DataFrame(env_dict)
    env_number = len((env_df[(env_df >= 1).sum(axis=1) >= 1]))

    # Separate the academic factor columns
    acad = df[
        [
            "academic_performance",
            "study_load",
            "teacher_student_relationship",
            "future_career_concerns",
        ]
    ]

    acad_dict = {}
    for column, row in acad.items():
        # People in the upper 40% for study load and future career concners get counted
        if column in {"study_load", "future_career_concerns"}:
            count = row > np.percentile(acad[column], 60)
            acad_dict[column] = count
        else:
            count = row < np.percentile(acad[column], 40)
            acad_dict[column] = count

    acad_df = pd.DataFrame(acad_dict)
    acad_number = len((acad_df[(acad_df >= 1).sum(axis=1) >= 1]))

    # Separate the social factor columns
    social = df.iloc[:, 16:20]

    social_dict = {}
    for column, row in social.items():
        # People in the upper 40% for peer pressure, extracurricular activities and bullying get counted
        if column in {"peer_pressure", "extracurricular_activities", "bullying"}:
            count = row > np.percentile(social[column], 60)
            social_dict[column] = count
        else:
            count = row < np.percentile(social[column], 40)
            social_dict[column] = count

    social_df = pd.DataFrame(social_dict)
    social_number = len((social_df[(social_df >= 1).sum(axis=1) >= 1]))

    # Create a pandas series from the numbers
    neg = pd.Series(
        [mental_number, physical_number, env_number, acad_number, social_number]
    )
    col_names = ["Mental", "Physical", "Environmental", "Academic", "Social"]
    ax = sns.barplot(x=col_names, y=neg.values)
    ax.set(title="Number of students with negative experiences in the different fields")
    ax.bar_label(ax.containers[0])
    ax.set_ylabel("Number of students")
    plt.savefig(os.path.join("outputs", "negative_experiences_plot.png"))

    # Choose which factor has the biggest impact on stress level within each variable subgroup.
    correl = df.corr()
    print("\n\nGraph in output folder\n\n")
    print(
        "In mental variables",
        round(correl.iloc[-1:, 0:4].abs().max(), 2).index.max().replace("_", " "),
        "has the biggest impact.",
    )
    print(
        "In physical variables",
        round(correl.iloc[-1:, 4:8].abs().max(), 2).index.max().replace("_", " "),
        "has the biggest impact.",
    )
    print(
        "In environmental variables",
        round(correl.iloc[-1:, 8:12].abs().max(), 2).index.max().replace("_", " "),
        "has the biggest impact.",
    )
    print(
        "In academic variables",
        round(correl.iloc[-1:, 12:16].abs().max(), 2).index.max().replace("_", " "),
        "has the biggest impact.",
    )
    print(
        "In social variables",
        round(correl.iloc[-1:, 16:20].abs().max(), 2).index.max().replace("_", " "),
        "has the biggest impact.",
    )


def plot_two_variables(df, variable1, variable2):
    """
    Function to plot two variables in a scatter plot, making the weight of each point more visible
    """
    print("\n\nGraph in output folder\n\n")
    plt.figure(figsize=(8, 6))

    # Create a list of marker sizes based on the values of variable2
    marker_sizes = [50 * (i / np.max(df[variable2])) for i in df[variable2]]

    # Create a colormap based on the weights
    # pylint: disable=E1101
    cmap = plt.cm.viridis

    # Normalize the weights to be in the range [0, 1]
    norm = plt.Normalize(vmin=min(marker_sizes), vmax=max(marker_sizes))

    # Create the scatter plot with size-weighted markers and varied color intensity
    sc = plt.scatter(
        x=df[variable1],
        y=df[variable2],
        s=marker_sizes,
        c=marker_sizes,
        cmap=cmap,
        alpha=0.7,
        norm=norm,
    )

    # Add a colorbar to the plot
    cbar = plt.colorbar(sc, orientation="vertical")
    cbar.set_label("Weight")

    plt.title(
        f"Scatter Plot with Size-Weighted Markers between {variable1} and {variable2}"
    )
    plt.xlabel(variable1)
    plt.ylabel(variable2)
    plt.savefig(os.path.join("outputs", f"scatter_plot_{variable1}_{variable2}.png"))


def plot_two_variables_after_filtering(filtered_df, variable1, variable2):
    """
    Function to plot two variables in a scatter plot, making the weight of each point more visible
    """
    print("\n\nGraph in output folder\n\n")
    plt.figure(figsize=(8, 6))

    # Create a list of marker sizes based on the values of variable2
    marker_sizes = [
        50 * (i / np.max(filtered_df[variable2])) for i in filtered_df[variable2]
    ]

    # Create a colormap based on the weights
    # pylint: disable=E1101
    cmap = plt.cm.viridis

    # Normalize the weights to be in the range [0, 1]
    norm = plt.Normalize(vmin=min(marker_sizes), vmax=max(marker_sizes))

    # Create the scatter plot with size-weighted markers and varied color intensity
    sc = plt.scatter(
        x=filtered_df[variable1],
        y=filtered_df[variable2],
        s=marker_sizes,
        c=marker_sizes,
        cmap=cmap,
        alpha=0.7,
        norm=norm,
    )

    # Add a colorbar to the plot
    cbar = plt.colorbar(sc, orientation="vertical")
    cbar.set_label("Weight")

    plt.title(
        f"Scatter Plot with Size-Weighted Markers between {variable1} and {variable2}"
    )
    plt.xlabel(variable1)
    plt.ylabel(variable2)
    plt.savefig(
        os.path.join("outputs", f"filtered_scatter_plot_{variable1}_{variable2}.png")
    )
