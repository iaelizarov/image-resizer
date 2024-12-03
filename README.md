# Image Resizer Application

## 1. Structure

The image resizer application is organized as follows:

- **API Endpoints:** Defined in the api.py file, the application provides endpoint to retrieve frames from resized image based on 2 parameters depth_min and depth_max

- **Initializing functions:** All core logic for initializing the databased, resizing the image, and putting it into database is located in utils folder.

- **Database:** A SQLite database (resized_image.db) stores information about resized image with columns depth, col1, col2, ..., col150.

- **Docker Configuration:** The Dockerfile contains all the steps to set up the application in a containerized environment, and it includes running the main script.

- **Main Logic:** The project contains the Challenge2.csv file with the original image. Running the application will trigger the creation of a database, resizing of the original image, and insertion of the resized image into the database, after which the service will start.

## 2. How to Run It

**Build the Docker Image**

`docker build -t image-resizing-app .`

**Run the Docker Container**

`docker run -d -p 8000:8000 --name resizing-app image-resizing-app`

**Access the Running Application**

The application will be accessible at http://127.0.0.1:8000.

## 3. Description of API Requests

**Get Frames**

Endpoint: `GET /api/get-frames/`

Description: Getting the frames between depth_min and depth_max for the resized image.

## 4. Visualization of the results

There is a notebook "resize_test_requests.ipynb" attached that contains the request and the results of the visualization. Custom colormap can be applied in this notebook.
