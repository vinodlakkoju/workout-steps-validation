from datetime import datetime

class Utils:
    def __init__(self):
        pass

    @staticmethod
    def getDate(val):
        return datetime.utcfromtimestamp(val).strftime('%Y-%m-%d')

    @staticmethod
    def getDateTime(val):
        return datetime.utcfromtimestamp(val).strftime('%Y-%m-%d %H:%M:%S')

    @staticmethod
    def getValue(val: str):
        try:
            return float(val)
        except:
            v = float(f'0.{val.split(".")[1]}')
            print(v)
            return v