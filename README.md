# AI Document Intelligence 📄🤖

A beginner-built Retrieval-Augmented Generation (RAG) system that answers questions about PDF documents using semantic search, text embeddings, and Google Gemini.

This project implements the core RAG pipeline step by step to understand how document ingestion, chunking, embeddings, retrieval, and LLM-based answer generation work together.

## 🚀 What Does This Project Do?

This project lets you ask questions about a PDF document and receive answers generated using information retrieved from that document.

For example, you can provide a college booklet and ask:

- What subjects are taught in the first year?
- What is the course structure?
- What documents are required for verification?

The application extracts text from your PDF, splits it into chunks, finds relevant chunks using semantic similarity, and sends those chunks with your question to Google Gemini.

## ⚙️ How the Project Works

1. **PDF ingestion:** Extracts text using `pypdf`.
2. **Text chunking:** Divides extracted text into smaller, overlapping pieces.
3. **Embeddings:** Converts text into numerical vectors using Sentence Transformers.
4. **Semantic retrieval:** Ranks chunks using cosine similarity.
5. **LLM generation:** Sends the retrieved context and question to Google Gemini.
6. **Answer generation:** Displays a natural-language answer based on the supplied context.

## 🛠️ Tech Stack

- Python 3.13
- pypdf
- NumPy
- Sentence Transformers
- `all-MiniLM-L6-v2`
- Google Gemini API
- Git and GitHub

## 📁 Project Structure

```text
AI-Document-Intelligence/
├── data/
│   └── documents/
├── src/
│   ├── ingestion/
│   │   └── pdf_loader.py
│   ├── chunking/
│   │   └── chunker.py
│   ├── embeddings/
│   │   └── embedder.py
│   ├── retrieval/
│   │   └── vector_store.py
│   └── generation/
│       └── llm.py
├── tests/
│   └── test_retrieval.py
├── ask_pdf.py
├── test_gemini.py
├── requirements.txt
├── .gitignore
└── README.md
```

## 💻 Getting Started — Windows

Follow these steps in order. You do not need to open every Python file manually to run the application.

### Step 1: Install the Required Software

Install the following:

- **Python 3.13:** https://www.python.org/downloads/
- **Git:** https://git-scm.com/downloads
- **Visual Studio Code (recommended):** https://code.visualstudio.com/

During Python installation, enable **Add Python to PATH** if that option is available.

To check whether Python is installed, open **Windows PowerShell** or the VS Code terminal and run:

```powershell
py -3.13 --version
```

You should see a Python 3.13 version number.

### Step 2: Download the Project from GitHub

You can do this using either method.

**Option A — Using Git**

1. Open Windows PowerShell or the terminal inside VS Code.
2. Navigate to the folder where you want to store the project.
3. Run these commands, replacing `YOUR_USERNAME` with your GitHub username:

```powershell
git clone https://github.com/YOUR_USERNAME/AI-Document-Intelligence.git
cd AI-Document-Intelligence
```

**Option B — Without Git**

1. Open this repository on GitHub in your web browser.
2. Click the green **Code** button.
3. Select **Download ZIP**.
4. Extract the ZIP file.
5. Open the extracted project folder in VS Code.
6. In VS Code, select **Terminal → New Terminal**.

### Step 3: Install the Python Libraries

**Where:** Run this command in the terminal opened at the project root — the folder containing `ask_pdf.py` and `requirements.txt`.

```powershell
py -3.13 -m pip install -r requirements.txt
```

This installs the libraries required by the project.

The first run may take some time because Sentence Transformers downloads its embedding model.

### Step 4: Add Your PDF Document

The original PDF used during development is not included in the public repository.

1. Open the project folder in File Explorer or VS Code.
2. Inside the project root, create a folder named `data` if it does not exist.
3. Inside `data`, create another folder named `documents`.
4. Copy your PDF into `data/documents/`.
5. Rename the PDF to:

```text
ANYTHING YOU WANT BUT SPECIFY THE SAME IN THE CODE TOO!!!.
```

Your folder structure should look like this:

```text
AI-Document-Intelligence/
├── data/
│   └── documents/
│       └── 1st Year CSIT Booklet.pdf
├── ask_pdf.py
└── requirements.txt
```

You can use another PDF, but if its filename or location differs, update the `pdf_path` variable inside `ask_pdf.py` and `tests/test_retrieval.py` accordingly.

Use documents you are permitted to process and share.

### Step 5: Get a Google Gemini API Key

The project uses the Gemini API to generate answers.

1. Open Google AI Studio: https://aistudio.google.com/
2. Sign in with your Google account.
3. Find the option to create or obtain an API key.
4. Create a key and keep it private.

**Where to enter the key:** Open the VS Code terminal or Windows PowerShell in which you will run the project.

```powershell
$env:GEMINI_API_KEY = "YOUR_API_KEY"
```

Replace `YOUR_API_KEY` with your actual key. Keep the quotation marks.

This command sets the key for the current PowerShell session. If you close that terminal, you will need to set it again in the new session.

**Important:** Never paste your real API key into Python source files, your README, screenshots, or GitHub commits.

### Step 6: Run the Application

**Where:** In the VS Code terminal or PowerShell, make sure the current directory is the project root containing `ask_pdf.py`.

Run:

```powershell
py -3.13 ask_pdf.py
```

When prompted, type a question about your PDF and press Enter.

The application will retrieve relevant text chunks, send the context and question to Gemini, and display the generated answer.

### Step 7: Run the Individual Tests

You can test individual components separately from the same project-root terminal.

**Test PDF extraction and retrieval:**

```powershell
py -3.13 -m tests.test_retrieval
```

**Test the Gemini API connection:**

```powershell
py -3.13 test_gemini.py
```

The Gemini test requires a valid `GEMINI_API_KEY` in the current terminal session.

## 📌 Current Features

- PDF text extraction
- Overlapping text chunking
- Text embeddings using Sentence Transformers
- Cosine-similarity-based semantic retrieval
- Retrieval of the top matching chunks
- Gemini-powered answer generation
- Basic instructions to answer using the supplied document context

## ⚠️ Current Limitations

This is an early-stage learning project.

- Retrieval quality depends on the chunks retrieved.
- The application currently retrieves the top three chunks for answer generation.
- Relevant information can be missed when the retrieval step fails to find it.
- Answers may be incomplete or incorrect.
- Embeddings are recalculated for document chunks when a question is asked.
- Page-level citations and automated answer evaluation are not yet implemented.

## 🗺️ Future Improvements

- Improved chunking and retrieval accuracy
- Reuse of previously generated embeddings
- Page-level source references
- Support for multiple documents
- Automated tests and answer evaluation
- A simple user interface

## 🎯 Project Goal

The goal is to understand the fundamentals of Retrieval-Augmented Generation by implementing the pipeline incrementally, rather than relying on a high-level RAG framework.

This project will evolve as new concepts are learned and implemented.

## 👨‍💻 Author

**YOUR NAME**

GitHub: https://github.com/YOUR_USERNAME

---

⭐ If you find this project interesting, feel free to explore the code and follow its development.
