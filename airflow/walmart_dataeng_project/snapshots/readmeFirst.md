### SnapShots in DBT
Snapshots helps us to implement Slowly Changing Dimensions (SCD) in DBT.
snapshots record changes to a mutable table over time.
snapshots manages the history.
* DBT implements SCD Type 2

### Type 2 SCD
In Type 2, we retain the history (Keep both old and new version) by adding a new record and then create version (start_date, end_date)
SCD Type 2 preserves historical changes by creating a new row for every changed version of a dimension record instead of overwriting the existing row.


Here we are using the snapshot to keep track of the changes on the Ephemeral Dimension tables defined in the [gold layer at](../models/gold/ephemeral/)
