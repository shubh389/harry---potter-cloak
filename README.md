# 🎭 Enhanced Invisibility Cloak Project

This project creates a Harry Potter-style invisibility cloak effect using computer vision and OpenCV.

## ✨ New Features in Enhanced Version

- **Multiple Color Options**: Red, Blue, Green, White, and Yellow cloaks
- **Better User Interface**: Colorful prompts and clear instructions
- **Improved Background Capture**: Uses multiple frames for more stable background
- **Enhanced Mask Processing**: Better edge smoothing and noise reduction
- **Real-time Controls**:
  - 'q' or ESC: Exit
  - 'r': Recapture background
  - 's': Save screenshot
- **Error Handling**: Better camera detection and error messages
- **Visual Feedback**: On-screen status display

## 📁 Project Files

- `invisibility_cloak.py` - Enhanced version with all features
- `simple_invisibility_cloak.py` - Simplified version
- `README.md` - This documentation

## 🎯 How it Works

1. **Background Capture**: Captures multiple background frames for stability
2. **Color Detection**: Detects colored cloth using optimized HSV ranges
3. **Advanced Masking**: Uses morphological operations and Gaussian blur
4. **Seamless Replacement**: Replaces cloak area with background

## 📋 Requirements

- Python 3.x
- OpenCV (`opencv-python`)
- NumPy
- A webcam
- A colored cloth/cloak

## 🚀 How to Use

### invisible cloak

```bash
python invisibility_cloak.py
```

## 📖 Step-by-Step Instructions

1. **Run the script** and choose your cloak color (1-5)
2. **Step OUT of camera view** when prompted (very important!)
3. **Wait for background capture** (30 frames for stability)
4. **Put on your colored cloak** and step back into view
5. **Enjoy the magic!** You'll appear invisible where the cloak is
6. **Use controls**:
   - Press 'q' or ESC to exit
   - Press 'r' to recapture background if needed
   - Press 's' to save a screenshot

## 💡 Tips for Best Results

- Use a **solid-colored cloth** that contrasts with surroundings
- Ensure **good, even lighting**
- Keep the **background relatively static**
- The cloth should **completely cover** the area you want invisible
- **Red and blue** tend to work best
- If detection is poor, try **recapturing background** with 'r'

## 🎨 Available Colors

- **🔴 Red**: Best overall performance (dual HSV ranges)
- **🔵 Blue**: Great for blue items and clothing
- **🟢 Green**: Perfect for green screen effects
- **⚪ White**: Good for white/light colored materials
- **🟡 Yellow**: Works well in most lighting conditions

## 🔧 Technical Improvements

- **Median Background**: Uses median of 30 frames instead of single frame
- **Enhanced Morphology**: Multiple operations for cleaner masks
- **Gaussian Blur**: Smoother edge transitions
- **Better Blending**: Improved color mixing at edges
- **Input Validation**: Robust user input handling
- **Camera Settings**: Optimized resolution and FPS

## 🐛 Troubleshooting

- **Camera not detected**: Make sure camera is connected and not in use
- **Poor invisibility effect**: Try different lighting or recapture background
- **Color not detected**: Ensure good contrast and try different colors
- **Laggy performance**: Reduce camera resolution or close other applications

## 📸 Screenshots

Screenshots are automatically saved when you press 's' during the session.

---

**Have fun becoming invisible! 🎭✨**
C:/Users/subha/AppData/Local/Programs/Python/Python313/python.exe invisibility_cloak.py
