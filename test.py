import time
import threading

def start_timer(duration):
    start_time = time.time()

    def get_time_left():
        elapsed_time = time.time() - start_time
        time_left = max(0, duration - elapsed_time)
        minutes, seconds = divmod(int(time_left), 60)
        return f"{minutes}분 {seconds}초"

    def countdown():
        while time.time() - start_time < duration:
            time.sleep(1)

    threading.Thread(target=countdown).start()
    return get_time_left


def timer():
    get_time_left = start_timer(600)
    return get_time_left()

