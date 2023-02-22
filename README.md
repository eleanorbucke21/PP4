<img src="markdown/AmIResponsive.png">

# Bawarchi Khana # 

:desktop_computer: [Live Website] (https://pp4.herokuapp.com/)

:open_file_folder: [Github Repository] (https://github.com/eleanorbucke21/PP4)

## UX

### User Stories

HomePage <strong><u>(Not logged in)</u></strong>

- As a user I want to be able to tell what the website is about.
- As a user I want to see the posts.
- As a user I want to be able to register.
- As a user I want to be able to login. 
- As a user I want to be able to see the likes and dislikes.
    
Homepage <strong><u>(Logged in) </u></strong>
- As a user I want to be able to add recipes.
- As a user I want to be able to logout.

Admin Page

- As an admin I want to be able to add posts.
- As an admin I want to be able to approve or not approve posts.
- As an admin I want to be able to approve or not approve comments. 

Register

- As a user I want to be able to register.

Login Page

- As a user I want to be able to login with username and password.
- As a user I want to have the option of remembering me indtead of having to login.

Logout Page

- As a user I want to be able to logout.

# Features 
## Navigation
- Featured at the top of the page with the name of the website on the left.
- The navigation bar also has a register, login, add recipe and logout depending on if user is logged in. 
- The navigation is also responsive to smaller screens with a toggle option on the navbar, which hides the links till tapped.
## Header
- The header shows the name of the website <i>Bawarchi Khana</i>.
- The header has a colorful background which is why I used an opac background with dark text to display the name of the website.
- The image used as the background represents what the website is about.
## Footer
- The footer has a link to facebook.
- The footer has a link to Twitter.
- The footer has a link to my github.

## Register
- The register page has a form.
- The form displays the details needed.
- If username is already in use it will ask you to fill out form again.
<img src="markdown/username.png">
- If a user does not put in same password in both password fields they will get a warning to fill out form again.
- If a user uses a common password they will get a warning to choose another.
<img src="markdown/password.png">
- Once you register you are re-directed to home page.
## Login
- The login page has a form.
- The form displays where to type name and password.
- The form also has an option to tick ✔️ remember me so they won't need to login the next time they visit the page.
- If a user enters the incorrect username they will recieve an error.
- If a user enters the incorrect password they will recieve an error.
<img src="markdown/loginerror.png">
## Logout
- A user is asked if they are sure they want to logout.
- After clicking <i>signout</i> they are redirected to the home page.
<img src="markdown/signout.png" width="200">
## Posts
- The post page displays the recipe.
- The post has an image that the author of the post chooses to upload.

<u><strong>When user is logged in:</strong></u>
- The post has two buttons underneath displaying the likes and dislikes. <br>
<img src="markdown/likedislike1.png" width="100" height="150"> <img src="markdown/likedislike2.png" width="100" height="150">

<u><strong> When user is author of the post: </strong></u>
- Two buttons display if the user is the author of the post.
- An edit button is displayed if the user is the author of the post.
- A delete button is displayed if the user is the author of the post.
<img src="markdown/editdelete.png">

## Future Features ##

- In the future I would like to add an option to download the recipe posts as a pdf to view offline.

# Typography and Color Scheme

## Font
- The font used was from an imported bootstrap template.
- The fonts used in this template are <i>Open Sans</i> and <i>Lora</i>.
- The Font used for the website brand is <i>Sassy Frass</i>.
- The <i>Sassy Frass</i> font was used as it most resembled Urdu, the language of Pakistan.

## Color Scheme
- The colors used were grey and white.
- These colors where chosen to emphasize the images of the recipes.

## Wireframes

## Technologies
### Languages used
- [HTML](https://en.wikipedia.org/wiki/HTML5) - Add content and formatting to web page.

- [CSS](https://en.wikipedia.org/wiki/CSS) - Add styling and colours to web page.

- [JavaScript](https://en.wikipedia.org/wiki/JavaScript) - Add interactive features to web page.

- [Django](https://en.wikipedia.org/wiki/Django_(web_framework)) - A Python-based web framework that follows the model–template–views (MTV) architectural pattern. 

### Frameworks, Libraries and Programs Used

- [Gitpod](https://gitpod.io/) - web-based editor optimised for debugging, testing, syntax highlighting and extension support.

- [Git](https://git-scm.com/) - used to allow for tracking of any changes in the code and for the version control.

- [Github](https://github.com/) - used to host the project files and host webpage onto the internet.

- [Heroku](https://www.heroku.com/) - A cloud platform service that supports several programming languages.

- [ElephantSQL](https://www.elephantsql.com/) - Also known as postgres, is a free and open-source relational database management system (RDBMS) emphasizing extensibility and SQL compliance.

- [Fontawesome](https://fontawesome.com/) - to insert icons in the website to make site more visually appealing and easy to navigate.

- [Google Fonts](https://fonts.google.com/) - used to import fonts in the style.css stylesheet.

- [Favicon](https://favicon.io/) - to insert icons in the website to make site more visually appealing.

## Testing
- [Chrome DevTools](https://developer.chrome.com/docs/devtools/)
    was used during the development process to test, debug, explore and modify HTML elements, and to test responsiveness in different screen sizes.
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)  was used to test for error codes in the CSS.
- [W3C Markup Validation Serice](https://validator.w3.org/) was used to test for error codes in the HTML.