# Topic 3: Communication Protocols in Multi-Agent Systems (MAS) — 10 Marks

## 1. ELI5 — What are Communication Protocols in MAS?

Imagine an international emergency rescue team consisting of a French doctor, a German firefighter, and a Japanese drone engineer:
* If the doctor shouts medical instructions in French, the firefighter might not understand.
* Even if they all speak English, if the doctor says *"Patient needs 50 units"*, without specifying whether that means insulin or saline, medical catastrophe follows.

To work effectively, the team needs:
1. A **shared common language** (Syntax).
2. A **shared dictionary of concepts** (Ontology / Semantics).
3. **Structured rules of engagement** (Protocol: *"When I request help, you must confirm or decline within 10 seconds"*).

In a Multi-Agent System (MAS), **Communication Protocols** are the formal rules, message syntaxes, and semantic standards that allow heterogeneous AI agents to exchange knowledge, negotiate tasks, and coordinate joint actions reliably.

```text
┌─────────────────┐       Structured Message (Envelope)       ┌─────────────────┐
│ AGENT A: SENDER │ ────────────────────────────────────────► │ AGENT B: RECVR  │
│ Diagnostician   │ ◄──────────────────────────────────────── │ Pharmacist      │
└─────────────────┘              Response Message             └─────────────────┘
```

### Exam Definition:
> **Communication Protocols in MAS** are standardized sets of conventions governing the formatting, semantic interpretation, sequencing, and delivery of messages between autonomous agents to enable coordination, negotiation, and distributed problem-solving.

---

## 2. Theoretical Foundation: Speech Act Theory

Unlike simple data-serialization formats (like raw CSV or database rows), agent communication is rooted in linguistics—specifically **Speech Act Theory** (developed by philosophers John Austin and John Searle).

Speech Act Theory posits that **utterances are actions** (termed *performatives*). When an agent sends a message, it is not merely moving bytes; it is attempting to alter the mental state of the receiving agent:
1. **Locutionary Act:** The physical act of uttering the words (transmitting the raw byte stream).
2. **Illocutionary Act:** The intended communicative force or purpose behind the utterance (requesting, promising, informing, ordering).
3. **Perlocutionary Act:** The actual consequence or psychological effect achieved in the listener (the receiver agreeing to perform the action).

---

## 3. Anatomy of an Agent Message: The FIPA-ACL Envelope

In standardized MAS architectures, every communication is wrapped inside a structured message envelope containing both **metadata** and **content**.

```text
┌────────────────────────────────────────────────────────────────────────┐
│ MESSAGE ENVELOPE (FIPA-ACL Standard)                                   │
├────────────────────────────────────────────────────────────────────────┤
│ • Performative   : REQUEST                                             │
│ • Sender         : agent_cardiology_ai                                 │
│ • Receiver       : agent_pharmacy_inventory                            │
│ • Content        : (check-availability :drug "Aspirin" :dosage "100mg")│
│ • Language       : KIF (Knowledge Interchange Format) / JSON           │
│ • Ontology       : medical-pharmacology-v2                             │
│ • Conversation-ID: conv_heart_emergency_9481                           │
│ • Reply-With     : msg_req_01                                          │
│ • In-Reply-To    : [None]                                              │
└────────────────────────────────────────────────────────────────────────┘
```

### Core Message Fields:
| Field | Purpose in MAS | Exam Importance |
| :--- | :--- | :--- |
| **Sender** | Identity address of the transmitting agent | Guarantees traceability |
| **Receiver** | Target recipient agent(s) | Supports unicast and multicast broadcasts |
| **Performative** | The communicative act indicating **intent** | Distinguishes a command (`request`) from a statement (`inform`) |
| **Content** | The payload carrying the actual information | The domain data being transferred |
| **Language** | Syntax used to encode the payload | e.g., JSON, XML, Prolog, KIF |
| **Ontology** | Shared conceptual taxonomy giving words precise meaning | Eliminates vocabulary mismatch (e.g., "bank" = river vs. finance) |
| **Conversation-ID** | Unique tracking token across multi-turn dialogues | Links requests to matching responses |

---

## 4. Agent Communication Languages (ACL) & Standards

```text
                        AGENT COMMUNICATION PROTOCOLS
                                      │
     ┌────────────────────────────────┼────────────────────────────────┐
     ▼                                ▼                                ▼
[FIPA-ACL]                         [KQML]                         [HTTP / REST / gRPC]
• International standard          • First historical ACL         • Modern web microservices
• 22 formalized performatives     • Introduced performatives     • Standard JSON payloads
• Rigorous modal logic semantics  • Knowledge query & sharing    • Lacks formal speech-act logic
```

### A. FIPA-ACL (Foundation for Intelligent Physical Agents)
* **What it is:** The global gold standard for agent communication, formalized by IEEE FIPA.
* **Core Strength:** Defines **22 explicit communicative performatives** grounded in formal mental attitudes (beliefs, desires, intentions - BDI).
* **Key Mechanisms:** Mandates explicit preconditions and rational effects for every message type.

### B. KQML (Knowledge Query and Manipulation Language)
* **What it is:** Developed in the early 1990s under the DARPA Knowledge Sharing Effort; the historical predecessor to FIPA-ACL.
* **Core Strength:** Separated the communication layer from the content language, establishing the concept of performatives in multi-agent software.

### C. Modern Web Standards: HTTP/REST, JSON-RPC, & WebSockets
* **What it is:** General-purpose networking protocols widely used in contemporary production LLM agent frameworks (e.g., AutoGen, CrewAI, LangGraph).
* **Key Trade-off:** Extremely fast, accessible, and easily integrated with cloud databases, but lacks standardized formal speech-act semantics.

---

### Comparison: FIPA-ACL vs. KQML vs. HTTP/REST

| Evaluation Dimension | FIPA-ACL | KQML | HTTP/REST |
| :--- | :--- | :--- | :--- |
| **Primary Domain** | Formal autonomous agent research | Early distributed AI knowledge sharing | Commercial web microservices & APIs |
| **Semantic Foundation**| Formal modal logic (Speech Act Theory)| Informal speech act conventions | HTTP Verbs (`GET`, `POST`, `PUT`, `DELETE`)|
| **Message Intention** | Explicit via 22 standardized performatives | Defined via performatives | Inferred from endpoint paths and JSON bodies |
| **Ontology Support** | **Explicit header field** | Explicit header field | Requires custom payload engineering |
| **Standardization** | IEEE Computer Society / FIPA | DARPA / Academic Consortium | W3C / IETF RFCs |

---

## 5. Common Communicative Performatives

The **Performative** determines how the receiving agent should interpret the content payload:

```text
┌─────────────────┐                                              ┌─────────────────┐
│     SENDER      │ ────► query-if ("Is bed free?") ───────────► │    RECEIVER     │
│                 │ ◄──── inform ("Bed is free") ─────────────── │                 │
│                 │                                              │                 │
│                 │ ────► propose ("I can take patient in 5m") ─► │                 │
│                 │ ◄──── accept-proposal ("Approved") ───────── │                 │
└─────────────────┘                                              └─────────────────┘
```

| Performative | Semantic Meaning | Concrete Real-World Example |
| :--- | :--- | :--- |
| **`request`** | Sender asks receiver to perform an action | `"Please reserve Operating Room 3 for 14:00."` |
| **`inform`** | Sender asserts that a statement is true | `"Blood pressure is 120/80 mmHg."` |
| **`query-if`** | Sender asks whether a specific proposition holds | `"Is ventilator 4 available right now?"` |
| **`propose`** | Sender offers a conditional commitment | `"I can deliver the blood sample in 6 minutes."` |
| **`accept-proposal`**| Sender formally accepts an offer | `"Your bid of 6 minutes is accepted. Proceed."` |
| **`reject-proposal`**| Sender declines a submitted offer | `"Rejected: another drone offered 3 minutes."` |
| **`failure`** | Receiver notifies that an agreed action failed | `"Unable to reach Ward 4: door is locked."` |

---

## 6. Interaction Protocols: The Contract Net Protocol (CNP)

Agent communication is rarely a single message; it follows multi-turn **Interaction Protocols**. The most celebrated coordination protocol in MAS is the **Contract Net Protocol (Smith, 1980)** for distributed task allocation:

```text
   MANAGER AGENT                                                BIDDER AGENTS (Robots)
         │                                                      Robot 1        Robot 2
         │─── Call for Proposals (CFP: Deliver Package) ──────────►│              │
         │─────────────────────────────────────────────────────────┼─────────────►│
         │                                                         │              │
         │◄── Propose (Cost = 8 mins) ─────────────────────────────│              │
         │◄── Propose (Cost = 4 mins) ─────────────────────────────┼──────────────│
         │                                                         │              │
         │ [Manager Evaluates Bids: Robot 2 wins!]                 │              │
         │                                                         │              │
         │─── Reject-Proposal ────────────────────────────────────►│              │
         │─── Accept-Proposal (Execute Delivery) ──────────────────┼─────────────►│
         │                                                         │              │
         │◄── Inform-Done (Delivery Complete) ─────────────────────┼──────────────│
         ▼                                                         ▼              ▼
```

### Phases of Contract Net Protocol:
1. **Task Announcement (CFP):** Manager broadcasts a Call for Proposals specifying task requirements.
2. **Bidding:** Eligible agents evaluate their availability, compute costs, and return a `propose` (or `refuse`) message.
3. **Bid Evaluation:** Manager selects the most competitive bid based on an evaluation function.
4. **Awarding:** Manager sends `accept-proposal` to the winner and `reject-proposal` to all other bidders.
5. **Execution & Confirmation:** Winning bidder completes the task and responds with `inform-done` (or `failure`).

---

## 7. Concrete Worked Example: Emergency Traffic Incident

**Scenario:** A Traffic Monitoring Drone ($A_{\text{Drone}}$) discovers a severe multi-vehicle collision on Route 101 and must alert a City Route Planning Agent ($A_{\text{Route}}$).

```text
Step 1: Drone Formulates Incident Alert
        • Envelope:
          {
            "performative": "inform",
            "sender": "drone_highway_patrol_04",
            "receiver": "city_route_optimizer",
            "ontology": "urban_traffic_incidents_v1",
            "conversation_id": "incident_rt101_crash",
            "content": {
              "type": "vehicle_collision",
              "location": "Route 101 Northbound, Mile 42",
              "severity": "critical",
              "blockage": "3 lanes closed",
              "expected_clearing_time": "120 mins"
            }
          }

Step 2: Transmission & Reception
        • Transmitted via WebSocket message broker; Route Optimizer confirms receipt.

Step 3: Route Optimizer Processing
        • Reads ontology terms; immediately recalculates dynamic weights on Route 101 graph edges.

Step 4: Downstream Multi-Agent Action
        • Route Optimizer issues 'request' performatives to Navigation Agents,
          diverting 15,000 incoming commuters to arterial detours before gridlock forms.
```

---

## 8. Advantages and Technical Challenges

### Advantages:
* **Interoperability Across Heterogeneous Systems:** A Python agent running on Linux can seamlessly negotiate with a C++ robotic agent on ROS via FIPA-ACL.
* **Semantic Precision:** Ontologies eliminate vocabulary ambiguity across diverse domains.
* **Decentralized Coordination:** Enables complex contract negotiations without requiring a centralized master database.

### Technical Challenges:
* **Communication Latency & Bandwidth Consumption:** High-frequency broadcasting creates network bottlenecks.
* **Semantic / Ontology Mismatches:** If two agents use different versions of an ontology, message interpretation fails.
* **Security & Malicious Spoofing:** Lack of cryptographic signing allows rogue agents to inject fake `inform` or `propose` messages.
* **Deadlocks in Asynchronous Dialogues:** An agent blocked waiting for a response to a `request` can hang if the receiver crashes without sending a `failure` notice.

---

## 9. Conclusion

Communication protocols are the connective tissue of Multi-Agent Systems. Grounded in **Speech Act Theory**, standards like **FIPA-ACL** and protocols like the **Contract Net Protocol** provide the grammatical and conversational scaffolding necessary for independent AI agents to make requests, assert facts, evaluate competitive bids, and coordinate distributed intelligence across complex environments.

---

## 10. Quick Revision Sheet

* **Communication Protocol:** Standardized rules governing how autonomous agents exchange and interpret messages.
* **Speech Act Theory:** Utterances are actions (Performatives) designed to alter receiver mental states.
* **FIPA-ACL Message Components:** Sender, Receiver, Performative, Content, Language, Ontology, Conversation-ID.
* **Top Performatives:** `request`, `inform`, `query-if`, `propose`, `accept-proposal`, `reject-proposal`, `failure`.
* **Contract Net Protocol (CNP):** CFP $\to$ Propose $\to$ Accept/Reject $\to$ Inform-Done.

### 🧠 One-line memory trick
> **The performative declares the intent, the content carries the data, and the ontology ensures they speak the exact same language!**

---

## 11. Active Recall & Self-Evaluation (Q&A)

### Q1. What is a communication protocol in MAS?
* **Answer:** A standardized set of syntactic, semantic, and procedural rules that dictate how autonomous agents structure, transmit, interpret, and sequence messages to coordinate actions, share knowledge, and resolve conflicts.

### Q2. What is the difference between a message's performative and its content?
* **Answer:**
  * **Performative:** Specifies the **communicative intention or illocutionary force** of the message (e.g., `request`, `inform`, `propose`). It tells the receiver *what type of action* the sender is executing.
  * **Content:** Represents the **actual domain payload or data** being communicated (e.g., `"Heart rate is 140 bpm"` or `"Check drug inventory"`).

### Q3. Name two agent communication languages and explain one.
* **Answer:**
  * Two languages: **FIPA-ACL** and **KQML**.
  * **FIPA-ACL (Foundation for Intelligent Physical Agents - Agent Communication Language):** An internationally standardized agent language based on formal Speech Act Theory. It defines 22 distinct performatives (such as `request`, `inform`, `propose`) along with explicit envelope fields (ontology, language, conversation-id) to guarantee semantic precision and interoperability between heterogeneous agents.

### Q4. Practical: A traffic-monitoring agent detects a road accident and needs to notify a route-planning agent. Describe the message exchange and how the receiver acts.
* **Answer:**
  * **Message Exchange:** The traffic agent sends an **`inform`** performative containing structured crash details (GPS coordinates, lane closures, expected duration) referenced against a shared urban traffic ontology.
  * **Action Taken:** The route-planning agent interprets the `inform` assertion as a validated world-state update. It immediately increases the travel-time cost of that road segment in its routing graph and issues rerouting recommendations to all connected vehicular navigation agents.
