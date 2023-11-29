'''
Achmad Dhani

Objective : Creating a main page of the webapps.
'''

import streamlit as st
import eda
import model

# navigating pages
page = st.sidebar.selectbox(label='Select Page:', options=['Home Page', 'Exploration Data Analysis', 'Emotion Classification'])

if page == 'Home Page':
    st.header('Home Page') 
    st.write('')
    st.write('Phase 2 Graded Challenge 7')
    st.write('Name      : Achmad Dhani')
    st.write('Batch     : HCK-009')
    st.markdown('Dataset: [Emotion Dataset](https://www.kaggle.com/datasets/abdallahwagih/emotion-dataset)')
    st.write("Objective : Mental health is important and a lot of people either doubt or confused regarding in what they are feeling. Validation helps as a reassurance for a lot of people, giving them affirmation by knowing that others shares those same feelings. Employing NLP machine learning with high accuracy will efficiently classify emotions in the hopes to make a person's day a brighter.")
    st.write('')
    st.caption('Please pick the options in the Select Page Box located on the left of the screen to start!')
    st.write('')
    st.write('')
    
#============================= Background Info ==========================
    
    with st.expander("Background Information"):
        st.caption("The dataset is obtained from keggle. It has 5937 entries with 2 object columns. The columns consist of data of people's comments and their each respective emotion")
        
#============================= Work Flow ================================
    
    with st.expander("Work Flow"):
        st.caption(
        '''
            - Data loading from keggle
            - Basic Analysis
            - EDA on most common words
            - Text processing in feature engineering
            - Vectorization
            - Building the models
            - Tuning the models
            - Inference
            - Deployment
        '''
        )

#============================= Conclussion =================================
    with st.expander("Conclusion"): # conclusion
        st.caption(
            '''
            The dataset is well maintained and has a balance target class. EDA shows that most people are quite concise when it comes to expressing their feelings, only a few whom can write really long and be more open about what they feel. Life, good, day, something, going and well are words that are most often expressed when people describe a joyful experience. Would, even, way, think, and angry are words that's the most often expressed when a person is mad. Still, bit, strange, ank think are words that is most often expressed when a person describing a fearful experience. Anger and fear are a special case. Anger words such as 'would' and 'even' is an auxillary verb that indicates a mood or tense. Fear is a broad emotion where it can classify into fear of the unknown that involes anxiety and fear as if being scared or teriffied, giving goosebumps. The best model uses LSTM network with 93% accuracy. There still seems to be a lot of noise therefor, focusing on preprocessing such as adding more stopwords could help the model learn patterns more accurately in the future. The dataset currently includes just three emotions, but incorporating data on a wider range of emotions would enhance the model's ability to classify more diverse emotional states.
            '''
        )

#============================ Other Page ======================================
elif page == 'Exploration Data Analysis':
    eda.run()
else:
     model.run()
