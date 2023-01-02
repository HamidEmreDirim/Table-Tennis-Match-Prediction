import pandas as pd
import pickle




class GenerateMassage:

    def __init__(self, competitor_1, competitor_2):
        self.competitor_1 = competitor_1
        self.competitor_2 = competitor_2
        self.massage = ""
        self.evaluate_data()



    def evaluate_data(self):
        player_rankings = pd.read_csv("player_data.csv").values.tolist()
        matches = pd.read_csv("match_data.csv").values.tolist()

        temp = dict()

        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        player_rankings = [x for x in player_rankings if x[-1][0] not in numbers]
        player_names = [x[0] for x in player_rankings]

        for x in player_rankings:
            temp[x[0]] = x[2:]
        self.player_names = player_names
        self.data = temp

    def __str__(self):

        return self.generate_massage()

    def asses_winner(self):

        def ranking(x):
            return x[0]

        def avg_point(x):
            return x[1]

        def country(x):
            return x[2]

        def age(x):
            return x[3]

        def dominant_hand(x):
            return x[4]

        def grip(x):
            return x[5]

        def player_style(x):
            return x[7]

        p1_data = pd.DataFrame()
        p1_df = pd.DataFrame(self.data[self.competitor_1])
        p1_data["ranking"] = p1_df.apply(ranking)
        p1_data["avg_point"] = p1_df.apply(avg_point)
        p1_data["country"] = p1_df.apply(country)
        p1_data["age"] = p1_df.apply(age)
        p1_data["dominant_hand"] = p1_df.apply(dominant_hand)
        p1_data["grip"] = p1_df.apply(grip)
        p1_data["player_style"] = p1_df.apply(player_style)

        p2_data = pd.DataFrame()
        p2_df = pd.DataFrame(self.data[self.competitor_2])
        p2_data["ranking"] = p2_df.apply(ranking)
        p2_data["avg_point"] = p2_df.apply(avg_point)
        p2_data["country"] = p2_df.apply(country)
        p2_data["age"] = p2_df.apply(age)
        p2_data["dominant_hand"] = p2_df.apply(dominant_hand)
        p2_data["grip"] = p2_df.apply(grip)
        p2_data["player_style"] = p2_df.apply(player_style)


        final_data = pd.DataFrame()
        final_data = pd.concat([p1_data, p2_data], axis=1)

        

        ml_model = pickle.load(open("match_predictor.pickle", 'rb'))
        result = ml_model.predict(final_data)

        if result == 1:
            return self.competitor_1
        else:
            return self.competitor_2

    def generate_massage(self):

        self.massage = f"{self.competitor_1} vs {self.competitor_2}  my model says that {self.asses_winner()} will win."
        return self.generate_massage()







                







