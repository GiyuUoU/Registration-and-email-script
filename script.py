import streamlit as st
import smtplib
from email.mime.text import MIMEText

# Email Credentials (Replace with your actual credentials)
EMAIL = "uninotify451@gmail.com"
PASSWORD = "emfh fqmw yogm fyyf"

st.title("Registration Form")
st.write("Please fill in the form below")

# Event Options
event_options = {
    "Recall-O-Tune 🎶🧠": "Music event confirmation",
    "CodeX 💻👨🏻‍💻": "Coding competition details",
    "Free Fire 🎮🔥": "Gaming tournament schedule",
    "BGMI 🎮⚔": "BGMI battle details",
    "Robo दौड़ 🤖🏃": "Robot race instructions",
    "Robo फ़ुटबॉल 🤖⚽": "Robot football match details",
    "Robo War 🤖🪖": "Robot war guidelines",
    "Drone Race 🛸🏃🏻": "Drone race participation info",
    "Reasoning Rumble 🧩🤓": "Reasoning challenge details",
    "Boat Race 🚤🌊": "Boat race competition info",
    "Find the Language 💻🔍": "Language guessing game details",
    "Hack-a-thon 💻🚀": "Hackathon registration confirmation",
    "Digi Art 🎨🖥": "Digital art submission details",
    "Structromania 🏗🧩": "Structure building contest guidelines",
    "Laser Light Show 🪩🎵": "Laser light show participation info",
    "Path Finder Robot 🤖🔍": "Pathfinding robot competition",
    "Rubik's Cube 🔳🎲": "Rubik’s Cube challenge details",
    "Buddhi क्षमता 🧠🔮": "Mind game competition info",
    "Bug Hunting 🐛🔍": "Bug hunting competition rules",
    "AI Workshop (Generative AI) 🤖🖼 / Power BI Workshop 📊⚙": "Workshop schedule and details",
    "Workshop on Configuring the Network Layers 🌐🛠": "Network layers workshop information"
}

# Form Inputs
with st.form(key="user_info_form"):
    name = st.text_input("Name")
    course = st.text_input("Course")
    roll_no = st.text_input("Roll Number")
    contact = st.text_input("Contact Number")
    email = st.text_input("Email")
    event_selected = st.multiselect("Select Event(s)", list(event_options.keys()))
    
    submitted = st.form_submit_button("Register")
    
    if submitted:
        if not all([name, course, roll_no, contact, email]) or not event_selected:
            st.warning("Please fill all the sections and select at least one event!")
        else:
            # Sending Email
            try:
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()
                server.login(EMAIL, PASSWORD)
                
                for event in event_selected:
                    subject = f"Registration Confirmation: {event}"
                    message = f"Hello {name},\n\nYour registration for {event} has been successfully completed!\n{event_options[event]}\n\nRegards,\nEvent Team"
                    
                    msg = MIMEText(message, "plain", "utf-8")
                    msg["Subject"] = subject
                    msg["From"] = EMAIL
                    msg["To"] = email
                    
                    server.sendmail(EMAIL, email, msg.as_string())
                
                server.quit()
                
                st.success(f"Registration successful! Confirmation emails have been sent for selected events to {email}.")
            except Exception as e:
                st.error(f"Failed to send email: {e}")
