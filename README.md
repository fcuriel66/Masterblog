# Masterblog

A relatively simple blog management web application built with Flask.  
It allows viewing, adding, updating, deleting, and liking blog posts stored in a local JSON file (`blogs.json`).

---

## Features

- View all blog posts
- Add new posts
- Update existing posts
- Delete posts
- Like posts (increment likes count per post)

---

## Project Structure

Masterblog/
├── app.py
├── blogs.json
├── static/
│ └── style.css
└── templates/
├── index.html
├── add.html
└── update.html


- `app.py`: Flask application logic (routes for listing, adding, updating, deleting, liking posts)  
- `blogs.json`: Data storage file for blog posts  
- `static/style.css`: Stylesheet (dark / space theme)  
- `templates/`: HTML templates for views

---

## Setup & Installation

1. **Clone the repository**

   git clone https://github.com/fcuriel66/Masterblog.git
   cd Masterblog

2. **Install dependencies**

pip install -r requirements.txt

## Usage

A. **Start the Flask app**

python app.py

B. **Open in your browser**

Navigate to http://127.0.0.1:8080/ (or http://localhost:8080/), and you’ll see the blog homepage.

## Data format(blogs.json)

Each blog post is stored as an object in a JSON array. Example:

{
  "id": 1,
  "title": "Sample Post Title",
  "author": "Author Name",
  "content": "Some blog content.",
  "likes": 0
}


**Fields**:

id: integer, unique for each post

title: string

author: string

content: string

likes: integer (number of likes), defaults to 0 if not present

**Styling**

The app uses a dark / space theme via static/style.css, with:

Dark backgrounds

Neon/cosmic accent colors

Buttons styled for Add, Delete, Like, Update actions
