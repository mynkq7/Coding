# Day 05 — While Loops & Functions

## Topics Covered
- While loops  
- Input validation  
- Loop conditions  
- Using `not` in loops  
- Basic functions  
- Return statements  
- Simple arithmetic operations  
- String formatting (`capitalize()`)

---

## Files in This Folder
- `day-05.py` — main script containing all exercises

---

## Summary

Day 05 focuses on **while loops** for repeating actions until a condition becomes false, and **functions**, which allow you to write reusable blocks of code.

### ✔ While Loops  
Used to keep asking for input until correct or quitting:
- Asking for a non-empty name  
- Preventing negative age input  
- Looping until the user enters `'q'`  
- Validating numbers between 1 and 10  

### ✔ Input Validation  
Ensures the user only enters acceptable values by repeating prompts until correct.  
This logic is heavily used in automation, scripting, and cybersecurity tools (menus, brute forcing, payload loops, etc.)

### ✔ Functions  
Created multiple functions with arguments and reusable logic:
- `happy_birthday(name, age)`  
- `generate_invoice(customer, amount, date)`  
- Arithmetic functions: `add`, `sub`, `mul`, `div`  
- `create_name(first, last)` — returns formatted full name  

### ✔ Return Statements  
Used in arithmetic functions to send back computed results instead of printing them directly.

---

## Run

To execute Day 05:

```bash
python3 day-05.py