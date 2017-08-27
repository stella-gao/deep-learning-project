```
name: "polya_model"
input: "data"
input_dim: 10000
input_dim: 1
input_dim: 4
input_dim: 162
layers {
  bottom: "data"
  top: "conv1_1"
  name: "conv1_1"
  type: CONVOLUTION
  convolution_param {
    num_output: 16
    pad: 1
    kernel_size: 4
  }
}
layers {
  bottom: "conv1_1"
  top: "conv1_1"
  name: "relu1_1"
  type: RELU
}
layers {
  bottom: "conv1_1"
  top: "drop1"
  name: "drop1"
  type: DROPOUT
  dropout_param {
    dropout_ratio: 0.4
  }
}

layers {
  bottom: "drop1"
  top: "conv1_2"
  name: "conv1_2"
  type: CONVOLUTION
  convolution_param {
    num_output: 64
    pad: 1
    kernel_size: 4
  }
}
layers {
  bottom: "conv1_2"
  top: "conv1_2"
  name: "relu1_2"
  type: RELU
}
layers {
  bottom: "conv1_2"
  top: "pool1"
  name: "pool1"
  type: POOLING
  pooling_param {
    pool: MAX
    kernel_size: 2
    stride: 2
  }
}

layers {
  bottom: "pool1"
  top: "drop2"
  name: "drop2"
  type: DROPOUT
  dropout_param {
    dropout_ratio: 0.4
  }
}
layers {
  bottom: "drop2"
  top: "fc1"
  name: "fc1"
  type: INNER_PRODUCT
  inner_product_param {
    num_output: 64
  }
}
layers {
  bottom: "fc1"
  top: "fc1"
  name: "relu2"
  type: RELU
}
layers {
  bottom: "fc1"
  top: "drop3"
  name: "drop3"
  type: DROPOUT
  dropout_param {
    dropout_ratio: 0.8
  }
}
layers {
  bottom: "drop3"
  top: "fc2"
  name: "fc2"
  type: INNER_PRODUCT
  inner_product_param {
    num_output: 1
  }
}
layers {
  bottom: "fc2"
  top: "prob"
  name: "prob"
  type: SOFTMAX
}
```
