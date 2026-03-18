from pawpal_system import Owner, Pet, Task, Scheduler
from datetime import datetime, time

def main():
    scheduler = Scheduler()
    owner = Owner(id="owner1", name="John Doe", email="john@example.com")

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

    owner.add_pet(pet1)
    owner.add_pet(pet2)

    today = datetime.now().date()

    # Add tasks out of order
    task1 = Task(
        id="task1",
        title="Evening Play",
        description="Play with Buddy for 20 minutes",
        due_date=datetime.combine(today, time(18, 0)),
        pet=pet1,
        frequency="once"
    )
    task2 = Task(
        id="task2",
        title="Morning Walk",
        description="Take Buddy for a 30-minute walk",
        due_date=datetime.combine(today, time(8, 0)),
        pet=pet1,
        frequency="daily"
    )
    task3 = Task(
        id="task3",
        title="Feed Cat",
        description="Feed Whiskers with wet food",
        due_date=datetime.combine(today, time(12, 0)),
        pet=pet2,
        frequency="daily"
    )

    # Conflict task: same time as Feed Cat
    task4 = Task(
        id="task4",
        title="Vet Reminder",
        description="Check Whiskers' medicine",
        due_date=datetime.combine(today, time(12, 0)),
        pet=pet2,
        frequency="once"
    )

    pet1.add_task(task1)
    pet1.add_task(task2)
    pet2.add_task(task3)
    pet2.add_task(task4)

    print(f"Today's Schedule for {owner.name}:")
    print("=" * 40)

    todays_tasks = scheduler.get_tasks_for_date(datetime.now())
    sorted_tasks = scheduler.sort_by_time(todays_tasks)

    for task in sorted_tasks:
        status = "Completed" if task.completed else "Pending"
        print(f"- {task.due_date.strftime('%H:%M')}: {task.title} ({task.pet.name}) - {status}")

    print("\nIncomplete tasks for Buddy:")
    buddy_tasks = scheduler.filter_tasks(completed=False, pet_name="Buddy")
    for task in scheduler.sort_by_time(buddy_tasks):
        print(f"- {task.title} at {task.due_date.strftime('%H:%M')}")

    print("\nMarking Morning Walk complete...")
    scheduler.mark_task_complete("task2")

    print("\nConflict Warnings:")
    warnings = scheduler.detect_conflicts()
    if warnings:
        for warning in warnings:
            print(warning)
    else:
        print("No conflicts found.")

    print("\nAll tasks after recurrence logic:")
    for task in scheduler.sort_by_time():
        print(
            f"- {task.due_date.strftime('%Y-%m-%d %H:%M')} | "
            f"{task.title} | {task.pet.name} | completed={task.completed} | frequency={task.frequency}"
        )

if __name__ == "__main__":
    main()