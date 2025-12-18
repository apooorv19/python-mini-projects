FROM python:3.11.8-slim

WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

COPY train.py main.py ./

RUN python train.py

# Expose the port the app runs on
EXPOSE 8000

# Command to run the API when the container starts
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]