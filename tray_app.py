# tray_app.py
import pystray
from PIL import Image
import threading
import webbrowser
import time
import os
import signal
import sys
import requests

# Import your Flask app instance from your existing app file
# Make sure your_flask_app.py exists and defines an 'app' instance
try:
    from main import app as flask_app_instance
except ImportError:
    print("Error: Could not import 'app' from 'my_flask_app.py'.")
    print("Please ensure your Flask app file is named 'my_flask_app.py' and contains 'app = Flask(__name__)' or adjust the import statement.")
    sys.exit(1)

# --- Configuration ---
HOST = '127.0.0.1'
PORT = 5505
BASE_URL = f"http://{HOST}:{PORT}"
AGENTIC_DASHBOARD_PATH = "/AgentDashboard"
AGENTIC_WORKFLOW_PATH = "/AgenticWorkflow"
ICON_PATH = 'static/CDN/images/trayicon.png' # Make sure this image file exists in the same directory

# Global variable for the Flask app's thread
flask_thread = None

def run_flask_app_in_thread():
    """Runs the Flask app in a separate thread."""
    global flask_thread
    print(f"Starting Flask app on {BASE_URL}...")
    try:
        # Create a thread to run the Flask app
        # Use debug=False and use_reloader=False for background threads
        flask_thread = threading.Thread(
            target=lambda: flask_app_instance.run(
                host=HOST,
                port=PORT,
                debug=False,
                use_reloader=False
            )
        )
        flask_thread.daemon = True # Allow the main program to exit even if this thread is running
        flask_thread.start()
        print("Flask app thread started.")

        # Give Flask a moment to start up before trying to open the browser
        time.sleep(2)
        return True
    except Exception as e:
        print(f"Error starting Flask app: {e}")
        return False

def open_url_in_browser(url_path="/"):
    """Opens a specific page of the Flask app in the default browser."""
    url = f"{BASE_URL}{url_path}"
    print(f"Opening {url} in browser...")
    webbrowser.open_new_tab(url)

def trigger_background_process(url_path: str):
    """
    Makes an HTTP GET request to the given URL in the background.
    No browser window will be opened.
    """
    url = f"{BASE_URL}{url_path}"
    print(f"Triggering background URL: {url}...")
    try:
        response = requests.get(url, timeout=50) # 5-second timeout
        response.raise_for_status() # Raise an exception for HTTP errors (4xx or 5xx)
        print(f"Background process at {url} triggered successfully. Status: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error triggering background process at {url}: {e}")

def exit_app(icon, item):
    """Exits the tray application and attempts to stop the Flask app."""
    print("Exiting application...")
    if flask_thread and flask_thread.is_alive():
        print("Flask app thread is running, attempting to join/stop it...")
        # Note: Directly stopping a thread running app.run() is tricky.
        # Setting it as daemon means it will exit with the main process.
        # For more complex shutdowns, consider multiprocessing or a more
        # sophisticated server like Waitress/Gunicorn.
        # For simple cases, daemon thread + sys.exit() is often sufficient.
        pass # Daemon thread will die with the main thread
    icon.stop()
    sys.exit(0)

def setup_tray_icon():
    """Sets up the system tray icon and its menu."""
    try:
        # Load the icon image
        image = Image.open(ICON_PATH)
    except FileNotFoundError:
        print(f"Warning: Icon file not found at '{ICON_PATH}'. Using a blank image.")
        print("Please create an 'static/CDN/images/trayicon.png' file in the same directory for a custom icon.")
        # Create a simple fallback image if the icon is not found
        image = Image.new('RGB', (64, 64), 'white')
    except Exception as e:
        print(f"Error loading icon: {e}. Using a blank image.")
        image = Image.new('RGB', (64, 64), 'white')

    menu = (
        pystray.MenuItem('Open Home Page', lambda icon, item: open_url_in_browser(AGENTIC_DASHBOARD_PATH)),
        pystray.MenuItem('Open Agentic Workflow', lambda icon, item: open_url_in_browser(AGENTIC_WORKFLOW_PATH)),
        pystray.MenuItem('Execute Agents', lambda icon, item: trigger_background_process('/execute_agents')),
        pystray.Menu.SEPARATOR, # CORRECTED LINE: No MenuItem() wrapper for SEPARATOR
        pystray.MenuItem('Exit', exit_app)
    )

    icon = pystray.Icon(
        "flask_agentic_app",
        image,
        "Flask Agentic Workflow App", # Tooltip text for the icon
        menu
    )
    return icon

if __name__ == '__main__':
    # Start the Flask app in a separate thread
    if not run_flask_app_in_thread():
        print("Failed to start Flask app. Exiting tray application.")
        sys.exit(1)

    # Set up and run the tray icon
    icon = setup_tray_icon()

    # Register signal handlers for graceful exit (e.g., Ctrl+C in console)
    # This helps clean up if the script is terminated from the terminal.
    def handle_exit_signal(signum, frame):
        print(f"Received signal {signum}. Stopping application gracefully.")
        # No need to explicitly stop Flask thread if it's daemon, it will exit
        icon.stop()
        sys.exit(0)

    signal.signal(signal.SIGINT, handle_exit_signal)
    signal.signal(signal.SIGTERM, handle_exit_signal)

    print("Tray icon application started. Look for 'Flask Agentic Workflow App' in your system tray.")
    icon.run() # This is a blocking call, keeps the tray icon alive