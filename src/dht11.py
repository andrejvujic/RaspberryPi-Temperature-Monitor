import Adafruit_DHT
import threading
import time


class DHT11:
    def __init__(
        self,
        pin: int,
    ) -> None:
        self.temperature = None
        self.humidity = None

        self.pin = pin
        self.type = Adafruit_DHT.DHT11

        self.thread = threading.Thread(
            target=self.update,
        )

        self.THREAD_ALIVE = None

    def start_thread(self) -> None:
        self.THREAD_ALIVE = True
        self.thread.start()

    def update(self) -> None:
        while self.THREAD_ALIVE:
            _humidity, _temperature = Adafruit_DHT.read(
                self.type,
                self.pin,
            )

            if not _humidity or not _temperature:
                print(
                    "[DHT11] Couldn't read values.",
                )
            else:
                """
                print(
                    "[DHT11] Humidity",
                    humidity,
                )

                print(
                    "[DHT11] Temperature",
                    temperature,
                )
                """
                self.humidity = _humidity
                self.temperature = _temperature

            time.sleep(
                3.0,
            )

        print(
            "[DHT11] Killing thread...",
        )

    def kill_thread(self) -> None:
        self.THREAD_ALIVE = False

    def __repr__(self) -> str:
        return f"temperature={self.temperature}\nhumidity={self.humidity}"
