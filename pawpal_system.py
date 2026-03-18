from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List, Optional


class Owner:
    """Represents a pet owner who manages multiple pets."""
    def __init__(self, id: str, name: str, email: str):
        self.id: str = id
        self.name: str = name
        self.email: str = email
        self.pets: List[Pet] = []

    def add_pet(self, pet: "Pet") -> None:
        if pet not in self.pets:
            self.pets.append(pet)

    def remove_pet(self, pet_id: str) -> None:
        self.pets = [pet for pet in self.pets if pet.id != pet_id]

    def get_pets(self) -> List["Pet"]:
        return self.pets


@dataclass
class Pet:

    """Represents a pet connected to an owner and scheduler."""

    id: str
    name: str
    species: str
    breed: str
    owner: Owner
    scheduler: "Scheduler"

    def add_task(self, task: "Task") -> None:
        self.scheduler.schedule_task(task)

    def remove_task(self, task_id: str) -> None:
        self.scheduler.tasks = [t for t in self.scheduler.tasks if t.id != task_id]

    def get_tasks(self) -> List["Task"]:
        return [t for t in self.scheduler.tasks if t.pet.id == self.id]


@dataclass
class Task:
    id: str
    title: str
    description: str
    due_date: datetime
    pet: Pet = None
    duration_minutes: int = 0
    priority: str = "medium"
    frequency: str = "once"
    completed: bool = False

    def mark_complete(self) -> None:
        self.completed = True

    def reschedule(self, new_date: datetime) -> None:
        self.due_date = new_date

@dataclass
class Scheduler:
    def __init__(self):
        self.tasks: List[Task] = []

    def schedule_task(self, task: Task) -> None:
        for existing in self.tasks:
            if (
                existing.title == task.title
                and existing.pet.id == task.pet.id
                and existing.due_date == task.due_date
            ):
                return
        self.tasks.append(task)

    def get_tasks_for_date(self, date: datetime) -> List[Task]:
        return [t for t in self.tasks if t.due_date.date() == date.date()]

    def get_tasks_for_pet(self, pet_id: str) -> List[Task]:
        return [t for t in self.tasks if t.pet.id == pet_id]

    def sort_by_time(self, tasks: Optional[List[Task]] = None) -> List[Task]:
        """Return tasks sorted by due date and time."""
        tasks_to_sort = tasks if tasks is not None else self.tasks
        return sorted(tasks_to_sort, key=lambda t: t.due_date)

    def filter_tasks(self, completed: Optional[bool] = None, pet_name: Optional[str] = None) -> List[Task]:
        """Filter tasks by completion status and/or pet name."""
        filtered = self.tasks

        if completed is not None:
            filtered = [task for task in filtered if task.completed == completed]

        if pet_name is not None:
            filtered = [task for task in filtered if task.pet.name.lower() == pet_name.lower()]

        return filtered

    def mark_task_complete(self, task_id: str) -> None:
        """Mark a task complete and create the next recurring task if needed."""
        for task in self.tasks:
            if task.id == task_id:
                task.mark_complete()

                if task.frequency == "daily":
                    new_task = Task(
                        id=f"{task.id}_next",
                        title=task.title,
                        description=task.description,
                        due_date=task.due_date + timedelta(days=1),
                        pet=task.pet,
                        frequency=task.frequency
                    )
                    self.tasks.append(new_task)

                elif task.frequency == "weekly":
                    new_task = Task(
                        id=f"{task.id}_next",
                        title=task.title,
                        description=task.description,
                        due_date=task.due_date + timedelta(weeks=1),
                        pet=task.pet,
                        frequency=task.frequency
                    )
                    self.tasks.append(new_task)
                return

    def detect_conflicts(self) -> List[str]:
        warnings = []
        sorted_tasks = self.sort_by_time()

        for i in range(len(sorted_tasks)):
            for j in range(i + 1, len(sorted_tasks)):
                if sorted_tasks[i].due_date == sorted_tasks[j].due_date:
                    warnings.append(
                        f"Conflict: '{sorted_tasks[i].title}' for {sorted_tasks[i].pet.name} "
                        f"and '{sorted_tasks[j].title}' for {sorted_tasks[j].pet.name} "
                        f"are both scheduled at {sorted_tasks[i].due_date.strftime('%Y-%m-%d %H:%M')}."
                    )
        return warnings

    def notify_upcoming_tasks(self) -> None:
        now = datetime.now()
        upcoming = [
            t for t in self.tasks
            if not t.completed and now <= t.due_date <= now + timedelta(days=1)
        ]
        for task in upcoming:
            print(f"Upcoming task: {task.title} for {task.pet.name} at {task.due_date}")
