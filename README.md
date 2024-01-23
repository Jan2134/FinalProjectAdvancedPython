# Final Project Advanced Python Class

In this project, I analyze a dataset that deals with stress factors among students during an academic year. This topic is particularly interesting to me as a student, given the stress I experience in certain situations. Understanding the correlation between stress and other factors can provide valuable insights. The dataset includes various numerical information, such as:

- anxiety_level
- self_esteem
- mental_health_history
- depression
- headache
- blood_pressure
- sleep_quality
- breathing_problem
- noise_level
- living_conditions
- safety
- basic_needs
- academic_performance
- study_load
- teacher_student_relationship
- future_career_concerns
- social_support
- peer_pressure
- extracurricular_activities
- bullying
- stress_level (target variable)

**Note that `stress_level` is the target variable.**

<br><br>

# Table of Contents
1. [Code Execution and Main Insights](#1-code-execution-and-main-insights)
    - [Environment set-up](#setting-up-the-environment)
    - [Cleaning the dataset](#cleaning-the-data)
    - [CLI options](#cli-options)
    - [Gaining insights](#gaining-insights)
2. [Testing](#2-testing)
3. [Linting and Others](#3-lynting-and-others)


<br><br>

# 1. Code Execution and Main Insights

## Setting up the environment
Before running the script, navigate to the project folder in the command line interface (CLI) and activate the environment. The script has dependencies that need to be installed. To install all dependencies with the correct versions in the environment, run:

    make install

This will upgrade pip (if needed) and install all the necessary dependencies. These can also be found in the requirements.txt file which indicates the respective versions.

<br>
<br>

## Cleaning the data
To run the code it is alwas necessary to introduce the following initial statement into the CLI:

    python scripts/main_script.py -id dataset/StressLevelDataset.csv

The -id introduces the input to the notebook, located in the dataset folder. This command only, however, will not give any output since more arguements are required. <br><br>
The first action that needs to be taken is to clean the dataset. In order to do so, it is necessary to append -clean to the initial code script:

    python scripts/main_script.py -id dataset/StressLevelDataset.csv -clean
The expected outcome from the StressLevelDataset is that there are no null values, thus, also no rows will be deleted. For other datasets, this might be different.

<br><br>
## CLI Options
From here on, there are various options to discover the dataset from the command line. The options are as follows:
<br><br>
### Filtering:
This instance will print the filtered dataset.
<br>

    python scripts/main_script.py -id       dataset/StressLevelDataset.csv -f filter_column -big numerical_value
_To filter a column for a value bigger than the given value._ <br>
<br>
    
    python scripts/main_script.py -id dataset/StressLevelDataset.csv -f filter_column -small numerical_value
_To filter a column for a value bigger than the given value._ <br>
<br>
### Plotting:
This can create scatter plots for two variables from the dataframe, for filtered data, and can create an overview plot for this dataset. All plots will be saved to the outputs folder with their respective names.
<br>

    python scripts/main_script.py -id dataset/StressLevelDataset.csv -plot -var1 first_plotting_variable -var2 second_plotting_variable
_To plot a scatter plot of the first and second column and compare their relation._ <br>
<br>

    python scripts/main_script.py -id dataset/StressLevelDataset.csv -f filter_column -small numerical_value -plot -var1 first_plotting_variable -var2 second_plotting_variable
_To e.g. filter the data for a column smaller than a given value and then plot a scatter plot of two variables._ <br>
<br>

    python scripts/main_script.py -id dataset/StressLevelDataset.csv -plot -main
_To plot the "overview graph" and print the main stress factors._ <br><br>

### Correlation:
The script will print a heatmap of the biggest correlations among the columns and print the three highest correlations per column.
<br>

    python scripts/main_script.py -id dataset/StressLevelDataset.csv -corr
_To print the correlation heatmaps and highest factors._
<br>
<br>
### Regression:
The script can conduct a regression analysis with scikit-learn. It will print the Mean-Squared Error, the R2, and plot an acutal vs predicted graphs in the outputs folder.
<br>

    python scripts/main_script.py -id dataset/StressLevelDataset.csv -reg
_To print the MSE, R2, and plot the prediction accuracy._
<br>
<br>
## Gaining insights
To start it makes a lot of sense to print the "overview graph" related to all the stress factors that classifies them and shows the main reasons. To do so, the following CLI input:

    python scripts/main_script.py -id dataset/StressLevelDataset.csv -plot -main

should give the following output:
![Alt text](https://file%2B.vscode-resource.vscode-cdn.net/Users/jansternberg/Desktop/Advanced%20python/6%20Repository%20and%20final/FinalProjectAdvancedPython/outputs/negative_experiences_plot.png?version%3D1706000795655)


Graph in output folder


In mental variables self esteem has the biggest impact. <br>
In physical variables sleep quality has the biggest impact. <br>
In environmental variables safety has the biggest impact. <br>
In academic variables teacher student relationship has the biggest impact. <br>
In social variables social support has the biggest impact. <br>
