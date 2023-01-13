
from flask import Flask, jsonify, render_template
from dht11 import DHT11

dht11 = DHT11(
    pin=23,
)

app = Flask(
    __name__,
)


@app.route(
    "/dht11/readings",
)
def DHT11_readings():
    data = {
        "humidity": dht11.humidity,
        "temperature": dht11.temperature,
    }

    return render_template(
        "DHT11_Readings.html",
        data=data,
    )


@app.route(
    "/dht11/readings/json",
)
def DHT11_readings_JSON():
    return jsonify(
        {
            "temperature": dht11.temperature,
            "humidity": dht11.humidity,
        }
    )


HOST = "0.0.0.0"

if __name__ == "__main__":
    try:
        dht11.start_thread()

        app.run(
            host=HOST,
        )
    finally:
        dht11.kill_thread()
