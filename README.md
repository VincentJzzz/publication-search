# pulication-search
Yale BIDS Technical Assessment

Author: Vincent Jim Zhang

Contact: zhang.vi@northeastern.edu
# Description:
This project is a web application that helps users find medical publications from the National Library of Medicine database. The backend is developed using Python and Flask, which handle the server tasks. The frontend is implemented with Vue.js and uses Ant Design to optimize the user interface for a better user experience.

# Project Structure
- `/Backend`: Contains all the backend code, including the Flask application.
  - `app.py`: The main Flask application file.
  - `method.py`: Includes functions for fetching data.

- `/Frontend`: Contains all the frontend Vue.js code.
  - `/src`: Source files for the Vue application.
    - `App.vue`: Main application file, generates the main page.
    - `/api`: Contains TypeScript scripts that process the backend API.
    - `/components`: Contains all the Vue components used in the application.
    - `/types` Contains file define the data type.

# Environment Requirements and dependencies:
- Python 3.8 or above
- Node.js 14 or above
## Packege use:
  - Python:
  
    `flask`, `flask-cors`
  
  - Vue:
  
    `vue`, `vite`, `axios`, `ant-design-vue`

## Install:
- python:

  Open terminal, insert command: `pip install flask flask-cors` and execute it

- vue:

  In `Frontend` directory, open terminal, insert command: `npm install` and execute it.

  This will install all required dependecies.

# How to Use:
1. Prepare the server side: Open a terminal in the `Backend` directory and execute `python3 app.py`. Keep the terminal open.
2. Open the frontend application: Open another terminal in the `Frontend` directory and execute `npm run dev`.
3. A URL will be displayed in the frontend terminal, prefixed by `Local:`. Copy this URL.
4. Open a browser and paste the URL to view the web page.
5. To terminate the program, type `q` in the frontend terminal and execute it, then press `Ctrl` + `C` in the backend terminal to stop the server.

## Caution:
Ensure that your `localhost:5000` port is available.

## Test:
The program has been thoroughly tested.
