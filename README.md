
# Crime Data Query Processing 🚓📊

A data-intensive application built using **Apache Spark**, **Streamlit**, and **Flask** to enable fast, scalable querying and analysis of crime data. This project demonstrates the use of distributed systems and big data technologies for efficient data handling and real-time querying.

## 📌 Features

- 🔍 Query large-scale crime data using Apache Spark
- 📈 Visualize crime trends, patterns, and statistics via Streamlit
- 🖥️ Backend integration using Flask for query management
- 🗃️ Support for distributed and parallel data processing
- ⚡ Optimized for performance and scalability

## 🧰 Tech Stack

| Technology     | Description                                  |
|----------------|----------------------------------------------|
| Apache Spark   | Distributed data processing engine           |
| Streamlit      | Interactive web application frontend         |
| Flask          | Lightweight Python web framework (API layer) |
| Pandas         | Data manipulation and preprocessing          |
| Python         | Core programming language                    |

## 📁 Project Structure

```
Crime-Data-Query-Processing/
├── app/                    # Flask backend
│   ├── routes/             # API route handlers
│   └── __init__.py
├── streamlit_app/          # Streamlit frontend
│   └── main.py
├── spark_jobs/             # Spark data processing scripts
│   └── query_processor.py
├── data/                   # Crime dataset (sample)
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Apache Spark
- pip (Python package manager)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Gaurav-04-06/Crime-Data-Query-Processing.git
   cd Crime-Data-Query-Processing
   ```

2. Set up the Python environment:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure Apache Spark is installed and configured correctly.

4. Run the Flask backend:
   ```bash
   cd app
   python run.py
   ```

5. In a new terminal, launch the Streamlit app:
   ```bash
   cd streamlit_app
   streamlit run main.py
   ```

## 📊 Use Case Scenarios

- Urban planning & policy decisions based on crime data
- Law enforcement analytics
- Real-time crime data querying for research and journalism


## 📂 Dataset

This project uses publicly available crime data. You can replace the dataset in the `data/` folder with your own, maintaining the same format (CSV or Parquet).

## 🔧 Future Enhancements

- Integration with live crime databases via APIs
- User authentication and access control
- Advanced analytics with ML models (e.g., crime prediction)
- Caching and performance improvements with Spark SQL

## 🤝 Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements or bug fixes.

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

**Made with 💻 by [Gaurav](https://github.com/Gaurav-04-06)**
