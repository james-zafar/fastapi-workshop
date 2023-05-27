### Introduction

In this workshop we will be implementing a simple API using FastAPI using the spec provided in `workshop-v1.0.yaml`. Some
code has been provided for you. You may add or change the code provided if you wish. The API has four key modules:
 - `operations` - this should contain the functions that handle requests for each endpoint.
 - `resources` - this should contain a list of object definitions that are defined in the API spec.
 - `store` - This contains the in memory database we will use for this workshop.
 - `main.py` - This is the entry point that should be used to launch the API.

### Prerequisites

Before starting this workshop make sure that you have Python 3.10 installed. Next install the
packages you will be using by running `pip install -r requirements.txt`.


### Tasks

You should familiarise yourself with the code provided before you get started. In operations and incomplete implementation
of `POST /models` has been provided, you will need to finish this later. In `resources` the definitions of a `Model` and
`Results` have been provided for you. Finally in `store` some core functionality for storing models and results has been
provided for you.