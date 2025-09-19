from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

@app.route('/')
def index():
    """Opens and loads the blogs.json file. Then
     passes blog_posts into the template as 'posts'
     using the render_template function."""
    if os.path.exists("blogs.json"):
        with open("blogs.json", "r") as f:
            blog_posts = json.load(f)
    else:
        blog_posts = []

    return render_template("index.html", posts=blog_posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    """If request-method is 'POST', gets data from form,
      loads the existing posts, assigns a unique new id for the post
       and then creates the new_post. Finally the new_post is
       dumped into the json file. The return is the redirect to
       homepage (/index)"""
    if request.method == 'POST':
        title = request.form.get("title")
        author = request.form.get("author")
        content = request.form.get("content")

        # Loads existing posts
        if os.path.exists("blogs.json"):
            with open("blogs.json", "r") as f:
                blog_posts = json.load(f)
        else:
            blog_posts = []

        # New id for post
        new_id = max((post["id"] for post in blog_posts), default=0) + 1

        # Creates the new post
        new_post = {
            "id": new_id,
            "title": title,
            "author": author,
            "content": content
        }

        # Append new post and save back to file
        blog_posts.append(new_post)
        with open("blogs.json", "w") as f:
            json.dump(blog_posts, f, indent=4)

        return redirect(url_for("index"))

    # If method is GET...
    return render_template("add.html")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)



# from flask import Flask, render_template
# import json
#
# app = Flask(__name__)
#
# @app.route('/')
# def index():
#     """Opens and loads the blogs.json file. Then
#     passes blog_posts into the template as 'posts'
#     using the render_template function."""
#     with open("blogs.json", "r") as f:
#         blog_posts = json.load(f)
#
#     return render_template("index.html", posts=blog_posts)
#
#
# from flask import request, render_template
#
# @app.route('/add', methods=['GET', 'POST'])
# def add():
#     if request.method == 'POST':
#         # Fill this
#         pass
#     return render_template('add.html')
#
# if __name__ == '__main__':
#     app.run(host="0.0.0.0", port=8080, debug=True)
