import streamlit as st
import pandas as pd
from datetime import datetime

# Page Config
st.set_page_config(
  page_title='Niks portofolio',
  page_icon='🚀',
  layout='wide'
)

# Custom CSS (optional - for styling)
st.markdown('''
                <style>  
                    .main-header {font-size: 42px; font-weight: bold; text-align:center;}
                    .sub-header {font-size: 24px; text-align:center; color: #666;}
                </style>
            ''', unsafe_allow_html=True)

# Sidebar
st.sidebar.title('📍Navigation')
page = st.sidebar.radio('Go to',
                        ['🏡 Home', '🚶🏾‍♂️ About', '📁 Projects', '🔧 Skills', '📝 Resume', '📩 Contact'])

# Home Page
if page == '🏡 Home':
  st.markdown('<p class="main-header">Nik Sil</p>', unsafe_allow_html=True)
  st.markdown('<p class="sub-header">Aspiring Tech Genius | Medgar Evers College</p>', unsafe_allow_html=True)

  # Three Columns for stats
  col1, col2, col3 = st.columns(3)

  with col1:
      st.metric('GPA', '3.8', '📚')
  with col2:
      st.metric('Projects', '5', '💻')
  with col3:
      st.metric('Skills', '10+', '🚀')

  st.write('---')

  # Introduction with columns
  col1, col2 = st.columns([2,1])
  with col1:
    st.subheader('Welcome to my digital space!👋')
    st.write('''
                I am a Computer Information Systems student passionate about web development and emerging technologies. Currently learning
                HTML, CSS, JavaScript, and Python to build innovative solutions.
            
                🎯 **Current Focus:** Building This Damn Website
            
                📚 **Currently Learning:** Internet and Emergin Technologies (CIS 211)
            
                💭 **Fun Fact:** I can swim!
            ''')
  with col2:
    # Placeholder for image
       st.image('ZombieManSpace.jpg', use_column_width=True)

# About Page
if page == '🚶🏾‍♂️ About':
    st.title('About Me')

  # Timeline of my Professional Journey
    st.subheader('My Journey 🗺️')

with st.expander('2025 - Present: Medgar Evers College'):
  st.write('''
              - Major: Stacking Bricks 🧱
              - Relevant Coursework: Internet & Emerging Technologies, Programming, Database Systems, AI
              - Activities: Ball Team, Track Team, Game Team, Music Team
          ''')

  with st.expander('2023 - 2025: NYC Museum School'):
    st.write('''
                - Graduated with stacking bricks
                - AP Computer Brick Stacker A (Score: 5)
                - Founded Get Rich Quick Club
            ''')

  st.subheader('Interests & Hobbies 🏀')
  interests = ['Web Development', 'AI/Machine Learning', 'Game Development', 'Basketball', 'Travel', 'Hockey']

  # Display the interests in columns
  cols = st.columns([1,2])
for i, interest in enumerate(interests):
with cols[i % 3]:
        st.info(f'💎 {interests}')
if page == '📂 Projects':
  st.title('My Projects')
st.write('Here are some projects ive worked on:')
