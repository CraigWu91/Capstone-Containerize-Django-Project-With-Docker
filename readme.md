# Overview
The dockerfile will install all the pre=requisites to get the web app working. "python manage.py runserver 0.0.0.0:8000" will map the port from the container to your local computer with the URL http://127.0.0.1:8000/

# Instructions
* To run the mySite web application using Docker make sure you have Docker installed https://docs.docker.com/get-docker/
* In the commands.txt file you will see 2 commands that you need to run
* First run "docker build --tag mysite ." first to build the image. You should see the image in your docker desktop
* Second run "docker run --publish 8000:8000 mysite" to create a container. You should see the container in your docker desktop now running
* Go to http://127.0.0.1:8000/ in your browser and the web page should be running
