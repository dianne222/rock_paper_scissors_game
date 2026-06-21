import cv2
import cvzone
import time

from cvzone.HandTrackingModule import HandDetector

from players.ai_player import AIPlayer
from players.human_player import HumanPlayer
from scoreboard import ScoreBoard

class RockPaperScissorsGame:

    def __init__(self):

        self._camera = cv2.VideoCapture(0)
        self._camera.set(3, 640)
        self._camera.set(4, 480)

        self._detector = HandDetector(maxHands=1)

        self._human = HumanPlayer(self._detector)
        self._ai = AIPlayer()

        self._scoreboard = ScoreBoard()

        self._start_game = False
        self._state_result = False

        self._timer = 0
        self._image_ai = None

    def _load_ai_image(self, move):

        return cv2.imread(
            f"images/{move}_image.png",
            cv2.IMREAD_UNCHANGED
        )

    def run(self):

        while True:

            background = cv2.imread(
                "images/background_image.png"
            )

            success, frame = self._camera.read()

            if not success:
                break

            frame_scaled = cv2.resize(
                frame,
                (0, 0),
                None,
                0.875,
                0.875
            )

            frame_scaled = frame_scaled[:, 80:480]

            hands, frame_scaled = self._detector.findHands(
                frame_scaled,
                draw=True,
                flipType=True
            )

            if self._start_game:

                if not self._state_result:

                    self._timer = (
                        time.time() - self._initial_time
                    )

                    cv2.putText(
                        background,
                        str(int(self._timer)),
                        (605, 435),
                        cv2.FONT_HERSHEY_PLAIN,
                        6,
                        (255, 0, 255),
                        4
                    )

                    if self._timer > 3:

                        self._state_result = True

                        player_move = (
                            self._human.get_move(hands)
                        )

                        ai_move = (
                            self._ai.get_move()
                        )

                        if player_move:

                            self._image_ai = (
                                self._load_ai_image(ai_move)
                            )

                            self._scoreboard.update(
                                ai_move,
                                player_move
                            )

            background[233:653, 795:1195] = frame_scaled

            if self._state_result and self._image_ai is not None and self._image_ai.size > 0:
                background = cvzone.overlayPNG(
                    background,
                    self._image_ai,
                    (149, 310)
                )

            cv2.putText(
                background,
                str(self._scoreboard.ai_score),
                (410, 215),
                cv2.FONT_HERSHEY_PLAIN,
                4,
                (255, 255, 255),
                6
            )

            cv2.putText(
                background,
                str(self._scoreboard.player_score),
                (1112, 215),
                cv2.FONT_HERSHEY_PLAIN,
                4,
                (255, 255, 255),
                6
            )

            cv2.putText(
                background,
                "Press 's' to play",
                (570, 150),
                cv2.FONT_HERSHEY_PLAIN,
                1,
                (0, 0, 0),
                1
            )

            cv2.imshow(
                "Background",
                background
            )

            key = cv2.waitKey(1)

            if key == ord('s'):
                self._start_game = True
                self._state_result = False
                self._initial_time = time.time()

            elif key == ord('q'):
                break

        self._camera.release()
        cv2.destroyAllWindows()