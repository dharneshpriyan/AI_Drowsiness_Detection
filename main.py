import cv2
import numpy as np
import time
import winsound
import sys
import os


# =========================================================
# ---------------- WINDOW SETTINGS ------------------------
# =========================================================

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

width, height = 1280, 720
window_name = "AI Drowsiness Detection"

cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

logo = cv2.imread(resource_path("assets/logo.png"))
if logo is not None:
    logo = cv2.resize(logo, (180, 180))

start_clicked = False
exit_clicked = False
mouse_pos = (0, 0)

# 🔹 Smaller Buttons
start_btn = [width//2 - 90, 560, width//2 + 90, 600]
exit_btn  = [width//2 - 90, 620, width//2 + 90, 660]

# ---------- Rounded Button ----------
def draw_button(img, text, rect, base_color):
    x1, y1, x2, y2 = rect
    radius = 15

    hover = x1 < mouse_pos[0] < x2 and y1 < mouse_pos[1] < y2

    color = base_color
    if hover:
        color = (min(base_color[0]+40,255),
                 min(base_color[1]+40,255),
                 min(base_color[2]+40,255))

    overlay = img.copy()

    cv2.rectangle(overlay, (x1+radius, y1), (x2-radius, y2), color, -1)
    cv2.rectangle(overlay, (x1, y1+radius), (x2, y2-radius), color, -1)

    cv2.circle(overlay, (x1+radius, y1+radius), radius, color, -1)
    cv2.circle(overlay, (x2-radius, y1+radius), radius, color, -1)
    cv2.circle(overlay, (x1+radius, y2-radius), radius, color, -1)
    cv2.circle(overlay, (x2-radius, y2-radius), radius, color, -1)

    img[:] = overlay

    text_size = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 2)[0]
    text_x = x1 + (x2-x1)//2 - text_size[0]//2
    text_y = y1 + (y2-y1)//2 + text_size[1]//2

    cv2.putText(img, text, (text_x, text_y),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6, (255,255,255), 2)

# ---------- Mouse ----------
def mouse_callback(event, x, y, flags, param):
    global start_clicked, exit_clicked, mouse_pos
    mouse_pos = (x, y)

    if event == cv2.EVENT_LBUTTONDOWN:
        if start_btn[0] < x < start_btn[2] and start_btn[1] < y < start_btn[3]:
            start_clicked = True
        if exit_btn[0] < x < exit_btn[2] and exit_btn[1] < y < exit_btn[3]:
            exit_clicked = True

cv2.setMouseCallback(window_name, mouse_callback)

# ================= INTRO LOOP =================
while True:
    frame = np.zeros((height, width, 3), dtype=np.uint8)

    # Logo
    if logo is not None:
        frame[100:280, width//2 - 90:width//2 + 90] = logo

    # Title
    title = "AI BASED DROWSINESS DETECTION"
    text_size = cv2.getTextSize(title, cv2.FONT_HERSHEY_DUPLEX, 1.3, 3)[0]
    text_x = width//2 - text_size[0]//2

    cv2.putText(frame,
                title,
                (text_x, 350),
                cv2.FONT_HERSHEY_DUPLEX,
                1.3, (0,255,255), 3)

    # Team Members
    members = ["BY Team members :                                          ", "Dharnesh Priyan J", "Member 2","Member 3","Member 4"]

    y = 400
    for m in members:
        text_size = cv2.getTextSize(m, cv2.FONT_HERSHEY_SIMPLEX, 0.7, 2)[0]
        text_x = width//2 - text_size[0]//2
        cv2.putText(frame,
                    m,
                    (text_x, y),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7, (255,255,255), 2)
        y += 30

    # Buttons
    draw_button(frame, "START", start_btn, (0, 150, 0))
    draw_button(frame, "EXIT", exit_btn, (0, 0, 150))

    cv2.imshow(window_name, frame)

    if exit_clicked:
        cv2.destroyAllWindows()
        exit()

    if start_clicked:

    # -------- FADE OUT EFFECT --------
        for alpha in np.linspace(1, 0, 50):
            fade_frame = (frame * alpha).astype(np.uint8)
            cv2.imshow(window_name, fade_frame)
            cv2.waitKey(15)

        break

    if cv2.waitKey(30) & 0xFF == 27:
        break

# ================= LOADING SCREEN =================
for i in range(101):
    loading_frame = np.zeros((height, width, 3), dtype=np.uint8)

    text = "Starting AI Drowsiness System..."
    text_size = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 1, 2)[0]
    text_x = width//2 - text_size[0]//2

    cv2.putText(loading_frame,
                text,
                (text_x, 320),
                cv2.FONT_HERSHEY_SIMPLEX,
                1, (255,255,255), 2)

    # Loading Bar Background
    cv2.rectangle(loading_frame,
                  (width//2 - 250, 380),
                  (width//2 + 250, 420),
                  (80,80,80), -1)

    # Progress
    cv2.rectangle(loading_frame,
                  (width//2 - 250, 380),
                  (width//2 - 250 + 5*i, 420),
                  (0,255,0), -1)

    percent = f"{i}%"
    cv2.putText(loading_frame,
                percent,
                (width//2 - 30, 460),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8, (255,255,255), 2)

    cv2.imshow(window_name, loading_frame)
    cv2.waitKey(20)



# =========================================================
# ---------------- CAMERA SECTION -------------------------
# =========================================================

# Load cascades
face_cascade = cv2.CascadeClassifier(resource_path("haarcascade_frontalface_default.xml"))
eye_cascade = cv2.CascadeClassifier(resource_path("haarcascade_eye.xml"))

cap = cv2.VideoCapture(0)

window_name = "AI Drowsiness Detection System"
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

eye_closed_start = None
no_face_start = None

EYE_ALERT_TIME = 1
NO_FACE_ALERT_TIME = 1.4

prev_time = 0

# ---- Blinking variables ----
blink_state = False
blink_timer = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    current_time = time.time()
    fps = 1 / (current_time - prev_time) if prev_time != 0 else 0
    prev_time = current_time

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    h, w = frame.shape[:2]

    alert_active = False

    if len(faces) > 0:
        no_face_start = None

        for (x, y, w1, h1) in faces:

            cv2.rectangle(frame, (x, y), (x+w1, y+h1), (255, 0, 0), 2)

            face_gray = gray[y:y+h1, x:x+w1]
            eyes = eye_cascade.detectMultiScale(face_gray)

            if len(eyes) > 0:
                eye_closed_start = None

                cv2.putText(frame,
                            "Eye Monitoring Active",
                            (30, h-70),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.7, (0, 255, 0), 2)

                for (ex, ey, ew, eh) in eyes:
                    center = (x + ex + ew//2, y + ey + eh//2)
                    radius = int((ew + eh) / 4)
                    cv2.circle(frame, center, radius, (0, 255, 0), 2)

            else:
                if eye_closed_start is None:
                    eye_closed_start = time.time()

                elapsed = time.time() - eye_closed_start

                if elapsed >= EYE_ALERT_TIME:
                    alert_active = True
                    winsound.Beep(1200, 400)

    else:
        if no_face_start is None:
            no_face_start = time.time()

        elapsed = time.time() - no_face_start

        if elapsed >= NO_FACE_ALERT_TIME:
            alert_active = True
            winsound.Beep(1000, 500)

    # ================= PROFESSIONAL UI =================

    # ---- Top Bar ----
    overlay = frame.copy()
    cv2.rectangle(overlay, (0, 0), (w, 60), (15, 15, 15), -1)
    frame = cv2.addWeighted(overlay, 0.55, frame, 0.15, 0)

    # ---- Centered Title (Reduced Size) ----
    title = "AI Drowsiness Monitoring System"
    text_size = cv2.getTextSize(title, cv2.FONT_HERSHEY_DUPLEX, 0.8, 2)[0]
    text_x = w//2 - text_size[0]//2

    cv2.putText(frame,
                title,
                (text_x, 38),
                cv2.FONT_HERSHEY_DUPLEX,
                0.65, (0, 220, 255), 2)

    # ---- LIVE Indicator ----
    cv2.circle(frame, (w - 70, 30), 8, (0, 0, 255), -1)
    cv2.putText(frame,
                "LIVE",
                (w - 50, 35),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.55, (255, 255, 255), 2)

    # ---- FPS ----
    cv2.putText(frame,
                f"FPS: {int(fps)}",
                (w - 80, h - 15),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.45, (0, 255, 0), 2)

    # ---- Bottom Bar ----
    overlay2 = frame.copy()
    cv2.rectangle(overlay2, (0, h-35), (w, h), (15, 15, 15), -1)
    frame = cv2.addWeighted(overlay2, 0.55, frame, 0.15, 0)

    cv2.putText(frame,
                "Press Q to Exit",
                (20, h-15),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.45, (255, 255, 255), 2)

    # ---- Blinking Warning ----
    if alert_active:
        if time.time() - blink_timer > 0.5:
            blink_state = not blink_state
            blink_timer = time.time()

        if blink_state:
            cv2.putText(frame,
                        " !! DROWSINESS ALERT !!",
                        (w//2 - 220, h//2),
                        cv2.FONT_HERSHEY_DUPLEX,
                        1.0, (0, 0, 255), 3)

    # ---- Border Glow ----
    glow_color = (0, 255, 150)
    cv2.rectangle(frame, (0, 0), (w-1, h-1), glow_color, 2)
    for i in range(1, 4):
        cv2.rectangle(frame, (i, i), (w-i-1, h-i-1), glow_color, 1)

    cv2.imshow(window_name, frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()