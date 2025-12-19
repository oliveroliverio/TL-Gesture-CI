
# 2025-12-19 - Phase 1: Holistic Upgrade (ASL Conversion)

## Summary
Successfully transitioned the core tracking engine from `MediaPipe Hands` to `MediaPipe Holistic`. This is the foundational step for the ASL transcription project, enabling the application to perceive facial expressions and body language alongside hand gestures.

## Changes Implemented
*   **Engine Replacement**: Swapped `mp.solutions.hands` for `mp.solutions.holistic` in `app.py`.
*   **Visual Debugging**: Added real-time rendering of:
    *   **Face Mesh**: 468 facial landmarks to track eyes, eyebrows, and mouth.
    *   **Pose Landmarks**: Body skeletal tracking to detect arm arm/shoulder position.
*   **Compatibility**: 
    *   Maintained existing hand gesture classification for both Left and Right hands.
    *   Patched `draw_info_text` to accept string labels (e.g., "Left", "Right") as the new Holistic solution returns data differently than the pure Hands solution.

## Next Steps (Project Phase 2)
1.  **Segmentation**: The current visual output is very "busy" (full face mesh). We need to filter this data.
2.  **Feature Extraction**: modifying the logs to only record:
    *   Eyebrows (Questions/Emotion)
    *   Mouth (Lip reading/Context)
    *   Upper Body Arm vectors (Sign location)
3.  **Data Collection**: Begin recording new "Holistic" datasets to train the future ASL model.

# 2025-12-19 - Phase 2: Segmentation & Feature Extraction

## Summary
Refined the "Holistic" upgrade by implementing proper segmentation. The application now filters the raw MediaPipe stream to isolate only the features relevant to American Sign Language, significantly reducing visual noise and preparing the data structure for future training.

## Changes Implemented
*   **FeatureExtractor Module**: Created `model/feature_extractor.py` to manage landmark indices.
    *   **Face**: Defined subsets for Left/Right Eyebrows and Lips.
    *   **Pose**: Filted for Upper Body only (Shoulders, Elbows, Wrists).
*   **Visual Cleanup**:
    *   Removed the dense "Spiderweb" Face Mesh.
    *   Implemented custom drawing to show:
        *   **Yellow Dots**: Eyebrows (Grammar/Questions).
        *   **Red Dots**: Lips (Mouthing/Modifiers).
        *   **Blue Dots**: Upper Body joints (Sign Location).
*   **Data Logging**:
    *   Updated `logging_csv` in `app.py` to accept the new `holistic_features` dictionary.
    *   Created a parallel data stream `keypoint_holistic.csv` to record these new features without breaking the existing static hand classifier.

## Next Steps (Project Phase 3)
1.  **Data Collection**: Use the new app to record dataset samples for ASL alphabet + facial grammar.
2.  **Model Training**: Train a new classification model that uses this combined (Hand + Face + Pose) data.
