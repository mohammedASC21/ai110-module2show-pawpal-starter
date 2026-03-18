import streamlit as st
from datetime import datetime, date, time
from uuid import uuid4

from pawpal_system import Owner, Pet, Task, Scheduler


st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")
st.title("🐾 PawPal+")


def init_state():
    if "scheduler" not in st.session_state:
        st.session_state.scheduler = Scheduler()

    if "owner" not in st.session_state:
        st.session_state.owner = Owner(
            id="owner1",
            name="Jordan",
            email="jordan@example.com"
        )


init_state()

owner = st.session_state.owner
scheduler = st.session_state.scheduler

st.markdown("Plan pet care tasks and generate today’s schedule.")

st.divider()

# -----------------------------
# Owner section
# -----------------------------
st.subheader("Owner Info")

owner_name = st.text_input("Owner name", value=owner.name)
owner_email = st.text_input("Owner email", value=owner.email)

# keep owner object updated
owner.name = owner_name
owner.email = owner_email

st.divider()

# -----------------------------
# Add pet section
# -----------------------------
st.subheader("Add a Pet")

pet_name = st.text_input("Pet name")
species = st.selectbox("Species", ["Dog", "Cat", "Other"])
breed = st.text_input("Breed")

if st.button("Add Pet"):
    if not pet_name.strip():
        st.warning("Please enter a pet name.")
    else:
        new_pet = Pet(
            id=str(uuid4()),
            name=pet_name.strip(),
            species=species,
            breed=breed.strip() if breed.strip() else "Unknown",
            owner=owner,
            scheduler=scheduler
        )
        owner.add_pet(new_pet)
        st.success(f"{new_pet.name} was added.")

# show pets
if owner.get_pets():
    st.markdown("### Current Pets")
    pet_rows = []
    for pet in owner.get_pets():
        pet_rows.append({
            "Name": pet.name,
            "Species": pet.species,
            "Breed": pet.breed
        })
    st.table(pet_rows)
else:
    st.info("No pets added yet.")

st.divider()

# -----------------------------
# Add task section
# -----------------------------
st.subheader("Add a Task")

pets = owner.get_pets()

if not pets:
    st.warning("Add a pet first before creating tasks.")
else:
    pet_options = {f"{pet.name} ({pet.species})": pet for pet in pets}
    selected_pet_label = st.selectbox("Choose pet", list(pet_options.keys()))
    selected_pet = pet_options[selected_pet_label]

    task_title = st.text_input("Task title", value="Morning walk")
    task_description = st.text_area("Task description", value="Take pet outside for exercise")
    task_date = st.date_input("Task date", value=date.today())
    task_time = st.time_input("Task time", value=time(8, 0))
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
    priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)

    if st.button("Add Task"):
        if not task_title.strip():
            st.warning("Please enter a task title.")
        else:
            due_date = datetime.combine(task_date, task_time)

            new_task = Task(
                id=str(uuid4()),
                title=task_title.strip(),
                description=task_description.strip(),
                due_date=due_date,
                pet=selected_pet,
                duration_minutes=int(duration),
                priority=priority
            )

            selected_pet.add_task(new_task)
            st.success(f"Task '{new_task.title}' added for {selected_pet.name}.")

# show all tasks
if scheduler.tasks:
    st.markdown("### Current Tasks")
    task_rows = []
    for task in sorted(scheduler.tasks, key=lambda t: t.due_date):
        task_rows.append({
            "Time": task.due_date.strftime("%Y-%m-%d %H:%M"),
            "Task": task.title,
            "Pet": task.pet.name,
            "Duration": task.duration_minutes,
            "Priority": task.priority,
            "Status": "Completed" if task.completed else "Pending"
        })
    st.table(task_rows)
else:
    st.info("No tasks added yet.")

st.divider()

# -----------------------------
# Generate today's schedule
# -----------------------------
st.subheader("Today's Schedule")

if st.button("Generate Schedule"):
    todays_tasks = scheduler.get_tasks_for_date(datetime.now())
    todays_tasks = sorted(todays_tasks, key=lambda t: t.due_date)

    if not todays_tasks:
        st.warning("No tasks scheduled for today.")
    else:
        schedule_rows = []
        for task in todays_tasks:
            schedule_rows.append({
                "Time": task.due_date.strftime("%H:%M"),
                "Task": task.title,
                "Pet": task.pet.name,
                "Duration": task.duration_minutes,
                "Priority": task.priority,
                "Status": "Completed" if task.completed else "Pending"
            })

        st.success("Schedule generated successfully.")
        st.table(schedule_rows)

conflicts = scheduler.detect_conflicts()

if conflicts:
    for warning in conflicts:
        st.warning(warning)