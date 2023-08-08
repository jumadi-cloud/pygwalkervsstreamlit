import streamlit as st 
import os
from streamlit_option_menu import option_menu
import streamlit.components.v1 as stc 
import pandas as pd 
import pygwalker as pyg 

# Page Configuration
st.set_page_config(
    page_title="PyGWalker - Demo",
    layout="wide",
    page_icon="👋"
)

# Load Data 
def load_data(data):
    return pd.read_csv(data)

# Save Data
def save_upload(uploadfile):
    with open(os.path.join("Doc", uploadfile.name), "wb") as f:
        f.write(uploadfile.getbuffer())

def main():
    # Navigasi
    selected = option_menu(None, ["PyGWalker", "About"], 
        icons=['house', "list-task"], 
        menu_icon="cast", default_index=0, orientation="horizontal",)

    if selected == "PyGWalker":
        # Form
        with st.form("upload_form"):
            data_file = st.file_uploader("Upload a CSV File",type=["csv","txt"])
            submitted = st.form_submit_button("Submit")

        if submitted:
            df = load_data(data_file)
            st.dataframe(df)
            # Visualize
            pyg_html = pyg.walk(df,return_html=True)
            # Render with components
            stc.html(pyg_html,scrolling=True,height=1000)
            save_upload(data_file)
        
    if selected == "About":
        st.markdown("""

        ### Apa Itu PyGWalker?
        PyGWalker adalah sebuah library JavaScript yang dapat digunakan untuk membuat tabel dan data yang interactive🥳.
        
        Untuk lebih detail bisa dilihat di [Dokumentasi resminya](https://docs.kanaries.net/pygwalker)
        
        ### Cara install PyGWalker?
                    pip install pygwalker
        ### PyGWalker Dapat Digunakan?
                    Suport:
                    Jupyter Notebook, 
                    Google Colab, 
                    Kaggle Code,
                    Jupyter Lab (WIP: A few pesky CSS bugs persist), Jupyter Lite,
                    Databricks Notebook (Since version 0.1.4a0),
                    Jupyter Extension for Visual Studio Code (Since version 0.1.4a0),
                    Hex Projects (Since version 0.1.4a0),
                    Most web applications in harmony with IPython kernels (Since version 0.1.4a0),
                    Streamlit (Since version 0.1.4.9), activated with pyg.walk(df, env='Streamlit'),
                    dan Lebih banyak lagi 🥳. 
        """, True)
        st.write("---")  
if __name__ == "__main__":
    main()