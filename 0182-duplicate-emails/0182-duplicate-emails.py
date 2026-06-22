import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    duplicates = person[person.duplicated(subset=['email'], keep=False)]

    duplicate_email_col = duplicates[['email']]

    unique_duplicate = duplicate_email_col.drop_duplicates()

    return unique_duplicate.rename(columns={'email': 'Email'})