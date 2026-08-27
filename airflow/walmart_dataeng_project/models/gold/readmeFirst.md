### Gold Layer (Mart)
The Gold Layer prepares the data for Business use. The data can be used for Reporting, Dashboarding or decision making by the Business Team or stake holders.

This is where we perform the dimensional data modeling. 
Here the tables will be either:
* Dimension Table
* Facts Table

#### Dimensions Table: 
A dimension is a table containing descriptive information about something
The dimensions table are context focused. Here we put all the textual data. We don't store any kind of numbers. Not the numbers store in ID, but numbers that can be used for aggregations.
We create dedicated table each context.
     * The Dimensions table provides context to the fact table

#### Facts Table: 
Here we store only numbers that can be aggregated.
    * Facts = Numbers

In the Gold Layer we don't care about the storage, we care about data retrieval and also the performance of our reports.

* We are creating the dimensional tables from the One Big Table we created in the [Silver Layer](../silver_b/obt_b.sql)




### Ephemeral model in dbt
An ephemeral model in dbt is a materialization type that does not create any physical table or view in the database.
ephemeral models are not directly built into the database. Instead, dbt will interpolate the code from an ephemeral model into its dependent models using a common table expression (CTE).

The materialization for the  [Gold Layer Ephemeral Model](../gold/ephemeral/) is defined in the [dbt_project.yml](../../dbt_project.yml) as shown below

`````````yaml
models:
  walmart_dataeng_project:
    # Config indicated by + and applies to all files under models/example/
    silver_t:
      +materialized: table
      +schema: silver_t
    silver_b:
      +materialized: table
      +schema: silver_b
    gold:
      +materialized: table
      +schema: gold
      # Ephemeral Materialization
      ephemeral:
        +materialized: ephemeral
`````````