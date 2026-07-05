import streamlit as st

def footer_home():
    img_url = "https://i.ibb.co/YTYGn5qV/logo.png"
    st.markdown(f"""
                <div style = "
                display : flex;
                gap : 6px;
                items-align: center;
                justify-content : center;
                margin-top : 2rem;"
        <p style = "font-weight: bold; color: !important"> Created with ❤️ by JS</p>
                </div>
                """, unsafe_allow_html=True)
def footer_dashboard():
    img_url = "https://i.ibb.co/YTYGn5qV/logo.png"
    st.markdown(f"""
                <div style = "
                display : flex;
                gap : 6px;
                items-align: center;
                justify-content : center;
                margin-top : 2rem;"
        <p style = "font-weight:  bold; color: !important"> Created with ❤️ by JS</p>
                </div>
                """, unsafe_allow_html=True)

