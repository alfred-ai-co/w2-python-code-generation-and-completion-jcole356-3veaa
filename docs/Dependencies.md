### Project Dependencies

This project relies on several key dependencies to function correctly. Below is a list of the main dependencies along with a brief description of each:

#### FastAPI

- **Package**: [`fastapi`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fjoshuacole%2Fprojects%2Fapp_academy%2Fgen_ai%2Fw2-python-code-generation-and-completion-jcole356-3veaa%2Fapp%2Fapi%2Froutes%2Fprojects.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A1%2C%22character%22%3A5%7D%7D%5D%2C%22811c2635-dd41-4df6-a0d9-015a158f7da3%22%5D "Go to definition")
- **Description**: FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints. It is used to create the API endpoints and handle HTTP requests.
- **Documentation**: [FastAPI Documentation](https://fastapi.tiangolo.com/)

#### Uvicorn

- **Package**: [`uvicorn[standard]`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fjoshuacole%2Fprojects%2Fapp_academy%2Fgen_ai%2Fw2-python-code-generation-and-completion-jcole356-3veaa%2Frequirements.txt%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A1%2C%22character%22%3A0%7D%7D%5D%2C%22811c2635-dd41-4df6-a0d9-015a158f7da3%22%5D "Go to definition")
- **Description**: Uvicorn is a lightning-fast ASGI server implementation, using `uvloop` and `httptools`. It is used to serve the FastAPI application.
- **Documentation**: [Uvicorn Documentation](https://www.uvicorn.org/)

#### SQLAlchemy

- **Package**: [`sqlalchemy`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fjoshuacole%2Fprojects%2Fapp_academy%2Fgen_ai%2Fw2-python-code-generation-and-completion-jcole356-3veaa%2Fapp%2Fapi%2Froutes%2Fprojects.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A2%2C%22character%22%3A5%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fjoshuacole%2Fprojects%2Fapp_academy%2Fgen_ai%2Fw2-python-code-generation-and-completion-jcole356-3veaa%2Frequirements.txt%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A2%2C%22character%22%3A0%7D%7D%5D%2C%22811c2635-dd41-4df6-a0d9-015a158f7da3%22%5D "Go to definition")
- **Description**: SQLAlchemy is the Python SQL toolkit and Object-Relational Mapping (ORM) library. It is used for database interactions, including defining models and performing CRUD operations.
- **Documentation**: [SQLAlchemy Documentation](https://www.sqlalchemy.org/)

#### Pydantic Settings

- **Package**: [`pydantic-settings`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fjoshuacole%2Fprojects%2Fapp_academy%2Fgen_ai%2Fw2-python-code-generation-and-completion-jcole356-3veaa%2Frequirements.txt%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A3%2C%22character%22%3A0%7D%7D%5D%2C%22811c2635-dd41-4df6-a0d9-015a158f7da3%22%5D "Go to definition")
- **Description**: Pydantic is a data validation and settings management library using Python type annotations. It is used for configuration management in the project.
- **Documentation**: [Pydantic Documentation](https://pydantic-docs.helpmanual.io/)

#### Loguru

- **Package**: [`loguru`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fjoshuacole%2Fprojects%2Fapp_academy%2Fgen_ai%2Fw2-python-code-generation-and-completion-jcole356-3veaa%2Frequirements.txt%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A4%2C%22character%22%3A0%7D%7D%5D%2C%22811c2635-dd41-4df6-a0d9-015a158f7da3%22%5D "Go to definition")
- **Description**: Loguru is a library that aims to bring enjoyable logging in Python. It is used for logging within the application.
- **Documentation**: [Loguru Documentation](https://loguru.readthedocs.io/)

### Installation

To install the project dependencies, you can use the

requirements.txt

file. Run the following command in your terminal:

```sh
pip install -r requirements.txt
```

### Example

requirements.txt

File

```txt
fastapi
uvicorn[standard]
sqlalchemy
pydantic-settings
loguru
```

### Additional Information

- **Environment Variables**: The project uses environment variables for configuration. An example configuration is provided in the

.env.example

file.

- **Docker Support**: The project includes a Dockerfile for containerization. To build and run the Docker image, follow the instructions in the project documentation.

### Summary

These dependencies are essential for the functionality of the Project Management API. They provide the necessary tools for building, serving, and managing the API, as well as interacting with the database and handling configurations and logging. For more details on each dependency, refer to their respective documentation links provided above.
