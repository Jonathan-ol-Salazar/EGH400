# EGH400
Performance Analysis Of A Range Of Data Structures When Storing 4D Airspace Data From SkyyNetwork Blockchain


## Setup
- Install SkyyNetwork Blockchain 
- Open two terminals and run the following commands -> Terminal 1: 'make start', Terminal 2: 'make start-rest'
- Open main.py 

## Running
- Run main.py using command -> 'python main.py'

## Observing Data Structures
It's assumed the code editor is VSCode. The default setup is 50 flight plans with 10 points for each plan. Python 3.7.5 is used.

- Open main.py
- Put a breakpoint at line 78 (line should contain the following -> 'x = 1')
- Run main.py using debug mode
- Terminal should print 'APPROVED' or 'DENIED' to show a successful request to the blockchain
- Once all the requests are completed the breakpoint will be hit
- Look in the 'variables' tab in the 'debug' window to find data structures. They are under the names - quadtree, kdtree and rtree
