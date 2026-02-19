# Wide World Importers - Purchase Order Analytics
## Project Overview
The primary goal is to extract data for reporting purposes from a fictional wholesale novelty goods distributor, Wide World Importers

By leveraging the classic Microsoft sample database, Wide World Importers (OLTP), this project demonstrates a modern data workflow. It extracts transactional data from the operational database, performs transformations to clean and structure the data for analysis. The focus is specifically on the purchasing domain, utilizing tables related to purchase orders, suppliers, and financial transactions.

Throughout this document, I'm going to explain the setup I've used, why I used it, how you can achieve the same setup and, most importantly, the logic for the main task and for the bonus task.

## Why use this setup?
This probably looks a bit overwhelming given the requirements of the task(s), but I wanted to think a few steps ahead, challenge myself and interact with new concepts that I haven't really worked on too often, like packaging your own python module, doing "unit tests", implementing linters etc. I feel like this setup is closer to a real-world setup a Data Engineer might use, but at the end of the day it depends on the needs of the project. I wanted to combine multiple technologies to build something reliable, smart, not the most efficient for now, but I'll share my thoughts on improvements in the latest section

## Prerequisites
Before we get started, we need a few things: a Python version >= 3.13, an IDE and git. I don't believe we really need one of the latest versions of Python, but at the time I've worked on this assignment I had this version installed, so you should download and install the same requirements. Please check the official [Python website](https://www.python.org/) for more details on how to download and install it. For IDE, you can choose whatever IDE you want. I've used VS Code since I'm used to it. I'll leave the link to VS Code in case you want to use it as well: [VS Code](https://code.visualstudio.com/). Same thing for [git](https://git-scm.com/install/windows). Quick note: I work on Windows, so make sure to adapt this documentation according to your own OS.

## Getting started
### Step 1. Clone repository
To do it you can:
1. Go to code, press on the arrow next to it, and copy the https link <img width="1714" height="873" alt="image" src="https://github.com/user-attachments/assets/b42bdeaa-f2fa-40a5-9c4c-e3b181222699" />
2. Within your IDE, open a new terminal and run the below command. Make sure to clone it in the desired project location
```
git clone https://github.com/bonteanuionut/WideWorldImporters.git
```

### Step 2. Create a Virtual Environment (optional)
This step is not really necessary but it's recommended, so the dependencies used for this project don't mess with your general setup of your Python.
There are 2 approaches to create a venv (Virtual Environment)
#### IDE approach
1. Press ctrl+shift+p
2. Type "create environment" and press the "Python: Create Environment..." option
3. Choose the version of your interpreter. Job done!
#### CLI approach
1. Within your terminal type
```
# at the project root
py -3.13 -m venv .venv
```
2. Activate the venv
```
.\.venv\Scripts\activate
```
Note that -3.13 has been used to specify the version of the Python to use.

### Step 3. Install the necessary libraries.
To do that you can simply use the command below
```
pip install -e .
```
This will look at the pyproject.toml and install everything you need to run this project.
You also use the command below to install additional libraries that will help you format your code, test the code, etc. For more details, please refer to <code>pyproject.toml</code> file
```
pip install -e .[dev]
```
Note that you have to be inside the directory of the project you've cloned in order to run the commands above.

Now that we have the setup done, let's get to the solution of this assignment.

## Solution
There 2 approaches to run this solution. You can either use MSSQL or the actual setup and run the .py scripts to get the desired results
### MSSQL approach
To use it this approach, copy the sql code from src -> WideWorldImporters -> wide_world_importers_report.sql (that is the main task) or src -> WideWorldImporters -> purchase_orders_deduplication.sql (the bonus task), enter in your SQL editor (I use <code>SQL Server Management Studio 20</code>) and you can also download it from [here](https://learn.microsoft.com/en-us/ssms/install/install), pass in the required information. In our case we set:
- Server type: Database Engine
- Server name: {server-name}
- Authentication: SQL Server Authentication
- Login: {username}
- Password: {password}

After you've logged in, we can right-click on the WideWorldImporters (the database we're using) and New Query
<img width="604" height="526" alt="image" src="https://github.com/user-attachments/assets/23ed0ce1-51d6-45e7-a358-7e7e0b73063b" />

Now you can paste your SQL code and run it. Note that the current SQL uses jinja template (basically every notation that is between curly brackets). If you're running in the MSSQL, remove everything that is between <code>{{}}</code> and replace with the values in the comments section.

### VS Code approach
Within the current setup, we can simply open the terminal and run the following command for the main task
```
python src/WideWorldImporters/python_scripts/export_purchase_orders_duplicates.py
```
Or for the bonus task:
```
python src/WideWorldImporters/python_scripts/export_wide_world_importers.py
```

We can check the results in the <code>outputs</code> folder.

## Dataset Description
WideWorldImporters is a fictitious wholesale novelty goods importer and distributor based in San Francisco, designed by Microsoft to serve as a comprehensive sample database for SQL Server and Azure SQL Database. It demonstrates modern database capabilities, including transactional (OLTP) and analytical (OLAP) processing, with data covering sales, purchasing, and warehouse operations. For more details you can access the [Technical Documentation](https://docs.microsoft.com/en-us/sql/samples/wide-world-importers-oltp-database-catalog?view=sql-server-ver15).

During this assignment, we will only be working with Purchasing database. We are mainly interested in extracting transactions so to better understand the schema we are working with, consult the image below that shows the relational diagram of the used tables.
<img width="1866" height="1090" alt="image" src="https://github.com/user-attachments/assets/34bdf99f-527b-4f9d-a06c-1a959810499c" />



