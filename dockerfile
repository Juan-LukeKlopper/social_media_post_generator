#the official Python base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project to the working directory
COPY . .

# Expose the port on which the Streamlit application runs (if necessary)
EXPOSE 8501

# Set the environment variable for the Streamlit command
ENV STREAMLIT_SERVER_PORT=8501

# Run the Streamlit application
CMD ["streamlit", "run", "app.py"]

