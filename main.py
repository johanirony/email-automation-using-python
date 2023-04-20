from datetime import date  # core python module
import pandas as pd  # pip install pandas

from send_email import send_email  # local python module


# Public GoogleSheets url - not secure!
SHEET_ID = "1pDfSbuKnezITdj_QzWTOhi-X_T1tlmPei4wcjcsZmeU"  # !!! CHANGE ME !!!
SHEET_NAME = "data"  # !!! CHANGE ME !!!
URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"


def load_df(url):
    
    df = pd.read_csv(url)
    return df


def query_data_and_send_emails(df):
    email_counter=0
    for _, row in df.iterrows():
        send_email(
            subject=f'[DS PBL]',
            receiver_email=row["email"],
            name=row["name"]
        )
        email_counter +=1
    return f"Total Emails Send: {email_counter}"  

df = load_df(URL)
result= query_data_and_send_emails(df)
print(result)
