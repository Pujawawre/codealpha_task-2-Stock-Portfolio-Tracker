CodeAlpha Python Internship🔖


🖇️Stock Portfolio Tracker Project in Python


🖇️Overview:


The Stock Portfolio Tracker is a desktop application built with Python's Tkinter library. It allows users to manage a portfolio of stocks by adding, removing, and refreshing stock prices in real-time. The application fetches stock data using the Alpha Vantage API, providing users with an easy way to monitor their investments.

🖇️Core Functionalities:

1. Add Stock: Users can input a stock symbol to add it to their portfolio. The application fetches the current price of the stock and displays it in a list.

2. Remove Stock: Users can select a stock from the list and remove it from their portfolio.

3. Refresh Prices: Users can refresh the stock prices for all stocks in their portfolio, ensuring they have the latest data.

4. User Feedback: The application provides real-time feedback through a message label, indicating success or failure for each operation.
   

🖇️Technical Specifications:


1.Programming Language: Python 3.x

2.Libraries Used:
  tkinter: For the graphical user interface (GUI).
  requests: For making HTTP requests to the Alpha Vantage API.
  API: Alpha Vantage for fetching stock prices. Requires an API key for access.

  
🖇️Installation:


1. Prerequisites:
 - Python 3.x installed on your machine.
 - An internet connection for fetching stock prices.

2. Install Required Libraries: Open a terminal and run the following command to install the requests library:
pip install requests

3. API Key:
Sign up at Alpha Vantage to get a free API key. Replace YOUR_API_KEY in the code with your actual API key.


🖇️Usage:


1. Run the Application: Execute the script using Python:
 python stock_portfolio_tracker.py

2. Adding Stocks:
    - Enter the stock symbol (e.g., AAPL for Apple Inc.) in the "Stock Symbol" entry field.
    - Click the "Add Stock" button. If successful, the stock will appear in the list.
      
3. Removing Stocks: Select a stock from the list and click the "Remove Stock" button to delete it from your portfolio.

4. Refreshing Prices: Click the "Refresh Prices" button to update the prices for all stocks in your portfolio.


🖇️Code Structure: The code is organized into a single class, StockPortfolio, which encapsulates all functionalities related to managing the stock portfolio. 

Key methods include:

1. __init__: Initializes the GUI components and sets up the layout.

2. add_stock: Handles the addition of stocks and displays appropriate messages.

3. remove_stock: Manages stock removal and updates the display.

4. refresh_prices: Updates stock prices for all stocks in the portfolio.

5. get_stock_price: Fetches the current stock price using the Alpha Vantage API.

6. update_listbox: Refreshes the listbox to show the current stocks and their prices.

The main function creates the main window and starts the Tkinter main loop.
