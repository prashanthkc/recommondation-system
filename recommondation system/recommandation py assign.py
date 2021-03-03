import pandas as pd


game_data = pd.read_csv("F:/assignment/recommondation system/Datasets_Recommendation Engine/game.csv", encoding= "utf8")
game_data.shape
game_data.columns

#term frequencey- inverse document frequncy is a numerical statistic that is intended 
#to reflect how important a word is to document in a collecion or corpus

from sklearn.feature_extraction.text import TfidfVectorizer
# Creating a Tfidf Vectorizer to remove all stop words
# taking stop words from tfid vectorizer 

tfidf = TfidfVectorizer(stop_words = 'english')

game_data.isna().sum()
game_data.isnull().sum()

# Preparing the Tfidf matrix by fitting and transforming
#Transform a count matrix to a normalized tf or tf-idf representation
tfidf_matrix = tfidf.fit_transform(game_data.game)
tfidf_matrix.shape

from sklearn.metrics.pairwise import linear_kernel

# Computing the cosine similarity on Tfidf matrix

cosine_sim_matrix = linear_kernel(tfidf_matrix,tfidf_matrix)
# creating a mapping of movie name to index number 
game_index = pd.Series(game_data.index, index = game_data['game'])
game_index = game_index[~game_index.index.duplicated(keep='first')]

game_id = game_index["Grand Theft Auto IV"]
game_id

def get_recommendations(Name, topN):    
    # topN = 10
    # Getting the game index using its title 
    game_id = game_index[Name]
    
 # Getting the pair wise similarity score for all the game's with that 
    # game
    cosine_scores = list(enumerate(cosine_sim_matrix[game_id]))
    
    # Sorting the cosine_similarity scores based on scores 
    cosine_scores = sorted(cosine_scores, key=lambda x:x[1], reverse = True)
    
    # Get the scores of top N most similar movies 
    cosine_scores_N = cosine_scores[0: topN+1]
    
    # Getting the game index 
    game_idx  =  [i[0] for i in cosine_scores_N]
    game_scores =  [i[1] for i in cosine_scores_N]
    
    # Similar movies and scores
    game_similar_show = pd.DataFrame(columns=["name", "Score"])
    game_similar_show["name"] = game_data.iloc[game_idx,1]
    game_similar_show["Score"] = game_scores
    game_similar_show.reset_index(inplace = True)  
    print (game_similar_show)
    
# Enter your anime and number of games to be recommended 
get_recommendations("Tony Hawk's Pro Skater 3", topN = 10)
game_index["Tony Hawk's Pro Skater 3"]
    
############################# problem 2 ###################################

import pandas as pd


enmt_data = pd.read_csv("F:/assignment/recommondation system/Datasets_Recommendation Engine/Entertainment.csv", encoding= "utf8")
enmt_data.shape
enmt_data.columns

#term frequencey- inverse document frequncy is a numerical statistic that is intended 
#to reflect how important a word is to document in a collecion or corpus

from sklearn.feature_extraction.text import TfidfVectorizer
# Creating a Tfidf Vectorizer to remove all stop words
# taking stop words from tfid vectorizer 

tfidf = TfidfVectorizer(stop_words = 'english')

enmt_data.isna().sum()
enmt_data.isnull().sum()

# Preparing the Tfidf matrix by fitting and transforming
#Transform a count matrix to a normalized tf or tf-idf representation
tfidf_matrix = tfidf.fit_transform(enmt_data.Titles)
tfidf_matrix.shape

from sklearn.metrics.pairwise import linear_kernel

# Computing the cosine similarity on Tfidf matrix

cosine_sim_matrix = linear_kernel(tfidf_matrix,tfidf_matrix)
# creating a mapping of movie name to index number 
enmt_index = pd.Series(enmt_data.index, index = enmt_data['Titles'])
enmt_index = enmt_index[~enmt_index.index.duplicated(keep='first')]

enmt_id = enmt_index["Copycat (1995)"]
enmt_id

def get_recommendations(Name, topN):    
    # topN = 10
    # Getting the game index using its title 
    enmt_id = enmt_index[Name]
    
 # Getting the pair wise similarity score for all the game's with that 
    # game
    cosine_scores = list(enumerate(cosine_sim_matrix[enmt_id]))
    
    # Sorting the cosine_similarity scores based on scores 
    cosine_scores = sorted(cosine_scores, key=lambda x:x[1], reverse = True)
    
    # Get the scores of top N most similar movies 
    cosine_scores_N = cosine_scores[0: topN+1]
    
    # Getting the game index 
    enmt_idx  =  [i[0] for i in cosine_scores_N]
    enmt_scores =  [i[1] for i in cosine_scores_N]
    
    # Similar movies and scores
    enmt_similar_show = pd.DataFrame(columns=["name", "Score"])
    enmt_similar_show["name"] = enmt_data.iloc[enmt_idx,1]
    enmt_similar_show["Score"] = enmt_scores
    enmt_similar_show.reset_index(inplace = True)  
    print (enmt_similar_show)
    
# Enter your anime and number of movies to be recommended 
get_recommendations("Mighty Aphrodite (1995)", topN = 10)
enmt_index["Mighty Aphrodite (1995)"]

    
    
    