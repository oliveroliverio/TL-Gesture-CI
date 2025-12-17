# Mediapipe and Dependency Fixes

## Issues Encountered

### 1. Missing Dependencies
The project was missing `pyproject.toml` dependencies required to run `app.py`.
**Error:** `ModuleNotFoundError: No module named 'cv2'` (implied), and later `ModuleNotFoundError: No module named 'tensorflow'`.

### 2. Mediapipe `AttributeError`
When running with the latest `mediapipe` (v0.10.x), the `solutions` API was removed or refactored, causing the app to crash.
**Error:** `AttributeError: module 'mediapipe' has no attribute 'solutions'`

### 3. Python Version Incompatibility
`tensorflow` and older `mediapipe` versions had compatibility issues with the latest Python 3.13, requiring a downgrade to Python 3.11/3.10.

## Resolution Steps

### 1. Initialize Project & Add Basic Dependencies
First, we added the core libraries found in `app.py` imports.

```bash
# Add OpenCV, Numpy, and Mediapipe
uv add opencv-python numpy mediapipe
```

### 2. Fix Missing TensorFlow
The application uses TensorFlow Lite but imports `tensorflow` directly in the model classifiers.

```bash
# Add TensorFlow
uv add tensorflow
```

### 3. Fix Mediapipe Version Conflict
The latest `mediapipe` dropped support for the `mp.solutions` API used in this project. We successfully restored it by pinning `mediapipe` to version `0.10.9`.

We also had to pin `protobuf` to `<5` to ensure compatibility with TensorFlow and Mediapipe.

**Final `pyproject.toml` configuration:**
```toml
[project]
requires-python = ">=3.10, <3.13"
dependencies = [
    "opencv-python",
    "numpy",
    "mediapipe==0.10.9",
    "tensorflow",
    "protobuf<5",
]
```

### 4. Apply Changes
We successfully synced the environment with the correct versions.

```bash
# Sync dependencies and pin python version if needed (auto-handled by uv with requires-python)
uv sync
```

### 5. Run Application
The application now runs successfully.

```bash
uv run app.py
```
