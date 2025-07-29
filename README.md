# Real-Time Frequent Pattern Mining Using DGIM and Window-Based Itemset Algorithms on Streaming Data

This project implements real-time frequent pattern mining on streaming data using advanced streaming algorithms including:

- **DGIM (Datar–Gionis–Indyk–Motwani) Algorithm**
- **Time-Decaying Window-based Frequent Itemset Mining**
- **Lossy Counting Algorithm (as baseline)**

The goal is to compare and evaluate these algorithms in terms of **accuracy**, **memory usage**, and **processing speed** when applied to continuous data streams.

---

##  Key Features

-  Efficient approximation of frequent items in data streams
-  Time-decaying relevance to capture recent trends
-  Real-time updates for high-velocity data
-  Comparative evaluation of multiple algorithms

---

##  Algorithms Implemented

| Algorithm           | Description |
|--------------------|-------------|
| **DGIM**           | Used for binary stream counting using logarithmic memory. Ideal for 0/1 input streams. |
| **Decaying Window**| Captures recent itemset trends with more weight on recent data. |
| **Lossy Counting** | Maintains approximate frequent item counts within a predefined error margin. Serves as a baseline. |

---

##  Results Summary

| Metric           | DGIM       | Decaying Window | Lossy Counting |
|------------------|------------|-----------------|----------------|
| Accuracy         | High       | Very High       | Moderate       |
| Memory Usage     | Very Low   | Moderate        | High           |
| Processing Speed | Fast       | Fast            | Slower         |

---

##  Project Structure

```bash
streaming-algorithms/
│
├── dgim.py                  # Implementation of DGIM algorithm
├── decaying_window.py       # Time-decaying window-based itemset mining
├── lossy_counting.py        # Baseline Lossy Counting algorithm
├── stream_generator.py      # Simulates incoming data stream
├── evaluation.py            # Accuracy, memory, and time benchmarking
├── plots/                   # Visualizations for performance comparison
├── README.md                # Project overview
└── requirements.txt         # Python dependencies
