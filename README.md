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