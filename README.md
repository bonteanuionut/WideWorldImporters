# Wide World Importers - Purchase Order Analytics
## Project Overview
The primary goal is to extract data for reporting purposes from a fictional wholesale novelty goods distributor, Wide World Importers

By leveraging the classic Microsoft sample database, Wide World Importers (OLTP), this project demonstrates a modern data workflow. It extracts transactional data from the operational database, performs transformations to clean and structure the data for analysis. The focus is specifically on the purchasing domain, utilizing tables related to purchase orders, suppliers, and financial transactions.

Throughout this document, I'm going to explain the setup I've used, why I used it, how you can achieve the same setup and, most importantly, the logic for the main task and for the bonus task.
## Table of contents
1. [Why use this setup?](#why-setup)
2. [Prerequisites](#prerequisites)
3. [Getting started](#getting-started)
4. [How to run this solution?](#how-to-solution)
5. [Solution Logic - Explained](#solution-logic)
6. [VS Code setup - Pros and Cons](#vs-code-in-depth)
7. [Final Thoughts and Improvements](#improvements)

## Why use this setup? <a name="why-setup"></a>
This probably looks a bit overwhelming given the requirements of the task(s), but I wanted to think a few steps ahead, challenge myself and interact with new concepts that I haven't really worked on too often, like packaging your own python module, doing "unit tests", implementing linters etc. I feel like this setup is closer to a real-world setup a Data Engineer might use, but at the end of the day it depends on the needs of the project. I wanted to combine multiple technologies to build something reliable, smart, not the most efficient for now, but I'll share my thoughts on improvements in the latest section

## Prerequisites <a name="prerequisites"></a>
Before we get started, we need a few things: a Python version >= 3.13, an IDE and git. I don't believe we really need one of the latest versions of Python, but at the time I've worked on this assignment I had this version installed, so you should download and install the same requirements. Please check the official [Python website](https://www.python.org/) for more details on how to download and install it. For IDE, you can choose whatever IDE you want. I've used VS Code since I'm used to it. I'll leave the link to VS Code in case you want to use it as well: [VS Code](https://code.visualstudio.com/). Same thing for [git](https://git-scm.com/install/windows). Quick note: I work on Windows, so make sure to adapt this documentation according to your own OS.

## Getting started <a name="getting-started"></a>
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
You can also use the command below to install additional libraries that will help you format your code, test the code, etc. For more details, please refer to <code>pyproject.toml</code> file
```
pip install -e .[dev]
```
Note that you have to be inside the directory of the project you've cloned in order to run the commands above.

Now that we have the setup done, let's get to the solution of this assignment.

## How to run this solution? <a name="how-to-solution"></a>
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
Before running the main py scripts we need to add the .env configuration file. This ensures that the server_connection function can actually grab the necessary credentials it needs to connect to the server. Here's how it should look like:
```
DB_SERVER = {replace-with-server-address}
DB_NAME = "WideWorldImporters"
DB_USER = {replace-with-username}
DB_PASSWORD = {replace-with-password}
```
Make sure to keep the variable name as they are. The function will look at the exact names. You can save the <code>.env</code> in your root directory.
Within the current setup, we can simply open the terminal and run the following command for the main task
```
python src/WideWorldImporters/python_scripts/export_purchase_orders_duplicates.py
```
Or for the bonus task:
```
python src/WideWorldImporters/python_scripts/export_wide_world_importers.py
```

We can check the results in the <code>outputs</code> folder. Alternatively, we can use the <code>pytest</code> framework to test the output. What this framework does is to look at the sample output (which you will find it at tests -> fixtures -> invoiceReportNovember2015.xlsx) and compare with our results.
To run the tests we can use this command:
```
pytest tests/test_wide_world_importers.py 
```
The general idea of this solution is to parse the sql script as a string, use pandas to run the query and save the data in an excel file that can further be sent to the stakeholders let's say. A big advantage of this setup is we make use of the <code>argparse</code> library. Within the sql files, we'll some notations between curly brackets. Those are placeholders, so we can dinamycally change the values, without altering the code. We can pass desired values for the <code>where</code> clause at runtime. But for this assignment, by default, they are set according to the requirements. But that's just the flexibility this approach offers to the user.

## Solution Logic - Explained <a name="solution-logic"></a>
### Dataset Description
WideWorldImporters is a fictitious wholesale novelty goods importer and distributor based in San Francisco, designed by Microsoft to serve as a comprehensive sample database for SQL Server and Azure SQL Database. It demonstrates modern database capabilities, including transactional (OLTP) and analytical (OLAP) processing, with data covering sales, purchasing, and warehouse operations. For more details you can access the [Technical Documentation](https://docs.microsoft.com/en-us/sql/samples/wide-world-importers-oltp-database-catalog?view=sql-server-ver15).

During this assignment, we will only be working with Purchasing database. We are mainly interested in extracting transactions so to better understand the schema we are working with, consult the image below that shows the relational diagram of the used tables.
<img width="1866" height="1090" alt="image" src="https://github.com/user-attachments/assets/34bdf99f-527b-4f9d-a06c-1a959810499c" />

### Way of thinking - Main task
To be honest, it was more like a "reverse-engineering" kind of approach. Based on the sample output provided I started to build the query. The first thing I did was to draw the diagram, which helped a lot in identifying how to perform the correct joins. Next thing I did was to write the joins (inner joins in our case), then added the filters and in the end I wrote the select statement, grabbing the necessary columns. The filter was done on the following columns from the <code>SupplierTransactions</code> table:
- TransactionTypeID = 5
- month(sup_trans.TransactionDate) = 11 -- this extracts the month from the transaction date and eheck if it equals to 11
- year(sup_trans.TransactionDate) = 2015 -- same as month, but for year

In the select statement, I also applied some transformations so that it replicates exactly the test output.
1. I used cast on dates to make sure they are of type date.
2. I replaced the isFinalised column with "YES" and "NO" values using a case statement (1="YES", 0="NO")
3. For the Description column I removed the double-quotes. 

The tests run successfully in Python

<img width="1440" height="207" alt="image" src="https://github.com/user-attachments/assets/31b59c96-7372-4753-95e9-971a68ef1e5c" />

There are 5 tests that are performing:
<details>
<summary>1. It checks the number of rows in each outputs.</summary>
<pre>
  def test_counts(sample_output, actual_output):
    sample_counts = len(sample_output)
    actual_counts = len(actual_output)
    assert sample_counts == actual_counts, f"Sample counts: {sample_counts} vs Actual counts: {actual_counts}"
</pre>
</details>
<details>
<summary>2. It checks if both datasets have the same number of columns.</summary>
<pre>
  def test_number_of_columns(sample_output, actual_output):
    sample_columns = len(sample_output.columns)
    actual_columns = len(actual_output.columns)
    assert sample_columns == actual_columns, f"Sample number of columns: {sample_columns} vs number of columns: {actual_columns}"
</pre>
</details>
<details>
<summary>3. Test if they have the same schema (data types).</summary>
<pre>
  def test_schema(sample_output, actual_output):
    data_types_check = (sample_output.dtypes.sort_index() == actual_output.dtypes.sort_index())
    assert len(data_types_check.loc[data_types_check == False].index.to_list()) == 0, "Different data types"
</pre>
</details>
<details>
<summary>4. Check if they have the same name of columns.</summary>
<pre>
  def test_column_is_same(sample_output, actual_output):
    sample_columns = sorted(sample_output.columns)
    actual_columns = sorted(actual_output.columns)
    assert sample_columns == actual_columns, "Different columns"
</pre>
</details>
<details>
<summary>5. Compare the two tables.</summary>
<pre>
  def test_is_same(sample_output, actual_output):
    assert actual_output.equals(sample_output), "The two dataframes differ"
</pre>
</details>

For the whole code, please refer the .sql file from <code>src/WideWorldImporters/sql_scripts/wide_world_importers_report.sql</code>

### Way of thinking - Bonus task
The goal of this task was to perform a query that returns the duplicates from <code>PurchaseOrders</code> table <code>Purchasing</code> schema. This was fairly easy to perform: the main hint was that a duplicate was a combination of <code>SupplierID</code>, <code>SupplierReference</code> and <code>OrderDate</code> columns. So that bit was easy to replicate with a <code>row_number()</code> function.
```
row_number() over (
            partition by SupplierID, SupplierReference, OrderDate
        )
```
But now we need something to order by. In the state above, it identifies the duplicates, but we don't know for sure which one to keep. For this, we're going to use the order by clause on <code>LastEditedWhen</code> column.
```
row_number() over (
            partition by SupplierID, SupplierReference, OrderDate
            order by LastEditedWhen
        ) as rnk
```
We can plug this piece of code into a CTE (Common Table Expression), selecting all columns from PurchaseOrders, along with this newly created column that assigns a number for each duplicate (original including). A value of "1" means that particular row was the first one inserted with that combination of IDs, the rest of records up to nth rank are duplicates.
The final select looks like this
```
select *
from purchase_orders_ranking -- name of the cte
where rnk > 1
```
We're using the <code>rnk > 1</code> so we only get what is a duplication of the records.

## VS Code setup - Pros and Cons <a name="vs-code-in-depth"></a>
In this section, I'm going to present a few pros and cons.

### Pros:
- Facilitates testing using frameworks such as pytest
- Easier to automate this process if it's necessary
- The parameters can easily be changed
- Email automation
- Data pipelines orchestration

### Cons:
- This solution uses pandas to work with the data. In a real-world scenario, the result might be a lot bigger than a few hundreds of records, which would be impossible to work on a local environment
- Connection to database can be slower due to the speed of fetching data from database
- Performance issues overall using current framework

A nice feature of this approach is the use of argparse library. This allows you to change the values of the where clause when you run the program. By default, the parameters are set to the correct value, so we can either run the .py script from IDE or use the following command:
```
python src/WideWorldImporters/python_scripts/export_wide_world_importers.py
```
Alternatively, we can also use <code></code> <code></code> <code></code> to overwrite these parameters from console, without altering the code.
```
python src/WideWorldImporters/python_scripts/export_wide_world_importers.py --trc-type 15 --trc-month 11 -trc-year 2015
```
## Final Thoughts and Improvements <a name="improvements"></a>
I really enjoyed this assignment, even though at first glance might've looked easy to resolve. It was nice that I had to play around and use other technologies (assuming that I understood the assignment).
As for improvements, the main thing I feel like I could've more worked on was on the tests. The initial tests on the provided sample passed, but I could've also picked random values for the parameters to test for other subsets of data, among many other things :D. 

Hope that this document is useful, easy to understand and according to this assignment


