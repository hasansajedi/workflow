# Oculavis - Tech Check

This application uploaded on [Github](https://github.com/hasansajedi/workflow) and test automated with CircleCI.

All of options you want in tech document is implemented. 

## Installation
To build, test and deploy application please, run bash.sh file in root directory:

```bash
> ./script.sh
```
or
```bash
> python3.8 -m venv venv
> source venv/bin/activate
> pip install --upgrade pip
> pip install -r requirements.txt
> source .envrc
> python ./manage.py migrate
> python ./manage.py test
> pipenv run python manage.py runserver 
```
or, You can use CircleCI to build, test and deploy the project. The config file is in '.circleci' folder.

## Features

1. **Workflow**: View all workflows.
2. **Workflow**: View an instance of workflow by id.
3. **Workflow**: Create an instance of workflow.
4. **Workflow**: Update an instance of workflow by id.
5. **Workflow**: Delete an instance of workflow by id.
6. **Comment**: View all comments.
7. **Comment**: View an instance of comment by id.
8. **Comment**: Create an instance of comment.
9. **Comment**: Update an instance of comment by id.
10. **Comment**: Delete an instance of comment by id.

## Usage

Main url is:
> http://127.0.0.1:8000/api

##### You can access to all operations about Workflow, by below link:
* Get all workflows as json: 

Url: http://127.0.0.1:8000/api/workflow/ 

Action method: **Get**

Input: None

Output:
```json
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 2,
            "name": "How to start a car",
            "description": "Basic instructions to starting a car",
            "created_at": "2020-04-21T17:07:29.703119Z"
        },
        {
            "id": 3,
            "name": "How to Cook",
            "description": "Anyone can cook, but there is more to cooking than simply throwing ingredients together and hoping for the best. You have to understand basic cooking terms and techniques.",
            "created_at": "2020-04-23T20:24:57.173004Z"
        }
    ]
}
```
* Get an instance of workflow: 

Url: http://127.0.0.1:8000/api/workflow/{pk}

Action method: **Get**

Input: Refers to id of workflow.

Output: Return workflow fields and steps of workflow and comments that inserted for this workflow.
```json
{
    "name": "How to start a car",
    "description": "Basic instructions to starting a car",
    "steps": [
        {
            "id": 3,
            "name": "Get in the driver's seat and buckle up",
            "description": "Put on your seat belt. Do not drive without wearing a seat belt as it is both unsafe and illegal in many places",
            "status": "In definition"
        },
        {
            "id": 4,
            "name": "Insert the key into the ignition",
            "description": "The ignition point is often located near the steering wheel. It looks like a round piece of metal, often with writing on it, with a keyhole in the center of it. Insert the key all the way into the ignition after you find it",
            "status": "In definition"
        }
    ],
    "comments": [
        {
            "name": "First comment",
            "text": "First comment text",
            "created_at": "2020-04-22T13:15:28.337509Z"
        }
    ]
}
```

* Create a workflow instance:

Url: http://127.0.0.1:8000/api/workflow/

Action method: **Post**

Input: Json format.

```json
{
    "name": "",
    "description": "",
    "steps": []
}
```

Output: Return workflow instance that inserted.

* Update an instance of a workflow:

Url: http://127.0.0.1:8000/api/workflow/{pk}

Action method: **Put**

Input: Json format.

```json
{
    "name": "new test workflow",
    "description": "test description for workflow",
    "steps": [
        {
            "id": 15,
            "name": "step1",
            "description": "step1 desc",
            "status": "In definition"
        },
        {
            "id": 16,
            "name": "step2",
            "description": "step2 desc",
            "status": "In definition"
        }
    ]
}
```

Output: Return workflow instance that updated.
 
* Delete an instance of a workflow:

Url: http://127.0.0.1:8000/api/workflow/{pk}

Action method: **Delete**

Input: Refers to id of workflow.

Output: Return a Response with HTTP_204_NO_CONTENT status code.


##### And you can access to all operations about Workflow, by below link:
> http://127.0.0.1:8000/api/comment

* Get all comments as json: 

Url: http://127.0.0.1:8000/api/comment/ 

Action method: **Get**

Output:
```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "name": "First comment",
            "text": "First comment text",
            "created_at": "2020-04-22T13:15:28.337509Z",
            "workflow_id": 2
        }
    ]
}
```
* Get an instance of comment: 

Url: http://127.0.0.1:8000/api/comment/{pk}

Action method: **Get**

Input: Refers to id of comment.

Output: Return an instance of comment.
```json
{
    "workflow_id": 3,
    "name": "Hasan Sajedi",
    "text": "This is test text to start workflow."
}
```

* Create a comment instance:

Url: http://127.0.0.1:8000/api/comment/

Action method: **Post**

Input: Json format.

```json
{
    "workflow_id": id_of_workflow,
    "name": "",
    "text": ""
}
```

Output: Return comment instance that inserted.

* Update an instance of a comment:

Url: http://127.0.0.1:8000/api/comment/{pk}

Action method: **Put**

Input: Json format.

```json
{
    "workflow_id": 4,
    "name": "update test comment",
    "text": "update test comment text"
}
```

Output: Return comment instance that updated.
 
* Delete an instance of a comment:

Url: http://127.0.0.1:8000/api/comment/{pk}

Action method: **Delete**

Input: Refers to id of comment.

Output: Return a Response with HTTP_204_NO_CONTENT status code.

