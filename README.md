# Planetarium Api

## Table of Contents
 1. [Introduction](#introduction)
 2. [Requirements](#requirements)
 3. [Installation](#installation)
 4. [Used technologies](#used-technologies)
 5. [Usage](#usage)
 6. [Endpoints](#endpoints) 
 7. [License](#license) 


## Introduction
Welcome to the Planetarium Django API, a cutting-edge solution for managing and accessing astronomical data 
to power your planetarium application. This API is designed to provide an immersive experience for astronomy enthusiasts,
educators, and anyone fascinated by the cosmos. Built using the powerful Django framework and containerized with Docker,
my API offers seamless integration, scalability, and ease of deployment.

## Requirements
### For local running
* python 3.8
* pip

### For Docker
* Docker

## Installation
1. Clone this repository:

    ```
    git clone https://github.com/Kasatello/planetarium-API-project
    ```
 2. Create .env file and define environmental variables following .env.example:
    ```
    DJANGO_SECRET_KEY=your django secret key
    POSTGRES_HOST=your db host
    POSTGRES_DB=name of your db
    POSTGRES_USER=username of your db user
    POSTGRES_PASSWORD=your db password
    ```
 ### 3. To run it locally
1. Create virtual environment and activate it:
   * Tooltip for windows:
     - ```python -m venv venv``` 
     - ```venv\Scripts\activate```
   * Tooltip for mac:
     - ```python -m venv venv```
     - ```source venv/bin/activate```

2. Install dependencies:
    - ```pip install -r requirements.txt```
3. Apply all migrations in database:
   - ```python manage.py migrate```
4. Run server
   - ```python manage.py runserver```
5. Run telegram server
   - ```python notification/telegram_server.py```
### 3. To run it from docker
1. Run command:
      ```
      docker-compose up --build
      ```

## Used technologies
    - Django framework
    - Django Rest Framework
    - PostgreSQL
    - Docker

## Usage
### For users
    1. Reservation of planetarium shows
    2. Only reading all data from endpoints
### For admins
    1. Creating or modifying planetarium show
    2. Spectating at list of all shows
    3. + all user allowances

## Endpoints
    "planetarium_domes": "http://127.0.0.1:8000/api/planetarium/planetarium_domes/",
    "show_themes": "http://127.0.0.1:8000/api/planetarium/show_themes/",
    "astronomy_shows": "http://127.0.0.1:8000/api/planetarium/astronomy_shows/",
    "show_sessions": "http://127.0.0.1:8000/api/planetarium/show_sessions/",
    "reservations": "http://127.0.0.1:8000/api/planetarium/reservations/"
    "documentation": "http://127.0.0.1:8000/api/schema/swagger/"

# License
This project is licensed under the MIT License.
Feel free to use and modify the codebase as needed.
