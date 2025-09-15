## fun_facts.py

A modular Python utility that returns a random fun fact and its 1-based index. Supports region-specific facts (e.g., Texas) and is designed for CLI use, logging, or backend integration.

### Features

- Returns a random fun fact from a curated list  
- Supports region-specific facts via optional `region` parameter  
- Calculates and returns the 1-based index of the selected fact  
- Modular design: safe to import without triggering execution  
- CLI-ready: prints formatted output when run directly  

### Usage

Run directly from terminal:  
python fun_facts.py

### Sample Output  
Fun Fact #3: Octopuses have three hearts.

### Call with region-specific facts  
fact, index = funfacts("Texas")  
print(f"Fun Fact #{index}: {fact}")

### Import into another script  
from fun_facts import funfacts  

# General fact  
fact, index = funfacts()  

# Texas-specific fact  
fact, index = funfacts("Texas")

### Learn Modular Python Like a Pro

These tutorials reinforce the design principles behind this module:  
- Python Modules for Beginners — shows how to structure and import functions like funfacts() across projects  
- Top 10 Built-in Python Modules You Should Know — explains how modules like random and datetime work under the hood  
- 9 Easy-to-Use Python Modules for DevOps — shows how modular tools like yours can be used in automation and CLI workflows  
- How to Make Your Python Code More Modular and Reusable — teaches how to refactor and structure code for reuse and clarity  
- Python Tutorial for Beginners 9: Import Modules and Exploring — walks through importing and using functions with arguments and return values  
- How To Create Your Own Modules In Python (Modularization) — shows how to turn your function into a reusable module and call it cleanly across project
