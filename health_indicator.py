import json
import csv
from datetime import datetime


class HealthIndicator:
    """
    Inputs: push up, pull up, crunches, squats scores and 5km time
    Method: normalize and give a score
    Outputs: returns an overall health score
    """
    def __init__(self, file):
        self.push_up = file["push_up"]
        self.pull_up = file["pull_up"]
        self.squats = file["squat"]
        self.fivekm_time = file["fivekm_time"]
        self.crunches = file["crunches"]

    def calculate_normalize_score(self, score, min_score, max_score):
        score = float(score)
        normalized_score = int(max(((score - min_score)/ \
                                      (max_score - min_score)), 0) * 100)
        return normalized_score
    
    def calculate_average_scores(self, *args):
        if not args:
            return 0 
        total = sum(args)
        average = round(total / len(args), 0)
        return average

    def overall_score(self):
        push_up_norm = self.calculate_normalize_score(self.push_up, 15, 99)
        pull_up_norm = self.calculate_normalize_score(self.pull_up, 5, 37)
        squat_norm = self.calculate_normalize_score(self.squats, 16, 178)
        fivekm_time_norm = self.calculate_normalize_score(self.fivekm_time, 31.5, 19.75)
        crunches_norm = self.calculate_normalize_score(self.crunches, 23, 159)

        overall_score = self.calculate_average_scores(
            push_up_norm,
            pull_up_norm,
            squat_norm,
            fivekm_time_norm,
            crunches_norm
            )
        
        current_date, week_number = self.get_date_and_week()

        result = {
            'week_number' : week_number,
            'current_date': current_date,
            'overall_score': overall_score,
            'push_up_norm': push_up_norm,
            'pull_up_norm': pull_up_norm,
            'squat_norm': squat_norm,
            'fivekm_time_norm': fivekm_time_norm,
            'crunches_norm': crunches_norm
            }

        return result
    
    def get_date_and_week(self):
        current_date = datetime.now()
        week_number = current_date.isocalendar()[1]
        return current_date, week_number