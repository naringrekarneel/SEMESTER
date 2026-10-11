# Search Engine Architecture — 10 Marks

## 1. Introduction

A **search engine** is a software system that searches the World Wide Web for relevant information based on a user's query and displays the most relevant results in ranked order.

* **Examples:** Google, Bing, Yahoo, DuckDuckGo.
* The core architecture consists of four major components:
  1. **Web Crawling**
  2. **Indexing**
  3. **Query Processing**
  4. **Ranking**

---

## 2. Architecture of a Search Engine

```text
       Web Pages / Internet
                │
                ▼
       ┌──────────────────┐
       │   Web Crawler    │ ◄─── Seed URLs
       │     (Spider)     │
       └────────┬─────────┘
                │ Downloads Pages
                ▼
       ┌──────────────────┐
       │     Indexer      │
       └────────┬─────────┘
                │ Builds Index
                ▼
       ┌──────────────────┐
       │ Search Index /   │
       │ Inverted Index   │
       └────────┬─────────┘
                │ Look up terms
                ▼
       ┌──────────────────┐
       │ Query Processing │ ◄─── User Query
       └────────┬─────────┘
                │ Matching Documents
                ▼
       ┌──────────────────┐
       │ Ranking Engine   │ (PageRank, Relevance, ML)
       └────────┬─────────┘
                │ Ranked List
                ▼
       ┌──────────────────┐
       │  Results Display │
       │     (SERP)       │ ────► Final Ranked Results to User
       └──────────────────┘
```

### High-Level Components Overview:
1. **Web Crawler:** Discovers and downloads web pages.
2. **Indexer:** Processes pages and builds an inverted index.
3. **Search Index / Database:** Stores searchable document information.
4. **Query Processing & Ranking:** Interprets the query and ranks matching pages.
5. **Search Results Page (SERP):** Displays ranked results to the user.

---

## 3. Components of Search Engine Architecture

### 1. Web Crawler (Spider / Bot)
A **web crawler** is an automated program that discovers and collects web pages from the Internet.
* **Seed URLs:** Starts with a list of known URLs called seed URLs.
* **Downloading:** Fetches pages from web servers via HTTP/HTTPS.
* **Link Extraction:** Parses downloaded pages and extracts all hyperlinks (`<a href="...">`).
* **URL Queue (Frontier):** Adds newly discovered URLs to a queue for future crawling.
* **Policies:** Follows crawling rules, such as `robots.txt`, and manages crawl politeness and frequency.

> **Example:** A crawler visits a webpage about Python tutorials, finds links to other programming pages, and queues them for downloading.

---

### 2. Indexing
**Indexing** organizes the collected web pages into a searchable structure so that information can be retrieved in milliseconds.
* **Parsing:** The downloaded pages are parsed and plain text is extracted.
* **Cleaning:** HTML tags, scripts, duplicate content, and stop words are handled or removed.
* **Tokenization & Normalization:** Identifies distinct terms and normalizes them (lowercasing, stemming/lemmatization).
* **Inverted Index Creation:** Maps each distinct term to a posting list containing document IDs and positions.

#### Example of an Inverted Index:

| Term | Document IDs (Posting List) |
| :--- | :--- |
| **Python** | D1, D3, D5 |
| **Java** | D2, D3 |
| **Programming** | D1, D2, D4 |

> When a user searches for *"Python"*, the search engine directly retrieves documents **D1, D3, and D5** without scanning billions of web pages sequentially.

---

### 3. Query Processing
**Query Processing** handles user search requests and prepares them for index lookup.
* **User Input:** Receives queries in natural language or keywords.
* **Tokenization & Normalization:** Converts terms to standard forms (e.g., lowercasing).
* **Spell Check & Query Expansion:** Corrects typographical errors and finds synonyms or related terms.
* **Index Lookup:** Retrieves candidate document IDs matching the query terms using Boolean or vector matching.
* **Context Awareness:** Accounts for language, location, device, and user intent.

> **Example:** For the query *"best Python tutrials"*, the engine corrects the spelling to *"tutorials"*, identifies the core concepts, and fetches matching documents.

---

### 4. Ranking
The **Ranking Engine** evaluates retrieved candidate documents and arranges them from most relevant to least relevant.

Key ranking signals include:
* **Relevance:** How closely document content matches query terms (TF-IDF, BM25, semantic embeddings).
* **Link Analysis (Authority):** Structural importance based on inbound links (e.g., Google's PageRank algorithm).
* **Content Quality & Trust:** Authority of the domain, depth, and reliability.
* **Freshness:** How recently the content was updated (crucial for news/trending topics).
* **User Context:** Geolocation, search history, language, and personalization.

> **Example:** For *"latest AI breakthroughs"*, recently published research and reputable news sites will rank higher than an outdated blog post.

---

### 5. Search Results Display (SERP)
The search engine presents ranked documents on the **Search Engine Results Page (SERP)**.
* **Result Snippets:** Displays page title, URL breadcrumb, and relevant highlighted text snippets.
* **Rich Elements:** May include Knowledge Panels, images, videos, maps, and direct answer cards.
* **User Interaction:** Lets users click links, paginate, or refine their query.

---

## 4. Working of a Search Engine (Step-by-Step)

```text
Step 1: Crawl ──► Spider downloads pages starting from Seed URLs.
Step 2: Index ──► Indexer parses content and constructs an Inverted Index.
Step 3: Query ──► User submits a query via the search interface.
Step 4: Process ─► Query processor normalizes text and queries the index.
Step 5: Rank ───► Ranking algorithms score candidate pages using multiple signals.
Step 6: Display ─► SERP renders the ranked list of results to the user.
```

---

## 5. Summary & Key Takeaways

| Component | Primary Function | Output / Artifact |
| :--- | :--- | :--- |
| **Web Crawler** | Discovers & downloads web pages | Raw HTML Documents |
| **Indexer** | Parses & structures documents | Inverted Index & Metadata |
| **Query Processor** | Interprets user query & fetches candidates | Candidate Document Set |
| **Ranking Engine** | Scores and orders documents | Ranked List of Documents |
| **SERP Display** | Formats and renders results | Final Search Interface |

---

## 6. Conclusion

A search engine architecture combines **web crawling, indexing, query processing, and ranking** to efficiently locate and present information from billions of web pages. These components work together to provide fast, accurate, and relevant search results to users.

### ⭐ Exam keywords
**Web Crawler → Seed URLs → Inverted Index → Posting List → Query Processing → Tokenization → Ranking Engine → PageRank → BM25 → SERP**

### 🧠 One-line memory trick
> **Crawl to collect, Index to organize, Process to understand, Rank to sort, and Display to serve.**
