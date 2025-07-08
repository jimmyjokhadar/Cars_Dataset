# 🚗 Car Brand Image Scraper & Identity Classifier
This project is an experimental attempt to explore whether car brands maintain a consistent visual identity across different models.
To achieve this, the project:
- Scrapes car images by brand using the `duckduckgo_search` API.
- Prepares a structured dataset for training a classifier.
- Trains a computer vision model to predict car brands.
- Tests the model on unseen car models from each brand to evaluate generalization and design consistency.

## 🎯 Objective
Can a deep learning model trained on some car models from a specific brand correctly identify unseen models from that brand? \
This would suggest that brands have recognizable visual identity cues in their design language (e.g., grilles, headlight shapes, proportions).

## 🛠️ Project Workflow
### 1. Image Scraping
- Uses duckduckgo_search to programmatically collect images for various car brands and models.
- Ensures clean and relevant results with keyword filtering and image deduplication.

### 2. Dataset Preparation
- Filtering and preprocessing (resizing, augmentation).
- Split into training and test sets by excluding specific car models from training (e.g., exclude "BMW E46" to test generalization).

### 3. Model Training
- Train a deep learning model (e.g., CNN, ResNet) on car images by brand.
- Evaluate accuracy and generalization on test set containing unseen models.

### 4. Analysis
- Assess if the model can still identify the correct brand without having seen that specific model.
- Helps quantify brand identity retention across vehicle designs.
