
# Food Inspections Data Analysis Project

This repository contains the data modeling, integration, and BI dashboard creation for a comprehensive analysis of food establishment inspections across multiple cities including Chicago and Dallas. The project aims to transform raw food inspection data into insightful visualizations that highlight inspection results, types, risk categories, facility types, violations, and business information.

## Overview

- **Data Ingestion**: Data is acquired in a delimited format, loaded into staging tables prefixed with `stg_`, and undergoes data profiling.
- **Dimensional Modeling**: A star schema is designed to represent the inspection data, with SQL scripts for table creation.
- **Data Integration**: Data is processed and loaded into a dimensional model using ETL workflows, ensuring data integrity and consistency.
- **BI Dashboards**: Interactive dashboards are created in both Power BI and Tableau to visualize and analyze the inspection data.

## Project Structure

- `/staging` - Contains the initial staging scripts and data profiling reports.
- `/models` - Includes the dimensional model diagrams and DDL scripts.
- `/integration` - ETL workflows and scripts for populating the star schema.
- `/dashboards` - Dashboard files and supporting documents for BI tools.

## Insights

The dashboards provide a detailed breakdown of food inspection outcomes, facilitating an in-depth understanding of public health compliance in the food industry. The analysis covers various dimensions, such as inspection types, risk levels, and specific violation codes.

---

Feel free to customize this template further to match the specific details and structure of your GitHub repository.
