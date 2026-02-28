<h1>📰 Web Text Analysis & Sentiment Pipeline</h1>

<p>
A Python-based data processing pipeline that scrapes article content from URLs,
cleans and tokenizes the text using NLP techniques, and computes sentiment,
readability, and linguistic metrics. The final structured output is exported to an Excel file.
</p>

<div class="section">
    <span class="badge">Python</span>
    <span class="badge">BeautifulSoup</span>
    <span class="badge">NLTK</span>
    <span class="badge">Pandas</span>
    <span class="badge">Sentiment Analysis</span>
</div>

<hr>

<div class="section">
<h2>🚀 Features</h2>
<ul>
    <li>📥 Reads input URLs from an Excel file</li>
    <li>🌐 Extracts article title and content using web scraping</li>
    <li>🧹 Cleans and preprocesses text (tokenization, stopword removal, punctuation filtering)</li>
    <li>😊 Computes sentiment scores using VADER</li>
    <li>📊 Calculates readability and linguistic metrics</li>
    <li>📤 Exports structured results to Excel</li>
    <li>🚫 Supports exclusion of specific URLs</li>
</ul>
</div>

<hr>

<div class="section">
<h2>🧠 System Workflow</h2>

<pre>
Input Excel (URLs)
        │
        ▼
Web Scraping (BeautifulSoup)
        │
        ▼
Text Cleaning & Tokenization (NLTK)
        │
        ▼
Sentiment & Readability Analysis
        │
        ▼
Structured Output (Excel)
</pre>

</div>

<hr>

<div class="section">
<h2>📁 Project Structure</h2>

<pre>
text-analysis-project/
│
├── main.py
├── Input.xlsx
├── Output Data Structure.xlsx
├── requirements.txt
└── README.html
</pre>

</div>

<hr>

<div class="section">
<h2>⚙️ Installation</h2>

<h3>1️⃣ Clone Repository</h3>
<pre>
git clone https://github.com/your-username/text-analysis-project.git
cd text-analysis-project
</pre>

<h3>2️⃣ Create Virtual Environment</h3>
<pre>
python -m venv venv
source venv/bin/activate   (Linux/Mac)
venv\Scripts\activate      (Windows)
</pre>

<h3>3️⃣ Install Dependencies</h3>
<pre>
pip install -r requirements.txt
</pre>

</div>

<hr>

<div class="section">
<h2>▶️ Run the Script</h2>

<pre>
python main.py
</pre>

<p>
The script will:
</p>
<ul>
    <li>Load URLs from <code>Input.xlsx</code></li>
    <li>Scrape article content</li>
    <li>Process and analyze text</li>
    <li>Generate <code>Output Data Structure.xlsx</code></li>
</ul>

</div>

<hr>

<div class="section">
<h2>📥 Input Format</h2>

<p><strong>Input.xlsx</strong> must contain:</p>

<pre>
URL_ID | URL
----------------------------
1      | https://example.com/article1
2      | https://example.com/article2
</pre>

</div>

<hr>

<div class="section">
<h2>📤 Output Columns</h2>

<ul>
    <li>URL_ID</li>
    <li>URL</li>
    <li>Positive Score</li>
    <li>Negative Score</li>
    <li>Polarity Score</li>
    <li>Subjectivity Score</li>
    <li>Average Sentence Length</li>
    <li>Percentage of Complex Words</li>
    <li>Fog Index</li>
    <li>Average Word Length</li>
    <li>Complex Word Count</li>
    <li>Word Count</li>
    <li>Syllable Per Word</li>
    <li>Personal Pronouns</li>
</ul>

</div>

<hr>

<div class="section">
<h2>🛠 Technology Stack</h2>
<ul>
    <li>Python</li>
    <li>Requests</li>
    <li>BeautifulSoup (bs4)</li>
    <li>NLTK</li>
    <li>Pandas</li>
    <li>Excel (OpenPyXL)</li>
</ul>
</div>

<hr>

<div class="section">
<h2>🔐 Error Handling</h2>
<ul>
    <li>Handles missing or invalid URLs</li>
    <li>Skips excluded URLs</li>
    <li>Validates extracted article structure</li>
</ul>
</div>

</body>
</html>
