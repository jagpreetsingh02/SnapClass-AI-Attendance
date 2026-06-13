import streamlit as st

def subject_card(name, code, section, stats=None, footer_callback=None):
    html = f"""<div style="background:white; border-left: 8px solid #EB459E; padding: 25px; border-radius: 20px; border: 1px solid black; margin-bottom: 20px;">
<h3 style="margin:0; color:#1E293B; font-size:1.5rem;">{name}</h3>
<p style="color:#64748B; margin:10px 0;">Code: <span style="background:#E0E3FF; color:#5865F2; padding:2px 8px; border-radius:5px;">{code}</span> | Section: {section}</p>"""

    if stats:
        html += '<div style="display:flex; gap:8px; flex-wrap:wrap;">'
        for icon, label, value in stats:
            html += f'<div style="background:#EB459E10; padding:5px 12px; border-radius:12px; font-size:0.9rem;">{icon} <b>{value}</b> {label}</div>'
        html += "</div>"

    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)

    if footer_callback:
        footer_callback()


# import streamlit as st

# def subject_card(name, code, section, stats=None, footer_callback=None):

#     html = f"""
#     <div style="
#         background:white;
#         border-left:8px solid #EB459E;
#         padding:25px;
#         border-radius:20px;
#         border:1px solid black;
#         margin-bottom:20px;
#     ">
#         <h3 style="
#             margin:0;
#             color:#1E293B;
#             font-size:1.5rem;
#         ">
#             {name}
#         </h3>

#         <p style="
#             color:#64748B;
#             margin:10px 0;
#         ">
#             Code:
#             <span style="
#                 background:#E0E3FF;
#                 color:#5865F2;
#                 padding:2px 8px;
#                 border-radius:5px;
#             ">
#                 {code}
#             </span>
#             |
#             Section: {section}
#         </p>
#     """

#     if stats:
#         html += '<div style="margin-top:10px;">'

#         for icon, label, value in stats:
#             html += f"""
#             <span style="
#                 background:#EB459E10;
#                 padding:6px 12px;
#                 border-radius:12px;
#                 margin-right:8px;
#                 display:inline-block;
#                 margin-bottom:6px;
#                 color:#1E293B;
#             ">
#                 {icon} <b>{value}</b> {label}
#             </span>
#             """

#         html += "</div>"

#     # Close main card
#     html += "</div>"

#     st.markdown(html, unsafe_allow_html=True)

#     if footer_callback:
#         footer_callback()


# import streamlit as st

# def subject_card(name, code, section, stats=None, footer_callback=None):
#     # Base HTML structure
#     html = f"""
#     <div style="background:white; padding: 25px; border-radius: 20px; border: 1px solid #cbd5e1; border-left: 8px solid #EB459E; margin-bottom: 20px;">
#         <h3 style="margin:0; color: #1E293B; font-size: 1.5rem; font-family: sans-serif;">
#             {name}
#         </h3>
#         <p style="color: #64748B; margin: 15px 0; font-family: sans-serif;">
#             Code: 
#             <span style="background: #E0E3FF; color: #5865F2; padding: 2px 8px; border-radius: 5px; font-weight: bold;">
#                 {code}
#             </span>
#             | Section: {section}
#         </p>
#     """

#     # Append stats if they exist
#     if stats:
#         html += '<div style="display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 15px;">'
#         for icon, label, value in stats:
#             html += f"""
#             <div style="background: #EB459E10; color: #EB459E; padding: 6px 12px; border-radius: 12px; font-size: 0.9rem; font-family: sans-serif; font-weight: 500;">
#                 {icon} <b>{value}</b> {label}
#             </div>
#             """
#         html += "</div>"

#     # CRITICAL: Close the main outer container div
#     html += "</div>"

#     # Render the combined HTML safely
#     st.markdown(html, unsafe_allow_html=True)

#     # Execute your footer callback if provided
#     if footer_callback:
#         footer_callback()