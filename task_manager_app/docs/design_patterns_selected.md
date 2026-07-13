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

## design pattern 3: __________ design pattern
### What problem does it solve? 
### Is it necessary, or would a basic implementation work? 
### Avoid forcing patterns—document alternatives considered.
