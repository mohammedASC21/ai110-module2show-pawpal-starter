from datetime import datetime

from pawpal_system import Owner, Pet, Task, Scheduler


def test_mark_complete_changes_task_status():
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

    initial_count = len(pet.get_tasks())

    task = Task(
        id="task1",
        title="Morning Walk",
        description="Take Buddy for a walk",
        due_date=datetime.now(),
        pet=pet,
    )

    pet.add_task(task)

    assert len(pet.get_tasks()) == initial_count + 1