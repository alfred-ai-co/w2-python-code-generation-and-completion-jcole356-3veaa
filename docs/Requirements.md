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

   - **Package**: [`fastapi`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fjoshuacole%2Fprojects%2Fapp_academy%2Fgen_ai%2Fw2-python-code-generation-and-completion-jcole356-3veaa%2Fapp%2Fapi%2Froutes%2Fprojects.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A1%2C%22character%22%3A5%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fjoshuacole%2Fprojects%2Fapp_academy%2Fgen_ai%2Fw2-python-code-generation-and-completion-jcole356-3veaa%2Fdocs%2FDependencies.md%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A6%2C%22character%22%3A17%7D%7D%5D%2C%22708977cf-67c2-4dc1-8855-a81bd3474297%22%5D "Go to definition")
   - **Description**: FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints. It is used to create the API endpoints and handle HTTP requests.
   - **Documentation**: [FastAPI Documentation](https://fastapi.tiangolo.com/)

2. **Uvicorn**

   - **Package**: [`uvicorn[standard]`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fjoshuacole%2Fprojects%2Fapp_academy%2Fgen_ai%2Fw2-python-code-generation-and-completion-jcole356-3veaa%2Frequirements.txt%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A1%2C%22character%22%3A0%7D%7D%5D%2C%22708977cf-67c2-4dc1-8855-a81bd3474297%22%5D "Go to definition")
   - **Description**: Uvicorn is a lightning-fast ASGI server implementation, using [`uvloop`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fjoshuacole%2Fprojects%2Fapp_academy%2Fgen_ai%2Fw2-python-code-generation-and-completion-jcole356-3veaa%2Fdocs%2FDependencies.md%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A13%2C%22character%22%3A82%7D%7D%5D%2C%22708977cf-67c2-4dc1-8855-a81bd3474297%22%5D "Go to definition") and [`httptools`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fjoshuacole%2Fprojects%2Fapp_academy%2Fgen_ai%2Fw2-python-code-generation-and-completion-jcole356-3veaa%2Fdocs%2FDependencies.md%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A13%2C%22character%22%3A95%7D%7D%5D%2C%22708977cf-67c2-4dc1-8855-a81bd3474297%22%5D "Go to definition"). It is used to serve the FastAPI application.
   - **Documentation**: [Uvicorn Documentation](https://www.uvicorn.org/)

3. **SQLAlchemy**

   - **Package**: [`sqlalchemy`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fjoshuacole%2Fprojects%2Fapp_academy%2Fgen_ai%2Fw2-python-code-generation-and-completion-jcole356-3veaa%2Fapp%2Fapi%2Froutes%2Fprojects.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A2%2C%22character%22%3A5%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fjoshuacole%2Fprojects%2Fapp_academy%2Fgen_ai%2Fw2-python-code-generation-and-completion-jcole356-3veaa%2Fdocs%2FDependencies.md%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A18%2C%22character%22%3A17%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fjoshuacole%2Fprojects%2Fapp_academy%2Fgen_ai%2Fw2-python-code-generation-and-completion-jcole356-3veaa%2Frequirements.txt%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A2%2C%22character%22%3A0%7D%7D%5D%2C%22708977cf-67c2-4dc1-8855-a81bd3474297%22%5D "Go to definition")
   - **Description**: SQLAlchemy is the Python SQL toolkit and Object-Relational Mapping (ORM) library. It is used for database interactions, including defining models and performing CRUD operations.
   - **Documentation**: [SQLAlchemy Documentation](https://www.sqlalchemy.org/)

4. **Pydantic Settings**

   - **Package**: [`pydantic-settings`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fjoshuacole%2Fprojects%2Fapp_academy%2Fgen_ai%2Fw2-python-code-generation-and-completion-jcole356-3veaa%2Frequirements.txt%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A3%2C%22character%22%3A0%7D%7D%5D%2C%22708977cf-67c2-4dc1-8855-a81bd3474297%22%5D "Go to definition")
   - **Description**: Pydantic is a data validation and settings management library using Python type annotations. It is used for configuration management in the project.
   - **Documentation**: [Pydantic Documentation](https://pydantic-docs.helpmanual.io/)

5. **Loguru**
   - **Package**: [`loguru`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fjoshuacole%2Fprojects%2Fapp_academy%2Fgen_ai%2Fw2-python-code-generation-and-completion-jcole356-3veaa%2Frequirements.txt%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A4%2C%22character%22%3A0%7D%7D%5D%2C%22708977cf-67c2-4dc1-8855-a81bd3474297%22%5D "Go to definition")
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
