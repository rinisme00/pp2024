import threading
import gzip
import pickle
import time


class PersistenceThread(threading.Thread):
    def __init__(self, file_name, data_callback, interval=5):
        super().__init__()
        self.file_name = file_name
        self.data_callback = data_callback
        self.interval = interval
        self.stop_event = threading.Event()

    def run(self):
        while not self.stop_event.is_set():
            try:
                data = self.data_callback()
                with gzip.open(self.file_name, 'wb') as f:
                    pickle.dump(data, f)
                print(f"Data saved to {self.file_name} in background.")
            except Exception as e:
                print(f"Error in background persistence: {e}")
            self.stop_event.wait(self.interval)

    def stop(self):
        self.stop_event.set()
