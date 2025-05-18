import pandas as pd

# File paths
excel_path = 'population.xlsx'     # Replace with your Excel file name
sql_dump_path = 'dump.sql'

# Load Excel file
xls = pd.ExcelFile(excel_path)

with open(sql_dump_path, 'w', encoding='utf-8') as f:
    for sheet_name in xls.sheet_names:
        df = xls.parse(sheet_name)
        table_name = sheet_name.replace(" ", "_")  # Clean table name
        
        # Write CREATE TABLE
        f.write(f"DROP TABLE IF EXISTS `{table_name}`;\n")
        f.write(f"CREATE TABLE `{table_name}` (\n")
        for col in df.columns:
            f.write(f"  `{col}` TEXT,\n")
        f.seek(f.tell() - 2)  # Remove last comma
        f.write("\n);\n\n")

        # Write INSERT INTO
        for _, row in df.iterrows():
            values = ', '.join(f"'{str(v).replace('\'', '\\\'')}'" if pd.notna(v) else "NULL" for v in row)
            f.write(f"INSERT INTO `{table_name}` VALUES ({values});\n")
        f.write("\n")

print(f"SQL dump created: {sql_dump_path}")
