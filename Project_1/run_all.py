import subprocess
import os
import time

# Step 1: Start Flask API in a new terminal window
flask_path = os.path.join("api", "app.py")
flask_cmd = f'start cmd /k "python {flask_path}"'

# Step 2: Wait a few seconds to make sure Flask starts
print("Starting Flask API...")
os.system(flask_cmd)
time.sleep(3)

# Step 3: Start Streamlit app
streamlit_path = os.path.join("webapp", "dashboard.py")
print("Starting Streamlit dashboard...")
subprocess.run(["streamlit", "run", streamlit_path])
