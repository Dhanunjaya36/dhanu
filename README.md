# Optimizing k-means Clustering: A Tutorial on Selecting k

**Author:** Dhanunjaya Rao Thandra  
**Course:** Machine Learning and Neural Networks  
**University of Hertfordshire**

## 📌 Overview
This repository contains a comprehensive tutorial on k-means clustering, specifically focusing on the critical challenge of determining the optimal number of clusters (*k*). Unlike basic tutorials that only cover the Elbow Method, this project implements and compares three distinct validation techniques to ensure robust model selection.

## 🚀 Key Features
* **Synthetic Data Generation:** Uses `make_blobs` to create a ground-truth dataset for precise validation.
* **Triple Validation Strategy:**
    1.  **Elbow Method:** Analyzing inertia variance.
    2.  **Silhouette Analysis:** Quantifying cluster cohesion and separation.
    3.  **Gap Statistic:** A statistical approach comparing data against a random reference distribution.
* **Accessibility First:** All visualizations utilize the **Viridis** color palette and **dual-encoding** (color + shape markers) to ensure readability for colorblind users and grayscale printing.
* **Ethical Framework:** Includes a discussion on bias in clustering and "digital redlining."

## 📂 Repository Structure
* `KMeans_Tutorial_Notebook.ipynb`: The interactive Python notebook containing all code, visualizations, and analysis.
* `Tutorial_KMeans_Optimization.pdf`: The final formatted tutorial report.
* `requirements.txt`: List of Python dependencies required to run the notebook.
* `figures/`: Generated plots used in the report.

## 🛠️ Installation & Usage
To run the notebook locally:

1.  **Clone this repository:**
    ```bash
    git clone [https://github.com/Dhanunjaya36/dhanu/edit/main/README.md]
    ```
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Launch Jupyter Notebook:**
    ```bash
    jupyter notebook KMeans_Tutorial_Notebook.ipynb
    ```

## 📊 Results Summary
The analysis confirms that **k=4** is the optimal number of clusters for the generated dataset, with all three methods (Elbow, Silhouette, and Gap Statistic) reaching a consensus.

## ⚖️ License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
