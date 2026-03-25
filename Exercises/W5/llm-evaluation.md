## Part 1: Accuracy Evaluation (20 minutes)

### Task 1.1: SQL Accuracy Check

Submit the following prompt to your LLM:

```
Write a BigQuery SQL query that:
1. Calculates a 7-day rolling average of daily revenue
2. Uses the table: analytics.daily_sales (columns: sale_date DATE, revenue NUMERIC)
3. Uses a window function
4. Orders by date ascending
```

**Evaluate the output using this rubric:**
GEMINI, ChatGPT gave basically the same response 
| Criterion | Score (1-5) | Notes |
| --------- | ----------- | ----- |
| Syntax correctness (valid BigQuery SQL) | 5 | yes |
| Window function usage (correct frame clause) | 5 | ROWS BETWEEN 6 PRECEDING AND CURRENT ROW |
| Rolling average logic (correct 7-day calculation) | 5 | AVG(revenue) OVER ( ORDER BY sale_date ASC ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS rolling_avg_7d |
| Column references match the provided schema | 5 | analytics.daily_sales, sale_date, and revenue |
| Overall: would this query run correctly? | 5 | yes |

**Verification steps:**

1. Check that the window frame specifies the correct range (6 PRECEDING AND CURRENT ROW or equivalent)
2. Verify the function used is AVG, not SUM
3. Confirm DATE ordering is correct
4. Look for any BigQuery-specific syntax issues

### Task 1.2: Fact Check

Submit this prompt:

```
Explain how BigQuery stores data internally. Include details about:
1. The storage format
2. How partitioning works at the storage level
3. The relationship between slots and query processing
4. Compression techniques used
```

**Evaluate the response:**
GEMINI
| Statement from LLM | Verified? (Yes/No/Unsure) | Source Used to Verify |
| ------------------- | ------------------------- | --------------------- |
| 1. Storage Format: CapacitorBigQuery stores data in a proprietary columnar format called Capacitor. Unlike traditional databases that store data row-by-row, BigQuery stores each column separately.Efficiency: When you run a query like SELECT name FROM users, BigQuery only reads the "name" column from disk, ignoring all others. This drastically reduces I/O.Semi-Structured Data: Capacitor is specifically designed to handle nested and repeated fields (like JSON-style data) efficiently by "shredding" them into a columnar form while maintaining their structural relationship.| yes | https://medium.com/@nikhilmogre1998/how-google-bigquery-works-architecture-components-and-query-execution-db8b24c23946 |
| 2. Partitioning at the Storage Level Partitioning is a way of physically dividing a table into segments (partitions) based on a specific column, such as a DATE or TIMESTAMP. Physical Separation: Each partition is stored as a separate set of files in Colossus (Google’s distributed file system). Partition Pruning: When a query includes a filter on the partition column (e.g., WHERE date = '2024-01-01'), BigQuery’s engine looks at the table metadata and completely ignores all files belonging to other dates. Cost & Speed: This is the most effective way to limit the "bytes scanned," which directly lowers your costs and speeds up the query. | yes | https://docs.hevodata.com/destinations/data-warehouses/google-bigquery/bigquery-data-structure/ |
| 3. Slots and Query Processing: Query execution is handled by a massive distributed engine called Dremel. What is a Slot? A "slot" is a unit of computational capacity (CPU, RAM, and networking). You can think of it as a small worker node in a massive cluster. The Serving Tree: When you submit a query, Dremel builds an execution tree: Root Server: Receives the query and divides it into hundreds or thousands of smaller tasks. Mixers: Act as middle managers, aggregating partial results from the workers. Leaf Nodes (Slots): These are the actual workers that pull data from Colossus, perform the filters/math, and send results back up the tree. Dynamic Allocation: BigQuery automatically assigns more slots to complex queries and fewer to simple ones, ensuring multi-tenant fairness. | yes | https://medium.com/@nikhilmogre1998/how-google-bigquery-works-architecture-components-and-query-execution-db8b24c23946 |
| 4. Compression Techniques: Because similar data is stored together in columns, Capacitor achieves extremely high compression ratios (often 10:1 or better). It uses several advanced techniques: Run-Length Encoding (RLE): If a column has many repeating values (e.g., "USA" repeated 1,000 times), it stores the value once plus a count. Dictionary Encoding: Replaces long strings with short integer keys to save space. Bit-Vector Encoding: Used for columns with low cardinality (few unique values). Operating on Compressed Data: One of BigQuery’s "secret sauces" is its ability to perform many operations (like filters) directly on compressed data without decompressing it first, which saves massive amounts of CPU time. | unsure | https://airbyte.com/blog/bigquery-guide#:~:text=Advanced%20compression%20algorithms%20in%20Capacitor,costs%20while%20maintaining%20query%20performance .. https://medium.com/google-cloud/bigquery-basics-internals-part-2-7769f59d01e4 .. dictionary encoding, bit-vector encoding, and operating on compressed data sources seem sus. The keywords it gave are not written in the source that it gave. |


Use the [BigQuery documentation](https://cloud.google.com/bigquery/docs/storage_overview) to verify at least 3 claims made by the LLM. Document which claims are accurate and which appear to be hallucinated.


### Task 2.1: API Hallucination Hunt

Submit this prompt:

```
Show me the Python code to use BigQuery's built-in 
machine learning feature to create a linear regression 
model using the ML.CREATE_MODEL syntax. Include the 
Python client library code to execute this.
```

**Your Task:**

1. Read through the generated code carefully
2. Look for:
   - Function names that do not exist in the BigQuery Python client
   - SQL syntax that is not valid BigQuery ML syntax
   - Configuration options that do not exist
   - Import statements for non-existent modules
3. Verify against the [BigQuery ML documentation](https://cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create)

**Document your findings:**
GEMINI
| Item | LLM Generated | Actual (from docs) | Hallucination? |
| ---- | ------------- | ------------------- | -------------- |
| CREATE | CREATE OR REPLACE MODEL `model_name` | CREATE OR REPLACE MODEL `model_name` | no |
| OPTIONS() | OPTIONS( model_type='linear_reg', input_label_cols=['revenue'], ls_init_learn_rate=0.15, max_iterations=20 ) AS {query} | OPTIONS(model_type='linear_reg', input_label_cols=string_array, ls_init_learn_rate=float64_value, max_iterations=int64_value) {query} | no |
| {query statement} | SELECT revenue, is_holiday, temperature, day_of_week FROM `your_project.your_dataset.daily_sales_features` WHERE sale_date BETWEEN '2023-01-01' AND '2025-12-31' | [AS {query_statement (training_data AS (query_statement), custom_holiday AS (holiday_statement))}] | yes, only gave one statement |
| check training stats | client.get_model(model_id) | there is no get_model() | yes |


### Task 2.2: Citation Verification

Submit this prompt:

```
Cite three specific research papers or official documents 
that discuss best practices for data warehouse design. 
Include the title, author(s), year, and a one-sentence summary.
```

**Your Task:**
GEMINI OUTPUT

1. The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling
Author(s): Ralph Kimball and Margy Ross

Year: 2013 (3rd Edition)

Summary: This is the industry standard for "bottom-up" design, advocating for the Star Schema and Conformed Dimensions to ensure data is intuitive for business users and performant for analytical queries.

2. Building the Data Warehouse
Author(s): William H. Inmon

Year: 2005 (4th Edition)

Summary: Known as the "father of data warehousing," Inmon outlines a "top-down" approach where data is first integrated into a centralized, normalized (3NF) Enterprise Data Warehouse before being pushed out to specific departmental data marts.

3. Google Cloud Architecture Framework: Data Warehouse Design
Author(s): Google Cloud Professional Services / Engineering

Year: 2025/2026 (Updated continuously)

Summary: This official technical documentation outlines modern ELT (Extract, Load, Transform) best practices, emphasizing the separation of storage and compute, the use of nested/repeated fields for performance, and cost-optimization through partitioning and clustering.

1. Attempt to verify each citation
2. Search for the paper title online
3. Does it exist? Are the authors correct? Is the year correct?
4. Document your findings
    - The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, exists
        - Book by Margy Ross and Ralph Kimball
        - Correct publish year
    - Building the Data Warehouse, exists
        - Book by William (Bill) Inmon
        - Originally published in 1992, 4th edition published 2005
    - 