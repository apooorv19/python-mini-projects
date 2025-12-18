# 🎬 IMDb Random Movie Picker

A Python command-line tool that scrapes the live **IMDb Top 250** chart and suggests a random high-rated movie for you to watch.

## 🚀 Features
* **Real-Time Data:** Scrapes IMDb directly, so the ratings and rankings are always up to date.
* **Smart Parsing:** Extracts titles, years, and ratings securely.
* **Interactive:** Don't like the suggestion? Hit `Enter` to get another one instantly.
* **Dockerized:** Runs in a lightweight container without messing up your local environment.

## 🛠️ How to Run

### Option 1: Using Docker (Recommended)
You don't need to install Python or libraries on your machine.

1. **Build the image:**
   ```bash
   docker build -t imdb-picker .
2. Run the container: Note: We use -it to enable interactive mode so you can type inputs
   ```bash
   docker run -it --rm imdb-picker

### Option 2: Running Locally (Python)
If you prefer running it directly on your machine:

1. Install dependencies:
   ```bash
   pip install requests beautifulsoup4

2. Run the script:
   ```bash
   python main.py

## 📂 Project Structure
```
imdb-movie-picker/
├── Dockerfile
├── main.py
└── README.md
```

## 📝 Sample Output
```
Downloading Top 250 list... please wait...
Successfully found 250 movies.

🍿 Suggestion: The Godfather (1972) - Rating: 9.2

Hit [Enter] for another movie, or type 'q' to quit:
