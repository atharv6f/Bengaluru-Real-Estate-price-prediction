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
     * **sudo nano /etc/config.json** 
     ```
     {
          'SECRET_KEY': "YOUR_SECRET_KEY",
          'EMAIL_USER': "YOUR EMAIL ADDRESS",
          'EMAIL_PASS': "YOUR PASSWORD"
     }
     ```
