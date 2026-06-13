import streamlit as st

def header_home():
    img_url = "https://i.ibb.co/YTYGn5qV/logo.png"
    #st.write("HEADER UPDATED")
    st.markdown(f"""
        <div style = 
                "display : flex;
                flex-direction : column;
                align-items : center;
                justify-content : center;
                margin-bottom : 30px;
                margin-top : 30px">
            <img src = "{img_url}" style = "height:100px;" />
            <h1 style = "text-align : center; color: #E0E3FF">SNAP<br/>CLASS</h1> 
        </div>
                """, unsafe_allow_html=True)

def header_dashboard():
    img_url = "https://i.ibb.co/YTYGn5qV/logo.png"
   # st.header("SNAP CLASS")
    st.markdown(f"""
        <div style = 
                "display : flex;
                flex-direction : row;
                align-items : center;
                justify-content : center;
                gap : 10px;">
            <img src = "{img_url}" style = "height:85px;" />
            <h2 style =  "text-align : left; color: #5865F2">SNAP<br/>CLASS</h1>
        </div>
                """, unsafe_allow_html=True)
    
