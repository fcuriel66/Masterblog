from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    """Opens and loads the blogs.json file. Then
    passes blog_posts into the template as 'posts'
    using the render_template function."""
    with open("blogs.json", "r") as f:
        blog_posts = json.load(f)

    return render_template("index.html", posts=blog_posts)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
