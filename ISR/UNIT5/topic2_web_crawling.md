# Web Crawling — 10 Marks (ELI5)

## 1. What is Web Crawling?

**Web crawling** is the automated process of systematically browsing the World Wide Web, downloading webpage contents, and discovering hyperlinks to other pages using a software program called a **web crawler, spider, or bot**.

### ELI5 (Explain Like I'm 5)
Imagine you are a librarian who visits every shelf in an enormous library. You read each book's title, summarize its key ideas, note citations pointing to other books, and add those recommended books to your reading list. A web crawler does the exact same thing, but across billions of pages on the Internet.

> **Example:** Googlebot visits a tutorial on Python, identifies hyperlinks pointing to Java and C++ tutorials, and appends those URLs to its queue for upcoming visits.

---

## 2. Architecture of a Web Crawler

```text
                     Seed URLs
                         │
                         ▼
             ┌───────────────────────┐
             │ URL Frontier (Queue)  │ ◄─────────────────────────┐
             └───────────┬───────────┘                           │
                         │ Next URL                              │
                         ▼                                       │
             ┌───────────────────────┐                           │
             │ URL Scheduler &       │                           │
             │ Politeness Controller │                           │
             └───────────┬───────────┘                           │
                         │ Polite Fetch Request                  │
                         ▼                                       │
             ┌───────────────────────┐                           │
             │  Downloader / Fetcher │                           │
             └───────────┬───────────┘                           │
                         │ HTML Content                          │
                         ▼                                       │
             ┌───────────────────────┐                           │
             │ Parser & Link         │                           │
             │ Extractor             │                           │
             └─────┬───────────┬─────┘                           │
                   │           │                                 │
     Extracted Text│           │ Discovered Hyperlinks           │
                   ▼           ▼                                 │
             ┌───────────┐ ┌───────────────────────┐             │
             │ Document  │ │ Duplicate Detection   │             │
             │ Storage   │ │ & URL Filter          │─────────────┘
             └───────────┘ └───────────────────────┘
```

### Core Architecture Components:
1. **Seed URLs:** Initial starting list of authoritative webpages.
2. **URL Frontier / Queue:** Data structure storing prioritized URLs waiting to be fetched.
3. **URL Scheduler & Politeness Controller:** Regulates crawl frequency per domain to avoid overloading web servers (`robots.txt` compliance).
4. **Downloader (Fetcher):** Dispatches HTTP/HTTPS requests to download HTML pages.
5. **Parser & Link Extractor:** Extracts plain text, metadata, and embedded hyperlinks (`<a href="...">`).
6. **Duplicate Elimination & Storage:** Discards already-visited URLs, caches downloaded pages, and enqueues new candidate URLs back into the Frontier.

---

## 3. Working of a Web Crawler (Step-by-Step)

```text
Step 1: Seed Initialization ──► Provide initial list of URLs (e.g., www.example.com)
Step 2: Enqueue Frontier    ──► Push seed URLs into the URL Frontier
Step 3: Schedule Next URL   ──► Scheduler picks next URL based on priority & politeness
Step 4: Fetch Webpage       ──► Downloader issues HTTP/HTTPS GET request to target server
Step 5: Parse Document      ──► Extract text, document metadata, and outbound hyperlinks
Step 6: Discover & Filter   ──► Discard visited/duplicate links; check robots.txt
Step 7: Enqueue New URLs    ──► Add fresh unvisited URLs back into the URL Frontier
Step 8: Store & Repeat      ──► Save content to repository and repeat until threshold met
```

### Practical Loop Example:
Suppose the crawler visits **Page A**, which has links to **Page B** and **Page C**.
* It downloads and stores **A**.
* It adds **B** and **C** to the queue.
* When downloading **B**, if **B** links back to **A**, the crawler inspects its visited-URL hash table/filter and drops **A**, preventing infinite loops.

---

## 4. Crawling Strategies

A crawling strategy determines the order in which URLs in the Frontier are selected and crawled.

```text
                     Crawling Strategies
                              │
     ┌────────────────┬───────┴────────┬─────────────────┐
     ▼                ▼                ▼                 ▼
Breadth-First    Depth-First     Priority-Based       Focused
  (BFS)            (DFS)           Crawling          Crawling
```

### 1. Breadth-First Crawling (BFS)
* **Approach:** Explores all neighbor links at the current depth before venturing deeper.
* **Traversal Order:** Level by level ($A \rightarrow B, C \rightarrow D, E$).
* **Advantage:** Discovers high-level, authoritative pages located close to the seed site first.
* **Data Structure:** Standard First-In-First-Out (FIFO) Queue.

### 2. Depth-First Crawling (DFS)
* **Approach:** Follows a single chain of links deep into a website before backtracking.
* **Traversal Order:** Deep branch traversal ($A \rightarrow B \rightarrow D$, then back to $A \rightarrow C$).
* **Advantage:** Good for deeply structured hierarchical domains.
* **Risk:** High chance of getting stuck in deep link paths or crawler traps.
* **Data Structure:** Last-In-First-Out (LIFO) Stack.

### 3. Priority-Based Crawling
* **Approach:** Assigns priority scores to URLs based on importance metrics such as PageRank, backlink count, domain authority, or update frequency.
* **Example:** Major news outlets or Wikipedia entries are crawled before personal blogs.
* **Advantage:** Allocates network bandwidth and computational resources to the highest-quality pages.
* **Data Structure:** Priority Queue.

### 4. Focused (Topic-Specific) Crawling
* **Approach:** Evaluates page relevance to a specialized domain/topic before queuing outbound links.
* **Example:** A medical crawler retains only healthcare and biomedical URLs, ignoring entertainment sites.
* **Advantage:** Vastly conserves disk storage and bandwidth by avoiding non-relevant web space.

---

## 5. Comparison of Crawling Strategies

| Strategy | Traversal Order | Data Structure | Best Used For | Key Limitation |
| :--- | :--- | :--- | :--- | :--- |
| **BFS** | Level-by-level | Queue (FIFO) | Broad web coverage | Can explore many shallow, low-value pages |
| **DFS** | Deep branch path | Stack (LIFO) | Deep hierarchical sites | Vulnerable to infinite loops and crawler traps |
| **Priority** | By importance score | Priority Queue | High-value, authoritative discovery | Computationally intensive scoring |
| **Focused** | By topical relevance | Classifier + Queue | Vertical search engines (Medical, Legal) | Misses out-of-domain cross-links |

---

## 6. Challenges of Web Crawling

1. **Vast Scale of the Web:** Billions of dynamic pages require petabytes of storage, immense bandwidth, and distributed architectures.
2. **Duplicate & Near-Duplicate Content:** Mirrors, syndicated news, and URL aliases waste valuable crawling capacity without adding new data.
3. **Dynamic & Client-Side Content:** Heavy JavaScript frameworks (React, Angular) require headless browser rendering to execute and expose content.
4. **Spider Traps / Crawler Traps:** Dynamically generated infinite URLs (e.g., perpetual calendar dates, circular directory paths) consume crawler memory indefinitely.
5. **Politeness & Server Load:** Aggressive crawling can cause denial-of-service (DoS) on target servers. Crawlers must abide by delay directives in `robots.txt`.
6. **Content Churn (Dynamic Updates):** Pages change rapidly; crawlers must determine optimal revisit intervals (recrawling) without overwhelming sites.
7. **Access Barriers:** Login walls, CAPTCHAs, IP rate-limits, and paywalls restrict access to valuable pages.

---

## 7. Conclusion

**Web crawling** is the backbone of modern Information Retrieval systems, automating the discovery and extraction of web documents. Utilizing modular architectures consisting of the URL Frontier, Politeness Controller, Downloader, and Parser, crawlers navigate the web using strategies like BFS, DFS, priority, or focused crawling. Effective crawlers must mitigate real-world obstacles including scale, spider traps, duplicate data, and server rate limits.

---

## 8. Quick Revision for Exams

* **Definition:** Automated discovery and downloading of web pages across the Internet.
* **Core Pipeline:** Seed URLs $\rightarrow$ URL Frontier $\rightarrow$ Scheduler $\rightarrow$ Downloader $\rightarrow$ Parser $\rightarrow$ Storage $\rightarrow$ Loop.
* **Strategies:**
  * **BFS:** Level-wise, broad coverage.
  * **DFS:** Deep paths, stack-based.
  * **Priority:** Importance/PageRank driven.
  * **Focused:** Subject/topic restricted.
* **Top Challenges:** Scale, duplicates, dynamic JavaScript, crawler traps, `robots.txt` politeness.

### 🧠 One-line memory trick
> **A web crawler is like a tourist: it picks an attraction, visits it, takes notes, asks for local recommendations, queues them up, and moves to the next spot!**
