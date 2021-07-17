**Basic Web Application **

**Task:**
1. Build a web application with some sort of authentication system. The users must be able 
to login and logout of the system. You can use any form of authentication for this.
2. Create a panel to upload a JSON file and add validations for the type of 
file, the content of the file, etc. Parse and save this data to the database.
3. Create a page to display all the records from the database
**Softwares:**
Python

**Frameworks:**
Django

**IDE**
Sublime text-3

**Description:**
1. Built web application using html and save it in task/templates/pages/login.html. When user enters the credentials views.py check the user details in database. If user credentials found then it goes to index.html page.If user not found then it displays "Not a Valid User"
Username: Siva Jyothy
Password: 12345678

2. In task-2, when user upload a json file, i parsed the data from file and the values in the file inserted into user_posts table.
3. When user clicks the posts button, data in the posts table will be displayed.

**Models**
In models.py, i created two tables.
1. User with username and password fields.
2. user_posts with userId, postId, title and body fields.

**HTML files**
1. login.html : It is a login page. After login it redirects to index.html page.
2. index.html : In index.html page, user can upload a json file and user can see the posts by clicking posts button.
3. posts.html : User can see the posts here.
