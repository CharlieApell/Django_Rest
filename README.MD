# Foodie - API
Foodie is a vibrant online community tailored for food enthusiasts. It serves as a platform where users can freely share captivating images of their delectable meals, tantalizing drinks, and exceptional restaurant recommendations. Embracing the spirit of culinary exploration, Foodie allows users to immerse themselves in a world of flavors and engage with like-minded individuals.

Within this project, the backend API database has been meticulously crafted to provide robust support for the dynamic ReactJS frontend. Powered by the Django Rest Framework, it offers a seamless integration between the frontend and backend components, ensuring a smooth and enjoyable user experience. By leveraging this powerful technology stack, Foodie fosters an environment where users can connect, interact through likes, comments, and even follow fellow food enthusiasts.

#### [Deployed Backend API](https://drf-api-charlie.herokuapp.com/)
#### [Deployed Frontend](https://pp5-capell-745fa2049c09.herokuapp.com/)
#### [API Repository](https://github.com/CharlieApell/pp5-foodie-api)
#### [Frontend Repository](https://github.com/CharlieApell/project_portfolio_5)

***

## Table of Contents
+ [User Stories](#user-stories "User Stories")
+ [Database](#database "Database")
+ [Features](#features "Features")
+ [Testing](#testing "Testing")
  + [Validator Testing](#validator-testing "Validator Testing")
  + [Unfixed Bugs](#unfixed-bugs "Unfixed Bugs")
  + [Issues](#issues "Issues")
+ [Technologies Used](#technologies-used "Technologies Used")
  + [Main Languages Used](#main-languages-used "Main Languages Used")
  + [Frameworks, Libraries & Programs Used](#frameworks-libraries-programs-used "Frameworks, Libraries & Programs Used")
+ [Deployment](#deployment "Deployment")
  + [Github & Gitpod](#github--gitpod "Github & Gitpod")
  + [Create a Django Rest Framework project](#create-a-django-rest-framework-project "Create a Django Rest Framework project")
  + [Elephant SQL](#elephant-sql "Elephant SQL")
  + [Heroku](#heroku "Heroku")
+ [Credits](#credits "Credits")
  + [Content](#content "Content")
  + [Media](#media "Media")

***
## User Stories:
I have included links to the [GitHub Issues](https://github.com/CharlieApell/project_portfolio_5/issues) for this project, as well as the [Kanban board](https://github.com/users/CharlieApell/projects/7).

***
## Database:
![Database model](/assets/readme/data-schema.png)

***
## Features

The Foodie API consists of five apps, each with its own unique models, views, URLs, and serializers.

A superuser can log in through the Django admin site to access the backend and administer the User model. Other users can access the API data through [https://drf-api-charlie.herokuapp.com/](https://drf-api-charlie.herokuapp.com/) and the corresponding URL for each API endpoint.

- [Profiles](https://drf-api-charlie.herokuapp.com/profiles/)
- [Posts](https://drf-api-charlie.herokuapp.com/posts/)
- [Likes](https://drf-api-charlie.herokuapp.com/likes/)
- [Comments](https://drf-api-charlie.herokuapp.com/comments/)
- [Followers](https://drf-api-charlie.herokuapp.com/followers/)

***
## Testing:
### Validator Testing: 
All Python files have been successfully passed through the PEP8 validator in gitpod with no issues, except for some long-line errors that have been adressed.

![PEP8](/assets/readme/pep8.png)

### Manual Testing:
- I manually verified that each URL path created works and opens without any errors.
- I confirmed the availability of CRUD functionality in each app using the development version. This includes features for comments, contact, followers, likes, posts, and profiles.
  - I checked this by visiting each link.
  - I created a new item.
  - I verified the URL path of the new item.
  - I tested editing the item (not applicable for likes, followers, or users).
  - I tested deleting the item (not applicable for users or profiles).
- I ensured that the search feature for the Posts, User, Location, and Price apps returns results.

### Unfixed Bugs
- None so far.

### Issues
**Issue** - When attempting to set "localhost" as the allowed host in the settings.py file, I encountered an issue where the application was not able to run properly. Instead, I had to manually paste the address generated by Gitpod as the allowed host.

***
## Technologies Used:
### Main Languages Used:
- Python
- Git

### Frameworks, Libraries & Programs Used:
- Django
- Django RestFramework
- Cloudinary
- Heroku
- Pillow
- Django Rest Auth
- PostgreSQL
- Gunicorn
- psycopg2

***
## Deployment:

### Github & Gitpod

1. Create a repository on Github using this template [Code-Institute-Org/gitpod-full-template](https://github.com/Code-Institute-Org/gitpod-full-template), click "use this template" -> "Create a new repository.
2. Once the repository is created, click the green button on the right (Gitpod) to open a new Gitpod workspace.
3. To work on the project, it is recommended to open the workspace from Gitpod workspaces (instead of Github) to ensure continuity. Pin the workspace for easy access.
4. Make frequent commits with clear messages using the following commands:
   - `git add .`: adds all modified files to the staging area.
   - `git commit -m "A message explaining your commit"`: commits all changes to the local repository.
   - `git push`: pushes all committed changes to your Github repository.
5. During development, use the Gitpod development server to view the website by running the command `Python3 manage.py runserver`.

### Create a Django Rest Framework project

1. Install Django and supporting libraries such as Gunicorn, Cloudinary, psycopg2, Pillow, and Allauth.
2. In the terminal of the Gitpod workspace, type `django-admin startproject 'project_name'` to create the desired project name.
3. In the terminal of the Gitpod workspace, type `python3 manage.py startapp 'app_name'` to create the desired app name.
4. Create a `Requirements.txt` file (type `pip3 freeze --local > requirements.txt`), an `env.py` file, and a `Procfile` at the top level of the project directory.
5. In `settings.py`, add the names of the installed apps to the `INSTALLED_APPS` array variable and save the file.
6. Move the `SECRET KEY` to the `env.py` file and add the `DATABASE URL`, `ALLOWED_HOST`, `DEV`, and `CLOUDINARY URL` as well.
7. Migrate changes by using the command `python3 manage.py migrate`.

### Elephant SQL

1. Log into ElephantSQL or create a new account.
2. Click to create a new instance and set up the plan by giving it a name (e.g., the tiny turtle plan).
3. Select the region (data center) closest to your location.
4. Click "Review," check that all the details are correct, and then click "Create Instance."
5. Return to the ElephantSQL dashboard and click on the database instance name for the project.
6. Copy the ElephantSQL database URL that starts with `postgres://` using the copy icon.

### Heroku

1. Log into Heroku or create an account.
2. Click "New" to create a new Heroku app. Give the app a name and select your region (e.g., Europe).
3. Open the app settings tab and click "Reveal config vars."
4. Add a config var called `DATABASE_URL` and paste in the ElephantSQL database URL.
5. Add the config var `SECRET KEY` with the secret key from the Django `settings.py` file. It is recommended to create a new secret key for security purposes.
6. Add the config vars `CLOUDINARY_URL`, `DATABASE_URL`, `ALLOWED_HOST`, `CLIENT_ORIGIN`, `CLIENT_ORIGIN_DEV`, and `DISABLE_COLLECTSTATIC`.
7. Under the project deploy tab, select GitHub as the deployment method. Search for the repository name and click "Connect." Scroll down to the manual deployment section and click "Deploy Branch." Make sure to select the main branch.


***
## CREDITS:

### Content:
- The creation of this API database was provided through the step by step guide of the C.I. DRF-API walkthrough project.
- Modifications have been made to the 'Posts' and 'Profiles' app models.


### Media:
- The Default Profile Image was used provided by CI during the course [Default Profile Image](https://codeinstitute.s3.amazonaws.com/ReactEssentials/DRF/Images/default_profile.jpg)
- Default Post image from [Default Post Image](https://codeinstitute.s3.amazonaws.com/ReactEssentials/DRF/Images/default_post.jpg)