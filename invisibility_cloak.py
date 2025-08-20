import cv2
import numpy as np
import time
import sys

def get_color_choice():
    """Get user's color choice with input validation"""
    while True:
        print("\n" + "="*40)
        print("🎭 INVISIBILITY CLOAK SETUP")
        print("="*40)
        print("Choose cloak color: ")
        print("1. 🔴 Red")
        print("2. 🔵 Blue") 
        print("3. 🟢 Green")
        print("4. ⚪ White")
        print("5. 🟡 Yellow")
        print("="*40)
        
        try:
            choice = int(input("Enter your choice (1-5): "))
            if 1 <= choice <= 5:
                return choice
            else:
                print("❌ Invalid choice! Please enter a number between 1-5.")
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")

def get_color_ranges(choice):
    """Get HSV color ranges based on user choice"""
    color_ranges = {
        1: {  # Red
            'name': 'Red',
            'lower1': np.array([0, 120, 70]),
            'upper1': np.array([10, 255, 255]),
            'lower2': np.array([170, 120, 70]),
            'upper2': np.array([180, 255, 255]),
            'dual_range': True
        },
        2: {  # Blue
            'name': 'Blue',
            'lower1': np.array([94, 80, 2]),
            'upper1': np.array([126, 255, 255]),
            'dual_range': False
        },
        3: {  # Green
            'name': 'Green',
            'lower1': np.array([40, 40, 40]),
            'upper1': np.array([70, 255, 255]),
            'dual_range': False
        },
        4: {  # White
            'name': 'White',
            'lower1': np.array([0, 0, 200]),
            'upper1': np.array([180, 25, 255]),
            'dual_range': False
        },
        5: {  # Yellow
            'name': 'Yellow',
            'lower1': np.array([20, 100, 100]),
            'upper1': np.array([30, 255, 255]),
            'dual_range': False
        }
    }
    return color_ranges[choice]

# Get user choice
choice = get_color_choice()
color_config = get_color_ranges(choice)

print(f"\n✅ {color_config['name']} cloak selected!")
print("\n📷 Initializing camera...")

# Start webcam with error handling
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("❌ Error: Could not open camera!")
    print("Make sure your camera is connected and not being used by another application.")
    sys.exit(1)

# Set camera properties for better performance
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 30)

print("⏳ Camera warming up...")
time.sleep(2)  # Give camera time to adjust

print("\n🎬 IMPORTANT: Step OUT of camera view NOW!")
print("📸 Capturing background in...")
for i in range(5, 0, -1):
    print(f"   {i}...")
    time.sleep(1)

print("📸 Capturing background frames...")

# Capture multiple background frames for better stability
backgrounds = []
for i in range(30):
    ret, frame = cap.read()
    if ret:
        backgrounds.append(cv2.flip(frame, 1))
    print(f"\rProgress: {i+1}/30", end="", flush=True)

if not backgrounds:
    print("\n❌ Error: Could not capture background!")
    cap.release()
    sys.exit(1)

# Use median of backgrounds for more stable background
background = np.median(backgrounds, axis=0).astype(np.uint8)
print(f"\n✅ Background captured successfully!")

print("\n🎭 Put on your cloak and step back into view!")
print("💡 Tips:")
print("   • Use a solid-colored cloth")
print("   • Ensure good lighting")
print("   • Press 'q' or ESC to exit")
print("   • Press 'r' to recapture background")
print("   • Press 's' to save a screenshot")

frame_count = 0

# Main loop
while cap.isOpened():
    ret, img = cap.read()
    if not ret:
        print("❌ Error: Could not read frame from camera!")
        break

    img = cv2.flip(img, 1)  # Mirror the image
    frame_count += 1

    # Convert frame to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Create mask depending on color choice
    if color_config['dual_range']:  # for red cloak
        mask1 = cv2.inRange(hsv, color_config['lower1'], color_config['upper1'])
        mask2 = cv2.inRange(hsv, color_config['lower2'], color_config['upper2'])
        mask = mask1 + mask2
    else:
        mask = cv2.inRange(hsv, color_config['lower1'], color_config['upper1'])

    # Enhanced mask refinement
    # Remove small noise
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3,3), np.uint8), iterations=2)
    # Fill holes and smooth edges
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, np.ones((5,5), np.uint8), iterations=1)
    # Dilate to ensure complete coverage
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, np.ones((3,3), np.uint8), iterations=1)
    
    # Apply Gaussian blur for smoother edges
    mask = cv2.GaussianBlur(mask, (5, 5), 0)

    # Segment out cloak area
    res1 = cv2.bitwise_and(background, background, mask=mask)

    # Remove cloak area from current frame
    mask_inv = cv2.bitwise_not(mask)
    res2 = cv2.bitwise_and(img, img, mask=mask_inv)

    # Combine the results with improved blending
    final_output = cv2.add(res1, res2)
    
    # Add status information on screen
    cv2.putText(final_output, f"Cloak: {color_config['name']}", (10, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    cv2.putText(final_output, "Press 'q'/ESC: Exit | 'r': Recapture | 's': Screenshot", 
                (10, img.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    # Display the result
    cv2.imshow("🎭 Invisibility Cloak", final_output)
    
    # Optional: Show mask for debugging (uncomment next line)
    # cv2.imshow("Mask", mask)

    # Handle key presses
    key = cv2.waitKey(1) & 0xFF
    
    if key == 27 or key == ord('q'):  # ESC or 'q' to exit
        break
    elif key == ord('r'):  # 'r' to recapture background
        print("\n🔄 Recapturing background...")
        print("📸 Step out of view in 3 seconds...")
        for i in range(3, 0, -1):
            print(f"   {i}...")
            time.sleep(1)
        
        backgrounds = []
        for i in range(30):
            ret, frame = cap.read()
            if ret:
                backgrounds.append(cv2.flip(frame, 1))
        
        if backgrounds:
            background = np.median(backgrounds, axis=0).astype(np.uint8)
            print("✅ Background recaptured!")
    
    elif key == ord('s'):  # 's' to save screenshot
        filename = f"invisibility_cloak_screenshot_{int(time.time())}.jpg"
        cv2.imwrite(filename, final_output)
        print(f"📸 Screenshot saved as {filename}")

print("\n👋 Exiting Invisibility Cloak...")
cap.release()
cv2.destroyAllWindows()
print("✅ All done! Thanks for using the Invisibility Cloak!")
