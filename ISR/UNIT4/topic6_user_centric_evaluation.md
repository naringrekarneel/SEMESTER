# User-Centric Evaluation in Information Retrieval — 10 Marks

## 1. Definition

**User-Centric Evaluation** in Information Retrieval (IR) evaluates a search system from the **user's point of view**, rather than looking only at algorithmic metrics such as Precision, Recall, MAP, or NDCG.

The main question is:
> **“Does the search system actually help the user accomplish their information need?”**

A search engine may have good ranking metrics but still provide a poor user experience if results are difficult to understand, slow to access, or require many searches.

---

## 2. Why User-Centric Evaluation is Needed

Traditional IR evaluation mainly focuses on **system performance**.

For example:
* Precision
* Recall
* F-measure
* MAP
* MRR
* NDCG

These metrics tell us how well documents are retrieved or ranked.

However, they may not fully capture:
* User satisfaction
* Ease of use
* Search effort
* Time required to find information
* Whether the user's task was successfully completed

Therefore, **user-centric evaluation complements traditional IR metrics**.

---

## 3. Important User-Centric Factors

### 1. User Satisfaction
Measures whether users are satisfied with the search results and overall search experience.
Users can be asked to rate the system using:
* Surveys
* Questionnaires
* Ratings
* Interviews

Example:
> “How satisfied were you with the search results?”
A rating from 1 to 5 can be collected.

### 2. Task Success
Measures whether the user was able to **complete the intended task successfully**.

Example Task:
> Find a research paper about CNN architectures.

Evaluation checks whether the user successfully found a suitable paper.
A system with a high task-success rate is helping users accomplish their goals.

### 3. Search Time
Measures the time required to find satisfactory information.
$$
Search\ Time = Time_{end} - Time_{start}
$$
A shorter time can indicate more efficient interaction, although speed should be considered along with correctness and satisfaction.

### 4. User Effort
Measures how much effort users must spend.
Indicators can include:
* Number of queries
* Number of clicks
* Number of reformulations
* Number of pages opened
* Number of interaction steps

For example, if one system requires:
> 2 queries and 3 clicks

while another requires:
> 8 queries and 15 clicks

the interaction burden differs substantially.

### 5. Click Behavior
User interactions with search results can provide useful evidence.
Examples:
* Which result was clicked?
* How many results were clicked?
* Did the user return to the results page?
* How long did the user stay on a result?

These behaviors can help estimate whether results were useful.

### 6. Search Satisfaction
After completing a search, users can be asked:
> “Did you find what you were looking for?”
or
> “How useful were the results?”

This captures subjective quality that ranking metrics may miss.

---

## 4. Methods of User-Centric Evaluation

### 1. User Surveys
Users complete questionnaires about:
* Satisfaction
* Ease of use
* Result quality
* Trust
* Usefulness

**Example (A 1–5 scale):**
| Rating | Meaning |
| ---: | :--- |
| 1 | Very dissatisfied |
| 2 | Dissatisfied |
| 3 | Neutral |
| 4 | Satisfied |
| 5 | Very satisfied |

### 2. User Interviews
Researchers directly ask users about their experience.
Questions can include:
> “What was difficult about the search?”
> “Did the results match what you expected?”

Interviews provide detailed qualitative feedback.

### 3. User Studies / Experiments
A group of users is asked to perform predefined search tasks.
Example:
> Find three reliable sources about renewable energy within 5 minutes.

Researchers measure:
* Success rate
* Search time
* Number of queries
* Clicks
* User satisfaction

### 4. A/B Testing
Two versions of a search system are tested with users.

```text
Users
  ↓
 ┌───────────┬───────────┐
 ↓                       ↓
System A                System B
 ↓                       ↓
Measure behavior and satisfaction
          ↓
      Compare results
```

For example, one version may use a new ranking algorithm while another uses the old algorithm.

### 5. Log Analysis
Search logs can be analyzed to understand real user behavior.
Logs may contain:
* Queries
* Clicks
* Result positions
* Query reformulations
* Session duration
* Abandonment behavior

This allows evaluation using real-world usage data.

### 6. Think-Aloud Studies
Users perform search tasks while explaining what they are thinking.
Example:
> “I expected this result to answer my question, so I'm opening it.”

This helps researchers understand **why users make particular search decisions**.

---

## 5. User-Centric Evaluation Metrics

| Metric | What it Measures |
| :--- | :--- |
| **Task Success Rate** | Percentage of tasks successfully completed |
| **Search Time** | Time needed to find useful information |
| **Number of Queries** | Search effort/reformulation |
| **Click Count** | Interaction effort |
| **Session Duration** | Time spent during search |
| **User Satisfaction** | User's subjective experience |
| **Abandonment Rate** | Searches ended without useful interaction |
| **Query Reformulation Rate** | How often users modify queries |

---

## 6. Example

Suppose two search systems, **A** and **B**, are tested by 100 users.

| Measure | System A | System B |
| :--- | ---: | ---: |
| Task success | 90% | 82% |
| Average search time | 2.5 min | 4 min |
| Average queries | 2 | 4 |
| Satisfaction | 4.4/5 | 3.6/5 |

This evaluation considers not just document ranking, but **what happened to the users while searching**.
The purpose is to understand how system behavior affects the user's ability to complete tasks.

---

## 7. User-Centric vs System-Centric Evaluation

| System-Centric Evaluation | User-Centric Evaluation |
| :--- | :--- |
| Focuses on retrieval performance | Focuses on user experience |
| Uses Precision, Recall, MAP, NDCG | Uses satisfaction, success, time, effort |
| Often uses benchmark datasets | Often uses real users |
| Measures ranking/retrieval quality | Measures usefulness and usability |
| More objective and controlled | Includes subjective user feedback |
| May not capture task difficulty | Directly evaluates task completion |

---

## 8. Advantages

1. **Measures Real User Experience:** It determines whether the system is genuinely useful to users.
2. **Identifies Usability Problems:** Users may struggle with Query formulation, Navigation, Result interpretation, or Interface design.
3. **Measures Task Completion:** It shows whether users can actually accomplish their goals.
4. **Captures Subjective Satisfaction:** A system can be technically strong but frustrating to use; user studies can reveal that.
5. **Helps Improve Search Interfaces:** Findings can guide improvements in Ranking, Interface design, Query suggestions, Filters, or Result presentation.

---

## 9. Limitations

1. **Time-Consuming:** User studies require planning, participants, and analysis.
2. **Expensive:** Large-scale studies can require significant resources.
3. **Subjective:** Different users may have different expectations and preferences.
4. **Small Samples:** A study with a limited number of users may not represent the entire user population.
5. **Experimental Bias:** Users may behave differently when they know they are being observed.

---

## 10. Overall Evaluation Process

```text
             Define User Tasks
                    ↓
             Recruit Users
                    ↓
            Users Perform Search
                    ↓
        ┌───────────┼───────────┐
        ↓           ↓           ↓
     Success       Time       Effort
        ↓           ↓           ↓
        └───────────┼───────────┘
                    ↓
          Satisfaction Survey
                    ↓
             Analyze Results
                    ↓
        Improve Search System
```

---

## 11. Example of User-Centric Evaluation

Suppose an e-commerce search system is being evaluated.

**Task:**
> Find a gaming laptop under ₹80,000.

Researchers can measure:
* Did the user find a suitable laptop?
* How long did it take?
* How many searches were performed?
* How many products were opened?
* Did the user successfully complete the task?
* Was the user satisfied?

This provides a much richer evaluation than simply calculating Precision or NDCG.

---

## 12. Conclusion

**User-Centric Evaluation** evaluates an Information Retrieval system according to its **impact on real users and their information-seeking tasks**.

It considers factors such as **task success, search time, user effort, clicks, query reformulation, satisfaction, and usability**. Methods such as **surveys, interviews, user experiments, A/B testing, log analysis, and think-aloud studies** can be used.

Traditional IR metrics answer:
> **“How good are the retrieved results?”**

User-centric evaluation additionally asks:
> **“Did the user actually find what they needed, efficiently and satisfactorily?”**

### ⭐ Exam keywords
**User-Centric Evaluation → User Satisfaction → Task Success → Search Time → User Effort → Clicks → Query Reformulation → Surveys → User Studies → A/B Testing → Log Analysis → Usability**

### 🧠 One-line memory trick
> **System-centric = How well does the search algorithm work?**
> **User-centric = How well does the search system work for the human?**
