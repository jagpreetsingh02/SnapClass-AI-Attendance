import streamlit as st


from src.screen.home_screen import home_screen
from src.screen.student_screen import student_screen
from src.screen.teacher_screen import teacher_screen

def main():
    if "login_type" not in st.session_state:
        st.session_state["login_type"] = None

 #   st.write("Current login_type:", st.session_state["login_type"])
    #st.header("jagpreet")
    match st.session_state["login_type"]:
        case "teacher":
            teacher_screen()
        
        case "student":
            student_screen()

        case None:
            home_screen()
main()