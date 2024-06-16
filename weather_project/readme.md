# Weather Project

This Django application parses summarized weather data from the UK MetOffice and serves it via a RESTful API.

## Project Setup

### Prerequisites

Ensure you have the following installed:
- Python 3.11
- pip (Python package installer)
- Docker (optional, for containerization)

### Installation

1. **Clone the repository**:
    ```bash
    git clone <repository_url>
    cd weather_project
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    on ubuntu : source venv/bin/activate  
    On Windows,: `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations**:
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser** (optional, for admin access):
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

## Docker Setup

To run the project using Docker:

1. **Build the Docker image**:
    ```bash
    docker build -t weather_project .
    ```

2. **Run the Docker container**:
    ```bash
    docker run -p 8080:8080 weather_project
    ```

## URLs to Test

### API Endpoints

1. **List Weather Data**:
    - **URL**: `/weather/`
    - **Method**: GET
    - **Description**: Retrieve a list of all weather data.

2. **Retrieve Weather Data Detail**:
    - **URL**: `/weather/<int:pk>/`
    - **Method**: GET
    - **Description**: Retrieve detailed weather data for a specific entry.

3. **Filter Weather Data**:
    - **URL**: `/weatherdataFilter/`
    - **Method**: GET
    - **Description**: Filter weather data based on region, parameter, year, and month.
    - **Parameters**:
        - `region`: The region to filter by (e.g., Scotland).
        - `parameter`: The parameter to filter by (e.g., Rainfall).
        - `year`: The year to filter by (e.g., 2020).
        - `month`: The month to filter by (e.g., jan).

    - **Example**:
        ```
        /weatherdataFilter/?region=Scotland&parameter=Rainfall&year=2020&month=jan
        ```

4. **Parse Weather Data**:
    - **URL**: `/parse-weather-data/`
    - **Method**: GET
    - **Description**: Parse and store weather data from the UK MetOffice.

### HTML View

1. **Filter Weather Data Form**:
    - **URL**: `/filter/`
    - **Description**: A simple HTML form to filter weather data.

## Running Tests

To run the tests for the project:

```bash
python manage.py test
