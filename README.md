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
### Step 1. Clone this repository.


## Dataset Description
WideWorldImporters is a fictitious wholesale novelty goods importer and distributor based in San Francisco, designed by Microsoft to serve as a comprehensive sample database for SQL Server and Azure SQL Database. It demonstrates modern database capabilities, including transactional (OLTP) and analytical (OLAP) processing, with data covering sales, purchasing, and warehouse operations. For more details you can access the [Technical Documentation](https://docs.microsoft.com/en-us/sql/samples/wide-world-importers-oltp-database-catalog?view=sql-server-ver15).

During this assignment, we will only be working with Purchasing database. We are mainly interested in extracting transactions so to better understand the schema we are working with, consult the image below that shows the relational diagram of the used tables. 
<img width="1866" height="1090" alt="image" src="https://github.com/user-attachments/assets/34bdf99f-527b-4f9d-a06c-1a959810499c" />

