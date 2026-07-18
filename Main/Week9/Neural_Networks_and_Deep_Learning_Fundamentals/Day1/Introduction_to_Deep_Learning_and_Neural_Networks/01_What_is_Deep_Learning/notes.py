'''
Deep Learning is a branch of Machine Learning (ML) that uses artificial neural networks with many layers (hence the word deep) to learn patterns from data.

Simple analogy

Think of it like this:

Artificial Intelligence (AI) → The broad field of making machines perform tasks that typically require human intelligence.
Machine Learning (ML) → A subset of AI where computers learn from data instead of being explicitly programmed.
Deep Learning (DL) → A subset of ML that uses deep neural networks to automatically learn complex patterns.
Artificial Intelligence (AI)
│
├── Machine Learning (ML)
│      │
│      └── Deep Learning (DL)
How Deep Learning works

A deep learning model consists of multiple layers of neurons:

Input Layer
      │
Hidden Layer 1
      │
Hidden Layer 2
      │
Hidden Layer 3
      │
Output Layer

Each layer learns increasingly complex features.

Example: Recognizing a car in an image

Layer 1: Detects edges and lines.
Layer 2: Detects shapes like circles and rectangles.
Layer 3: Detects parts such as wheels, windows, and headlights.
Output Layer: Identifies the object as a car.
Common applications
Image recognition (face detection, medical imaging)
Speech recognition (voice assistants)
Natural Language Processing (translation, chatbots)
Autonomous driving
Fraud detection
Recommendation systems (Netflix, YouTube, Amazon)
Popular deep learning frameworks
TensorFlow
PyTorch
Keras
JAX
Deep Learning vs. Machine Learning
Machine Learning	Deep Learning
Often requires manual feature engineering	Learns features automatically
Works well with smaller datasets	Usually needs large datasets
Faster to train	More computationally intensive
Algorithms include Random Forest, SVM, Logistic Regression	Uses deep neural networks
Easier to interpret	Often less interpretable ("black box")
Example from your automotive work

A traditional machine learning model might use engineered features (such as speed, steering angle, or sensor values) to predict whether a navigation function will fail.

A deep learning model could instead learn directly from:

Camera images
Radar or LiDAR data
Large volumes of vehicle telemetry
Voice commands

This is why deep learning is widely used in areas like driver assistance systems, autonomous driving, and advanced speech recognition.

In one sentence: Deep learning is a machine learning technique that uses multi-layer neural networks to automatically learn complex patterns from large amounts of data, making it especially powerful for tasks involving images, speech, text, and other high-dimensional data.

'''