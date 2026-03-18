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
    """Represents a care task assigned to a pet."""
    id: str
    title: str
    description: str
    due_date: datetime
    completed: bool = False
    pet: Pet = None

    def mark_complete(self) -> None:
        self.completed = True

    def reschedule(self, new_date: datetime) -> None:
        self.due_date = new_date


class Scheduler:
    """Stores and retrieves scheduled pet tasks."""
    def __init__(self):
        self.tasks: List[Task] = []

    def schedule_task(self, task: Task) -> None:
        self.tasks.append(task)

    def get_tasks_for_date(self, date: datetime) -> List[Task]:
        return [t for t in self.tasks if t.due_date.date() == date.date()]

    def get_tasks_for_pet(self, pet_id: str) -> List[Task]:
        return [t for t in self.tasks if t.pet.id == pet_id]

    def notify_upcoming_tasks(self) -> None:
        # Simple notification: print upcoming tasks within the next 24 hours
        now = datetime.now()
        upcoming = [t for t in self.tasks if not t.completed and now <= t.due_date <= now + timedelta(days=1)]
        for task in upcoming:
            print(f"Upcoming task: {task.title} for {task.pet.name} at {task.due_date}")

