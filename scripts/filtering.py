"""
Filter dataset
"""


class Filtering:
    """
    Class to filter dataset
    """

    @staticmethod  # made the code run; it indicates that these methods do not depend on the state of an instance of the class (self)
    def bigger_than(df, filter_column, bigger_than):
        """
        Filter dataset for bigger than x
        """
        return df[df[filter_column] > bigger_than]

    @staticmethod
    def smaller_than(df, filter_column, smaller_than):
        """
        Filter dataset for smaller than x
        """
        return df[df[filter_column] < smaller_than]
