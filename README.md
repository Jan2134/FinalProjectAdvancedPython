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
3. [Linting and Others](#3-linting-and-others)


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

    python scripts/main_script.py -id dataset/StressLevelDataset.csv -f filter_column -big numerical_value
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
![alt text](https://github.com/Jan2134/FinalProjectAdvancedPython/blob/testing/outputs/negative_experiences_plot.png?raw=true)


Graph in output folder


In mental variables self esteem has the biggest impact. <br>
In physical variables sleep quality has the biggest impact. <br>
In environmental variables safety has the biggest impact. <br>
In academic variables teacher student relationship has the biggest impact. <br>
In social variables social support has the biggest impact. <br>

--<br>
Now, given that we know that students have the most problems with mental factors, we can further asses the correlations between the factors to have a more coherent perspective:

     python scripts/main_script.py -id dataset/StressLevelDataset.csv -corr

This gives the following graph:
![alt text](https://github.com/Jan2134/FinalProjectAdvancedPython/blob/testing/outputs/correlation_matrix_heatmap.png?raw=true)

...and a longer print. Most importantly:
1. Stress Level and Anxiety Level: The anxiety level has the highest correlation with stress level (0.7368). This suggests that there is a strong positive relationship between anxiety levels and stress levels among students. It implies that as anxiety levels increase, stress levels tend to increase as well.
Self-Esteem and Stress Level:

2. Self-esteem exhibits a strong negative correlation with stress level (-0.7562). This indicates that higher self-esteem is associated with lower stress levels. As self-esteem increases, stress levels tend to decrease, highlighting the importance of self-esteem in managing stress.
3. Future Career Concerns and Stress Level: Future career concerns also show a substantial positive correlation with stress level (0.7170). Students who express more concerns about their future careers tend to experience higher stress levels. This insight emphasizes the impact of future uncertainties on the stress levels of students.
4. Sleep Quality and Stress Level: Sleep quality demonstrates a significant negative correlation with stress level (-0.7491). This implies that students with better sleep quality tend to experience lower stress levels. It highlights the importance of adequate and quality sleep in mitigating stress among students.

5. Social Support and Blood Pressure: Social support shows a strong negative correlation with blood pressure (-0.7525). This suggests that individuals with higher levels of social support tend to have lower blood pressure. Social support may act as a protective factor against elevated blood pressure, indicating the potential health benefits of a supportive social environment.

--<br>
Let's now see that with graphs and filters. First, let's plot the three most prominant relationships from above: <br>

    python scripts/main_script.py -id dataset/StressLevelDataset.csv -plot -var1 stress_level -var2 anxiety_level
![alt text](https://github.com/Jan2134/FinalProjectAdvancedPython/blob/testing/outputs/scatter_plot_stress_level_anxiety_level.png?raw=true)
_Stress level and anxiety level._
<br>

    python scripts/main_script.py -id dataset/StressLevelDataset.csv -plot -var1 stress_level -var2 self_esteem
![alt text](https://github.com/Jan2134/FinalProjectAdvancedPython/blob/testing/outputs/scatter_plot_stress_level_self_esteem.png?raw=true)
_Stress level and self esteem._
<br>

    python scripts/main_script.py -id dataset/StressLevelDataset.csv -plot -var1 stress_level -var2 future_career_concerns
![alt text](https://github.com/Jan2134/FinalProjectAdvancedPython/blob/testing/outputs/scatter_plot_stress_level_future_career_concerns.png?raw=true)
_Stress level and future carrer concerns._<br>
--<br>
If we now filter that data and then plot it, it becomes more evident.

For exapmple, filtering the anxiety level for smaller than 8 should show major imporvemens on the stress level in the plot:

    python scripts/main_script.py -id dataset/StressLevelDataset.csv -f anxiety_level -small 8 -plot -var1 stress_level -var2 anxiety_level
This print the graph in the output but more importantly, it shows the filtered csv. From that can be decucted that the stress level is more often close to zero. <br> 
<br>Further filters and plot can be applied and the correlations further checked.

--<br>
Lastly, it is possible to conduct a regression with the model to predict future outcomes and check how much variablility can be explained with the target variable. It can be done like this:

    python scripts/main_script.py -id dataset/StressLevelDataset.csv -reg
...and should give the followin output: <br>
Mean Squared Error: 0.14076890911661943 <br>
R-squared: 0.7891624570247755

![alt text](https://github.com/Jan2134/FinalProjectAdvancedPython/blob/testing/outputs/Regression.png?raw=true)
In this case, an MSE of 0.1407 indicates that, on average, the squared difference between the actual and predicted stress levels is quite low. An R-squared value of 0.7891 suggests that approximately 78.91% of the variability in the stress levels can be explained by the independent variables in your dataset. This is a relatively high value, indicating that the model fits the data well. The outcome might vary slightly every time. The graph (in the outputs) suggests that the model is able to make fairly accurate predictions about stress levels. However, there is still some variation between the actual and predicted stress levels. This could be due to a number of factors, such as the complexity of the relationship between stress levels and the other variables in the model, or the presence of outliers in the data.

<br><br>
# 2. Testing
To test the file it is possible with unittest. For that enter:

    make test

No error should occur. <br>
<br>
Furthermore, it can be tested with pytest by entering:

    pytest
One Warning does occurr here for the regression model: <br>
"R^2 score is not well-defined with less than two samples."
This issue was not fixable without major changes. <br>
<br>
Lastly, also the test coverage can be shown by:

    python -m unittest coverage
following:

    coverage report
The coverage should be for all scripts around 100% besides the main script containing non-testable @click.commands. <br>
<br>
**Please note that for the tests a new plot is created that does not contain any valuable information for the dataset.**
<br>
<br>
# 3. Linting and others
The pylinting rating for the document should be a 10/10. For that, some adjustments needed to be done to the scripts, e.g. the plotting colormapping needed to be excluded and since there were so many pylint-errors in the main_script that could not be fixed (such as imports), I disabled linting for the main_scipt. To see the score, enter:

    pylint scripts

<br>
Running flake8 on the script should also not display any errors:

    flake8
<br>
Lastly, the script contains an action file from github testing the file every time before uploading. The file is in github/workflows/python-app.yml.
