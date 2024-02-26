import json


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

        return overall_score, push_up_norm, pull_up_norm, squat_norm, fivekm_time_norm, crunches_norm

    
# Readin json file
json_file = "test_folder/input_data.json"
with open(json_file, 'r') as file:
    file = json.load(file)

health_indicator = HealthIndicator(file)
overall_score,  push_up_norm, pull_up_norm, squat_norm, fivekm_time_norm, crunches_norm = health_indicator.overall_score()
print("Your overall fitness level is: " + str(overall_score) +" out of 100")
print("---------------------------------------------")
print("Your push up level is: " +str(push_up_norm))
print("Your pull up level is: " +str(pull_up_norm)) 
print("Your squat level is: " +str(squat_norm))
print("Your 5k level is: " +str(fivekm_time_norm))
print("Your crunches level is: " +str(crunches_norm))

