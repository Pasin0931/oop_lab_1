# Lab: Object-Oriented Data Processing with CSV Files

## Overview
This lab focuses on turning **procedural-style code** into a clean **object-oriented design** using Python classes.  
You will practice:
- Organizing logic with classes and methods.  
- Using **lambda functions** for filtering and aggregating data.

---

## Project Structure

README.md — Project documentation  
Cities.csv — Dataset of cities  
Countries.csv — Dataset of countries  
data_processing.py — Main script for data processing and analysis  

---

## Design Summary

**DataLoader** – Loads CSV files into lists of dictionaries.  
**DB** – Simple in-memory database to store and find tables.  
**Table** – Represents a dataset with methods to:
- `filter(condition)` – returns rows that meet a condition.  
- `aggregate(func, column)` – applies operations like average, min, or max.  
- `join(other, key)` – merges two tables using a shared key.  

---

## How to Run

Run the program in your terminal:

```bash
python data_processing.py
or click the Run ▶️ button in your editor.
```