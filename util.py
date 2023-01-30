import pandas as pd
import dropdown

PATH = r"C:\Users\Frank\game_sales\Games.csv"

def get_data(PATH):
    df = pd.read_csv(PATH)
    df.rename(columns = {'Sales':'Sales_in_Millions'}, inplace = True)
    df.rename(columns = {'Name':'Game'}, inplace = True)
    # print(df)
    return df
# print(get_data(PATH))
def get_publishers():
    df = get_data(PATH)
    pub = df.groupby("Publisher").sum().sort_values("Sales_in_Millions",ascending = False).iloc[:10]
    pub.reset_index(inplace=True)
    return pub

# def get_pub_games(dropdown):
#     df = get_data(PATH)
#     pub_game = df[["Name","Sales_in_Millions","Publisher"]]
#     filtered_data = pd.DataFrame(pub_game.query("Publisher in @dropdown"))
#     return filtered_data
# print(get_pub_games())
