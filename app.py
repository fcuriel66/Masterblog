from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

def fetch_post_by_id(post_id):
    """ The function fetches a post by its id (after checking
        if blog with files exists)"""
    if os.path.exists("blogs.json"):
        with open("blogs.json", "r") as f:
            blog_posts = json.load(f)
    else:
        blog_posts = []

    for post in blog_posts:
        if post["id"] == post_id:
            return post
    return None


@app.route('/')
def index():
    """ Opens and loads the blogs.json file. Then
     passes blog_posts into the template as 'posts'
     using the render_template function. os.path.exists was
     used to prevent crashing if json file does not exist
     in default path; in that case an empty list is created.
     the function returns the render of homepage index.html"""

    if os.path.exists("blogs.json"):
        with open("blogs.json", "r") as f:
            blog_posts = json.load(f)
    else:
        blog_posts = []

    return render_template("index.html", posts=blog_posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    """ If request-method is 'POST', gets data from form,
      loads the existing posts, assigns a unique new id for the post
       and then creates the new_post. Finally, the new_post is
       dumped into the json file. The function return is the
       redirect to the homepage (/) unless the method is GET, in
       which case the redirect is to the add (/add) page"""

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


@app.route('/delete/<int:post_id>', methods=['POST','GET'])
def delete(post_id):
    """Deletes the blog post with the given post_id."""
    if os.path.exists("blogs.json"):
        with open("blogs.json", "r") as f:
            blog_posts = json.load(f)
    else:
        blog_posts = []

    # Filter out the post to delete
    blog_posts = [post for post in blog_posts if post["id"] != post_id]

    # Save updated list back to file
    with open("blogs.json", "w") as f:
        json.dump(blog_posts, f, indent=4)

    return redirect(url_for("index"))


@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    """ Update route to display the update form"""
    # Load all posts
    with open("blogs.json", "r") as f:
        blog_posts = json.load(f)

    # Uses the fetch_post_by_id function above
    post = fetch_post_by_id(post_id)
    if post is None:
        return "Post not found", 404

    if request.method == 'POST':
        # Updates post with new values
        for bpost in blog_posts:
            if bpost["id"] == post_id:
                bpost["title"] = request.form.get("title")
                bpost["author"] = request.form.get("author")
                bpost["content"] = request.form.get("content")

        # Saves updated blog to file
        with open("blogs.json", "w") as f:
            json.dump(blog_posts, f, indent=4)

        return redirect(url_for("index"))

    # If it is a GET request -> render form update.html
    return render_template("update.html", post=post)


@app.route('/like/<int:post_id>', methods=['POST'])
def like(post_id):
    with open("blogs.json", "r") as f:
        blog_posts = json.load(f)

    # find the post
    for post in blog_posts:
        if post["id"] == post_id:
            # ensure likes field
            if "likes" not in post:
                post["likes"] = 0
            post["likes"] += 1
            break
    else:
        # post not found
        return "Post not found", 404

    #save_posts(posts)
    with open("blogs.json", "w") as f:
        json.dump(blog_posts, f, indent=4)
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)

