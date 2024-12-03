import uvicorn

from api import app
from utils import create_resized_image_database, resize_csv_image, insert_resized_data_to_db

if __name__ == "__main__":
    # Launch the API server
    print('creating db')
    create_resized_image_database()
    print('reading and resizing the image')
    resized_img = resize_csv_image('./Challenge2.csv')
    print('inserting the resized image into db')
    insert_resized_data_to_db(resized_img, './resized_image.db')

    uvicorn.run(app, host="0.0.0.0", port=8000)
