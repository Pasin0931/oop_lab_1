What is this lab is all about ?
- Practice implementing procedural-style code into an OOP-style code, by declare and use classes, which is not done in procedural-style code.
- Practice using lambda function integration inside the code.

Project Structure
├── README.md               # Current file
├── Cities.csv              # The dataset
├── data_processing.py      # The analysis code

Design overview
- DataLoader: Loads CSV files into dictionary lists
- Table: Wraps data for query operations
- filter(): Returns new Table with rows matching condition
- aggregate(): Applies operations like average/max on columns
- Workflow: Load -> Filter -> Aggregate with lambda functions

You can run the code by typing "python data_processing.py" inside the terminal below, or click on the run button on top right coner of the screen.