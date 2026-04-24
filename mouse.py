import cv2
import mediapipe as mp
from pynput.mouse import Button, Controller
import math
import time
import sys

# ---- CONFIGURAZIONE ----

SMOOTHING = 5          
CLICK_THRESHOLD = 0.04 

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

mouse = Controller()

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

if not cap.isOpened():
    print("ERRORE: Impossibile aprire la webcam.")
    sys.exit(1)

first_move = True
prev_x, prev_y = 0, 0
curr_x, curr_y = 0, 0
is_clicked = False

SCREEN_WIDTH = 1920 
SCREEN_HEIGHT = 1080 

def calculate_distance(p1, p2):
    return math.hypot(p2.x - p1.x, p2.y - p1.y)

print("===" * 15)
print("AVVIO AI MOUSE...")
print("ATTENZIONE SU MAC:")
print("Per permettere a questo script di muovere il cursore, devi autorizzare")
print("il tuo Editor / Terminale nelle Impostazioni -> Privacy -> Accessibilità.")
print("=== Premi ESC sulla finestra della webcam per uscire ===")

with mp_hands.Hands(
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7,
    max_num_hands=1) as hands:
    
    while True:
        success, image = cap.read()
        if not success:
            continue

        image = cv2.flip(image, 1)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        results = hands.process(image_rgb)
        
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                
                index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
                
                target_x = index_tip.x * SCREEN_WIDTH
                target_y = index_tip.y * SCREEN_HEIGHT
                
                if first_move:
                    prev_x, prev_y = target_x, target_y
                    first_move = False
                
                curr_x = prev_x + (target_x - prev_x) / SMOOTHING
                curr_y = prev_y + (target_y - prev_y) / SMOOTHING
                
                try:
                    mouse.position = (int(curr_x), int(curr_y))
                except Exception as e:
                    pass
                
                prev_x, prev_y = curr_x, curr_y
                
                # --- CALCOLO CLICK ---
                dist = calculate_distance(index_tip, thumb_tip)
                
                # Se pollice e indice sono molto vicini (pizzico) fa drag/drop click continuo
                if dist < CLICK_THRESHOLD and not is_clicked:
                    is_clicked = True
                    mouse.press(Button.left)
                    print("Mouse Premiuto (Drag Iniziato)")
                        
                # Se si respingono abbastanza lontano, rilascia
                elif dist > CLICK_THRESHOLD + 0.02 and is_clicked:
                    is_clicked = False
                    mouse.release(Button.left)
                    print("Mouse Rilasciato")

                # --- CALCOLO CLICK DESTRO (Alzata di pollice) ---
                # Se la punta del pollice è sensibilmente più "in alto" della sua base Y
                if thumb_tip.y < thumb_mcp.y - 0.05 and not is_right_clicked and not is_clicked:
                    is_right_clicked = True
                    mouse.press(Button.right)
                    mouse.release(Button.right)
                    print("Click Destro Eseguito")
                    
                # Rilascia lo stato destro quando abbassa il pollice
                elif thumb_tip.y >= thumb_mcp.y - 0.03 and is_right_clicked:
                    is_right_clicked = False

                # Testo debug visivo sulla finestra della cam
                stato_click = "CLICCATO/DRAG" if is_clicked else "Libero"
                colore = (0, 0, 255) if is_clicked else (0, 255, 0) # Rosso o Verde
                cv2.putText(image, stato_click, (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, colore, 2)
                        
        cv2.imshow('Mouse Tracking AI', image)
        
        if cv2.waitKey(5) & 0xFF == 27:
            break

if is_clicked:
    mouse.release(Button.left)
cap.release()
cv2.destroyAllWindows()

