import json
from typing import Any
import os
import cv2
import time
import numpy as np


class VideoCamera:
    def __init__(
        self,
        flip_h: bool = False,
        flip_v: bool = False,
        index: int = -1,
        zoom_factor: float = 1.0,
    ) -> None:
        self.flip_h = flip_h
        self.flip_v = flip_v

        self.index = index
        self.zoom_factor = zoom_factor

        self.cap = cv2.VideoCapture(
            self.index,
        )

        self.previous_frame = None

        time.sleep(2.0)

    def kill(self) -> None:
        self.cap.release()

    def apply_flips(self, frame: Any) -> Any:
        if self.flip_h:
            frame = np.fliplr(frame)

        if self.flip_v:
            frame = np.flip(frame, 0)

        return frame

    def get_frame(self) -> Any:
        _, frame = self.cap.read()
        frame = self.apply_flips(
            frame=frame,
        )
        return frame

        if _:
            frame = self.zoom(frame=frame)

            self.previous_frame = frame
            return frame

        return self.previous_frame

    def get_image_bytes(self) -> Any:
        frame = self.get_frame()
        _, image = cv2.imencode(
            ".jpg",
            frame,
        )
        return image.tobytes()

    def get_image(self) -> Any:
        frame = self.get_frame()
        return frame

        _, image = cv2.imencode(
            ".jpg",
            frame,
        )
        return image

    def save_image(self) -> int:
        image = self.get_image()

        id = int(
            time.time() * 1000,
        )

        cv2.imwrite(
            f"./static/generated/{id}.jpg",
            image,
        )

        return id

    def zoom(self, frame: Any, coord=None) -> Any:
        h, w, _ = [self.zoom_factor * i for i in frame.shape]

        if coord is None:
            cx, cy = w / 2, h / 2
        else:
            cx, cy = [self.zoom_factor * c for c in coord]

        frame = cv2.resize(
            frame,
            (0, 0),
            fx=self.zoom_factor, fy=self.zoom_factor,
        )

        frame = frame[
            int(
                round(
                    cy - h / self.zoom_factor * 0.5,
                ),
            ): int(
                round(
                    cy + h / self.zoom_factor * 0.5,
                ),
            ),
            int(
                round(
                    cx - w / self.zoom_factor * 0.5,
                ),
            ): int(
                round(
                    cx + w / self.zoom_factor * 0.5,
                ),
            ),
            :]

        return frame

    def to_grayscale(self, frame: Any) -> Any:
        return cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    def to_color(self, frame: Any) -> Any:
        return cv2.cvtColor(frame, cv2.COLOR_GRAY2RGB)
