## Authentication and Task Ownership

The application uses Flask sessions to identify the authenticated user instead of trusting a user ID provided by the browser.

Task operations use the authenticated user's ID from the session. Task deletion verifies that the requested task belongs to the authenticated user before deleting it.

Passwords are stored using password hashing instead of plain text.

Manual validation confirmed that changing the user ID in a request does not provide access to another user's tasks. It also confirmed that a user cannot delete a task belonging to another user.
