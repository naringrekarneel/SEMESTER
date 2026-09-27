### DEEP LEARNING — Complete Learning Roadmap

We'll cover your syllabus in a logical sequence, starting with how CNNs process images and progressing to advanced architectures and object detection.

Our approach will be exam-focused, concept-first and practical, with worked examples, important formulas and short quizzes to check your understanding.

### 1\. Your learning roadmap

### Module 1: CNN Fundamentals

Start here

| #   | Topic                   | Main focus                                               |
| --- | ----------------------- | -------------------------------------------------------- |
| 1   | Convolution Operation   | Filters, kernels, feature maps                           |
| 2   | Padding                 | Valid and same padding                                   |
| 3   | Stride                  | Output dimensions                                        |
| 4   | Pooling                 | Max and average pooling                                  |
| 5   | CNN Architecture Design | Convolution, activation, pooling, fully connected layers |

### Module 2: Classic CNN Architectures

| #   | Topic     | Main focus                |
| --- | --------- | ------------------------- |
| 6   | LeNet-5   | Early CNN architecture    |
| 7   | AlexNet   | ReLU, dropout, GPUs       |
| 8   | ZF-Net    | Feature visualization     |
| 9   | VGGNet    | Small $3\\times3$ filters |
| 10  | GoogLeNet | Inception modules         |
| 11  | ResNet    | Residual connections      |

### Module 3: Optimization and Learning

| #   | Topic             | Main focus                        |
| --- | ----------------- | --------------------------------- |
| 12  | Width and Depth   | Capacity and computational cost   |
| 13  | Transfer Learning | Pretrained models and fine-tuning |
| 14  | Data Augmentation | Improving generalization          |

### Module 4: Object Detection

| #   | Topic         | Main focus                              |
| --- | ------------- | --------------------------------------- |
| 15  | R-CNN Family  | Region-based object detection           |
| 16  | YOLO          | Real-time object detection              |
| 17  | YOLO vs R-CNN | Architecture and performance comparison |

We'll have a revision checkpoint after Topics 5, 11 and 14, followed by a final practice test.

### Topic 1: Convolution Operation

### 1\. What is convolution? (ELI5)

Imagine you're looking at a photograph of a cat. You can recognize the cat because you identify smaller features such as its ears, eyes, whiskers and fur.

A Convolutional Neural Network (CNN) works in a similar way. Instead of trying to understand the entire image at once, it examines small regions using a mathematical operation called convolution.

![cat](https://images.openai.com/static-rsc-4/ohQocFRRRTg5c9mHvGXo1PuPxQeuYsAcVbFeMSe9QHG9M1XEsJO1CrDiJUzapwYqJO7X5pH0DdjTpjqBPpVmTDaGcFWCvRVct0uzGUHDNVhEu6oRhfdHrPPIpOlm7tJyUVGUCiy_cf_OVy5YYr4oPUzE9pp4M-_zOJ4sXyWZjCzCBJZcEZAksTecyvgBV-5H?purpose=fullsize)

Convolution filters detect visual patterns

![Pillow ImageFilter](https://images.openai.com/static-rsc-4/5h2bPtjWVGz_4xZFhMIGfd1ytLjFqf2HGyVUQKWQtFotfXixlnzSIrl5jw2ts25_G9KYPtZFVwz1ASOIC61SY7U5P2dekdCIEipOppht4R-aDBiDNOhleen3SIDvGW2ADJlcE8JrFn_vBl-jpSoo139-KcQuFNFEMuinxQNB0CIndSfaX1XaQcHY7EHA51Vp?purpose=fullsize)

Edges

![White and black texture of cat fur abstract animal skin background](https://images.openai.com/static-rsc-4/e7jZ63a3KoN6TBsLitVwv_rbrSnWY2dQ1nLa07Oax22Qm1XlCPEqemYlcxIct-aG5G-6-aloVU2ZiWU8jKa1XYjSwz_0cm5M6EwpGabRB2oXazfT23r3uo-qNsqy2tThe7yED96sX6VDinXRAM4yoWzMwZsj3tsnsULkFuuw7Kg4Jz-9UIc3ymLyVRFlu517?purpose=fullsize)

Textures

![Closeup grayscale shot of a cat's eye - concept of animal protection](https://images.openai.com/static-rsc-4/xSwhphaDE-AanMss3XHVud0FAI5stLS9Dve2UAvz4WdFqoEaGBujQxqzdhV1WJOXH-nNeeY9alIa5XIbt3KGMMuN9QAe55a2oZLBYa8gtEmPVi3Z5Yvy6SDwhabYXeTsweGh-WBjaNjDJ1fhuO9CTmPOD_wyuCRq5rjW097gvb_9xVFdoiGwexMIudk9jUxD?purpose=fullsize)

Shapes

Illustrative examples of the kinds of features CNNs can learn.

A CNN learns which filters are useful for recognizing objects during training.

### 2\. Technical explanation

Convolution is a mathematical operation in which a small matrix called a kernel (or filter) slides over an input image and performs element-wise multiplication followed by summation.

Its output is called a feature map.

### How convolution works

The kernel slides over the input. Each position produces one value in the output feature map.

### Important terminology

| Term          | Meaning                             |
| ------------- | ----------------------------------- |
| Input image   | Original pixel matrix               |
| Kernel/filter | Small matrix of weights             |
| Feature map   | Output of the convolution           |
| Stride        | Number of pixels the filter moves   |
| Padding       | Extra pixels added around the image |

### 3\. Mathematical formula

For a single-channel image, the operation commonly called convolution in CNNs is:

$$ Y(i,j)=\\sum_^\\sum_^X(i+m,j+n)W(m,n)+b $$

Where:

* $X$ = input image

* $W$ = kernel weights

* $K$ = kernel size

* $b$ = bias

* $Y$ = output feature map

Exam note: CNN libraries typically perform cross-correlation rather than strict mathematical convolution, because they do not flip the kernel. Both are commonly called convolution in deep learning.

### 4\. Step-by-step numerical example

Important for numericals

Suppose we have the following $3\\times3$ image and $2\\times2$ kernel.

Input image

| 1   | 2   | 3   |
| --- | --- | --- |
| 4   | 5   | 6   |
| 7   | 8   | 9   |

Kernel

| 1   | 0   |
| --- | --- |
| 0   | −1  |

Assume stride = 1, padding = 0 and bias = 0.

Step 1: Place the kernel over the top-left $2\\times2$ region.

$$ \\begin Y(0,0)&=(1\\times1)+(2\\times0)\\ &\\quad +(4\\times0)+(5\\times-1)\\ &=1-5\\ &=-4 \\end $$

Step 2: Move the kernel one pixel to the right.

$$ Y(0,1)=(2\\times1)+(3\\times0) $$

$$ +(5\\times0)+(6\\times-1)=-4 $$

Step 3: Repeat for the remaining two positions.

$$ Y(1,0)=4-8=-4 $$

$$ Y(1,1)=5-9=-4 $$

Final output feature map

### -4

### -4

### -4

### -4

Output size: 2 × 2

### 5\. Output size formula

One of the most frequently tested CNN formulas is:

$$ O=\\left\\lfloor\\frac\\right\\rfloor+1 $$

Where $N$ is input size, $K$ is kernel size, $P$ is padding, $S$ is stride and $O$ is output size.

For our example:

$$ O=\\frac11+1=2 $$

Therefore, the output is $2\\times2$.

For rectangular images, calculate output height and width separately.

### 6\. Why convolution is useful

* Local connectivity: Filters examine small regions rather than every pixel at once.

* Parameter sharing: The same filter is reused across the entire image, reducing the number of learnable weights.

* Feature extraction: Early layers typically learn edges and textures, while deeper layers can learn complex patterns.

* Spatial structure: Convolution preserves spatial relationships between nearby pixels.

These properties make CNNs useful for face recognition, medical image analysis, autonomous driving and object detection.

### 7\. Quick revision sheet

### Must remember for exams

* Convolution extracts spatial features using learnable filters.

* Kernel values are multiplied element-wise with the corresponding image region and summed.

* The output is called a feature map.

* A filter is reused at every spatial position.

* Output size depends on input size, kernel size, padding and stride.

* For a standard convolution, each output channel has its own learned filter bank spanning all input channels.

Two essential formulas

$$Y(i,j)=\\sum_m\\sum_n X(i+m,j+n)W(m,n)+b$$

$$O=\\left\\lfloor\\frac\\right\\rfloor+1$$

### 8\. Active learning — Your turn

Answer these four questions before we move to padding.

Conceptual questions

Q1. What is the purpose of a kernel in a CNN?

Q2. Why does a CNN use the same kernel at different positions of an image?

Q3. What is the difference between an input image and a feature map?

Numerical question

Q4. Given an input image of size $7\\times7$, a kernel of size $3\\times3$, stride $1$ and padding $0$, calculate the output feature map size. Show your formula and working.

Reply with your answers numbered 1–4. I'll check them, explain any mistakes and then we'll move to Topic 2: Padding.
