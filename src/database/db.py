from src.database.config import supabase
import bcrypt

def check_teacher_username(username):
    #check for unique username in the table, return false if username doest exist
    response = supabase.table("teachers").select("teacher_username").eq("teacher_username", username).execute()
    return len(response.data) > 0 

def hash_pass(pwd):
    return bcrypt.hashpw(pwd.encode(), bcrypt.gensalt()).decode()

def create_teacher(username, password, name):
    data = {"teacher_username" : username, "teacher_pass" : hash_pass(password), "teacher_name": name}
    response = supabase.table("teachers").insert(data).execute() 
    return response.data 

def check_pass(pwd, hashed):
    return bcrypt.checkpw(pwd.encode(), hashed.encode())

def teacher_login(username, password):
    response = supabase.table("teachers").select("*").eq("teacher_username", username).execute()
    if response.data:
        teacher = response.data[0]
        if check_pass(password, teacher["teacher_pass"]):
            return teacher
    return None

def get_all_students():
    response = supabase.table("students").select("*").execute()
    return response.data 

def create_student(new_name, face_embedding = None, voice_embedding = None):
     data = {"student_name" : new_name, "face_embedding" : face_embedding, "voice_embedding" : voice_embedding}
     response = supabase.table("students").insert(data).execute() 
     return response.data 

def create_subject(subject_code, subject_name, subject_section, teacher_id):
    data = {"subject_code" : subject_code, "subject_name": subject_name, "subject_section" : subject_section, "teacher_id" : teacher_id}
    response = supabase.table("subjects").insert(data).execute()
    return response.data

def get_teacher_subjects(teacher_id):
    response = supabase.table("subjects").select("*, subject_students(count), attendence_logs(timestamp)").eq("teacher_id", teacher_id).execute()
    subjects = response.data

    for sub in subjects:
        sub["total_students"] = sub.get("subject_students", [{}] )[0].get("count", 0) if sub.get("subject_students") else 0 
        attendence = sub.get("attendence_logs", [])
        unique_sessions = len(set(log["timestamp"] for log in attendence))
        sub["total_classes"] = unique_sessions

        sub.pop("subject_students", None)
        sub.pop("attendence_logs", None)

    return subjects