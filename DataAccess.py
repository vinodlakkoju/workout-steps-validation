import pymysql
import os
import sys
#import logging
import datetime
import time
from Utils import Utils as ut
import pandas as pd

DB_CONNECTION_STRING = "motionapp.cedjav3ak2sb.us-west-1.rds.amazonaws.com"
DB_USERNAME = "pythonuser1"
DB_PASSWORD = "@1Python@23"

class Database:
    def __init__(self, user_id: int, current_date: str):
        self.__user_id = user_id
        self.__current_date = current_date
        # rds_proxy_host = os.environ['RDS_PROXY_HOST']
        # db_user_name = os.environ['USER_NAME']
        # db_password = DB_PASSWORD
        # db_name = os.environ['DB_NAME']
        rds_proxy_host = DB_CONNECTION_STRING
        db_user_name = DB_USERNAME
        db_password = DB_PASSWORD
        db_name = 'motionapp'
        #logger = logging.getLogger()
        #logger.setLevel(logging.INFO)
        try:
            self.__conn = pymysql.connect(host=rds_proxy_host, user=db_user_name, passwd=db_password, db=db_name, connect_timeout=5)
        except pymysql.MySQLError as e:
            #logger.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
            #logger.error(e)
            sys.exit()

    def getData(self) -> pd.DataFrame:
        current_date_obj = datetime.datetime.strptime(self.__current_date, "%Y-%m-%d")
        start_date = current_date_obj - datetime.timedelta(60)
        datetime_utc = time.mktime(start_date.timetuple())
        with self.__conn.cursor() as cur:
            sql_string = f"SELECT user_id, distance, date_time from distance_counters where user_id={self.__user_id} and date_time>={datetime_utc}"
            cur.execute(sql_string)
            result = cur.fetchall()
            df = pd.DataFrame(result, columns=['user_id', 'distance', 'date_time'])
            df['distance'] = df['distance'].apply(ut.getValue)
            df['date_time'] = df['date_time'].apply(ut.getDate)
            df = df.groupby('date_time', as_index=False, sort=False).agg({'distance': 'sum'})
            # df['moving_avg_30'] = df.distance.rolling(30).mean()
            # df['moving_avg_30'] = df['moving_avg_30'].fillna(0)
        return df

if __name__ == '__main__':
    db = Database(224, '2023-09-03')
    print(db.getData())



