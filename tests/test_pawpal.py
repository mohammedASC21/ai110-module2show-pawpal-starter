from datetime import datetime, timedelta

from pawpal_system import Owner, Pet, Task, Scheduler


def make_sample_pet():
    scheduler = Scheduler()
    owner = Owner(id="owner1", name="John Doe", email="john@example.com")
    pet = Pet(
        id="pet1",
        name="Buddy",
        species="Dog",
        breed="Golden Retriever",
        owner=owner,
        scheduler=scheduler,
    )
    owner.add_pet(pet)
    return scheduler, owner, pet


def test_mark_complete_changes_task_status():
    scheduler, owner, pet = make_sample_pet()

    task = Task(
        id="task1",
        title="Morning Walk",
        description="Take Buddy for a walk",
        due_date=datetime.now(),
        pet=pet,
    )

    assert task.completed is False
    task.mark_complete()
    assert task.completed is True


def test_adding_task_to_pet_increases_task_count():
    scheduler, owner, pet = make_sample_pet()

    initial_count = len(pet.get_tasks())

    task = Task(
        id="task1",
        title="Feed Buddy",
        description="Give breakfast",
        due_date=datetime.now(),
        pet=pet,
    )

    pet.add_task(task)

    assert len(pet.get_tasks()) == initial_count + 1


def test_sort_by_time_returns_tasks_in_order():
    scheduler, owner, pet = make_sample_pet()

    now = datetime.now().replace(second=0, microsecond=0)

    task1 = Task(
        id="task1",
        title="Evening Play",
        description="Playtime",
        due_date=now + timedelta(hours=5),
        pet=pet,
    )
    task2 = Task(
        id="task2",
        title="Morning Walk",
        description="Walk",
        due_date=now + timedelta(hours=1),
        pet=pet,
    )
    task3 = Task(
        id="task3",
        title="Lunch",
        description="Food",
        due_date=now + timedelta(hours=3),
        pet=pet,
    )

    pet.add_task(task1)
    pet.add_task(task2)
    pet.add_task(task3)

    sorted_tasks = scheduler.sort_by_time()

    assert [task.id for task in sorted_tasks] == ["task2", "task3", "task1"]


def test_daily_recurrence_creates_next_task():
    scheduler, owner, pet = make_sample_pet()

    due = datetime.now().replace(second=0, microsecond=0)

    task = Task(
        id="task1",
        title="Daily Medicine",
        description="Give medicine",
        due_date=due,
        pet=pet,
        frequency="daily",
    )

    pet.add_task(task)
    scheduler.mark_task_complete("task1")

    assert task.completed is True
    assert len(scheduler.tasks) == 2
    new_task = scheduler.tasks[1]
    assert new_task.title == "Daily Medicine"
    assert new_task.completed is False
    assert new_task.due_date.date() == (due + timedelta(days=1)).date()


def test_conflict_detection_flags_same_time_tasks():
    scheduler, owner, pet = make_sample_pet()

    due = datetime.now().replace(second=0, microsecond=0)

    task1 = Task(
        id="task1",
        title="Walk",
        description="Morning walk",
        due_date=due,
        pet=pet,
    )
    task2 = Task(
        id="task2",
        title="Vet Reminder",
        description="Checkup reminder",
        due_date=due,
        pet=pet,
    )

    pet.add_task(task1)
    pet.add_task(task2)

    warnings = scheduler.detect_conflicts()

    assert len(warnings) >= 1
    assert "Conflict" in warnings[0]

def test_filter_tasks_by_status_and_pet_name():
    scheduler, owner, pet1 = make_sample_pet()

    pet2 = Pet(
        id="pet2",
        name="Luna",
        species="Cat",
        breed="Siamese",
        owner=owner,
        scheduler=scheduler,
    )
    owner.add_pet(pet2)

    task1 = Task(
        id="task1",
        title="Morning Walk",
        description="Walk Buddy",
        due_date=datetime.now(),
        pet=pet1,
    )
    task2 = Task(
        id="task2",
        title="Feed Buddy",
        description="Give Buddy breakfast",
        due_date=datetime.now(),
        pet=pet1,
    )
    task3 = Task(
        id="task3",
        title="Feed Luna",
        description="Give Luna food",
        due_date=datetime.now(),
        pet=pet2,
    )

    pet1.add_task(task1)
    pet1.add_task(task2)
    pet2.add_task(task3)

    task1.mark_complete()

    incomplete_tasks = scheduler.filter_tasks(completed=False)
    buddy_tasks = scheduler.filter_tasks(pet_name="Buddy")
    completed_buddy_tasks = scheduler.filter_tasks(completed=True, pet_name="Buddy")

    assert len(incomplete_tasks) == 2
    assert len(buddy_tasks) == 2
    assert len(completed_buddy_tasks) == 1
    assert completed_buddy_tasks[0].title == "Morning Walk"