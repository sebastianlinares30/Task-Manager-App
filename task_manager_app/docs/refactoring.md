## Authentication and Task Ownership

### Issue
The application relied on a user ID provided by the browser to identify the current user. Passwords were also stored and compared as plain text.

### Improvement
Flask sessions were implemented to identify the authenticated user on the server. Password hashing was added so passwords are no longer stored as plain text. Task operations were also updated to use the authenticated user's ID, and task deletion now verifies both the task ID and user ID.

### Result
Authentication is more secure, and users cannot access or delete tasks belonging to another user by changing IDs in the request.