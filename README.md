# RaspberryPi-Temperature-Monitor

A simple Flask web server hosted on a RaspberryPi which shows temperature and humidity readings from a `DHT11` sensor.

# How do we read the DHT11 sensor?

The `DHT11` sensor's readings can be obtained with the use of the
`Adafruit_DHT` package. This package can be installed using the following command:

```
sudo pip3 install Adafruit_DHT
```

Please note that the use of `sudo` with `pip3 install` can lead to broken permissions and it's better to use virtual environments.

# How is the sensor data visualized?

The server contains two routes.

1.  <br>`/dht11/readings`<br>
    This route displays the data inside an HTML template file which is located in `templates/DHT11_Readings.html`.

2.  <br>`/dht11/readings/json`<br>
    This route displays the data as JSON. The response will look something like this:
    ```
    {
        "temperature": "xxx",
        "humidity": "xxx"
    }
    ```
