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
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
