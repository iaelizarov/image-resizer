import sqlite3

def create_resized_image_database(db_path='./resized_image.db', num_columns=150):
    """
    Create a SQLite database to store resized image data.

    Parameters:
        db_path (str): Path to the database file.
        num_columns (int): Number of columns for resized image (excluding depth).
    """
    # Connect to the SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create the column names dynamically
    columns = ", ".join([f"col{i+1} INTEGER" for i in range(num_columns)])

    # Create the table with depth and resized image columns
    cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS resized_image_data (
        depth REAL PRIMARY KEY,
        {columns}
    )
    ''')

    # Commit changes and close the connection
    conn.commit()
    conn.close()
    print(f"Database created successfully at '{db_path}'")