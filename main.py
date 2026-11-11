import datetime
import uuid

# --- SNIPPET LIBRARY ---
# This section contains organized, reusable code blocks (snippets).
# In a larger project, these might reside in a dedicated 'utils.py' or 'helpers.py' module.

def log_message(level: str, message: str):
    """
    Snippet: Logs a message with a given level and timestamp.
    Ensures consistent logging format across the application.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] [{level.upper()}] {message}")

def format_currency(amount: float, currency_symbol: str = "TL"):
    """
    Snippet: Formats a float as a currency string.
    Provides a consistent way to display monetary values.
    """
    return f"{amount:,.2f} {currency_symbol}"

def calculate_discount(price: float, discount_percentage: float):
    """
    Snippet: Calculates the final price after applying a discount.
    A common business logic snippet to avoid recalculating everywhere.
    """
    if not (0 <= discount_percentage <= 100):
        raise ValueError("Discount percentage must be between 0 and 100.")
    discount_amount = price * (discount_percentage / 100)
    return price - discount_amount

def generate_unique_id(prefix: str = "ID"):
    """
    Snippet: Generates a simple unique ID using UUID.
    Useful for temporary identifiers or placeholders.
    """
    return f"{prefix}-{uuid.uuid4().hex[:8].upper()}"

# --- APPLICATION LOGIC ---
# This part of the code demonstrates how to effectively use the organized snippets.

if __name__ == "__main__":
    print("--- Demonstrating Organized Code Snippets ---")

    # Using the logging snippet
    log_message("INFO", "Application started successfully.") # Illustrates using a reusable logging snippet
    log_message("DEBUG", "Processing user data...")

    # Using the currency formatting snippet
    product_price = 1234.567
    formatted_price = format_currency(product_price, "USD") # Illustrates using a reusable formatting snippet
    print(f"Product price: {formatted_price}")

    # Using the discount calculation snippet
    original_price = 250.0
    discount_rate = 15.0
    final_price = calculate_discount(original_price, discount_rate) # Illustrates using a reusable calculation snippet
    print(f"Original price: {format_currency(original_price)}")
    print(f"Discounted price ({discount_rate}%): {format_currency(final_price)}")

    # Using the unique ID generation snippet
    user_id = generate_unique_id("USER") # Illustrates using a reusable ID generation snippet
    order_id = generate_unique_id("ORDER")
    print(f"Generated User ID: {user_id}")
    print(f"Generated Order ID: {order_id}")

    log_message("INFO", "Application finished.")
