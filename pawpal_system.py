from __future__ import annotations

from datetime import datetime
from typing import List, Optional


class Owner:
    def __init__(self, id: str, name: str, email: str):
        self.id: str = id
        self.name: str = name
        self.email: str = email
        self.pets: List[Pet] = []

    def add_pet(self, pet: "Pet") -> None:
        pass

    def remove_pet(self, pet_id: str) -> None:
        pass

    def get_pets(self) -> List["Pet"]:
        pass


class Pet:
    def __init__(
        self,
        id: str,
        name: str,
        species: str,
        breed: str,
        owner: Owner,
        scheduler: "Scheduler",
    ):
        self.id: str = id
        self.name: str = name
        self.species: str = species
        self.breed: str = breed
        self.owner: Owner = owner
        self.scheduler: "Scheduler" = scheduler

    def add_task(self, task: "Task") -> None:
        pass

    def remove_task(self, task_id: str) -> None:
        pass

    def get_tasks(self) -> List["Task"]:
        pass


class Task:
    def __init__(
        self,
        id: str,
        title: str,
        description: str,
        due_date: datetime,
        pet: Pet,
    ):
        self.id: str = id
        self.title: str = title
        self.description: str = description
        self.due_date: datetime = due_date
        self.completed: bool = False
        self.pet: Pet = pet

    def mark_complete(self) -> None:
        pass

    def reschedule(self, new_date: datetime) -> None:
        pass


class Scheduler:
    def __init__(self):
        self.tasks: List[Task] = []

    def schedule_task(self, task: Task) -> None:
        pass

    def get_tasks_for_date(self, date: datetime) -> List[Task]:
        pass

    def get_tasks_for_pet(self, pet_id: str) -> List[Task]:
        pass

    def notify_upcoming_tasks(self) -> None:
        pass
