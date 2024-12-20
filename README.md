# A-CRUD-app-for-top-10-movies-using-flask

# Top 10 Movies Website

This project is a web application built with Flask that allows users to list and manage their top 10 movies.  Users can add, edit, delete, and rate movies.

## Features

* **List Top 10 Movies:** Displays movies ranked from highest to lowest.
* **Add New Movie:**  A form to add new movie entries with title, year, description, rating, ranking, review, and image URL.
* **Edit Existing Movie:** Modify details of existing movie entries.
* **Delete Movie:** Remove movie entries from the list.
* **Dynamic Ranking:** Movies are displayed ordered by their ranking.
* **Bootstrap Styling:** Uses Flask-Bootstrap for a responsive and visually appealing design.

## Technologies Used

* **Flask:** Python web framework.
* **Flask-SQLAlchemy:**  ORM for database interaction.
* **Flask-WTF:**  WTForms integration for form handling.
* **Flask-Bootstrap:**  Bootstrap integration for styling.
* **SQLite:** Database for storing movie data.
* **HTML, CSS, JavaScript:** Front-end technologies.
* **Jinja2:** Templating engine.

## Installation and Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/movies-on-top.git  # Replace with your repo URL
   ```
2. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   ```
3. **Activate the virtual environment:**
   ```bash
   # On Windows:
   venv\Scripts\activate

   # On macOS/Linux:
   source venv/bin/activate
   ```
4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
5. **Set up the database:**
   ```bash
   flask run  # This will create the movies.db file (or ensure that there isn't any data loss if movies.db file exists and isn't empty)
   ```
6. **Run the app:**
   ```bash
   flask run
   ```


## Usage

1. Access the website through your browser (the URL will be displayed in the terminal when you run `flask run`).
2. Use the "Add Movie" button to add new entries.
3. Click "Update" on a movie card to edit its details.
4. Click "Delete" to remove a movie.

## Project Structure

* `main.py`:  Flask application logic.
* `templates/`: Contains HTML templates.
    * `index.html`: Home page displaying the movie list.
    * `add.html`:  Form for adding new movies.
    * `edit.html`: Form for editing movies.
    * `base.html`: Base template for inheritance.
* `static/`: Contains static files (CSS, JS).
* `.env`: Stores environment variables.
* `requirements.txt`: List of project dependencies.


## Contributing

Contributions are welcome! 

## License

This project is licensed under the MIT License.
