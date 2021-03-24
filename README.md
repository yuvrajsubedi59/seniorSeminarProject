# seniorSeminarProject  
Senior Seminar Project  

pip3 install django  
 1996  sudo apt-get install postgresql  
 1997  apt-get update  
 1998  sudo apt-get update  
 1999  sudo apt-get install postgresql  
 2000  sudo -u postgres  
 2001  sudo -u postgres psql  
   
 CREATE DATABASE sportiasts;  
 CREATE USER **username** WITH PASSWORD '********';  
 GRANT ALL PRIVILEGES ON DATABASE sportiasts TO yuvraj;  
 \q  
 
 2002  sudo systemctl start postgres - if linux  
 2003  sudo service postgresql start - if wsl  
 2004  service --status-all   
 2006  sudo -u postgres psql  
 2022  pip3 install psycopg2-binary  
 2027  python3 manage.py makemigrations  
 2028  python3 manage.py migrate  
 2029  python3 manage.py createsuperuser  
 2032  python3 manage.py runserver 0:8080  
   
 Open browser: http://localhost:8080/              ------- if wsl  
               0.0.0.0:8080                        ------- if linux  
               http://localhost:8080/admin         ------- admin page
