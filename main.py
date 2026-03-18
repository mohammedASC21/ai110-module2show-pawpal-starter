from pawpal_system import Owner, Pet, Task, Scheduler
from datetime import datetime, time

def main():
    # Create a scheduler
    scheduler = Scheduler()

    # Create an owner
    owner = Owner(id="owner1", name="John Doe", email="john@example.com")

    # Create two pets
    pet1 = Pet(
        id="pet1",
        name="Buddy",
        species="Dog",
        breed="Golden Retriever",
        owner=owner,
        scheduler=scheduler
    )
    pet2 = Pet(
        id="pet2",
        name="Whiskers",
        species="Cat",
        breed="Siamese",
        owner=owner,
        scheduler=scheduler
    )

    # Add pets to owner
    owner.add_pet(pet1)
    owner.add_pet(pet2)

    # Create three tasks for today
    today = datetime.now().date()
    task1 = Task(
        id="task1",
        title="Morning Walk",
        description="Take Buddy for a 30-minute walk",
        due_date=datetime.combine(today, time(8, 0)),
        pet=pet1
    )
    task2 = Task(
        id="task2",
        title="Feed Cat",
        description="Feed Whiskers with wet food",
        due_date=datetime.combine(today, time(12, 0)),
        pet=pet2
    )
    task3 = Task(
        id="task3",
        title="Evening Play",
        description="Play with Buddy for 20 minutes",
        due_date=datetime.combine(today, time(18, 0)),
        pet=pet1
    )

    # Schedule tasks
    pet1.add_task(task1)
    pet2.add_task(task2)
    pet1.add_task(task3)

    # Get today's schedule
    todays_tasks = scheduler.get_tasks_for_date(datetime.now())

    # Print the schedule clearly
    print(f"Today's Schedule for {owner.name}:")
    print("=" * 40)
    if not todays_tasks:
        print("No tasks scheduled for today.")
    else:
        for task in sorted(todays_tasks, key=lambda t: t.due_date):
            status = "Completed" if task.completed else "Pending"
            print(f"- {task.due_date.strftime('%H:%M')}: {task.title} ({task.pet.name}) - {status}")
            print(f"  Description: {task.description}")
            print()

if __name__ == "__main__":
    main()