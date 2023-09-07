import pandas as pd
from DataAccess import Database

class DetectEngine:
    def __init__(self, user_id: int, current_date: str):
        self.__current_date = current_date
        db = Database(user_id, current_date)
        self.__user_data_df = db.getData()

    def __maxScoreRule(self) -> bool:
        df = self.__user_data_df
        self.__current_score = df.loc[df['date_time'] == self.__current_date, 'distance'].values[0]
        return False if self.__current_score >= 25.0 else True

    def __averageScoreRule(self) -> bool:
        past_data_df = self.__user_data_df[self.__user_data_df['date_time'] != self.__current_date]
        self.__average_score = past_data_df['distance'].mean()
        return False if (self.__average_score * 5 < self.__current_score) else True

    def isValidScore(self):
        result = False
        reason = ''
        if self.__maxScoreRule():
            if self.__averageScoreRule():
                result = True
            else:
                reason = f"Current score({round(self.__current_score,2)}km) faraway to average score({round(self.__average_score,2)})"
        else:
            reason = f"Impossible score of {round(self.__current_score, 2)}km recorded in a day"
        return result, reason



if __name__ == '__main__':
    de = DetectEngine(1143, '2023-09-06')
    result, reason = de.isValidScore()
    print(result, reason)
