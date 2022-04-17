from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)
print(__name__)


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/<string:page_name>")
def pages(page_name):
    return render_template(page_name)

def write_to_csv(data):
    with open('database.csv',mode="a",newline="") as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database, delimiter=",", quotechar="'", quoting=csv.QUOTE_MINIMAL)

        csv_writer.writerow([email,subject,message])

def thanks():
    return redirect("/thankyou.html")






# @app.route("/submit_form", methods=["POST", "GET"])
# def submit_form():
#     if request.method == 'POST':
#         try:
#             data = request.form.to_dict()
#             write_to_csv(data)
#             return redirect("/thankyou.html")
#         except:
#             return 'Did not save to Database'
#     else:
#         return "ERROR"




# @app.route("/about")
# def about():
#     return render_template('about.html')

# @app.route("/contact")
# def contact():
#     return render_template('contact.html')

# @app.route("/components")
# def components():
#     return render_template('components.html')

# @app.route("/works")
# def works():
#     return render_template('works.html')



# # username route
# @app.route("/<username>")
# def indexuser(username=None):
#     return render_template('index.html', username=username)

# username route
# @app.route("/index")
# def index(username=None):
#     return render_template('index.html')
    

# username + post_number route
# @app.route("/<username>/<int:post_id>")
# def indexUserPost(username=None, post_id=None):
#     return render_template('index.html', username=username, post_id=post_id)

# about route
# @app.route("/about")
# def about():
#     return render_template('about.html')

@app.route("/favicon.ico")
def favicon():
    return render_template('home.html')


