# Classroom API

## Description

Simple API for classroom management.

## Instalation

```bash
$ git clone
$ cd project-classroom-api
$ python3 -m venv venv
$ source venv/bin/activate # Linux
$ venv\Scripts\activate # Windows
$ pip install -r requirements.txt
```

## Usage

* Run the script

```bash
$ python classroom.py
```

* If you have a personal credentials.json file, you can use it by overriding the default one

This script will return a link to google classroom authentication.

## Features

* List all courses
* List all tasks of a course
* Filter tasks by status (assigned, returned, graded, done) - in progress
* List the student submissions of a task
