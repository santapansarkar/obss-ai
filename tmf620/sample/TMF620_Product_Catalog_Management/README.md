# TMF620 Product Catalog Management

This project is designed to manage product catalogs efficiently. It provides a set of services that allow users to interact with product data, manage categories, handle subscriptions, and perform various operations related to product management.

## Project Structure

The project is organized into several directories and files, each serving a specific purpose:

- **config.py**: Contains configuration settings for the application, including environment variables and constants.
- **config.json**: A JSON configuration file that stores settings in a structured format.
- **docker-compose.yaml**: Defines services, networks, and volumes for Docker containers, facilitating easy deployment.
- **Dockerfile**: Instructions for building a Docker image for the application.
- **express_server.py**: The main entry point for the application, setting up the server and routing.
- **index.py**: Initializes the application and starts the server.
- **logger.py**: Contains logging functionality to track application events and errors.
- **requirements.txt**: Lists the Python dependencies required for the project.
- **openapi_generator/**: Contains files related to OpenAPI specifications.
- **api/openapi.yaml**: Defines the API structure and endpoints in OpenAPI format.
- **controllers/**: Contains various controllers for handling different aspects of the application, such as categories and events.
- **event_server/**: Related to event handling and processing.
- **file_server/**: Handles file-related operations.
- **job_server/**: Related to job processing and management.
- **plugins/**: Contains plugin files that extend the application's functionality.
- **services/**: Encapsulates business logic.
- **subscription_server/**: Related to subscription management.
- **utils/**: Contains utility functions and helper methods.

## Setup Instructions

1. **Clone the Repository**: Clone this repository to your local machine.
2. **Install Dependencies**: Navigate to the project directory and run:
   ```
   pip install -r requirements.txt
   ```
3. **Run the Application**: Start the application using:
   ```
   python index.py
   ```
4. **Docker Deployment**: To deploy using Docker, run:
   ```
   docker-compose up
   ```

## Usage

After setting up the application, you can access the API endpoints defined in the `api/openapi.yaml` file. The application supports various operations for managing product catalogs, categories, and subscriptions.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.