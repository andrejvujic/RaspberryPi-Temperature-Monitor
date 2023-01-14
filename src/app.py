from datetime import datetime
from flask import Flask, request, jsonify, render_template, redirect
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
    args = request.args

    locale = args.get(
        "l",
    )

    if isinstance(
        locale,
        str,
    ):
        locale = locale.upper()

    if not locale or locale not in ["SR", "EN"]:
        locale = "SR"

    if not dht11.humidity or not dht11.temperature:
        return "Couldn't read DHT11 sensor's values."

    def _formatted_date(date: datetime) -> str:
        _ = "u" if locale == "SR" else "at"

        return f"{date.day}-{date.month}-{date.year} {_} {date.hour}:{date.minute}:{date.second}"

    data = {
        "humidity": int(
            dht11.humidity,
        ),
        "temperature": int(
            dht11.temperature,
        ),
        "last-updated-on": _formatted_date(
            dht11.last_updated_on,
        ),
    }

    return render_template(
        f"DHT11_Readings_{locale}.html",
        data=data,
    )


@app.route(
    "/dht11/readings/en",
)
def DHT11_readings_EN():
    return redirect(
        "/dht11/readings?l=EN"
    )


@app.route(
    "/dht11/readings/sr",
)
def DHT11_readings_SR():
    return redirect(
        "/dht11/readings?l=SR"
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
