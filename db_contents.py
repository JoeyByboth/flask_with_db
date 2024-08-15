from sqlalchemy import create_engine
import pandas as pd

DATABASE_URL = "postgresql://your_postgres_user:your_postgres_password@localhost:5432/your_postgres_db"
engine = create_engine(DATABASE_URL)

# Fetch data from a table
df = pd.read_sql("SELECT * FROM your_table_name", engine)
print(df)

