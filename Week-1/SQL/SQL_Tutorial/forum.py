import datetime
import collections
from flask import Flask, request, redirect, url_for
from flask import Flask, render_template, url_for, flash,redirect
from dbConection import get_posts, add_post

app = Flask(__name__)

HTML_WRAP = '''
<!DOCTYPE html>
<html>

<head>
    <title>DB Forum</title>
    <style>
        .post{{
            margin-top: 4px;
            border: black 1px solid;
        }}
    </style>
</head>

<body>
    <h1> BD Forum </h1>
    <form method="POST" action="">
        <div>
            <textarea name="content" id="content" cols="30" rows="10" style="width: 100%;"></textarea>
        </div>
        <div>
            <button id="go" type="submit">Post message</button>
        </div>
    </form>
    {}
</body>

</html>
'''

POST = '''
    <div class="post">
        <em class="date">{}</em><br/>{}
    </div>
'''

@app.route('/', methods=['GET'])
def main():
    posts = "".join(POST.format(date, text) for text, date in get_posts())
    html = HTML_WRAP.format(posts)
    return html

@app.route('/', methods=['POST'])
def post():
    content = request.form['content']
    add_post(content)
    return redirect(url_for('main'))


if( __name__ == "__main__"): # to execute the web server
    app.run(debug=True)