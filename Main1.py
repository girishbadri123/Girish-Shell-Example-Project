import os, random
from locust import HttpUser, task, between

AUDIO_DIR = os.path.join(os.path.dirname(__file__), "C:\Content\SanskritData")

class SpeechLoadTestUser(HttpUser):
    # wait between requests to simulate realistic pacing
    wait_time = between(1, 3)

    @task
    def send_audio(self):
        # pick a random file each time
        fname = random.choice([f for f in os.listdir(AUDIO_DIR) if f.endswith(".wav")])
        path = os.path.join(AUDIO_DIR, fname)
        with open(path, "rb") as wav:
            # adjust URL path if your app expects a different route
            self.client.post("/", files={"file": wav})
