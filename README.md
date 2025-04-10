# 🔌 Real-Time OHLC Data Pipeline using WebSocket & Zerodha API

This project is a real-time market data streaming backend built using WebSockets. It connects to the **Zerodha Kite API** to fetch live trade prices, aggregates them into OHLC (Open-High-Low-Close) candles for custom timeframes (1 min, 15 min, etc.), and stores the data efficiently using **MongoDB** and **Redis**. Designed as a foundational backend system for **quantitative trading and analysis**.

---

## 🚀 Features

- ⚡ **Real-Time Data Feed**: Connects to Zerodha API via WebSocket to receive live market ticks.
- 📊 **Custom OHLC Aggregation**: Supports configurable timeframes (1-min, 5-min, 15-min, etc.).
- 🧠 **Quant-Ready Architecture**: Creates a backend data flow suitable for quant research and strategies.
- 🗃️ **Efficient Data Storage**:
  - **Redis**: For storing and updating live tick data.
  - **MongoDB**: For persisting OHLC candles historically.
- ♻️ **Highly Modular**: Easy to extend with strategy logic, analytics, or REST APIs.

---

## 🧠 Tech Stack

| Component   | Technology          |
|-------------|----------------------|
| Backend     | Python               |
| Streaming   | WebSocket (Zerodha Kite Connect) |
| In-Memory DB| Redis                |
| NoSQL DB    | MongoDB              |
| Utilities   | Pandas, Logging, JSON |

---

## 📁 Folder Structure

```
Websocket-Connection/
│
├── connect.py                 # Handles WebSocket connection & tick subscription
├── data_handler.py            # OHLC aggregation logic and Redis/Mongo updates
├── utils/                     # Utility functions for timeframes, config
├── logs/                      # Stores log files for tick data or errors
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

---

## ⚙️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/piyushhh17/Websocket-Connection.git
cd Websocket-Connection
```

### 2. Set up environment and install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add Zerodha API credentials

Create a `.env` file or securely add your API key, access token, and user details.

```env
API_KEY=your_api_key
ACCESS_TOKEN=your_access_token
USER_ID=your_user_id
```

### 4. Run the WebSocket connection

```bash
python connect.py
```

Live ticks will be received, aggregated, and stored in real time.

---

## 🔎 Example Use Cases

- 📈 Real-time charting and visual dashboards
- 🧪 Backtesting trading strategies on real tick data
- 📉 Anomaly detection in live market feeds
- 📊 ML-driven prediction models using historical OHLC candles

---

## 📦 Future Enhancements

- Add REST API endpoints for OHLC retrieval
- Integrate with Plotly or Dash for visual monitoring
- Add strategy engine and alert triggers
- Support multiple instruments and exchanges dynamically

---

## 📜 License

This project is under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🙌 Author

**Piyush Kaushal**  
📧 piyushkaushal17@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/piyushhh17/)  
🐙 [GitHub](https://github.com/piyushhh17)

---

> If you're building algo trading systems, quant engines, or real-time dashboards—this backend is a great foundation. Feel free to fork, contribute, or star ⭐ the project!
