# Search Data, Interest Calculator, and Voice Recorder App

## Introduction

This project is a full-stack web application that includes three main functionalities: searching data from files, calculating simple interest, and recording and managing voice recordings. It consists of both frontend and backend components, providing a seamless user experience.

## Getting Started

### Backend

1. **Install Dependencies**
   - Create a folder for the backend and navigate to it.
   - Install all packages mentioned in the PipFile by running:
     ```
     pipenv install
     ```

2. **Database Setup**
   - Connect to your MSSQL server using the connection string provided in the `config.py` file.
   - Upload all files in the `data` folder to load data into the database.


3. **Deployment**
   - After database setup, create deployment commands to load file data into the database.
      ```
      flask db init
      flask db migrate -m "file data tables"
      flask db upgrade
      ```

4. **Develop Backend Applications**
   - Develop backend applications to perform operations.
   - Handle CORS to allow cross-platform access.

### Frontend

1. **Setup React App**
   - Create a React project using:
     ```
     npx create-react-app search-app
     ```
   - Navigate to the created directory:
     ```
     cd search-app
     ```
   - Download necessary packages like `react-router-dom` and `axios` by running:
     ```
     npm install react-router-dom axios
     ```

2. **Create UI Components**
   - Develop a landing page for easy navigation.
   - Create individual components for each task.

# Tasks

### Task 1: Search Data

1. **Search Input**
   - Allow the user to enter a search element in the input box.
   - User can select a dropdown (name, age, city) for search columns.

2. **Search Results**
   - Display results from three files based on entered input.


### Task 2: Simple Interest Calculator

1. **Input**
   - User can enter principal amount, rate of interest, and tenure.

2. **Calculate Interest**
   - Show calculated simple interest on the right side of the page.
</details>

### Task 3: Voice Recording

1. **Recording**
   - User can start and stop recording their voice.
   - Option to add or start a new recording.

2. **Preview and Save**
   - Preview recorded content.
   - Save recordings to Excel.

## Additional Features

1. **Loader**
   - Implemented loader to show until API response is fetched.

2. **Routing**
   - Implemented routing to handle all tasks in a single screen.

## Installation

1. **Backend**
   - Navigate to the backend folder and run:
     ```
     pipenv install
     ```
   - Create a `.env` file and provide necessary environment variables.
   - Start the Flask server:
     ```
     flask run
     ```

2. **Frontend**
   - Navigate to the frontend folder and run:
     ```
     npm install
     ```
   - Start the React app:
     ```
     npm start
     ```

## Usage

1. Open the web application in your browser.
2. Perform the desired task from the landing page.

## Contributing

Feel free to contribute by reporting bugs, suggesting new features, or submitting pull requests.

#### Thanks to NxtWave & Veera Security Pvt Ltd for this opportunity
