import cv2
import numpy as np
from datetime import datetime, timedelta


def get_black_background():
    return np.zeros((500, 500))

start_time = datetime.strptime("2019-01-01", "%Y-%m-%d")
end_time = start_time + timedelta(days=1)

def generate_image_with_text(text):
    image = get_black_background()
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(image, text, (int(image.shape[0]*0.23), int(image.shape[1]*0.55)), font, 3, (255, 255, 255), 2, cv2.LINE_AA)
    return image


while start_time < end_time:
    text = start_time.strftime('%H:%M')
    image = generate_image_with_text(text)
    cv2.imwrite('time_images/{0}.jpg'.format(text), image)
    start_time += timedelta(minutes=1)
