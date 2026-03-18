# PawPal+ Project Reflection

## 1. System Design


My design centered on three main user actions which are adding a pet, adding or updating care tasks, and viewing a daily schedule. The user first enters pet information so the system knows who the tasks belong to. Then the user creates tasks such as feeding, walking, or medication, including details like duration and priority. Finally, the user can generate a daily plan that organizes those tasks based on time and importance.


**a. Initial design**

- Briefly describe your initial UML design.
My initial design focused on three core user actions : adding a pet, adding care tasks for a pet, and generating a daily schedule. I wanted the system to model the pet owner, each pet, the tasks for each pet, and a scheduler that organizes those tasks.

- What classes did you include, and what responsibilities did you assign to each?
I used four main classes such as Owner, Pet, Task, and Scheduler. Owner stores the user’s information and their pets. Pet stores pet details and its list of tasks. Task represents an individual care activity with information like title, duration, priority, and completion status. Scheduler is responsible for collecting tasks and building a daily plan in a logical order.

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.
Yes, my design changed during implementation. At first, I had two different places storing tasks which was that I had one inside the Scheduler and another inside each Pet. But when I asked Copilot I found out it could cause problems because the task lists might get out of sync if a task was updated in one place but not the other. In order to fix that, I changed the design so the Scheduler became the main place where tasks are managed. Instead of each Pet keeping its own separate task list, the pet now works with the scheduler. I made this change because it keeps the system simpler, more organized, and avoids mistakes from having duplicate task data.

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
My scheduler mainly considers time, task status, and which pet the task belongs to. It organizes tasks by due time so the schedule is shown in the correct order. It also checks whether a task is completed or not, and it can filter tasks for a specific pet when needed. For repeating care, it also considers whether a task is one-time, daily, or weekly.

- How did you decide which constraints mattered most?
I decided these constraints mattered most because they are the most useful for a pet care app. The owner needs to know what should be done first, which pet needs attention, and whether a task still needs to be completed. I focused on these because they make the schedule clear and practical without making the system too complicated.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
One tradeoff my scheduler makes is that conflict detection is very simple. It only checks if two tasks are scheduled at the exact same time instead of checking for more detailed overlaps in task duration.

- Why is that tradeoff reasonable for this scenario?
This tradeoff is reasonable for this scenario because the goal of the project is to build a simple and working pet care scheduler, not a highly advanced planning system. Using exact-time conflict detection keeps the code easier to understand and still helps catch obvious scheduling problems.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
I used AI tools during this project for design brainstorming, debugging, refactoring, and testing. In the beginning, AI helped me think through the main classes I needed, such as Owner, Pet, Task, and Scheduler, and helped me organize how they should work together. Later, I used AI to debug errors in my code, improve method structure, and create test cases for the scheduling features.

- What kinds of prompts or questions were most helpful?
The most helpful prompts were the ones that were specific and focused on one task at a time. For example, prompts asking how to connect the Streamlit UI to my backend classes, how to add conflict detection to the scheduler, or how to write pytest tests for sorting and filtering were very useful. 

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
One moment where I did not accept an AI suggestion as-is was when I was deciding how tasks should be stored in the system. An AI suggestion leaned toward one design approach, but I had to compare it with the project requirements and with how my own code was already structured. Instead of copying it directly, I adjusted the idea so it fit my scheduler design and worked better with the rest of my project.

- How did you evaluate or verify what the AI suggested?
I evaluated AI suggestions by testing them in my project, checking whether they matched the assignment instructions, and making sure the code actually worked with my existing classes. I also verified suggestions by running the app, checking the output in the UI, and using pytest to confirm that the backend features behaved correctly.




## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
I tested the main behaviors of the scheduler. My tests checked that a task can be marked as complete, adding a task to a pet increases that pet’s task count, tasks are sorted in the correct order by time, recurring tasks create a new future task when completed, conflicts are detected when two tasks are scheduled for the same time, and that filtering works by task status and pet name. I tested all of these behaviors effectively.

- Why were these tests important?
These tests were important because they cover the core features of the app. The scheduler depends on tasks being stored correctly, shown in the right order, repeated when needed, and flagged when there is a conflict. Testing these behaviors helped me make sure the main scheduling logic was working as expected.

**b. Confidence**

- How confident are you that your scheduler works correctly?
I am very confident that my scheduler works correctly. All 6 of my automated tests passed, and they cover the most important backend features of the system. Because of that, I gave the project a 5-star confidence level.

- What edge cases would you test next if you had more time?

If I had more time, I would test more edge cases. For example, I would test tasks with overlapping durations instead of only exact matching times, tasks scheduled across different days, and more cases involving recurring tasks such as weekly schedules over a longer period.

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?
The part of this project I am most satisfied with is Phase 1, the System Design and UML portion. I enjoyed that stage the most because it gave me the chance to use my own ideas and creativity to build the architecture behind the system. Instead of jumping straight into coding, I was able to think carefully about how the classes should connect, what responsibilities each part should have, and how the overall system should work. 

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?
If I had another iteration, I would improve the scheduler by making the conflict detection more advanced. Right now, it mainly checks for tasks that happen at the exact same time, but in a future version I would want it to also detect overlapping durations and give smarter scheduling suggestions.

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
One one important thing you learned about designing systems or working with AI on this project is that I should prioritize my own ideas and creativity when designing systems instead of depending too much on AI. AI can be very helpful for brainstorming, debugging but it should support my thinking rather than replace it.
