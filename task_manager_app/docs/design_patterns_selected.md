# design patterns considered:
## design pattern 1: singleton design pattern
### What problem does it solve? 
possible problem: what if a team of students wanted to use this task app to work on a project?
**this could have th following effects:**
- two or more people are updating the same task
-- which one shows up in the database?
- someone is working on a task and someone else deletes
-- does the task get recreated or deleted?
  
### Is it necessary, or would a basic implementation work? 
this feature is abosultely necessary for group projects for students working on colaborative assignments, which is common as CS majors.
- would a basic implementation work?
-- i am imamgining having only one student have access to the task app and he/she updates it while the others just view it
--- this would be like if someone else is already logged in then you only can view the task list not edit it.
-- i dont think it would work, becuase as CS majors we often code alone when we have time, and if we have to wait for someone to update the document before we complete tasks it is either going to be too slow, or two or more people would be complating duplicate tasks. i could just text the edititor to update it now, or create a group text, but then you are losing the major benefits of the app.
### Avoid forcing patterns—document alternatives considered.
- i am imamgining having only one student have access to the task app and he/she updates it while the others just view it
-- this would be like if someone else is already logged in then you only can view the task list not edit it.
 i dont think it would work, becuase as CS majors we often code alone when we have time, and if we have to wait for someone to update the document before we complete tasks it is either going to be too slow, or two or more people would be complating duplicate tasks. i could just text the edititor to update it now, or create a group text, but then you are losing the major benefits of the app.
---

## design pattern 2: adapter design pattern
### What problem does it solve? 
Allows for two classes to work that might not typically work due to code or format differences. It's like bringing a US outlet adapter to vacation in the EU. It allows for the outlet to still function while the adapter bridges the connection for these 2 very different outlet types. 
### Is it necessary, or would a basic implementation work? 
A basic implementation would work for the current project we are working on. There are benefits that I can think of, such as, adapting to different database formats to still properly display for the UI. Ultimately, a basic implementation would work.

---

## design pattern 3: Strategy design pattern
### What problem does it solve? 
One of the future features in our backlog is allowing the user to organize tasks in different ways, such as:

- Group Tasks by Priority Level
- Group Tasks by Classes
- Sort Tasks

Right now, our project follows an MVC structure where the Controller receives the request, the Service processes it, and the Repository retrieves the tasks from the database. That works well because we only have one way to display the task list.

But, by considering future features that add multiple possibilities for grouping and sorting tasks, there could be too many if/else statements required inside the Controller or Service classes to define the way in which the tasks will be grouped. The Strategy design pattern could help us implement an approach where we can encapsulate all the grouping algorithms within separate classes and make it easier to introduce new grouping possibilities.
### Is it necessary, or would a basic implementation work? 
For our current features, such as Add Task Description and Add Task Priority, a basic implementation works perfectly. These features only require adding new fields to the Task model and updating our current MVC flow (Controller → Service → Repository → Database). Using a design pattern there would probably be forcing it because our current architecture already handles those updates well.

The Strategy pattern starts making sense when we implement features like Group Tasks by Priority Level or Group Tasks by Classes. Those features require different ways of organizing the same list of tasks, which is exactly the type of problem the Strategy pattern was designed to solve.
### Avoid forcing patterns—document alternatives considered.
Considering the current architecture of our app, I do not believe that introducing the Strategy design pattern into all future features would be reasonable. For example, features such as Add Task Description and Add Task Priority fit very well within the MVC architecture that we currently use, so applying another design pattern would make the system more complicated.

Also, the solution using if/else statements inside the Controller or Service classes can be applied to task grouping, but after some time of adding new grouping and sorting operations, this solution will be difficult to support.

In my opinion, the Strategy pattern should only be considered when we develop the task grouping and sorting features since this is the place where several algorithms for managing one task list naturally appear.
