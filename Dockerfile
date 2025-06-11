# Use slim Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy and install dependencies
COPY webapi/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY webapi/ .

RUN adduser --disabled-password appuser
USER appuser

# Run the Flask app
CMD ["python", "app.py"]
