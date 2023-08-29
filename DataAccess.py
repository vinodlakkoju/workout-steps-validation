import mysql.connector
from typing import Tuple, List
from datetime import datetime
import os
from Utils import Utils as ut
import pandas as pd
FILE_PATH = r'E:\Projects\MotionApp\data\distance_counters_20230809.csv'
DB_CONNECTION_STRING = "motionapp.cedjav3ak2sb.us-west-1.rds.amazonaws.com"
DB_USERNAME = "motion"
DB_PASSWORD = "1987*RoLon!22Pd"

class Database:
    def __init__(self, user_id: int, current_date: str):
        self.__user_data_df = pd.read_csv(FILE_PATH)

    def getOneDayUserData(self,user_id: int, current_date: str):
        df = self.__user_data_df
        df1 = df[df['user_id'] == user_id]
        df2 = df1[['id', 'user_id', 'distance', 'date_time']]
        df2['distance'] = df2['distance'].apply(ut.getValue)
        df2['date_time'] = df2['date_time'].apply(ut.getDate)
        df3 = df2.groupby('date_time', as_index=False, sort=False).agg({'distance': 'sum'})
        df4 = df3[df3['date_time'] == current_date]
        return df4

    def getOneMonthUserData(self, user_id: int) -> pd.DataFrame:
        df = self.__user_data_df
        df1 = df[df['user_id'] == user_id]
        df2 = df1[['id', 'user_id', 'distance', 'date_time']]
        df2['distance'] = df2['distance'].apply(ut.getValue)
        df2['date_time'] = df2['date_time'].apply(ut.getDate)
        df3 = df2.groupby('date_time', as_index=False, sort=False).agg({'distance': 'sum'})
        return df3


