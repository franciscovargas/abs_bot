from flask import Flask, jsonify, render_template, request
import json

app = Flask(__name__)

@app.route('/graph_data')
def get_json():
    d = json.loads(open("test.json").read())
    return jsonify(d)

@app.route('/main', methods=['GET', 'POST'])
def render_graph():
    if request.method == 'POST':
        print "POST"
        data = request.form["data"]
        print data, "DATA"

    else:
        pass
    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)