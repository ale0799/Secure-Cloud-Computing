FROM python:3.10.9-slim-buster

WORKDIR /app

# Copy requirements
COPY requirements.txt ./requirements.txt

# Install dependencies
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libxrender1 \
    gcc \
    g++ \
    build-essential
RUN pip3 install -r requirements.txt

# Expose port
EXPOSE 8501

# Copy all the files needes for the application
ADD data /app/data
COPY app.py /app
ADD models /app/models
ADD logs /app/logs

# Create an entry point to make the image executable
ENTRYPOINT ["streamlit", "run"]
# Run the application app.py otherwise app_pipeline.py for the pipeline
CMD ["app.py"]
#CMD ["app_pipeline.py"]



