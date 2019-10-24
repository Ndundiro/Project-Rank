## Project-Rank

## Author
Ndundiro Kamau 

## Decription
Project-Rank is a platform  for web designers to showcase their work and get their web applications voted for by different users.The most voted for site becomes the site of the day.

## Live Link 
[lick here](https://awwwards159.herokuapp.com/) view the live site.

## SetUp/Installations
1. Download the zip file of the project or Clone the repository using the following command:
git clone ```https://github.com/Ndundiro/Project-Rank```

Navigate to the project directory
```cd WEEK3-IP```

2. Virtual Environment
Install virtualenv  using pip:  
```python3.6 -m venv virtual```  
Proceed to activate the virtual environment   
```source virtual/bin/activate```

3. Install packages/dependancies  
Install the packages in the requirements.txt file:  
```pip install -r requirements.txt```

4. Create a database
Create a new postgress database,Type the following command  
psql  
Run the following command,it creates a new database named gallery1  
```#create database awwwards```

5. Create Database migrations
run the following command:    
 ```python3 manage.py makemigrations awwwards```
followed by:    
 ```python3 manage.py migrate```

6. Run the app
To run the application:  
```python3 manage.py runserver``` 

Open  the link http://127.0.0.1:8000/  in a browser.

7. To run tests:  
```python3 manage.py test```

For more Information,Read the following documents:

* [DjangoDocumentation](https://docs.djangoproject.com/en/1.11/)
* [PythonDocumentation](https://docs.python.org/3.6/)

User Story

A user should be able to:
1. View posted projects and their details
2. Post a project to be rated/reviewed
3. Rate/ review other users' projects
4. Search for projects 
5. View projects overall score
6. View my profile page

## Bugs
There are no known bugs yet

## Technologies Used
* Python3.6
* Django 2.20
* PostgreSQL
* HTML5
* CSS3
* Heroku

### Dependencies
* Postgresql

## Support and Contact Details
For any comments,suggestions,feedback or inquiries, contact me via email: ndundirokamau@gmail.com

## License
[MIT License](https://github.com/Ndundiro/Project-RankLICENSE)

Copyright © 2019 Ndundiro Kamau























<!--  -->
