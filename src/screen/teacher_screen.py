import streamlit as st
from src.components.header import header_dashboard
from src.ui.base_layout import style_background_dashboard, style_base_layout
from src.components.footer import footer_dashboard
from src.components.subject_card import subject_card
from src.components.dialog_create_subject import create_subject_dialog
from src.database.db import check_teacher_username, create_teacher, teacher_login, get_teacher_subjects
import time
from src.components.dialog_create_subject import create_subject_dialog
from src.components.dialog_share_subject import subject_share_dialog

def teacher_screen():
    style_background_dashboard()
    style_base_layout()

    if "teacher_data" in st.session_state:
        teacher_dashboard()
    elif "teacher_login_type" not in st.session_state or st.session_state.teacher_login_type == "login":
        teacher_screen_login()
    elif st.session_state.teacher_login_type == "register":
        teacher_screen_register()




def register_teacher(teacher_username, teacher_password, teacher_password_confirm, teacher_name):
    if not teacher_username or not teacher_password or not teacher_name:
        return False, "All fields are required!"
    if check_teacher_username(teacher_username):
        return False, "Username already exist"
    if teacher_password != teacher_password_confirm:
        return False, "Password does't match"
    try:
        create_teacher(teacher_username, teacher_password, teacher_name)
        return True, "Sucessfully created, Login now"
    except Exception as e:
        return False, str(e)

def login_teacher(username, password):
    if not username or not password:
        return False
    teacher = teacher_login(username, password)
    if teacher:
        st.session_state.user_role = "teacher"
        st.session_state.teacher_data = teacher
        st.session_state.is_teacher = True
        return True
    return False










def teacher_dashboard():
    teacher_data = st.session_state.teacher_data
    c1, c2 = st.columns(2, vertical_alignment = "center", gap = "xxlarge")

    with c1:
        header_dashboard()

    with c2:
        st.subheader(f"""Welcome {teacher_data["teacher_name"]}""") 
        if st.button("Logout", type = "secondary", key="loginbackbtn", shortcut="control+backspace"):
            st.session_state["is_logged_in"] = False
            del st.session_state.current_teacher_tab
            st.rerun()

    st.space()

    def teacher_tab_take_attendence():
        st.header("Take AI attendence")
        
    def teacher_tab_manage_subject():
        #st.header("Manage attendence")
        teacher_id = st.session_state.teacher_data["teacher_id"]
        col1, col2 = st.columns(2)
        with col1:
            st.header("Manage Subjects", width = "stretch" )
        with col2:
            if st.button("Create new subjects", width = "content"):
                create_subject_dialog(teacher_id) 
            
            # List all created subjects
        subjects = get_teacher_subjects(teacher_id)
        if subjects:
            for sub in subjects:
                stats = [
                    ("🫂", "Students", sub["total_students"]),
                    ("🕰️", "Classes", sub["total_classes"]),
                ]

                def share_btn(subject):
                    def callback():
                        if st.button(
                            f"Share code: {subject['subject_name']}",
                            key=f"share_{subject['subject_code']}",
                            icon=":material/share:"
                        ):
                            subject_share_dialog(subject["subject_name"], subject["subject_code"])
                        st.space()
                    return callback

                subject_card(
                    name=sub["subject_name"],
                    code=sub["subject_code"],
                    section=sub["subject_section"],
                    stats=stats,
                    footer_callback=share_btn(sub)
                )
        else:
            st.info("NO SUBJECTS FOUND. CREATE ONE ABOVE")  

    def teacher_tab_attendence_record():
        st.header("Attendence record")

    if "current_teacher_tab" not in st.session_state:
        st.session_state.current_teacher_tab = "take_attendence"

    tab1, tab2, tab3 = st.columns(3)
    with tab1:
        type1 = "primary" if st.session_state.current_teacher_tab == "take_attendence" else "tertiary"
        if st.button("Take attendence", type = type1, width = "stretch", icon = ":material/ar_on_you:"):
            st.session_state.current_teacher_tab = "take_attendence"

    with tab2:
        type2 = "primary" if st.session_state.current_teacher_tab == "manage_subject" else "tertiary"
        if st.button("Manage subject", type = type2, width = "stretch", icon = ":material/ar_on_you:"):
            st.session_state.current_teacher_tab = "manage_subject"

    with tab3:
        type3 = "primary" if st.session_state.current_teacher_tab == "attendence_record" else "tertiary"
        if st.button("Attendence record", type = type3, width = "stretch", icon = ":material/ar_on_you:"):
            st.session_state.current_teacher_tab = "attendence_record"
        
    st.divider()

    if st.session_state.current_teacher_tab == "take_attendence":
        teacher_tab_take_attendence()
        
    if st.session_state.current_teacher_tab == "manage_subject":
        teacher_tab_manage_subject()
        
    if st.session_state.current_teacher_tab == "attendence_record":
        teacher_tab_attendence_record()

    

    footer_dashboard()











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
        if st.button("Login", icon = ":material/passkey:", shortcut="control+Enter", width = "stretch"):
            if login_teacher(teacher_username, teacher_pass):
                st.toast("Welcome back", icon = "👋")
                time.sleep(1)
                st.rerun()
            else:
                st.error("Incorrect username and password combo")

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
        if st.button("Register", type = "primary",  icon = ":material/passkey:", width = "stretch"):
            success, message = register_teacher(teacher_username, teacher_password, teacher_password_confirm, teacher_name)
            if success:
                st.success(message)
                time.sleep(2)
                st.session_state.teacher_login_type = "login"
                st.rerun()
            else:
                st.error(message)

    with btnc2:
        if st.button("Login Instead", icon = ":material/passkey:", shortcut="control+Enter", width = "stretch"):
            st.session_state.teacher_login_type = "login"

    footer_dashboard()