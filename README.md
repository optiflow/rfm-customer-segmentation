# Advanced Customer Segmentation using RFM Analysis and K-Means Clustering

## Project Overview

This project demonstrates a powerful approach to customer segmentation by combining Recency, Frequency, Monetary (RFM) analysis with the K-Means clustering algorithm. The goal is to identify distinct customer groups within a transactional dataset, enabling businesses to tailor marketing strategies, improve customer engagement, and optimize resource allocation. By understanding the different behaviors and value of customer segments, businesses can make data-driven decisions to enhance profitability and customer satisfaction.

This repository provides a step-by-step guide through a Jupyter Notebook, from data preprocessing and RFM feature engineering to the application of K-Means clustering and interpretation of the resulting segments.

## Dataset

The analysis utilizes the **Online Retail Data Set** from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/online+retail). This is a transnational dataset that contains all the transactions occurring between 01/12/2010 and 09/12/2011 for a UK-based and registered non-store online retail. The company mainly sells unique all-occasion gifts. Many customers of the company are wholesalers.

Key features used from the dataset include:
*   `InvoiceNo`: Invoice number. Nominal, a 6-digit integral number uniquely assigned to each transaction.
*   `StockCode`: Product (item) code. Nominal, a 5-digit integral number uniquely assigned to each distinct product.
*   `Description`: Product (item) name. Nominal.
*   `Quantity`: The quantities of each product (item) per transaction. Numeric.
*   `InvoiceDate`: Invoice Date and time. Numeric, the day and time when each transaction was generated.
*   `UnitPrice`: Unit price. Numeric, Product price per unit in sterling.
*   `CustomerID`: Customer number. Nominal, a 5-digit integral number uniquely assigned to each customer.
*   `Country`: Country name. Nominal, the name of the country where each customer resides.

## Methodology

### 1. Data Preprocessing
The initial dataset is cleaned and prepared for analysis. This includes:
*   Handling missing values.
*   Removing duplicate entries.
*   Converting data types (e.g., `InvoiceDate` to datetime objects).
*   Filtering out cancelled transactions or records with invalid data.

### 2. RFM Analysis
RFM analysis is a behavior-based customer segmentation technique. It uses three key metrics:
*   **Recency (R)**: How recently did the customer make a purchase? (e.g., days since the last purchase). Lower values indicate more recent activity.
*   **Frequency (F)**: How often do they make purchases? (e.g., total number of transactions). Higher values indicate more frequent engagement.
*   **Monetary (M)**: How much money do they spend? (e.g., total monetary value of purchases). Higher values indicate higher spending.

These RFM values are calculated for each customer.

### 3. K-Means Clustering
Once the RFM values are derived, K-Means clustering is applied to segment customers based on these three dimensions.
*   **Scaling:** RFM values are typically scaled (e.g., using StandardScaler) before clustering to ensure that each feature contributes proportionally to the distance calculations.
*   **Determining Optimal K:** The Elbow Method or Silhouette Analysis is used to find the optimal number of clusters (K) for the dataset.
*   **Clustering:** The K-Means algorithm partitions customers into K distinct, non-overlapping clusters, where customers within each cluster are similar in their RFM characteristics.

### 4. Segment Interpretation
The resulting clusters are analyzed to understand their characteristics. This involves examining the average RFM values for each segment and assigning meaningful labels (e.g., "High-Value Loyal Customers", "At-Risk Customers", "New Customers").

## Key Findings/Visualizations (Example)

*(This section would ideally be populated with actual outputs from the notebook, such as cluster plots or tables summarizing segment characteristics. Below are placeholder descriptions.)*

*   **Elbow Method Plot:** A plot showing the sum of squared distances for different values of K, helping to identify the optimal number of clusters.
*   **Silhouette Scores:** Provides a metric for how well-separated the clusters are.
*   **3D Scatter Plot of RFM Clusters:** Visualizing the customer segments in a 3D space with R, F, and M as axes.
*   **Segment Profiles:** A table or bar charts showing the average Recency, Frequency, and Monetary values for each customer segment, highlighting their distinct characteristics. For example:
    *   **Segment 0 (Champions):** Low R, High F, High M. Your best customers.
    *   **Segment 1 (Potential Loyalists):** Recent customers with average frequency and spending.
    *   **Segment 2 (At Risk):** High R, Average/Low F, Average/Low M. Haven't purchased in a while.

## How to Use

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/optiflow/rfm-customer-segmentation.git
    cd rfm-customer-segmentation
    ```
2.  **Set up a Python environment and install dependencies.** It's recommended to use a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install pandas numpy matplotlib seaborn scikit-learn jupyterlab
    ```
3.  **Download the dataset:**
    *   Obtain the `Online Retail.xlsx` file from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/online+retail).
    *   Place the `Online Retail.xlsx` file in the root directory of this repository.
4.  **Run the Jupyter Notebook:**
    ```bash
    jupyter lab "Customer Segmentation of Online Retail Transactions.ipynb"
    ```
    Execute the cells in the notebook sequentially to perform the analysis.

## Improvements/Future Work

This project provides a solid foundation for customer segmentation. Potential future enhancements include:
*   **Exploring other clustering algorithms:** Compare K-Means with other methods like DBSCAN, Hierarchical Clustering, or Gaussian Mixture Models.
*   **Adding more features:** Incorporate other customer attributes (e.g., demographics, product preferences if available) for richer segmentation.
*   **Dynamic Segmentation:** Develop a system for updating segments as new customer data arrives.
*   **Predictive Modeling:** Build models to predict future customer behavior or segment migration.
*   **Interactive Dashboard:** Create a dashboard (e.g., using Dash or Streamlit) for interactive exploration of customer segments.

## Contributing

Contributions are welcome! If you have suggestions for improvements or want to add new features, please feel free to:
1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/your-feature-name`).
3.  Make your changes.
4.  Commit your changes (`git commit -m 'Add some feature'`).
5.  Push to the branch (`git push origin feature/your-feature-name`).
6.  Open a Pull Request.

Please ensure your code follows good practices and includes comments where necessary.

## License

The contents of this repository are covered under the [MIT License](LICENSE).
