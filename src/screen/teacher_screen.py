import streamlit as st
from src.components.header import header_dashboard
from src.ui.base_layout import style_background_dashboard, style_base_layout
from src.components.footer import footer_dashboard


def teacher_screen():
    style_background_dashboard()
    style_base_layout()

    if "teacher_login_type" not in st.session_state or st.session_state.teacher_login_type == "login":
        teacher_screen_login()
    elif st.session_state.teacher_login_type == "register":
        teacher_screen_register()


def teacher_screen_login():
    c1, c2 = st.columns(2, vertical_alignment = "center", gap = "xxlarge")

    with c1:
        header_dashboard()

    with c2:
        if st.button("Go back to home", type = "secondary", key="loginbackbtn", shortcut="control+backspace"):
            st.session_state["login_type"] = None
            st.rerun()

    st.header("login using password", text_alignment="center")
    st.space()
    st.space()
    teacher_username = st.text_input("Username", placeholder = "Jagpreet Singh")
    teacher_pass = st.text_input("Password", type = "password", placeholder = "Enter password")
    st.divider()

    btnc1, btnc2 = st.columns(2, vertical_alignment = "center",   gap="xxsmall")

    with btnc1:
        st.button("Login", icon = ":material/passkey:", shortcut="control+Enter", width = "stretch")

    with btnc2:
        if st.button("Register Instead", type = "primary",  icon = ":material/passkey:", width = "stretch"):
            st.session_state.teacher_login_type = "register" 

    footer_dashboard()


def teacher_screen_register():
    c1, c2 = st.columns(2, vertical_alignment = "center", gap = "xxlarge")

    with c1:
        header_dashboard()

    with c2:
        if st.button("Go back to home", type = "secondary", key="loginbackbtn", shortcut="control+backspace"):
            st.session_state["login_type"] = None
            st.rerun()
            
    st.header("Register your teacher profile", text_alignment="center")
    st.space()
    st.space()
    teacher_username = st.text_input("Enter username", placeholder = "jagpreet02")
    teacher_name = st.text_input("Enter name", placeholder = "Jagpreet Singh")
    teacher_password = st.text_input("Enter Password", type = "password", placeholder = "Set password")
    teacher_password_confirm = st.text_input("Confirm Password", type = "password", placeholder = "Confirm password" )
    st.divider()

    btnc1, btnc2 = st.columns(2, vertical_alignment = "center",   gap="xxsmall")

    with btnc1:
        st.button("Register", type = "primary",  icon = ":material/passkey:", width = "stretch")

    with btnc2:
        if st.button("Login Instead", icon = ":material/passkey:", shortcut="control+Enter", width = "stretch"):
            st.session_state.teacher_login_type = "login"

    footer_dashboard()