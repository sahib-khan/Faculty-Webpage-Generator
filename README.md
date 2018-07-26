# Profile Manager

An intranet portal where faculties can manage and publish their profiles and
students can view their profiles.

## Getting Started

Clone or fork the repo to make changes and test the site.

### Prerequisites

* python v2.7
* django v1.10.2
* django-recaptcha
* Pillow



### Installing
#### Linux installation
Create a vitual enviroment if you have deal with multiple python projects.

```
sudo apt-get install python-virtualenv
or
sudo easy_install virtualenv
or
sudo pip install virtualenv
```

```
mkdir ~/virtualenvironment
virtualenv ~/virtualenvironment/my_new_app
cd ~/virtualenvironment/my_new_app/bin
source activate
```

To install django.
Note: Use sudo only if some errors pop up.

```
sudo pip install -r requirements.txt
```
#### Windows installation
Make sure you have python 2.7 installed. <br>
Open Command prompt.

To make virtual virtualenvironment

```
pip install virtualenv
python -m virtualenv MYVENV
```
Now go to the directory your virtual enviroment is created.

```
MYVENV\Scripts\activate
```
Your virtual environment will be activated. <br>

Now go the directory where you have cloned the repository.
```
pip install -r requirements.txt
```
All the dependencies will be installed now.

###### Finally run

```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

in the directory which has manage.py to get your site up and running.


## Built With
##### Backend
* [Django](https://www.djangoproject.com/) - A python-based web framework

##### Front end
* HTML5
* CSS
* JavaScript
* Bootstrap

## Authors

* **[Sahib Khan](https://github.com/sahib-khan)**
* **[Shivam Kumar](https://github.com/shivamkr143)**
* **[Kapil Goyal](https://github.com/kapil-goyal)**
