# pulication-search
Yale BIDS Technical Assessment

Author: Vincent Jim Zhang

Contact: zhang.vi@northeastern.edu
# Description:
This project is a web application helps people find medical publication from the National Library of Medicine database. The backend part is made with Python and Flask, which handle the server tasks. The frontend part is made with Vue.js and is made to well design with Ant Design.

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

# Environment Requirements
- Python 3.8 or above
- Node.js 14 or above
# Dependencies:
Python:

`flask`, `flask-cors`

Vue:

`vue`, `vite`, `axios`, `ant-design-vue`

## Install:
python:

Open terminal, insert command: `pip install flask flask-cors` and execute it

vue:

In `Frontend` directory, open terminal, insert command: `npm install` and execute it.

This will install all required dependecies.

# How to use:
1. Prepare server end, open terminal at `Backend` directory, execute `python3 app.py`, do not close the terminal, let server run.
2. Open frontend applcation, open another terminal at `Frontend` directory, execute `npm run dev`.
3. An URL will display on frontend terminal, follow by `Local:` copy it.
4. Open a browser, paste the URL, then it will shows the web page.
5. To terminate program, at frontend terminal insert `q` and execute it, then at backend terminal click `ctrl` + `c` to terminate program.

Caution: Make sure your `localhost:5000` port is avaliable.

# Test:
The program has been thoroughly tested.

