Spaces

About: A basic asynchronous chat application utilising the idea of chat rooms (called Spaces). It allows for a user
to create an account, join a space and talk with other users in that space. I used  Django and Daphne 
for the back-end, while vanilla JavaScript is used for the front-end Websockets implementation.



Important Points

Applications: 
-"chatapp" is the base of the project.
-"core" is the main app, containing the top-level template, models and forms. (urls: /, /login, /logout, /register)
-"space" is used to render individual spaces, aswell as the page where all spaces are displayed. (urls: /spaces, /spaces/*)

Known issues:
-A sender's username isn't displayed until the page is refreshed
-Sometimes a single message will be sent multiple times
