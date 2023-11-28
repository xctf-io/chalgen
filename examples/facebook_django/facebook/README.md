purepython-project
==================

Course Project for http://purepython.eaudeweb.ro

System prerequisites
--------------------

1. Install pip:
  
  ```
  wget https://bootstrap.pypa.io/get-pip.py
  sudo python get-pip.py
  ```

2. Install Django 1.6: 

  ```
  sudo pip install Django==1.6.2
  ```
  
Project installation
--------------------

1. Clone repository:

  ```
  git clone https://github.com/eaudeweb/purepython-project.git
  ```

2. Initialize database:

  ```
  cd purepython-project
  ./manage.py syncdb
  ```
  
3. Run development server:

  ```
  ./manage.py runserver
  ```
