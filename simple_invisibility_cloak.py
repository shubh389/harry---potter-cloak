import cv2
import numpy as np
import time

# Simple version of invisibility cloak
print("🎭 Simple Invisibility Cloak")
print("="*30)

# Start camera
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("❌ Camera not found!")
    exit()

print("📸 Step out of view to capture background...")
time.sleep(3)

# Capture background
print("📸 Capturing background...")
ret, background = cap.read()
background = cv2.flip(background, 1)

# Red cloak detection (simple version)
lower_red1 = np.array([0, 120, 70])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 120, 70])
upper_red2 = np.array([180, 255, 255])

print("🎭 Put on red cloak and enjoy!")
print("Press ESC to exit")

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    frame = cv2.flip(frame, 1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Create red mask
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = mask1 + mask2
    
    # Clean up mask
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3,3), np.uint8))
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, np.ones((3,3), np.uint8))
    
    # Apply invisibility effect
    mask_inv = cv2.bitwise_not(mask)
    res1 = cv2.bitwise_and(background, background, mask=mask)
    res2 = cv2.bitwise_and(frame, frame, mask=mask_inv)
    result = cv2.add(res1, res2)
    
    cv2.imshow("Simple Invisibility Cloak", result)
    
    if cv2.waitKey(1) == 27:  # ESC to exit
        break

cap.release()
cv2.destroyAllWindows()
print("✅ Done!")
