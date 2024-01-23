from flask import Flask

app=Flask(__name__) # CREATING THE APP INSTANCE

@app.route("/")

def home():
    return "<h1>welcome to Flask by Namayanja Ritah </h1>"\
        '<p>My first project</p>'


@app.route("/about")
def about():
    return "<h2>flask basics</h2>"

#tturning on the debug mode
if __name__=="_main_":
    app.run(debug=True)