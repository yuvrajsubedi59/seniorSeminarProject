# seniorSeminarProject  
Senior Seminar Project  

This is the code to setup the project in linux/wsl.
Before running you must set your own username and password
in enthusports/settings.py. This needs to be the same username
created in the database. It also need to match your command
line username.

    pip3 install django
    pip3 install folium
    pip3 install geopy
    sudo apt-get update  
    sudo apt-get install postgresql  
    sudo service postgresql start - if wsl
    sudo systemctl start postgres - if linux
    sudo -u postgres psql  
        CREATE DATABASE sportiasts;  
        CREATE USER **username** WITH PASSWORD '********';  
        GRANT ALL PRIVILEGES ON DATABASE sportiasts TO **username**;  
        \q  
    service --status-all    
    pip3 install psycopg2-binary  
    python3 manage.py makemigrations  
    python3 manage.py migrate  
    python3 manage.py createsuperuser  
    python3 manage.py runserver 0:8080  

Open browser: http://localhost:8080/     ------- if wsl  
0.0.0.0:8080                        ------- if linux  
http://localhost:8080/admin         ------- admin page
