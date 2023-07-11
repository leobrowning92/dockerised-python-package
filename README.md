# Ball Passing Test

## TLDR

I used a depth first search considering only bidirectional edges on a graph of player visibility. Solution is Dockerised for easy productionisation and dependancy management.

## Getting started

### Running Locally

`poetry install` to install dependancies
then
`poetry run python ball_pass <file path>` to run the program on any input file

`poetry run pytest` to run the tests

`poetry run python ball_pass -h` for help

#### Dependencies
`python 3.11` and `poetry` for dependancy management to run locally

### Running Containerized

To run the tests:
```
make build-test
make test
```

To run directly on a file in the `input_files/` directory:
```
make build
make run FILE='input.txt'
```

#### Dependencies
`docker` and `Make` to run containerized


## Problem Discussion

### Problem Description

In brief:

> Some players are standing in a field playing a game. If two players can see each other then they can throw a ball between them. 
> 
> Write a program to calculate the maximum number of players that can touch a single ball. The ball can be given to any single player at the start, and each player can touch the ball an unlimited number of times.

Input is via a comma seperated text file.

## Discussion of Solution

I chose to approach this as a graph problem, where players are nodes, and directed edges from node `a` to `b` denote that player `a` can see player `b`.

Wherever possible I have written this in a way that it could easily be run in a containerised manner on cloud infrastructure, while still being easy to work with and develop on locally.

Note: if this were a truelly professional problem, I would not have written the manual solutions. They are there only for discussion. I would use networkx unless there was a good reason not to. 

### Time Complexity

I used a deapth first search on a directed graph. 

The time complexity of this is `O(V + E)` where `V` is the number of vertices and `E` is the number of edges. 

Note that although only bidirectional edges are counted for the final value, their bidirectionality is not known before hand, and so they still must be checked for each edge, thus the `E` term being total edges, not bidirectional edges.

### Tools used

- Make: dependency free build tool for bundling common command patterns
- Poetry: dependency management and virtual environment tool
- Docker: containerization tool. Trivial to push and deploy images in production. Avoids many "works on my machine" issues


#### Libraries used
- Networkx: graph library for python. Performant, established graph library.
- Pytest: standard testing framework.
- Argparse: standard library for parsing command line arguments. easy and fuss-free


## Further consideration

### Input Validation
Depending on "real" context I would consider the following:
- Are the players always from a standard set of names? If so validate with an enum or configuration file of allowed names.
- If this was intended to be run on batches of files, I would consider adding directory consumption to the CLI arguments.
- For actual production use, I would add some push commands to the makefile to push the image to a container registry. 



