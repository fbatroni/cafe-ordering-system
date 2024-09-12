# Cafe Ordering System

## Overview

The Cafe Ordering System is a full-stack monorepo designed to manage a cafe’s ordering system. The system includes both a frontend React app and two backend APIs (one written in Python using FastAPI and another in Node.js). This README provides instructions to set up the development environment, run the database setup, and start the applications.

### Monorepo Structure

- **Frontend**: A React-based application located in the `frontend` directory.
- **Python Backend**: A Python FastAPI application located in the `python-backend` directory.
- **Node.js Backend**: A Node.js API located in the `nodejs-backend` directory, provided as a demonstration of an API written in Node.js.
- **Scripts**: Utility scripts to set up the database and run the applications are located in the `scripts` directory.

## Prerequisites

Ensure that you have the following installed on your system before proceeding with the setup:

- [Node.js](https://nodejs.org/) (version 20.17.0 or later)
- [Python](https://www.python.org/downloads/) (version 3.8 or later)
- [PostgreSQL](https://www.postgresql.org/download/) (version 12 or later)
- [Git](https://git-scm.com/)
- [Virtualenv](https://virtualenv.pypa.io/en/stable/)

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/professorbatroni/cafe-ordering-system.git
cd cafe-ordering-system
```

### 2. Set Up the Database
To set up the PostgreSQL database, navigate to the scripts directory and run the setup_database.sh script.

```bash
cd scripts
./setup_database.sh
```

This will create the necessary tables and seed the database with sample data.

### 3. Configure Environment Variables
1.  Before running the backend applications, create a .env file in the python-backend and nodejs-backend directories to store environment variables required by the apps.

Navigate to the python-backend directory:

```bash
cd ../python-backend
```

2. Create a .env file with the following contents:

```bash
DATABASE_URL=postgresql://<username>:<password>@localhost:5432/cafe_ordering_system
SECRET_KEY=2d7e2ccc6520e7b8719b7669850394d618d8dcddd552a117624f002963fce697
```

-   Replace <username> and <password> with your PostgreSQL credentials.
-   You can generate a new secret key using an online tool such as SHA256 Key Generator to create a more secure key.

### 4. Build the Backend Environment
To build and configure the backend environment (both Python and Node.js backends), simply run the build-backend.sh script.

```bash
./scripts/build-backend.sh
```

### 4. Build the Frontend Environment
To build and configure the frontend environment (ReactJS), simply run the build-frontend.sh script.

```bash
./scripts/build-frontend.sh
```

This script will:

- Install the JavaScript dependencies from the package.json file

### 5. Running the Applications
##### Start Backend (FastAPI)
Once the environment is built and configured, you can start the FastAPI backend by running the provided script.

```bash
./scripts/run-backend.sh
```

##### Start Frontend (React)

To start the React frontend, run the run-frontend.sh script.

```bash
./scripts/run-frontend.sh
```

***NOTE***: It is recommended that you open another terminal since the first terminal will be running the backend application. If you close out that terminal, it will close the backend API. So in order to run both frontend and backend simultaneously, the frontend needs to be in another terminal session.

### 6. Testing the Setup

The frontend will be available on http://localhost:3000, the FastAPI backend on http://localhost:8000, and the Node.js backend on http://localhost:5000.

Once both backend APIs and the frontend are running, you can test the functionality by interacting with the cafe ordering system via the frontend. Ensure that the database is properly set up and populated by checking the API responses from both backends.


### Project Summary
#### Frontend (React)
The frontend is built using React.js, providing an intuitive user interface for placing orders, viewing the menu, and managing orders.

##### Key Features:
Interactive ordering system.
Menu listing with categories.
Order tracking for customers and admins.
#### Dependencies:
React 18+
Axios (for API requests)
React Router DOM (for navigation)
#### Backend (FastAPI)
The backend is a Python FastAPI application that handles all the core business logic, such as managing orders, interacting with the database, and authenticating users.

##### Key Features:
Fast and efficient API endpoints.
Role-based access control for orders and order statuses.
Integration with PostgreSQL for storing data.
##### Dependencies:
FastAPI
SQLAlchemy
PostgreSQL
Pydantic
#### Backend (Node.js)
The Node.js backend serves as an alternative API implementation to demonstrate how the same functionalities can be built using Node.js.

##### Key Features:
RESTful API for cafe ordering operations.
Uses Express.js and PostgreSQL for database interactions.
##### Dependencies:
Express.js
PostgreSQL
Sequelize (ORM)

### Additional Notes
If you are using Windows, make sure to use Git Bash or another compatible shell to run the provided scripts.
Ensure that your PostgreSQL service is running before starting the backend.
The frontend and backend applications communicate via HTTP requests, so ensure all are running concurrently.
Troubleshooting
Database connection issues: Ensure the DATABASE_URL in the .env files is properly configured and that PostgreSQL is running.
Missing dependencies: Double-check that all dependencies for both frontend and backend are installed.
Port conflicts: Ensure that ports 3000 (frontend), 8000 (FastAPI backend), and 5000 (Node.js backend) are free before starting the applications.
