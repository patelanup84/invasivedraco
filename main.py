from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/category/<string:category_name>')
def category(category_name):
    # Replace this with actual data fetching and pass to the template
    return render_template('category.html', category_name=category_name)

@app.route('/post/<string:post_type>/<int:post_id>')
def post(post_type, post_id):
    # Replace this with actual data fetching based on post_type and post_id
    return render_template('post.html', post_type=post_type, post_id=post_id)

if __name__ == '__main__':
    app.run(debug=True)