from typing import Any

import json
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
        print(
            "[RPiCamera] Releasing...",
        )
        self.cap.release()

    def apply_flips(self, frame: Any) -> Any:
        if self.flip_h:
            frame = np.fliplr(frame)

        if self.flip_v:
            frame = np.flip(frame, 0)

        return frame

    def get_frame(self) -> Any:
        _, frame = self.cap.read()

        if _:
            frame = self.apply_flips(
                frame=frame,
            )

            return frame

        return self.previous_frame

    def get_image(self) -> Any:
        return self.get_frame()

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
