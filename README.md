# Coffee Dashboard

A web application for tracking and analyzing coffee consumption patterns. Built with Flask, MongoDB, and Chart.js.

## Features

- User authentication (register/login)
- Track coffee consumption with details (type, size, notes)
- Visual analytics with interactive charts
- Daily consumption tracking
- Coffee type distribution analysis

## Prerequisites

- Python 3.7+
- MongoDB
- pip (Python package manager)

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root with the following content:
   ```
   MONGODB_URI=mongodb://localhost:27017/
   SECRET_KEY=your-secret-key-here
   ```

4. Start the application:
   ```bash
   python app.py
   ```

5. Open your browser and navigate to `http://localhost:5000`

## Usage

1. Register a new account or login with existing credentials
2. Navigate to the dashboard
3. Add new coffee entries using the "Add Coffee Entry" button
4. View your coffee consumption statistics and trends

## Project Structure

- `app.py`: Main application file
- `auth.py`: Authentication routes and logic
- `coffee.py`: Coffee tracking functionality
- `templates/`: HTML templates
  - `index.html`: Landing page
  - `dashboard.html`: Main dashboard
  - `auth.html`: Login/Register pages

## Technologies Used

- Backend: Flask, PyMongo
- Frontend: Bootstrap 5, Chart.js
- Database: MongoDB
- Authentication: Flask-Login