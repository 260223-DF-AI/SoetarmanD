Using only zero-shot prompting (no examples), write a prompt that generates a BigQuery SQL query to:

- Find the top 5 departments by average salary
- Include the department name, average salary, and employee count
- Only include departments with more than 10 employees
- Order by average salary descending

**Your Task:**

1. Write your prompt
2. Submit it to the LLM
3. Evaluate the output -- does it produce valid BigQuery SQL?
4. If not, refine your prompt and try again
5. Document your original prompt, your refined prompt (if needed), and the final output

You are a BigQuery expert developer.
Write me a BigQuery SQL query to find the top 5 departments by average salary.
Be sure to include these columns:
department name, average salary, employee count
Only inlcude departments with more than 10 employees.
Ensure that it is ordered by average salary descending.

# Claude: 
Here's the BigQuery SQL query:
sqlSELECT
    department_name,
    ROUND(AVG(salary), 2)   AS average_salary,
    COUNT(*)                AS employee_count
FROM
    `your_project.your_dataset.employees`
GROUP BY
    department_name
HAVING
    COUNT(*) > 10
ORDER BY
    average_salary DESC
LIMIT 5;
A few notes:

Replace `your_project.your_dataset.employees` with your actual table reference.
HAVING COUNT(*) > 10 filters out departments with 10 or fewer employees after grouping — this is the correct place for that filter rather than WHERE, since it applies to an aggregate.
ROUND(..., 2) keeps the average salary tidy to 2 decimal places — drop it if you want full precision.
ORDER BY average_salary DESC works here because BigQuery allows referencing aliases in ORDER BY.

# ChatGPT:
Here’s a clean and efficient BigQuery SQL query that meets all your requirements:

SELECT
  department_name,
  AVG(salary) AS average_salary,
  COUNT(*) AS employee_count
FROM
  `your_project.your_dataset.employees`
GROUP BY
  department_name
HAVING
  COUNT(*) > 10
ORDER BY
  average_salary DESC
LIMIT 5;
🔍 What this does:
AVG(salary) → calculates the average salary per department
COUNT(*) → counts employees in each department
HAVING COUNT(*) > 10 → filters only departments with more than 10 employees
ORDER BY average_salary DESC → ranks highest average salary first
LIMIT 5 → returns only the top 5 departments
⚠️ Replace:
your_project.your_dataset.employees with your actual table path

If your column names differ (e.g., dept_name or emp_salary), adjust accordingly.

# Gemini:
Gemini said
As requested, here is the BigQuery SQL query to identify your top-performing departments by compensation.

I have used a standard GROUP BY clause and a HAVING filter to ensure we only look at departments with a robust enough sample size (more than 10 employees).

SQL
SELECT
    department_name,
    AVG(salary) AS average_salary,
    COUNT(employee_id) AS employee_count
FROM
    `your_project.your_dataset.employees`
GROUP BY
    department_name
HAVING
    employee_count > 10
ORDER BY
    average_salary DESC
LIMIT 5;
A Few Expert Tips for BigQuery:
Precision: If your salary column is a FLOAT64, you might want to wrap the average in a ROUND(..., 2) to keep the output clean for financial reporting.

Cost Efficiency: BigQuery is a columnar database. If your table has 100 columns but you only need department_name, salary, and employee_id, this query is already optimized because it only "touches" those specific columns.

NULL Handling: Note that AVG() automatically ignores NULL values in BigQuery, but COUNT(employee_id) will only count rows where the ID is present. If you want to count every row regardless of nulls, you could use COUNT(*).

Would you like me to show you how to join this with a separate departments table if your current table only contains department_id?

### Challenge 1.2: Error Explanation

Write a zero-shot prompt that asks the LLM to explain this error message in plain English and suggest a fix:

```
google.api_core.exceptions.BadRequest: 400 Syntax error: 
Expected end of input but got keyword SELECT at [3:1]
```

**Your Task:**

1. Craft a prompt that provides enough context for a useful explanation
2. Evaluate whether the explanation is accurate
3. Rate the quality of the fix suggestion (1-5 scale)

# Prompt
You are an expert at diagnosing errors within SQL queries and Google APIs.
Explain the following error message in plain English so any human could understand it.
google.api_core.exceptions.BadRequest: 400 Syntax error: 
Expected end of input but got keyword SELECT at [3:1]
Also include a suggestion as to how to fix the given error.

# Claude: 4/5 could have given a better detailed breakdown of potential reasons the error was happening.
This error means you accidentally wrote two SELECT statements where only one is expected — BigQuery hit a second SELECT keyword when it thought the query was already finished.
Common cause: Two queries stacked together without a semicolon separator or a proper subquery structure. For example:
sql-- ❌ Broken
SELECT name FROM users
SELECT age FROM users
How to fix it — pick one of these depending on what you actually want:

Run just one query — delete the extra SELECT:

sql   SELECT name FROM users

Combine columns into one query:

sql   SELECT name, age FROM users

Use a subquery (if the second SELECT depends on the first):

sql   SELECT name
   FROM (SELECT name, age FROM users)
   WHERE age > 30

Run them as separate statements (if your client supports it) by separating them with a semicolon:

sql   SELECT name FROM users;
   SELECT age FROM users;
The [3:1] in the error tells you the rogue SELECT is on line 3, column 1 of your query — that's the exact spot to look at.


# ChatGPT: 5/5
Here’s what that error means in plain English:

🧠 What the error is saying

“Expected end of input but got keyword SELECT at [3:1]”

BigQuery was reading your SQL query.
It thought your query was already finished.
But then it unexpectedly found another SELECT statement at line 3, column 1.

👉 In simple terms:
“I thought your query was done, but then you started a new SELECT statement where I wasn’t expecting one.”

💥 Why this usually happens

This error typically occurs when:

You accidentally wrote two SELECT statements back-to-back

SELECT * FROM table1
SELECT * FROM table2  -- ❌ not allowed like this
You forgot something before the second SELECT, like:
A comma (,) in a CTE
A UNION / UNION ALL
Proper query structure

You’re using a CTE (WITH clause) incorrectly

WITH my_cte AS (
  SELECT * FROM table1
)
SELECT * FROM table2  -- ✅ valid

SELECT * FROM table3  -- ❌ unexpected extra query
✅ How to fix it

Depending on your intent, here are common fixes:

✔️ If you meant to combine results:

Use UNION ALL (or UNION)

SELECT * FROM table1
UNION ALL
SELECT * FROM table2
✔️ If you're using CTEs:

Make sure everything connects into one final SELECT

WITH my_cte AS (
  SELECT * FROM table1
)
SELECT * FROM my_cte
✔️ If it’s just extra code:

Remove the unintended second SELECT

🔧 Quick debugging tip

Go to line 3, column 1 in your query and check:

Is there a SELECT starting there?
Should it be connected to the previous query?
Or should it be removed?


# Gemini: 5/5
This error is the SQL equivalent of a "run-on sentence." It usually happens when you try to cram two separate thoughts into one space without the proper punctuation or structure.

In plain English, the computer is saying: "I finished reading your first command, and I expected you to stop talking—but then you started a second command right in the middle of the page, and I don't know what to do with it."

Breaking Down the Message
400 BadRequest: This is a general status code meaning the server received your request but can't process it because something is wrong with the way you wrote it.

Expected end of input: The database engine thought your query was over.

but got keyword SELECT: Instead of finding the "end," it found a new SELECT statement starting up.

at [3:1]: This is your GPS coordinate for the error. It happened on Line 3, Character 1.

Why This Happens
This error almost always stems from one of two scenarios:

Missing Semicolons: You are trying to run two queries at once (e.g., a CREATE TABLE followed by a SELECT), but you didn't put a semicolon (;) between them to tell the engine where the first one ends.

Accidental Copy-Paste: You might have accidentally pasted a second query at the bottom of your script, or you have a "dangling" SELECT that isn't wrapped in a subquery.

How to Fix It
Depending on what you are trying to achieve, here are the two most common solutions:

Option A: Separate the queries with a semicolon
If you actually want to run two different commands, simply put a ; at the end of the first one.

The Error:

SQL

SELECT * FROM users
SELECT * FROM orders -- The engine trips here!
The Fix:

SQL

SELECT * FROM users;
SELECT * FROM orders;
Option B: Use a Subquery or Union
If you intended for both SELECT statements to be part of the same result, you need to use a operator like UNION ALL or wrap one in parentheses.

The Fix (Combining results):

SQL

SELECT user_name FROM users
UNION ALL
SELECT admin_name FROM admins;
Would you like to paste the specific SQL code you're working on so I can pinpoint exactly where the syntax broke down for you?

### Challenge 1.3: Data Dictionary Entry

Write a zero-shot prompt to generate a data dictionary entry for a column called `customer_lifetime_value` in a `dim_customer` table. The entry should include: data type, description, business definition, calculation method, and example values.

**Your Task:**

1. Write the prompt
2. Evaluate whether the output would be useful for a new team member
3. Note what additional context you would need to add to make it more accurate

You are an expert data engineer that is going to generate a data dictionary.
This data dictionary entry will be for a column called:
`customer_lifetime_value`
and is inside of a table called:
`dim_customer`
Ensure that the entry includes:
data type, description, business definition, calculation method, example values
Make this in a way that would be useful for a potential new team member.

# Claude: Gave an 'improved' prompt instead of implementing what was asked of it
Here's a prompt you could improve or use as-is — but first, a few thoughts:
This is already a solid prompt. To make it even stronger for a new team member, I'd suggest a couple of quick enhancements:This is already a solid prompt. Here are two quick improvements worth making:

Add a notes / caveats field — new team members often get tripped up by edge cases (nulls, exclusions, restatements). Calling this out explicitly saves confusion.
Add a related columns / tables field — helps orient someone navigating an unfamiliar schema.

Here's a polished version with those additions:
  ::view-transition-group(*),
  ::view-transition-old(*),
  ::view-transition-new(*) {
    animation-duration: 0.25s;
    animation-timing-function: cubic-bezier(0.19, 1, 0.22, 1);
  }
VvisualizeVvisualize show_widgetThe two new fields (highlighted in green) are the main additions:
Notes & caveats — CLV columns are notorious for surprises: nulls for brand-new customers, exclusion of refunded orders, periodic restatements. Explicitly asking for this prevents a new analyst from confidently using a value that has hidden gotchas.
Related columns / tables — CLV rarely lives alone. Someone new to the schema needs to know that clv_segment or first_order_date are the natural companions, or they'll end up joining to the wrong place.
Everything else from your original prompt is preserved as-is — it was already well-structured.


# ChatGPT: gave a pretty comprehensive breakdown, to make it more accurate could give additional context/information like how the CLV is calculated, etc.
Here’s a clear, onboarding-friendly data dictionary entry for your column:

Data Dictionary Entry

Table Name: dim_customer
Column Name: customer_lifetime_value

1. Data Type

NUMERIC (or DECIMAL(18,2) depending on warehouse)
Represents a monetary value stored with precision (typically 2 decimal places).

2. Description

The total net revenue a customer is expected to generate over the entire duration of their relationship with the business.

3. Business Definition

Customer Lifetime Value (CLV) measures how valuable a customer is to the company from their first purchase through their most recent (or predicted final) interaction.

It is used by business stakeholders to:

Identify high-value customers
Guide marketing spend and customer acquisition strategies
Segment customers for retention campaigns
Forecast long-term revenue
4. Calculation Method

CLV can be calculated in different ways depending on data maturity. In this table, it is typically derived using a historical model:

Basic Historical Formula:

customer_lifetime_value = SUM(total_revenue - total_cost)

Where:

total_revenue = sum of all completed purchases by the customer
total_cost = associated costs (e.g., discounts, returns, servicing costs)

Alternative (Predictive Model - if applicable):

CLV = (average_order_value * purchase_frequency) * customer_lifespan

Implementation Notes:

Only completed/paid transactions are included
Refunds and returns should reduce total revenue
Value is aggregated at the customer_id level
Updated periodically (e.g., daily or weekly ETL job)
5. Example Values
customer_id	customer_lifetime_value
1001	1250.75
1002	89.99
1003	5430.20
1004	0.00
6. Additional Notes for New Team Members
This field is non-negative in most cases, but edge cases (e.g., excessive refunds) may result in negative values depending on business rules.
Always confirm whether the value is:
Historical (actuals only) or
Predictive (includes modeled future value)
Check upstream transformation logic (e.g., in fact_orders or revenue models) if numbers look off.

If you want, I can also generate a dbt-style YAML version or align this with your company’s documentation standard.


# Gemini: acted as a member of the team welcoming in a new team member. Gave a good breakdown of important things to consider  
Welcome to the team! Glad to have you on board. As you're getting settled into our dim_customer table, one of the most critical fields you'll be working with is customer_lifetime_value (CLV).Think of this as the "VIP Score." It tells us exactly how much a customer is worth to the business over the long haul, helping Marketing decide who to pamper and Finance predict future cash flows.Here is the breakdown for your data dictionary:Column: customer_lifetime_valueTable: dim_customerAttributeDetailsData TypeDECIMAL(18, 2)Business DefinitionThe total gross profit a customer is expected to generate for the company throughout their entire relationship with the brand. It accounts for historical purchases and predicts future value based on engagement patterns.DescriptionA calculated metric used to segment customers by their long-term financial contribution. High values indicate "Whale" accounts, while low or zero values may indicate one-time buyers or high-acquisition-cost leads.Example Values450.00, 1250.75, 0.00 (New Lead), 15200.40Calculation MethodTo keep our reporting consistent, we use a Predictive CLV model. While the exact SQL logic lives in our dbt transformation layer, the conceptual formula is:$$CLV = (\text{Average Order Value} \times \text{Purchase Frequency}) \times \text{Customer Lifespan}$$Note: In our current pipeline, this value is updated nightly during the ETL run. It incorporates a churn probability factor—if a customer hasn't purchased in 6 months, you'll see this value begin to decay in the upstream models.Why This MattersWhen you're building dashboards or joining this table to fct_orders, keep in mind that this column is a snapshot in time. If you need to see what a customer's CLV was six months ago, you'll need to reference our snapshot table, scd_dim_customer.Would you like me to generate the SQL DDL for this table so you can see how the rest of the schema is structured?


## Part 2: Few-Shot Prompting (15 minutes)

### Challenge 2.1: Column Name Standardization

You need the LLM to convert column names from various formats to snake_case following your team's convention.

**Provide these examples in your prompt:**

- `CustomerFirstName` -> `customer_first_name`
- `order-total-amount` -> `order_total_amount`
- `PRODUCT ID` -> `product_id`

**Then ask it to convert:**

- `ShippingAddress Line1`
- `total_Revenue_YTD`
- `customerEmailAddress`
- `ORDER__STATUS__CODE`

**Your Task:**

1. Write the few-shot prompt with the 3 examples
2. Submit and evaluate: did it follow the pattern correctly for all 4 inputs?
3. Were there any the model struggled with? Why?
