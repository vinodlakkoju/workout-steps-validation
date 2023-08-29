import pandas as pd
from DataAccess import Database

class DetectEngine:
    def __init__(self):
        self.__db = Database()

    def __maxScoreRule(self, user_id: int, current_date: str) -> bool:
        data_df = self.__db.getOneDayUserData(user_id, current_date)
        current_score = list(data_df['distance'])[0]
        return False if current_score >= 25.0 else True

    def __averageScoreRule(self, user_id: int, current_date: str) -> bool:
        previous_data_df = self.__db.getOneMonthUserData(user_id)
        current_score = list(previous_data_df[previous_data_df['date_time'] == current_date]['distance'])[0]
        past_data_df = previous_data_df[previous_data_df['date_time'] != current_date]
        average = past_data_df.mean()['distance']
        return False if (average * 5 < current_score) else True

    def isValidScore(self, user_id: int, current_date: str):
        result = False
        reason = ''
        if self.__maxScoreRule(user_id, current_date):
            if self.__averageScoreRule(user_id, current_date):
                result = True
            else:
                reason = "Not matching with average score"
        else:
            reason = "Above the possible valid score"
        return result, reason



if __name__ == '__main__':
    de = DetectEngine()
    result, reason = de.isValidScore(454, '2023-08-09')
