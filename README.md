# Bengaluru-Real-Estate-price-prediction
## A fullstack web app to predict the real estate prices based on the user given parameters

## Part 1: Model

* **Algorithm**: Ridge Resgression
* **R2-Score** : 0.89
* **Dataset**: https://www.kaggle.com/amitabhajoy/bengaluru-house-price-data

## Part 2: Web Application
* **git clone https://github.com/atharv6f/Bengaluru-Real-Estate-price-prediction.git**
* **Web Development Stack**: Python-Flask
* **Database Engine**: SQLite

## Part 3: Deploying on AWS

1. Launch an EC2 instance running Ubuntu 18.04 AMI.
2. Set up a security group with the following configuration
     * **Inbound Rules**: Allow http traffic at port 80, https traffic at port 443 and SSH(TCP protocol)  at port 22
     * **Outbound Rules**: Allow all inbound traffic
2. **sudo apt-get update** (To update the existing software on AMI)
3. **sudo apt install python3-pip**( Install pip)
4. **Virtual Environment**
      * *Creating a Virtual environment*: **sudo apt install python3-venv**
      * *Activating Virtual environment*: **source venv/bin/activate**
      * *Installing Libraries*: **pip install -r requirements.txt**
      
 5. **Configuring Environment Variables**
      * **sudo touch /etc/config.json** (Add environment variables in this file.)
      * **sudo nano /etc/config.json**  (Copy the following code in the config.json file)
          ```
         {
          'SECRET_KEY': "YOUR_SECRET_KEY",
          'EMAIL_USER': "YOUR EMAIL ADDRESS",
          'EMAIL_PASS': "YOUR PASSWORD"
         }
        ```
 6. **Configuring Flask-Migrate**
    * **export FLASK_APP=app.py** (Allows the user to run flask application from CLI)
    * **flask db init** (Creates a migration repo that stores different versions of our database schema)
    * **flask db migrate -m "YOUR_MESSAGE"** (Generates the initial migration accounting for the changes in the database schema)
    * **flask db upgrade** (Applies the upgrade to the database schema)
    
 7. **Configuring Nginx**
    * *Nginx is a web server that is highly optimized to serve static files, forward requests which need to be dynamic to Gunicorn and handle lots of requests coming in at once*
    * **sudo apt install nginx** (Make sure that the virtual environment in activated)
    * **sudo rm/etc/nginx/sites-enabled/default** (Remove the default nginx config file)
    * **sudo touch /etc/nginx/sites-enabled/any_file_name** (Create our own config file in the sites-enabled directory
    * **sudo nano /etc/nginx/sites-enabled/any_file_name** (Copy this code in the <file_name>.conf file)
    
        ```
        server {
            listen 80;
            server_name YOUR_IP_OR_DOMAIN;

            location /static {
                alias /home/YOUR_USER/YOUR_PROJECT/project/static;
            }

            location / {
                proxy_pass http://localhost:8000;
                include /etc/nginx/proxy_params;
                proxy_redirect off;
            }
       }
       ```
  
   * **sudo systemctl restart nginx** (Closes all the sub-processes adn restarts the whole package)
   
 9. **Configuring Gunicorn**
    * *Once Nginx decides, that a particular request should be passed on to Gunicorn, then, Gunicorn translates requests coming in from Nginx to be WSGI compatible, translates the WSGI responses of our app into proper http responses and actually calls the python code when a request comes in*
    * **pip install gunicorn** (Again make sure that the virtual environment is activated)
    * **gunicorn -w 3 app:app** (Number of workers = 2 * (Number of cores) + 1)
    * **nproc --all** (Gives the number of cores)
 
* **Configuring Supervisor**
    * *Supervisor looks after the Gunicorn processes and it makes sure that they are restarted if anything goes wrong.*
    * **sudo apt install supervisor** (Install supervisor in the virtual environment)
    * **sudo nano /etc/supervisor/conf.d/<file_name>.conf** (Copy this code in <file_name>.conf file)
    ```
    [program:project]
    directory=/home/YOUR_USER/YOUR_PROJECT
    command=/home/YOUR_USER/YOUR_PROJECT/venv/bin/gunicorn -w 3 app:app
    user=YOUR_USER
    autostart=true
    autorestart=true
    stopasgroup=true
    killasgroup=true
    stderr_logfile=/var/log/project/project.err.log
    stdout_logfile=/var/log/project/project.out.log
    ```

    * **sudo mkdir -p /var/log/project** (Creating a directory to store log files)
    * **sudo touch /var/log/project/project.err.log** (Process writes normal information to this file)
    * **sudo touch /var/log/project/project.out.log** (Process writes error information to this file)
    * **sudo supervisorctl restart** (Stops and restarts all managed applications)
    * **sudo systemctl restart nginx** (Closes all the sub-processes adn restarts the whole package)
