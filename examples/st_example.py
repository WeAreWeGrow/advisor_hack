# You may need to install additional libraries to run this example.
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    st.title('Comprehensive Streamlit Application Demo')

    # Sidebar widgets
    st.sidebar.header('Sidebar Options')
    selectbox_option = st.sidebar.selectbox('Select a number', options=list(range(1, 11)), index=0)
    slider_val = st.sidebar.slider('Select a range', min_value=0, max_value=100, value=(25, 75))

    # Display selections
    st.write('Selected number from sidebar:', selectbox_option)
    st.write('Selected range from sidebar:', slider_val)

    # Text input
    name = st.text_input('Enter your name:', 'John Doe')
    st.write('Hello,', name)

    # Data file upload
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write(df)
        
        # Data visualization
        st.subheader('Data Visualization')
        st.line_chart(df.select_dtypes(include=np.number))

    # Interactive widgets
    if st.button('Click Me'):
        st.write('Button clicked!')

    checkbox_val = st.checkbox('Check me out')
    if checkbox_val:
        st.write('Checkbox is checked!')

    # Using containers and columns for layout
    st.subheader('Layouts with Containers and Columns')
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header('A cat')
        st.image('https://via.placeholder.com/150')
    with col2:
        st.header('A dog')
        st.image('https://via.placeholder.com/150')
    with col3:
        st.header('An owl')
        st.image('https://via.placeholder.com/150')

    # Expander
    with st.expander("See explanation"):
        st.write("""
            This is a detailed explanation of something. You can put any content inside an expander, 
            including text, images, and even other interactive widgets. Expanders are useful for keeping 
            the UI clean and uncluttered.
        """)

    # Color picker
    color = st.color_picker('Pick A Color', '#00f900')
    st.write('Selected Color:', color)

    # Plotting with matplotlib
    st.subheader('Plotting with Matplotlib')
    fig, ax = plt.subplots()
    sns.histplot(np.random.randn(1000), bins=30, kde=True, ax=ax)
    st.pyplot(fig)

if __name__ == "__main__":
    main()
