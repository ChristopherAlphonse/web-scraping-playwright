# YouTube Data Extraction with Playwright and AgentQL

This repository demonstrates how to use Playwright and AgentQL with Python to interact with YouTube, automate browsing, and extract data such as video details, descriptions, and comments.

---

## Features

- **YouTube Automation with Playwright**: Automate interactions like searching, clicking videos, and scrolling.
- **Data Extraction with AgentQL**: Use AI-driven queries to simplify data extraction from web elements.
- **Logging and Debugging**: Includes detailed logging for debugging and performance tracking.

---

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Playwright
- AgentQL

---

### Installation

1. **Clone the Repository**:

   ```sh
   git clone https://github.com/ChristopherAlphonse/youtube-data-extraction.git
   cd youtube-data-extraction
   ```

2. **Dependencies:**

   ```sh
   pip install -r requirements.txt && playwright install
   ```

   **Running the Script:**

**Run the script:**

```sh
python youtube_scrape.py
```

### Expect to see:

1. Enter a YouTube search query when prompted in the shell.
2. The script will:
   Perform a YouTube search.
   Open the first video from the results.
   Extract and log video details, descriptions, and comments.
