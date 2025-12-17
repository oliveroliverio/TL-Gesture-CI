# Project Brief: ASL Transcription & Segmentation Upgrade

## 1. Overview
The goal of this project is to evolve the current Hand Gesture Recognition application into a full American Sign Language (ASL) transcription system. While the current application utilizes MediaPipe for hand shape detection, ASL requires a holistic understanding of the signer, including facial expressions (non-manual markers) and body posture, to accurately interpret complex gestures and grammar.

## 2. Current State
- **Technology**: MediaPipe Hands (Single/Dual hand tracking).
- **Functionality**:
    - Detects hand landmarks (21 points per hand).
    - Classifies static hand shapes (KeyPointClassifier).
    - Classifies dynamic finger gestures (PointHistoryClassifier).
    - Logs landmark data to CSV.
- **Limitation**: Ignores facial features and body pose, which are critical for ASL intonation, grammar, and distinguishing similar signs.

## 3. Objectives
### 3.1. Holistic "Understanding"
- **Upgrade Detection**: Transition from `MediaPipe Hands` to **`MediaPipe Holistic`**.
- **Scope**: Simultaneous tracking of:
    - **Hands**: Finger shapes and orientation.
    - **Face**: Eyes, eyebrows, nose, mouth, and chin (critical for non-manual signals like questions or negation).
    - **Pose**: Arm movements, shoulders, and chest orientation (spatial referencing).

### 3.2. Segmentation Requirements
The system must segment and extract features from specific ROI (Regions of Interest) to feed into the "understanding" model:
- **Head Components**:
    - **Eyes**: Open/closed state, gaze direction (squinting is grammar).
    - **Eyebrows**: Raised vs. furrowed (questions vs. statements).
    - **Mouth/Chin**: Shape and movement (mouthing words or modifiers).
- **Body Components**:
    - **Arms/Chest**: Position relative to the body (e.g., signs produced on the chest vs. neutral space).
    - **Torso Orientation**: Lean forward/back.

### 3.3. Transcription (Shape to Text)
- Develop a logic layer or improved classification model that translates the combination of these "shapes" (Hand + Face + Pose) into written text.
- **Phases**:
    1.  **Static Alphabet/Numbers**: Enhanced precision using body context.
    2.  **Dynamic Words**: Recognizing movements over time (requires temporal sequence modeling).
    3.  **Sentence Structure**: Using facial segmentations to determine punctuation and tone (e.g., Question Mark based on eyebrows).

## 4. Implementation Plan (High Level)

### Phase 1: Integration of MediaPipe Holistic
- Modify `app.py` to initialize `mp.solutions.holistic`.
- Replace current `hands.process()` with `holistic.process()`.
- Update visualization to draw Face Mesh and Pose landmarks alongside Hands.

### Phase 2: Segmentation & Feature Extraction
- Create a `FeatureExtractor` module.
- **Face**: Extract subsets of the 468 face landmarks corresponding to eyes, mouth, and brows.
- **Pose**: Filter for upper body landmarks (shoulders, elbows, wrists) and ignore lower body to reduce noise.
- Normalize these coordinates relative to the user's torso to handle distance variations.

### Phase 3: Data Collection & Model Upgrade
- **Data Logging**: Update `logging_csv` to record Face and Pose vectors in addition to Hand vectors.
- **Model Architecture**:
    - *Current*: Simple Multi-Layer Perceptron (MLP) for static frames.
    - *Target*: Recurrent Neural Network (LSTM/GRU) or Transformer-based model to handle the *temporal* nature of signing (movements like "J" or "Z" or multi-sign sentences).

### Phase 4: Text Transcription Implementation
- Implement a decoding buffer that converts the model's confidence stream into stable text.
- Add "Hold" logic: Only transcribe a character/word if the confidence remains high for $N$ frames.
- Display transcribed text on screen in real-time.

## 5. Success Criteria
- [ ] Application tracks Hands, Face, and Pose simultaneously without significant lag.
- [ ] System accurately distinguishes specific facial markers (e.g., eyebrows up).
- [ ] Validated transcription of basic ASL alphabet with higher accuracy than hand-only approach.
