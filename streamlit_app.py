import streamlit as st
import pandas as pd
from datetime import datetime

# Page Config
st.set_page_config(
  page_title='Niks portofolio',
  page_icon='🚀',
  layout='wide'
)

# Adding New Font Test


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
                I am a aspiring future genius and entrepreneur currentlty studying at Medgar Evers College.
            
                🎯 **Current Focus:** Building This Damn Website
            
                📚 **Currently Learning:** Internet and Emergin Technologies (CIS 211)
            
                💭 **Fun Fact:** I can swim!
            ''')
  with col2:
    # Placeholder for image
    st.image('https://pbs.twimg.com/media/F1NDFmdXgAUHtoR.jpg', use_container_width=True)

# About Page
if page == '🚶🏾‍♂️ About':
    st.title('About Me')

    # Timeline of my Professional Journey
    st.subheader('My Professional Journey 🗺️')

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
    cols = st.columns(3)
    for i, interest in enumerate(interests):
        with cols[i % 3]:
            st.info(f'🏆 {interest}')

# Projects Page
if page == '📁 Projects':
    st.title('My Projects')
    st.write('Here are some projects Ive worked on:')

    # Project 1
    with st.container():
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image('https://cdn.mos.cms.futurecdn.net/kj3ZbACtQnnhFTB6nCMFUC-2000-80.jpg', use_column_width=True)
        with col2:
            st.subheader('🖥️ Pc-Building')
            st.write('Building a custom PC from scratch')
            st.caption('**Technologies:** Professional Tools, Electronics')

    # Project 2
    with st.container():
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image('https://cdn.sanity.io/images/atvntylo/production/0cd77247c5feb149ad710e311c6ed13c3c11a14f-2500x1406.webp', use_column_width=True)
        with col2:
            st.subheader('🌴 Mexico Trips, and Hotels')
            st.write('Planning and documenting trips to Mexico')
            st.caption('**Vacations:** Travel Planning, Photography')
    
    # Project 3
    with st.container():
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image('https://www.luxurybazaar.com/grey-market/wp-content/uploads/2025/06/TOP_TEN_WATCHES_61542.jpg', use_column_width=True)
        with col2:
            st.subheader('⌚ Watch Collection')
            st.write('Showcasing my collection of stylish watches')
            st.caption('**Collection:** Fashion, Timepieces')

# Skills Page
if page == '🔧 Skills':
    st.title('Life Skills')

    # Skills with progress bars
    st.subheader('Skill Progression')

    skills_data = {
        'Skate boarding': 85,
        'Swimming': 70,
        'Reading': 60,
        'Driving': 50,
        'Technical Writing': 40
    }

    for skill, level in skills_data.items():
        col1, col2 = st.columns([1, 3])
        with col1:
            st.write(skill)
        with col2:
            st.progress(level/100)

    st.subheader('Tools & Technologies')

    col1, col2, col3 = st.columns(3)
    with col1:
        st.success('Excel')
        st.info('Word')
        st.warning('Access')

    with col2:
        st.success('PowerPoint')
        st.info('Google Docs')
        st.warning('ChatGPT/AI Tools')

    with col3:
        st.success('Presentations')
        st.info('Writing')
        st.warning('Social Media')

# Resume Page
if page == '📝 Resume':
    st.title('Resume')
    st.write('My professional resume and experience:')
    st.info('Resume section coming soon! Download or view my full resume here.')

 # read PDF from my github 
    with open('my_resume1.pdf', 'rb') as pdf_file:
      PDFbyte = pdf_file.read()
    
    st.download_button(
      label ='🔼 Download My Resume here (PDF)',
      data = PDFbyte,
      file_name = 'my_resume1.pdf',
      mime ='application/pdf'
    )

# Contact Page
if page == '📩 Contact':
    st.title('Contact Me')
    st.write('Get in touch with me!')

    col1, col2 = st.columns(2)
    with col1:
        st.subheader('Connect with me')
        st.markdown('''
            📧 **Email:** [demnuts911@gmai.com](mailto:demnuts911@gmail.com)
            
            🔗 **LinkedIn:** [Your LinkedIn Profile](https://linkedin.com)
            
            💻 **GitHub:** [Your GitHub Profile](https://github.com/NikCoolMint)
            
            🐦 **Twitter:** [Your Twitter Handle](https://twitter.com)
        ''')

    with col2:
        st.subheader('Send me a message')
        with st.form('contact_form'):
            name = st.text_input('Your Name')
            email = st.text_input('Your Email')
            message = st.text_area('Your Message')
            submitted = st.form_submit_button('Send Message')
            if submitted:
                st.success('Thank you for your message! I will get back to you soon.')

        # Fun interactive element
        st.subheader('Current Status')

        status = st.selectbox(
            "I'm currently:",
            [
                'Available for work'
                'Open fr collabortations',
                'Just Chilling',
                'Learning something new'
            ]
        )
    

        st.info(f'status: {status}')

        # Footer
        st.write('---')
        st.markdown(
            f'<center>Made with ❤️ by Nik Sil | © {datetime.now().year} Nik Sil </center>', unsafe_allow_html = True
        )

