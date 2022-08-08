import csv
from os.path import exists
import pandas as pd

class Scoreboard:
    def __init__(self): # user_score_tup of form (user, score)
        if exists('scoreboard.csv'): self.__initial_run = False
        else:
            self.__initial_run = True
            with open('scoreboard.csv','w+') as file_:
                writer = csv.writer(file_)
                writer.writerow(["Username", "Score"])
                file_.close()

    @staticmethod
    def new_score(user_score_list):
        with open('scoreboard.csv','a') as file_:
            appender = csv.writer(file_)
            appender.writerow(user_score_list)

    def show_top(self):
        if self.__initial_run == False:
            df = pd.read_csv('scoreboard.csv')
            df.sort_values(["Score"], ascending=False, inplace=True)
            return df
        else: return "It looks like this is the first time the snake game is being run on this computer. No scoreboard exists yet."

