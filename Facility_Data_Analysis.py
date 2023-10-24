import sqlite3
import pandas as pd


# Question 1
def counties_with_above_average_violations(column_name):
    conn = sqlite3.connect("region.db")
    cursor = conn.cursor()

    sql = f"SELECT * FROM county_per_1000 WHERE {column_name}>(SELECT AVG({column_name}) FROM county_per_1000)"
    df_fac = pd.read_sql_query(sql, conn)

    return df_fac


# Question 2
def counties_with_below_average_violations_or_inspections(
    violation_or_inspection_table_name,
):
    conn = sqlite3.connect("region.db")
    cursor = conn.cursor()

    if violation_or_inspection_table_name == "violation":
        sql = f"SELECT * FROM violation WHERE count<(SELECT AVG(count) FROM violation)"
    elif violation_or_inspection_table_name == "inspection":
        sql = (
            f"SELECT * FROM inspection WHERE count<(SELECT AVG(count) FROM inspection)"
        )
    else:
        raise Exception("Use the exact table name for the parameters")
    df_fac = pd.read_sql_query(sql, conn)

    return df_fac
