# Bengaluru-Real-Estate-price-prediction
## A fullstack web app to predict the real estate prices based on the user given parameters

## Part 1: Model

* **Algorithm**: Ridge Resgression
* **R2-Score** : 0.89
* **Dataset**: https://www.kaggle.com/amitabhajoy/bengaluru-house-price-data

## Part 2: Web Application

* **Web Development Stack**: Python-Flask
* **Database Engine**: SQLite

## Part 3: Deploying on AWS

1. Launch an EC2 instance running Ubuntu 18.04 AMI.
2. Set up security with the following configuration
     * **Inbound Rules**: Allow http traffic at port 80, https traffic at port 443 and SSH(TCP protocol)  at port 22
     * **Outbound Rules**: Allow all inbound traffic
2. **sudo apt-get update** (To update the existing software on AMI)
3. **sudo apt install python3-pip**( Install pip)
4. **Virtual Environment**
      * *Create Virtual environment*: **sudo apt install python3-venv**
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
 6. **Configuring Nginx**
 * **sudo apt install nginx** (Make sure that the virtual environment in activated)
 * **sudo rm/etc/nginx/sites-enabled/default** (Remove the default nginx config file)
 * **sudo touch /etc/nginx/sites-enabled/any_file_name** (Create our own config file in the sites-enabled directory
 * **sudi nano /etc/nginx/sites-enabled/any_file_name** 
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
 7. **Configuring Gunicorn**
 * **pip install gunicorn** (Again make sure that the virtual environment is activated)
 * **gunicorn -w 3 app:app** (Number of workers = 2 * (Number of cores) + 1)
 * **nproc --all** (Gives the number of cores)
 
