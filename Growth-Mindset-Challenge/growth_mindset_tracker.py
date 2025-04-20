import streamlit as st
import json
import os
from datetime import datetime
import pytz
import random

TODO_FILE = "todo.json"

# Load and Save Tasks
def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Motivational Quotes
QUOTES = [
    "Mistakes are proof you are trying.",
    "Believe in yourself and all that you are.",
    "Growth is never by mere chance; it is the result of forces working together.",
    "Success is the ability to go from one failure to another with no loss of enthusiasm.",
    "The expert in anything was once a beginner."
]

# App Title
st.set_page_config(page_title="Growth Mindset Tracker")
st.title("🌱 Growth Mindset Daily Tracker")

# Show time and quote
tz = pytz.timezone("Asia/Karachi")  # Change timezone if needed
current_time = datetime.now(tz).strftime("%A, %d %B %Y | %I:%M %p")
st.markdown(f"**🕒 Today is:** {current_time}")
st.info(f"💡 *Quote of the Day:* {random.choice(QUOTES)}")

# Daily Reflection
st.subheader("🧠 Reflect on Your Growth Today")
reflection = st.text_area("What did you learn today or what challenge did you overcome?")

# Add a new task
st.subheader("✅ Add Daily Goals / Tasks")
new_task = st.text_input("Enter a task or goal for today:")
if st.button("Add Task"):
    tasks = load_tasks()
    tasks.append({"task": new_task, "done": False})
    save_tasks(tasks)
    st.success("Task added!")

# Show all tasks
st.subheader("📋 Your Tasks")
tasks = load_tasks()
for i, task in enumerate(tasks):
    col1, col2 = st.columns([0.8, 0.2])
    with col1:
        st.text(task["task"])
    with col2:
        if not task["done"]:
            if st.button(f"✅ Complete {i}", key=f"done_{i}"):
                tasks[i]["done"] = True
                save_tasks(tasks)
                st.experimental_rerun()
        else:
            st.markdown("✅ Done")

# Optional: Save reflection
if reflection:
    if st.button("💾 Save Reflection"):
        with open("reflections.txt", "a") as f:
            f.write(f"{current_time}:\n{reflection}\n\n")
        st.success("Reflection saved successfully!")

