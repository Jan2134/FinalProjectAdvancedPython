"""
Script to test plotting
"""
import unittest
import pandas as pd
from scripts.plotting import (
    stress_factor_analysis,
    plot_two_variables,
    plot_two_variables_after_filtering,
)
from unittest.mock import patch


class TestPlottingFunctions(unittest.TestCase):
    def setUp(self):
        """
        Create a sample DataFrame for testing
        """
        data = {
            "anxiety_level": [1, 2, 3, 4, 5],
            "self_esteem": [10, 20, 30, 40, 50],
            "mental_health_history": [0, 1, 1, 0, 1],
            "depression": [5, 4, 3, 2, 1],
            "headache": [2, 3, 1, 4, 5],
            "blood_pressure": [120, 130, 110, 140, 150],
            "sleep_quality": [7, 8, 6, 9, 5],
            "breathing_problem": [0, 1, 0, 1, 0],
            "noise_level": [3, 2, 4, 1, 5],
            "living_conditions": [2, 4, 3, 5, 1],
            "safety": [4, 3, 5, 1, 2],
            "basic_needs": [5, 1, 2, 4, 3],
            "academic_performance": [3, 5, 1, 2, 4],
            "study_load": [2, 4, 3, 5, 1],
            "teacher_student_relationship": [4, 3, 5, 1, 2],
            "future_career_concerns": [1, 2, 3, 4, 5],
            "social_support": [3, 4, 2, 5, 1],
            "peer_pressure": [2, 5, 3, 4, 1],
            "extracurricular_activities": [4, 3, 5, 1, 2],
            "bullying": [5, 1, 2, 3, 4],
            "stress_level": [3, 4, 2, 5, 1],
        }
        self.df = pd.DataFrame(data)

    @patch("scripts.plotting.plt.savefig")
    def test_stressfactor_analysis(self, mock_savefig):
        stress_factor_analysis(self.df)

    @patch("scripts.plotting.plt.savefig")
    def test_plot_two_variables(self, mock_savefig):
        variable1 = "anxiety_level"
        variable2 = "depression"
        plot_two_variables(self.df, variable1, variable2)

    @patch("scripts.plotting.plt.savefig")
    def test_plot_two_variables_after_filtering(self, mock_savefig):
        variable1 = "anxiety_level"
        variable2 = "depression"
        filtered_df = self.df[self.df["anxiety_level"] > 2]
        plot_two_variables_after_filtering(filtered_df, variable1, variable2)


if __name__ == "__main__":
    unittest.main()
