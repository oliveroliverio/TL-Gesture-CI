
import numpy as np
import itertools
import copy

class FeatureExtractor:
    def __init__(self):
        # Mediapipe Face Mesh Indices
        self.LEFT_EYEBROW = [336, 296, 334, 293, 300, 276, 283, 282, 295, 285]
        self.RIGHT_EYEBROW = [70, 63, 105, 66, 107, 55, 65, 52, 53, 46]
        self.LIPS = [61, 146, 91, 181, 84, 17, 314, 405, 321, 375, 291, 308, 324, 318, 402, 317, 14, 87, 178, 88, 95, 185, 40, 39, 37, 0, 267, 269, 270, 409, 415, 310, 311, 312, 13, 82, 81, 42, 183, 78]
        
        # Mediapipe Pose Indices (Upper Body)
        # 11-12: Shoulders, 13-14: Elbows, 15-16: Wrists
        self.POSE_UPPER_BODY = [11, 12, 13, 14, 15, 16] 
        
    def extract_features(self, holistic_results, image_width=1, image_height=1):
        """
        Extracts specific subsets of landmarks from holistic results.
        Returns a dictionary of normalized lists.
        """
        features = {
            "face": [],
            "pose": [],
            "left_hand": [],
            "right_hand": []
        }
        
        # 1. Face Segmentation (Eyebrows + Lips)
        if holistic_results.face_landmarks:
            all_landmarks = holistic_results.face_landmarks.landmark
            relevant_indices = self.LEFT_EYEBROW + self.RIGHT_EYEBROW + self.LIPS
            
            # Extract and Flatten
            face_subset = []
            for i in relevant_indices:
                pt = all_landmarks[i]
                face_subset.extend([pt.x, pt.y]) # Ignore Z for now
            features["face"] = face_subset

        # 2. Pose Segmentation (Upper Body)
        if holistic_results.pose_landmarks:
            all_landmarks = holistic_results.pose_landmarks.landmark
            pose_subset = []
            for i in self.POSE_UPPER_BODY:
                pt = all_landmarks[i]
                pose_subset.extend([pt.x, pt.y])
            features["pose"] = pose_subset
            
        # 3. Hands (Keep full 21 points, pre-processed)
        # Note: Hand processing is usually done relative to wrist in the main app
        # This extractor returns raw normalized absolute coords for now,
        # but the main app does relative pre-processing.
        
        return features

    def get_segemented_landmarks_for_drawing(self, holistic_results):
        """
        Returns lists of landmarks objects for drawing utilities,
        containing only the segmented points.
        """
        drawing_data = {
            "face": [],
            "pose": []
        }
        
        if holistic_results.face_landmarks:
            all_landmarks = holistic_results.face_landmarks.landmark
            relevant_indices = set(self.LEFT_EYEBROW + self.RIGHT_EYEBROW + self.LIPS)
            
            # We can't easily return a "partial" LandmarkList object for standard drawing utils
            # without reconstructing it. 
            # So we return a list of (x,y) tuples scaled to image for custom drawing
            pass 

        return drawing_data
