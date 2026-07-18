'''
Sigmoid
    --Use Case: Binary classfication in the output layer
    --Limitation: Can Suffer from vanishing gradients for large positive/negative z
Tanh(Hyperbolic Tangent)
    --Use Case: Hidden Layers where zero centered outputs are preferred
    --Limitation: Also prone to vanishing gradients
ReLU(Rectified Linear Unit)
    --use Case: Most commonly used in hidden layers due to simplicity and efficiency 
    --Limitation: Can suffer from the ''dying ReLU' problem(neurons stuck at zero)
Softmax
    --Use Case: Milti classification in the output layer

'''