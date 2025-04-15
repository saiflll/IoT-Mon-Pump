from flask import Flask, request, render_template

app = Flask(__name__)
sensor_data = {
    "water_level": 0,
    "moisture": 0,
    "ph": 0,
    "temperature": 0,
    "ammonia": 0
}

@app.route("/")
def index():
    return render_template("dashboard.html", data=sensor_data)
#endpoin recive
@app.route("/update", methods=["POST"])
def update():
    global sensor_data
    sensor_data.update(request.get_json())
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)