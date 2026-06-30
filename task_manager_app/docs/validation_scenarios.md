# Validation Scenarios

## Scenario 1: Login with Incorrect Password

**Goal:** Confirm that the application prevents access when an incorrect password is entered.

**Steps:**
1. Open the login page.
2. Enter a valid email.
3. Enter an incorrect password.
4. Click the Login button.

**Expected Result:**  
The user is not logged in, and an error message is displayed indicating that the credentials are invalid.

**Actual Result:**  
The application rejected the login attempt and displayed an error message.

**Observation:**  
This validates that authentication correctly checks user credentials before granting access.

**Screenshot:**  
![Incorrect Password](image.png)

## Scenario 2: Login with Invalid Username

**Goal:**  
Verify that the application denies access when a user enters an email that is not registered.

**Steps:**
1. Open the login page.
2. Enter an email address that is not registered.
3. Enter a valid password.
4. Click **Login**.

**Expected Result:**  
The user is not logged in, and an error message is displayed indicating that the username or password is invalid.

**Actual Result:**  
The application rejected the login attempt and displayed an error message.

**Observation:**  
The authentication process correctly verifies that the username exists before allowing access.

**Screenshot:**  
![Invalid Username](image-1.png)



## Scenario 3: User Login

**Goal:** Confirm that a user can log in with valid credentials.

**Steps:**
1. Open the login page.
2. Enter a valid email and password.
3. Click the Login button.

**Expected Result:**  
The user is redirected to the task page.

**Actual Result:**  
The login worked correctly and the user was redirected.

**Observation:**  
This confirms the controller correctly communicates with the database and view.

**Screenshot:**  
![Scenario 3](screenshots/scenario 3.png)