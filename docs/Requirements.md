### Project Requirements

This section outlines the requirements for setting up and running the Project Management API. The requirements include the necessary software, dependencies, and environment configurations.

#### Software Requirements

1. **Python**: The project is built using Python 3.6+.
2. **SQLite**: The project uses SQLite as the database. SQLite is included with Python, so no additional installation is required.
3. **Docker** (Optional): For containerization and running the application in a Docker container.

#### Python Dependencies

The project relies on several Python packages, which are listed in the

requirements.txt

file. Below is a list of the main dependencies along with a brief description of each:

1. **FastAPI**

   - **Package**: `fastapi`
   - **Description**: FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints. It is used to create the API endpoints and handle HTTP requests.
   - **Documentation**: [FastAPI Documentation](https://fastapi.tiangolo.com/)

2. **Uvicorn**

   - **Package**: `uvicorn[standard]`
   - **Description**: Uvicorn is a lightning-fast ASGI server implementation, using `uvloop` and `httptools`. It is used to serve the FastAPI application.
   - **Documentation**: [Uvicorn Documentation](https://www.uvicorn.org/)

3. **SQLAlchemy**

   - **Package**: `sqlalchemy`
   - **Description**: SQLAlchemy is the Python SQL toolkit and Object-Relational Mapping (ORM) library. It is used for database interactions, including defining models and performing CRUD operations.
   - **Documentation**: [SQLAlchemy Documentation](https://www.sqlalchemy.org/)

4. **Pydantic Settings**

   - **Package**: `pydantic-settings`
   - **Description**: Pydantic is a data validation and settings management library using Python type annotations. It is used for configuration management in the project.
   - **Documentation**: [Pydantic Documentation](https://pydantic-docs.helpmanual.io/)

5. **Loguru**
   - **Package**: `loguru`
   - **Description**: Loguru is a library that aims to bring enjoyable logging in Python. It is used for logging within the application.
   - **Documentation**: [Loguru Documentation](https://loguru.readthedocs.io/)

#### Installation

To install the project dependencies, you can use the

requirements.txt

file. Run the following command in your terminal:

```sh
pip install -r requirements.txt
```

#### Example

requirements.txt

File

```txt
fastapi
uvicorn[standard]
sqlalchemy
pydantic-settings
loguru
```

#### Environment Variables

The project uses environment variables for configuration. An example configuration is provided in the `.env.example` file. You can create a `.env` file based on this example.

**Example `.env` File**

```example
APP_ENV=dev
```

#### Running the Application

To run the application locally:

1. **Install Dependencies**: Ensure you have installed all the dependencies listed in the

requirements.txt

file.
`sh
    pip install -r requirements.txt
    `

2. **Run the Application**: Use Uvicorn to serve the FastAPI application.

   ```sh
   uvicorn app.main:app --reload
   ```

3. **Access the Application**: Navigate to `http://localhost:8000` to view the application.

#### Docker Support

The project includes a Dockerfile for containerization. To build and run the Docker image:

1. **Build the Docker Image**:

   ```sh
   docker build -t <image_name> .
   ```

2. **Run the Docker Container**:
   ```sh
   docker run --env-file app/.env -p 8000:8000 <image_name>
   ```

#### Summary

This documentation provides an overview of the project requirements, including software requirements, Python dependencies, environment variables, and instructions for installing dependencies and running the application. For more details, refer to the source code and the README.md file.
