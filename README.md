# Wide World Importers - Purchase Order Analytics
## Project Overview
The primary goal is to extract data for reporting purposes from a fictional wholesale novelty goods distributor, Wide World Importers

By leveraging the classic Microsoft sample database, Wide World Importers (OLTP), this project demonstrates a modern data workflow. It extracts transactional data from the operational database, performs transformations to clean and structure the data for analysis. The focus is specifically on the purchasing domain, utilizing tables related to purchase orders, suppliers, and financial transactions.

Throughout this document, I'm going to explain the setup I've used, why I used it, how you can have the same setup in order to use this repo and, most importantly, the logic for the main task and for the bonus task. This whole setup might be unnecessary, but I tried to think a few steps ahead and tried to come with a setup that might be closer to a real-world implementation of this kind of pipeline. There's still room for improvements
```bash tree
