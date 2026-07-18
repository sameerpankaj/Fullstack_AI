'''

An Artificial Neural Network (ANN) is a machine learning model inspired by the way the human brain processes information. It consists of interconnected processing units called neurons that learn patterns from data.

Basic Structure of an ANN
          Input Layer
      x1    x2    x3    x4
       │     │     │     │
       └─────┼─────┼─────┘
             │
      Hidden Layer 1
      ●   ●   ●   ●   ●
             │
      Hidden Layer 2
      ●   ●   ●   ●
             │
        Output Layer
             ●

An ANN typically has three types of layers:

Input Layer
Receives the input data.
Example: Age, salary, tenure, monthly charges.
Hidden Layers
Perform calculations and extract patterns.
More hidden layers = "Deep" Neural Network.
Output Layer
Produces the final prediction.
Example:
Customer will churn (Yes/No)
Image is a cat
Fraud detected
How a Neuron Works

Each neuron receives inputs, assigns weights, adds a bias, and applies an activation function.

Inputs
 x1
 x2 ------> Σ (Weighted Sum) ----> Activation Function ----> Output
 x3

The calculation is:

z=w
1
	​

x
1
	​

+w
2
	​

x
2
	​

+w
3
	​

x
3
	​

+b

Then an activation function is applied:

Output=f(z)

where:

x = input values
w = weights (importance of each input)
b = bias
f = activation function
Common Activation Functions
1. Sigmoid

Output ranges from 0 to 1.

Used for:

Binary classification
2. ReLU (Rectified Linear Unit)
f(x)=max(0,x)

Most commonly used in hidden layers because it trains efficiently.

3. Tanh

Output ranges from -1 to 1.

Often used when data contains negative values.

4. Softmax

Used for multi-class classification.

Example:

Cat
Dog
Horse

Outputs probabilities that sum to 1.

Training Process

The ANN learns by repeatedly adjusting its weights.

Step 1

Provide input data.

↓

Step 2

Forward propagation:
The network predicts an output.

↓

Step 3

Calculate the error (loss).

↓

Step 4

Backpropagation:
The error is propagated backward to update the weights.

↓

Step 5

Repeat over many epochs until the error is minimized.

Important Terms
Epoch

One complete pass through the entire training dataset.

Batch

A subset of the training data processed before updating weights.

Learning Rate

Controls how much the weights change during each update.

Loss Function

Measures how far predictions are from the true values.

Examples:

Mean Squared Error (Regression)
Binary Cross-Entropy (Binary Classification)
Categorical Cross-Entropy (Multi-Class Classification)
Optimizer

Algorithm that updates the weights.

Popular optimizers:

Gradient Descent
Stochastic Gradient Descent (SGD)
Adam (most widely used)
RMSprop
Advantages
Learns complex patterns automatically.
Excellent for images, speech, text, and time-series data.
Handles large datasets well.
High predictive accuracy for many tasks.
Limitations
Requires large amounts of data.
Computationally intensive.
Longer training time.
Harder to interpret than simpler models like decision trees.
Applications
Image recognition
Speech recognition
Natural Language Processing (NLP)
Fraud detection
Medical diagnosis
Recommendation systems
Autonomous driving
Predictive maintenance
Customer churn prediction
ANN vs Traditional Machine Learning
Traditional ML	Artificial Neural Networks
Requires manual feature engineering	Learns features automatically
Performs well on small datasets	Excels with large datasets
Faster to train	Slower to train
Easier to interpret	More difficult to interpret
Examples: Random Forest, SVM, Logistic Regression	Multi-layer Neural Networks
Example in Automotive

Suppose you're building a system to predict whether a vehicle function will fail.

Traditional ML: You manually create features (e.g., speed, GPS signal strength, sensor values) and train a model like Random Forest.
ANN: The network learns which combinations of inputs are important by adjusting its weights during training, reducing the need for manual feature engineering.
Key Takeaway

An Artificial Neural Network is a machine learning model made up of interconnected neurons arranged in layers. It learns by adjusting weights through forward propagation and backpropagation, making it particularly effective for solving complex problems such as image recognition, speech processing, language understanding, and many other AI applications.

'''