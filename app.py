import streamlit as st
import pickle
import pandas as pd
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances=similarity[index]
    movies_list = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movies=[]
    for i in movies_list:

        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

movies_dict=pickle.load(open('movie_list.pkl','rb'))

movies=pd.DataFrame(movies_dict)
similarity=pickle.load(open('similarity.pkl','rb'))

st.title('Movie recommender system')
selected_movie_name=st.selectbox(
    'How would you like to be connected?',
    movies['title'].values)
if st.button('Recommend'):
    recommendations=recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)



