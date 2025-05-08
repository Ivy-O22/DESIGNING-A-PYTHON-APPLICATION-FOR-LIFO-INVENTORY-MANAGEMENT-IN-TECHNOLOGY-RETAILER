📦 **LIFO Inventory Management System in Python**

**Project Title:** Designing a Python Application for LIFO Inventory Management in Technology Retailer | LifoStack
**Created By:** Ona, Ivy Noelle Marie M. | Peñaflorida, Derick Gabriel A. | Peñaflorida, Cedrick Miguel A.  
**Date:** May 2025

---

## 📌 Table of Contents
1. [Main Features](#main-features)
2. [Tools and Techniques](#tools-and-techniques)

---

## Main Features
• A fully functional Python script named LifoStack.
• An in-memory system for tracking product batches using dictionaries and lists.
• Core program functions:
  -> add_product() – Adds new product batches, storing quantity, cost, and batch date.
  -> remove_product() – Removes stock using Last-In, First-Out (LIFO) logic.
  -> check_inventory() – Displays the current inventory with all batch details.
• Support for input validation to ensure clean and accurate data handling.
• Console-based interface for easy navigation and usage.
• Inline code comments and basic user instructions for better understanding and maintenance.

---

## Tools and Techniques
  1.Python version 3.+: The system is written in Python because of its beginner-friendly syntax, support for dynamic data structures, and built-in error handling. It manages core tasks like adding and removing stock, user input, and product listing.
  2.Text Editor or IDE (VS Code, etc.): The code is developed and run using a text editor or an IDE. These tools help streamline coding with useful features such as syntax highlighting, error detection, and integrated terminal support.
  3.  Terminal Interface:  All interactions with the system take place through a text-based terminal. This keeps the system lightweight and avoids the need for a graphical user interface (GUI), making it easy to run on most computers.
  4.  Dictionaries for In-Memory Storage: Product information is stored in a Python dictionary, where each product name maps to a list of batch records (each containing date, quantity, and cost). This allows for quick and flexible data access and modification during runtime.
  5.  No Persistent Storage: The system does not use text files or databases to save data. All inventory records exist only while the program is running. Once the user exits the terminal or ends the session, all data is lost.
  6.  String and Date Handling: The program uses string methods like strip() and lower() to clean user input and ensure case-insensitive matching. Dates are handled using Python's datetime module to validate and sort batch entries correctly.
  7.  LIFO (Last-In, First-Out) Logic: The inventory uses a LIFO approach when removing stock. This means the most recently added batch (latest date) is prioritized for removal. It ensures that older inventory remains untouched until newer items are cleared out.
8.Error Checking: The system includes multiple error-handling checks—such as validating date formats, numeric inputs, and available stock—to avoid crashes and guide the user to enter correct data.

---
