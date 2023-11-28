'''
===============================================
Phase 2 Graded Challenge 7

Achmad Dhani

HCK-009

Objective: Creating a page for NLP Exploratory Data Analysis
'''

import streamlit as st
import pandas as pd
from PIL import Image
import plotly.express as px

def run():
    '''
    Function for EDA page
    '''
    st.title('Exploration Data Analysis Section')
# ============================= Showing Data ==========================
    df = pd.read_csv('Emotion_classify_Data.csv')
    horizontal_radio_css = """<style>div.row-widget.stRadio > div{flex-direction:row;}</style>"""
    st.markdown(horizontal_radio_css, unsafe_allow_html=True)
    data_show = st.radio("**Viewing Options**", ['Top 10 Entries', 'Bottom 10 Entries'])
    if data_show == 'Top 10 Entries':
        st.table(df.head(10))
    else:
        st.table(df.tail(10))
# ============================= Simple Analysis ========================

    eda=pd.read_csv('eda.csv')
    
    # basic summary analysis
    emotion_counts = eda['Emotion'].value_counts()
    
    eda['Comment Length'] = eda['Comment'].apply(len)
    eda['Word Count'] = eda['Comment'].apply(lambda x: len(x.split()))
    
    # emotion distribution
    fig_emotions = px.bar(emotion_counts,
                          x=emotion_counts.index,
                          y=emotion_counts.values,
                          labels={'x': 'Emotion', 'y': 'Count'},
                          title='Distribution of Emotions')
    fig_emotions.update_traces(marker_line_width=1, marker_line_color='black')
    fig_emotions.update_layout(xaxis_title='Emotions', yaxis_title='Count', width=700)
    
    # comment distribution
    fig_comment_length = px.histogram(eda,
                                      x='Comment Length',
                                      nbins=30,
                                      marginal='box',
                                      title='Distribution of Comment Length')
    fig_comment_length.update_traces(marker_line_width=1, marker_line_color='black')
    fig_comment_length.update_layout(xaxis_title='Length of Comment', yaxis_title='Count', width=700, bargap=0)
    
    # word count distribution
    fig_word_count = px.histogram(eda,
                                  x='Word Count',
                                  nbins=30,
                                  marginal='box',
                                  title='Distribution of Word Count')
    fig_word_count.update_traces(marker_line_width=1, marker_line_color='black')
    fig_word_count.update_layout(xaxis_title='Word Count', yaxis_title='Count', width=700)
    
    # Display the figures in Streamlit
    st.plotly_chart(fig_emotions)
    st.plotly_chart(fig_comment_length)
    st.plotly_chart(fig_word_count)
    with st.expander('Explanation'):
        st.caption(
            '''
            The visualization above shows:
            - The dataset has a balance target class which are `anger, joy, and fear`
            - The distribution of comment length skewed to the right with the majority of the data is within `30 to 130` comment length
            - The outliers are the comment lengths that is above `244`
            - The same goes to the word count, the distribution is skewed to the right with the majority of the data is within the range of `5 to 30` word count
            - This gives insight about how expressive the people are in the dataset. Most people quite concise but there are a few who's very expressive and open about what they feel.
            '''
            )
# ============================= Joy Word Cloud ==================================
    st.subheader('Joy Word Cloud')
    image1 = Image.open('joy_wordcloud.png')
    st.image(image1, caption='Figure 1 Joy Emotion Word Cloud',  width=700)

    # explaination
    with st.expander('Explanation'):
        st.caption(
            '''
            The Joy word cloud highlights commonly used words associated with feelings of joy, such as `life, good, day, something, going, and well`, indicating that these terms are often expressed when people describe joyful experiences.
            '''
            )

# ============================= Anger Word Cloud =====================================

    st.subheader('Anger Word Cloud')
    image2 = Image.open('anger_wordcloud.png')
    st.image(image2, caption='Figure 2 Anger Emotion Word Cloud',  width=700)

    # explaination
    with st.expander('Explanation'):
        st.caption(
            '''
            The Anger word cloud highlights commonly used words associated with feelings of anger, such as would, even, way, think, angry, indicating that these terms mostly expressed when people are angry. Anger is a special case where, words like would and even is an auxiliary verb, which indicates a mood or tense.
            '''
            )

# =============================== Fear Word Cloud ====================================

    st.subheader('Fear Word Cloud')
    image3 = Image.open('fear_wordcloud.png')
    st.image(image3, caption='Figure 3 Fear Emotion Word Cloud',  width=700)

    # explaination
    with st.expander('Explanation'):
        st.caption(
            '''
            The Fear word cloud highlights commonly used words associated with feelings of fear, such as `still, bit, strange, think`, indicating that these terms are often expressed when people describing or more accurately worriness and anxiousness. This is justified since fear in the context of fear of the unknown is believe to cause worriness and anxiousness on a person. Fear is a broad emotion that can be more interpreted two ways, fear of the unknown that cause anxiety or being scared/teriffied and giving goosebumps.
            '''
            )