# Hello World Application

This is a simple Python application build using the Flask framework that displays "Hello, World!". 

## Requirememnts

- Python 3.9 or higher
- Docker (if running via Docker)

## Getting Started

Follow the below instructions to downlaod the source code on your local machine and run the application manually. 

### Clone the repository

Firstly, clone the repository to your local machine:
```
git clone https://github.com/yourusername/my-flask-app.git
```


### Manual Installation

1. Navigate into the cloned repository:
```
cd my-flask-app
```
2. Install the dependencies:
```
pip install -r requirements.txt
```
3. Now you can run the server:
```
python app.py
```
4. Navigate to `http://localhost:5000` in your web browser to view the application.

### Docker Installation

You can also run this app as a Docker container.

1. Build the Docker image:
```
docker build -t my-flask-app .
```
2. Run the Docker container:
```
docker run -p 5000:5000 my-flask-app
```
3. Navigate to `http://localhost:5000` in your web browser to view the application.
