import sqlite3

def insert_resized_data_to_db(resized_df, db_path):
    """
    Inserts resized dataframe into the SQLite database.

    Args:
        resized_df (pd.DataFrame): The dataframe containing resized image data.
        db_path (str): Path to the SQLite database.
    """
    try:
        # Connect to the database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Prepare columns and placeholders dynamically
        columns = ", ".join(resized_df.columns)
        placeholders = ", ".join(["?"] * len(resized_df.columns))

        # SQL Insert query
        insert_query = f"INSERT INTO resized_image_data ({columns}) VALUES ({placeholders})"

        # Insert each row from the dataframe
        for _, row in resized_df.iterrows():
            cursor.execute(insert_query, tuple(row))

        # Commit the transaction
        conn.commit()
        print(f"Data inserted successfully into the database at {db_path}")

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the connection
        conn.close()