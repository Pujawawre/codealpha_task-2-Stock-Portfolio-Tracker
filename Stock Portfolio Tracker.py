import tkinter as tk  # Import the Tkinter library for GUI
from tkinter import messagebox  # Import messagebox for displaying messages
import requests  # Import requests to make HTTP requests

class StockPortfolio:
    def __init__(self, master):
        self.master = master
        self.master.title("Stock Portfolio Tracker")  # Set the window title
        self.stocks = {}  # Initialize a dictionary to store stock symbols and prices

        # Create and position the label and entry for stock symbol
        self.symbol_label = tk.Label(master, text="Stock Symbol:")
        self.symbol_label.grid(row=0, column=0)
        self.symbol_entry = tk.Entry(master)
        self.symbol_entry.grid(row=0, column=1)

        # Create and position the button to add stocks
        self.add_button = tk.Button(master, text="Add Stock", command=self.add_stock)
        self.add_button.grid(row=0, column=2)

        # Create and position the listbox to display stocks
        self.stock_listbox = tk.Listbox(master, width=40)
        self.stock_listbox.grid(row=1, columnspan=3)

        # Create and position the button to remove stocks
        self.remove_button = tk.Button(master, text="Remove Stock", command=self.remove_stock)
        self.remove_button.grid(row=2, column=1)

        # Create and position the button to refresh stock prices
        self.refresh_button = tk.Button(master, text="Refresh Prices", command=self.refresh_prices)
        self.refresh_button.grid(row=2, column=2)

        # Create and position a label for messages
        self.message_label = tk.Label(master, text="")
        self.message_label.grid(row=3, columnspan=3)

    def add_stock(self):
        # Get the stock symbol entered by the user
        symbol = self.symbol_entry.get().upper()
        if not symbol:
            self.message_label.config(text="Stock symbol cannot be empty.")
            return
        
        if symbol in self.stocks:
            self.message_label.config(text="Stock already exists in the portfolio.")
            return

        try:
            # Get the current price of the stock and add it to the portfolio
            price = self.get_stock_price(symbol)
            self.stocks[symbol] = price
            self.update_listbox()  # Update the listbox to show the new stock
            self.message_label.config(text="Stock added successfully.")
        except Exception as e:
            self.message_label.config(text=f"Failed to add stock: {e}")

    def remove_stock(self):
        # Get the selected stock from the listbox
        selected_index = self.stock_listbox.curselection()
        if not selected_index:
            self.message_label.config(text="Please select a stock to remove.")
            return

        # Remove the selected stock from the portfolio
        symbol = self.stock_listbox.get(selected_index[0]).split(":")[0].strip()
        del self.stocks[symbol]
        self.update_listbox()  # Update the listbox to reflect the removal
        self.message_label.config(text="Stock removed successfully.")

    def refresh_prices(self):
        # Refresh the prices for all stocks in the portfolio
        for symbol in list(self.stocks.keys()):  # Use list to avoid RuntimeError
            try:
                price = self.get_stock_price(symbol)
                self.stocks[symbol] = price  # Update the stock price
            except Exception as e:
                self.message_label.config(text=f"Failed to refresh price for {symbol}: {e}")
        self.update_listbox()  # Update the listbox to show updated prices

    def get_stock_price(self, symbol):
        # Fetch the current stock price from the Alpha Vantage API
        api_key = "YOUR_API_KEY"  # Replace with your actual API key
        url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}"
        response = requests.get(url)  # Make the API request
        data = response.json()  # Parse the response as JSON
        if "Global Quote" in data and "05. price" in data["Global Quote"]:
            return float(data["Global Quote"]["05. price"])  # Return the stock price
        else:
            raise Exception("Invalid response from API")  # Raise an error if the response is invalid

    def update_listbox(self):
        # Clear the current listbox and add all stocks and prices
        self.stock_listbox.delete(0, tk.END)
        for symbol, price in self.stocks.items():
            self.stock_listbox.insert(tk.END, f"{symbol}: ${price:.2f}")

def main():
    root = tk.Tk()  # Create the main window
    app = StockPortfolio(root)  # Initialize the StockPortfolio class
    root.mainloop()  # Start the Tkinter main loop

if __name__ == "__main__":
    main() 