# TOPSIS-Based Selection of Best Conversational AI Model

---

## Introduction

Conversational AI models are widely used in chatbots, virtual assistants, and automated communication systems. Selecting the best model is a **multi-criteria decision-making problem**, since performance depends on several factors such as quality, latency, cost, and contextual understanding.

This project applies the **TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)** method to evaluate and rank popular pre-trained conversational AI models.

---

## Objective

The objective of this project is to:

* Compare multiple conversational AI models
* Evaluate them using benchmark performance metrics
* Apply the TOPSIS algorithm to determine the best model

---

## Models Compared

The following conversational AI models are evaluated:

* Claude Opus
* Gemini 2.5
* GPT-4.1
* LLaMA 3.3
* GPT-4o Turbo

---

## Evaluation Criteria

The models are evaluated using the following criteria:

| Criterion     | Description                              | Type      |
| ------------- | ---------------------------------------- | --------- |
| Elo Score     | Human preference ranking                 | Benefit ↑ |
| Quality Index | Response accuracy and coherence          | Benefit ↑ |
| Latency (s)   | Response time                            | Cost ↓    |
| Context Score | Ability to maintain conversation context | Benefit ↑ |
| Cost ($)      | API usage cost                           | Cost ↓    |

---

## Dataset

| Model        | Elo  | Quality | Latency | Context | Cost |
| ------------ | ---- | ------- | ------- | ------- | ---- |
| Claude Opus  | 1496 | 0.88    | 1.13    | 5       | 15   |
| Gemini 2.5   | 1486 | 0.83    | 0.51    | 4       | 2.8  |
| GPT-4.1      | 1287 | 0.99    | 0.48    | 4       | 10   |
| LLaMA 3.3    | 1000 | 0.74    | 0.59    | 3       | 3.5  |
| GPT-4o Turbo | 1100 | 0.88    | 0.60    | 4       | 15   |

---

## TOPSIS Methodology

TOPSIS ranks alternatives based on their distance from an **ideal best** and **ideal worst** solution.

### Step 1: Decision Matrix

Let the decision matrix be:

[
X = [x_{ij}]
]

where:

* (i = 1,2,...,m) (models)
* (j = 1,2,...,n) (criteria)

---

### Step 2: Normalization

Each value is normalized using vector normalization:

[
r_{ij} = \frac{x_{ij}}{\sqrt{\sum_{i=1}^{m} x_{ij}^2}}
]

---

### Step 3: Weighted Normalized Matrix

Weights are applied to each criterion:

[
v_{ij} = w_j \cdot r_{ij}
]

Weights used in this project:

```
[0.25, 0.25, 0.15, 0.20, 0.15]
```

---

### Step 4: Ideal Best and Worst Solutions

[
A^+ = {v_1^+, v_2^+, ..., v_n^+}
]

[
A^- = {v_1^-, v_2^-, ..., v_n^-}
]

For benefit criteria:

[
v_j^+ = \max(v_{ij}), \quad v_j^- = \min(v_{ij})
]

For cost criteria:

[
v_j^+ = \min(v_{ij}), \quad v_j^- = \max(v_{ij})
]

---

### Step 5: Distance Measures

Distance from ideal best:

[
S_i^+ = \sqrt{\sum_{j=1}^{n} (v_{ij} - v_j^+)^2}
]

Distance from ideal worst:

[
S_i^- = \sqrt{\sum_{j=1}^{n} (v_{ij} - v_j^-)^2}
]

---

### Step 6: TOPSIS Score

[
C_i = \frac{S_i^-}{S_i^+ + S_i^-}
]

Higher (C_i) indicates a better alternative.

---

## Visualization

A **bar graph** is generated to visualize the TOPSIS scores of the models. The model with the highest score is ranked as the best conversational AI model.
<img width="1000" height="600" alt="image" src="https://github.com/user-attachments/assets/a5e9f56d-ae06-4f7b-bd13-86a86bb0ad86" />

---

## Results and Analysis

The bar graph below shows the TOPSIS scores of the evaluated conversational AI models.

From the computed TOPSIS scores:

* **Gemini 2.5** achieved the highest score (~0.78) and is ranked **1st**
* **GPT-4.1** ranked **2nd** with a score of ~0.61
* **LLaMA 3.3** ranked **3rd**
* **GPT-4o Turbo** ranked **4th**
* **Claude Opus** ranked **5th**

The results indicate that Gemini 2.5 provides the best balance between conversational quality, latency, context handling, and cost among the evaluated models.

Higher TOPSIS scores indicate closer proximity to the ideal best solution and greater distance from the worst solution. Therefore, Gemini 2.5 is selected as the optimal conversational AI model in this study.

The visualization clearly highlights performance differences and supports objective decision-making using the TOPSIS framework.

---

## 🛠️ Technologies Used

* Python
* NumPy
* Pandas
* Matplotlib

---

## ▶️ How to Run the Project

### 1. Clone the repository

```
git clone <your-repository-link>
```

### 2. Install dependencies

```
pip install numpy pandas matplotlib
```

### 3. Run the script

```
python topsis.py
```

---

## Project Structure

```
TOPSIS-Conversational-AI
 ┣ topsis.py
 ┣ result.png
 ┗ README.md
```

---

## Conclusion

The TOPSIS method provides a systematic and quantitative approach to selecting the best conversational AI model. By considering multiple evaluation criteria simultaneously, the method ensures a balanced and objective comparison.

This framework can be extended to other AI model evaluation and multi-criteria decision-making problems.

---
