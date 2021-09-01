# Employee Management System (dummy application) with backend database integration

## Project description

This project aims to deploy a Django Application in Heroku with backend database integration.  

## Pre-requisites
Operating System: Ubuntu 18.04 LTE
Python-3.6.14

## Django web-application which performs basic CRUD operations.

The application's requirement is to use a form to take Employee ID and Employee Name and store it in database. Further we can edit,update, and delete the employee details. User Authentication has been added further to ensure only authenticated users can make changes to employee details in the database.

This has been achieved using a Django web-application. Code has been pushed to GitHub repository. The application has been hosted on Heroku using GitHub repository.

By default Django applications are connected to SQLite database, however, we have made changes in [settings.py](https://github.com/gade-raghav/kubernetes-assignment/blob/master/employeedb/settings.py) to connect it to Postgres Database which is deployed directly in Heroku.

Application link: https://ems-ap.herokuapp.com/home/

The following are the test credentials to access the application.

User Id: test_user

Password: test_pass
















