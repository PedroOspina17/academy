import datetime
import collections
# from flask import Flask, request, redirect, url_for
from flask import Flask, render_template, url_for, flash,redirect
# from forumdb import get_posts, add_post

# app = Flask(__name__)

# HTML template for the forum page

HTML_WRAP = '''
<!DOCTYPE html>
<html>

<head>
    <title>DB Forum</title>
    <style>

    </style>
</head>

<body>
    <h1> BD Forum </h1>
    <form method="POST" action="">
        <div>
            <textarea name="content" id="content" cols="30" rows="10"></textarea>
        </div>
        <div>
            <button id="go" type="submit">Post message</button>
        </div>
    </form>
    %s
</body>

</html>
'''

POST = '''
    <div class="post">
        <em class="date">{}</em><br/>{}
    </div>
'''

# @app.route('/', methods=['GET'])
def main():
    # posts = "".join(POST.format(date, text) for text, date in get_posts())
    # html = HTML_WRAP % posts
    # return html
    return "TESTING..."

# @app.route('/', methods=['POST'])
def post():
    # content = request.form['content']
    # add_post(content)
    # return redirect(url_for('main'))
    return "TESTING..."


# if( __name__ == "__main__"): # to execute the web server
    # app.run(debug=True)