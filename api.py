from fastapi import FastAPI, HTTPException, Query
import sqlite3
import pandas as pd
from typing import List

# Initialize the FastAPI app
app = FastAPI()

# Path to your SQLite database
DB_PATH = "resized_image.db"

@app.get("/get-frames/")
def get_frames(depth_min: float = Query(..., description="Minimum depth"),
               depth_max: float = Query(..., description="Maximum depth")):
    """
    Retrieve frames from the database between depth_min and depth_max.

    Args:
        depth_min (float): Minimum depth value.
        depth_max (float): Maximum depth value.

    Returns:
        dict: Contains the frames between depth_min and depth_max.
    """
    try:
        conn = sqlite3.connect(DB_PATH)
        
        # Fetch data between depth_min and depth_max
        query = """
            SELECT * FROM resized_image_data
            WHERE depth BETWEEN ? AND ?
            ORDER BY depth
        """
        result = pd.read_sql_query(query, conn, params=(depth_min, depth_max))

        # Close the connection
        conn.close()

        # Check if any data was returned
        if result.empty:
            raise HTTPException(status_code=404, detail="No data found for the given depth range.")

        # Convert data to a dictionary for JSON response
        data = result.to_dict(orient="records")
        return {"frames": data}

    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f"Database error: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {e}")
