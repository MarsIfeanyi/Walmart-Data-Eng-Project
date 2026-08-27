
* SILVER (Transformation) Layer: In this Layer data will be transformed and also aggregated.
In the Silver layer, we implement or create the One Big Table, OBT


silver_t = Silver Technical Layer (Staging and Intermediate)

The Technical Layer is for the data team and ensures the data is reliable and consistent.
It focuses on the technical, behind-the-scenes tasks of cleaning and organizing raw data from source

The schema materialization is defined in the [bdt_project.yml](../../dbt_project.yml) as a custom schema using the [macro](../../macros/custom_schema.sql), hence we don't have separate schema defintion for each file(table) in the silver_t folder.