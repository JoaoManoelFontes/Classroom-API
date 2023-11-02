# Classroom API

## Description

Simple API for classroom management.

## Instalation

```bash
$ git clone
$ cd classroom-api
$ python3 -m venv venv
$ source venv/bin/activate # Linux
$ venv\Scripts\activate # Windows
$ pip install -r requirements.txt
```

## Usage

```bash
$ python classroom.py
```

This script will return a link to google classroom authentication.

## Features

* List all courses
* List all tasks of a course
* Filter tasks by status (assigned, returned, graded, done) - in progress
* List the student submissions of a task