from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    strawberry = int(request.form['strawberry'])
    raspberry = int(request.form['raspberry'])
    apple = int(request.form['apple'])
    firstName = request.form['first_name']
    lastName = request.form['last_name']
    identity = request.form['student_id']
    count = strawberry+raspberry+apple
    print(f"Charging {firstName} for {count}")
    return render_template("checkout.html",strawberry=strawberry, raspberry=raspberry,apple=apple, firstName=firstName, lastName=lastName,identity=identity)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    