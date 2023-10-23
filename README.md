
## Django Health

  
  

## This is the final project for CS50's web programming with Python and JS.

  

#### Course link: https://www.edx.org/course/cs50s-web-programming-with-python-and-javascript

  
  

### Overview:

  

Django Health is a web application that allows users to view different plans, each plan offers several meals with recipes for breakfast, lunch, dinner, and snack.

  

After registration and creating an account by a user, in the user’s profile, the user is asked to enter personal information like current weight, height, gender, and target weight, and then they have the possibility to choose a plan.

  

The application gives users a report on their daily calorie consumption, BMI, and health status based on the data they provided. The daily calorie intake is determined by factors like gender and target weight, while the BMI/health status is determined by factors like current weight and height.

  

Users will have access to their own plan of choice, and they can keep track of the meals they've consumed as well as their daily calorie intake. The application also has a "History" option (My Diaries), where users may choose the desired date and then have access to all of the previous days' information, including the calories they had ingested and the meals they had.

  
  

### Distinctiveness and Complexity:

  

This project is a web application that is entirely distinct from an e-commerce site that deals with buying and selling products, like project 2, where we were able to list our products for sale, get various price suggestions from other users, choose the winner, and inform the winner of his or her victory. It also differs from any previous projects I worked on in this course, such as project 4's social network application, which deals with sharing posts, following other users, commenting under them, and like our favorite comments or posts.

  

The usage and functionality of this web application are distinct and introduce a virtual dietician, with the help of which the user can achieve his or her ideal weight in accordance with the calculated factors, as stated in the overview section's explanations. I'll go into more detail regarding the technical aspects and their intricacy below.

  

For the data used in the application, such as in the plans (which contain meals, recipes, and calories), I used a JSON file as a source of data to be used by the API endpoints. It was further integrated with the Plan model in the database. In various places of the JS file, the fetch methods are using the data from the JSON file to show on the intended pages of the application.

  

In order to get the required user information, there is a form in the user's profile that receives the information from the user. There are some computations and conditions before submitting the form in javascript, and if any of the conditions are not met, an error is thrown to the user. This information is transmitted to the backend via javascript and saved as a Profile model that is defined in 'model.py'. Javascript can be used to alter this data, which includes suggested daily calorie intake, BMI, and health status. This data (Profile model) is calculated in the backend (views.py) and then displayed on the user's profile. There are two links on the same page, one of which directs users to the page displaying the selected menu plan with all of the recipes, and the other of which directs users to the Calorie Tracker (diary.html) page.

  

There is another form in diary.html where we can choose the daily meals we consume from the plan of our choice. This form also has a counter that can calculate how many calories we consume each day while picking each field (breakfast, lunch, supper, and snack). The doughnut chart js package was used to style and function the counter. The chart is given some counter-related variables in order to improve coordination between the counter and the graphic. It is a requirement for submitting the form that all fields be checked; otherwise, it cannot be submitted and returns an error. After submitting this form, the data from this page, including the number of calories consumed, the name of the selected meal plan, and the date for the current date, will be sent to the backend via javascript. All of these data are then saved as a Track_cal model (defined in model.py), and both the information and the meals can be changed, but only on the same day.

  

The data is being fetched from the '/all_history' API path using Javascript on the 'My Diaries' page (history_page.html), and all Track_cal objects created by the user are displayed on the 'Calorie Tracker page 'diary.html' from the Track_cal model (in model.py). By selecting one of these objects, the 'id' of the chosen object is fetched into the ('/one_history/int:id>') API path, and it can be seen that the chosen object contains the date, the number of calories eaten, the name of the chosen plan, and the meals chosen.

  

I also included a date input in the form of a date picker, so that whenever the user thinks about a particular date, they can select it. Using JavaScript and the 'onchange' method, the date can be fetched and found the Track_cal object, which is only built by the same user, and its date is matched with the considered date. Then, it displays information (date, consumed calories, name of the chosen plan, and selected meals), or if it cannot find any object

  

I used both Bootstrap and CSS to style the various sections and pages of this web application, and every page is responsive on mobile screen sizes. I made an effort to use the defined grid and flex in bootstrap as much as I could, as well as media queries in the CSS stylesheet, to make the application responsive.

  

In addition to all of the above step-by-step explanations, it is important to note that this project was very difficult for me in terms of putting everything from the idea on paper into practice and also thinking about the application's architecture, from data flows and their relationships to how to make the application as fluid and user-friendly as possible (UI/UX). Nevertheless, I really enjoyed this challenge and I learned a lot from it.


  

### Project Structure & Files contents:

  

* final: main application directory.

* static/final: contains all static content.

* styles.css: contains all styles used in the project.

* index.js: contains all JavaScript used in the project and some pages like:

* Single meal: contains meal's image, its title, calorie and recipe.

* Single History: contains number of daily calories and the meals that the user consumed.

* images: contains all images used in project.

* templates/final: contains all application templates.

* layout.html: base template that all other tempalates extend it, containing Navbar and Footer.

* index.html: template that shows four diet plans.

* plan.html: template that shows a single plan (contains three meals for breakfast, three meals for lunch, three meals for dinner, and three meals for snack).

* my_profile.html: template that shows profile form.

* report.html: template that shows personal information and profile report of the user and edit form.

* diary.html: template contains a calorie counter and a form where we can choose the meals of our desired plan daily.

* history_page.html: template that shows all information of the previous days.

* login.html: template that shows login form.

* register.html: template that shows registration form.

* models.py: contains four models I used in the project. UserExtended model extends the standard User model, Plan model is for the plans, and Profile model represents users' profile consisting of weight, height, gender, target and user's desired plan and Track_cal model is for tracking consumed daily calories and meals.

* admin.py: I added admin classes and registered User model.

* urls.py: all application URLs.

* views.py: contains all application views.

* mydata.json: I made this json file containing all plans consisting of all the meal titles and their calories, recipes, and image addresses.

  
  

### Technology Used & Features:

  

* Python

* JavaScript

* JSON

* HTML

* CSS

* Bootstrap

* Mobile Responsive

  
  

### How to run:

  

* Run following commands to migrate database:

- python manage.py makemigrations final

- python manage.py migrate

  

* You can run this command to run your server:

- python manage.py runserver