import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    class_counts = courses.groupby('class')['student'].count().reset_index()

    valid_classes = class_counts[class_counts['student'] >= 5]

    return valid_classes[['class']]