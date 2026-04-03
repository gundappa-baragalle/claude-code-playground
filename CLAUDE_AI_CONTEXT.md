# UPSC PYQ Classification Task — Full Context

You are classifying UPSC Previous Year Questions (PYQs) for an enrichment pipeline.
Return ONLY a valid JSON array — no explanation, no markdown, no extra text.

---

## CLASSIFICATION RULES

1. **CSAT detection (highest priority — check FIRST before subject):**
   - Math/arithmetic/geometry/volumes/percentages/algebra → CSAT > Quantitative Aptitude
   - Speed-distance, work-time, profit-loss, ratio, sets/Venn diagrams → CSAT > Quantitative Aptitude
   - Seating/blood-relations/direction sense/coding-decoding/syllogism → CSAT > Logical Reasoning
   - English reading comprehension/vocabulary/grammar → CSAT > Reading Comprehension
   - Any question solvable purely by logic/math without domain knowledge → CSAT

2. **Paper=GS4 → subject MUST be "Ethics" always** (ignore question content)

3. **Paper=Essay → subject = dominant theme of essay question**

4. **Prelims priority distribution: ~45% HIGH / ~35% MEDIUM / ~20% LOW** (enforce across the batch)
   - HIGH: frequently asked, high-yield topics (fundamental concepts, recurring themes)
   - MEDIUM: moderately important, tested occasionally
   - LOW: very specific/dated/obscure facts unlikely to recur

5. **Use ONLY topics from the taxonomy below.** If unsure, pick the closest match.

---

## TAXONOMY (Subject > Category > Topics)

**CSAT** *(not in standard taxonomy — use these)*
- Quantitative Aptitude: Number System | Percentages | Ratio & Proportion | Time Speed Distance | Work and Time | Profit and Loss | Simple and Compound Interest | Geometry | Mensuration | Volume and Mensuration | Algebra | Set Theory and Venn Diagrams | Data Interpretation | Permutation and Combination | Probability | Exponential Growth and Series | Seating Arrangement (if math-based)
- Logical Reasoning: Seating Arrangement | Blood Relations | Direction Sense | Coding-Decoding | Syllogisms | Ordering and Ranking | Analogy | Input-Output | Series Completion
- Reading Comprehension: Reading Comprehension | Vocabulary | Grammar

**History**
- Ancient India: Prehistoric Period | Indus Valley Civilization | Vedic Age | Buddhism | Jainism | Mauryan Empire | Post-Mauryan Period | Gupta Empire | Post-Gupta Period | Sangam Age
- Medieval India: Delhi Sultanate | Mughal Empire | Regional Kingdoms | Bhakti Movement | Sufi Movement | Maratha Empire | Medieval Art & Architecture
- Modern India: British Expansion | Economic Impact of British Rule | Social & Religious Reform | 1857 Revolt | Rise of Nationalism | Gandhian Era | Revolutionary Movement | Communal Politics & Partition | Constitutional Development | British-Era Committees and Commissions
- Post-Independence India: Integration of States | Reorganization of States
- World History: Industrial Revolution | Colonialism & Imperialism | World Wars | Decolonization | Political Philosophies

**Geography**
- Physical Geography: Geomorphology | Climatology | Oceanography | Biogeography
- Indian Geography: Physiography | Drainage System | Climate & Monsoon | Soils | Natural Vegetation | Minerals & Energy | Agriculture | Industries | Physical Features of India | Agricultural Geography
- World Geography: Continents & Regions | Resource Distribution | World Population Distribution | Ethnic Communities and Tribes | Economic Geography

**Society**
- Indian Society: Features of Indian Society | Caste System | Family & Kinship | Religion & Communalism | Regionalism | Romani and Diaspora Communities
- Women & Gender: Women's Issues | Women Empowerment
- Population & Development: Population Issues | Poverty & Inequality | Urbanization
- Globalization: Impact of Globalization

**Polity**
- Constitutional Framework: Historical Background | Preamble | Basic Structure | Fundamental Rights | DPSP & Fundamental Duties | Constitutional Amendments
- Union Government: President | Vice President | Prime Minister & Council | Parliament | Supreme Court | Lok Sabha | Rajya Sabha
- State Government: Governor | State Legislature | High Court
- Federalism: Centre-State Relations | Interstate Relations | Local Government
- Constitutional Bodies: Election Commission | Finance Commission | UPSC & State PSCs | CAG | Other Bodies
- Statutory & Regulatory Bodies: Statutory Bodies | Regulatory Bodies
- Elections & Representation: Electoral System | RPA Act | Political Parties

**Governance**
- Government Schemes & Policies: Social Sector Schemes | Welfare of Vulnerable Sections
- Development & Civil Society: Role of NGOs & SHGs | Development Issues
- Health & Education: Health Issues | Education
- Poverty & Hunger: Poverty Alleviation | Food Security
- E-Governance & Transparency: E-Governance | Transparency & Accountability
- Civil Services: Role of Civil Services
- Awards and Honours: Dadasaheb Phalke Award | Padma Awards | Bharat Ratna | National Awards
- Prominent Personalities: Eminent Indians

**International Relations**
- India's Foreign Policy: Foreign Policy Principles
- India & Neighbours: India-Pakistan | India-China | India-Bangladesh | India-Nepal | India-Sri Lanka | Other Neighbours
- International Organizations: United Nations | Regional Groupings | Multilateral Forums
- Global Issues: Global Challenges | Indian Diaspora
- Africa: African Political Leadership
- Global Political Movements: International Political Movements

**Economy**
- Macroeconomics: National Income | Money & Banking | Banking System | Inflation | Savings and Investment
- Public Finance: Government Budget | Taxation | Fiscal Federalism
- External Sector: Balance of Payments | Trade Policy | Foreign Investment | Exchange Rate
- Agriculture: Agricultural Economy | Agricultural Policy | Irrigation & Technology | Food Security | Land Reforms
- Industry & Infrastructure: Industrial Policy | Infrastructure | Energy
- Development & Planning: Planning | Inclusive Growth | Human Development

**Environment**
- Ecology & Ecosystem: Ecology Basics | Biodiversity | Ecosystem Types
- Environmental Issues: Pollution | Climate Change | Environmental Degradation
- Conservation: Protected Areas | Conservation Laws & Bodies | International Conservation
- Disaster Management: Disasters | Disaster Management

**Science & Technology**
- Space Technology: Indian Space Programme | Space Applications
- Defence Technology: Defence R&D
- Biotechnology: Biotech Applications | Biotech Ethics
- IT & Communication: Digital Technology | Cyber Security
- Nuclear Technology: Nuclear Programme
- Basic Sciences: Physics | Chemistry | Biology
- Intellectual Property: IPR
- Astronomy: Solar System | Space Exploration
- Emerging Technologies: Optical and Wireless Communication | AI and Robotics | Nanotechnology

**Internal Security**
- Security Challenges: Terrorism | Left Wing Extremism | Insurgency
- Border Security: Border Management | Organized Crime
- Cyber & Communication Security: Cyber Security Challenges | Social Media & Security
- Security Forces: Security Apparatus

**Ethics** *(Paper=GS4 questions always go here)*
- Ethics Fundamentals: Ethics Basics | Human Values | Attitude
- Thinkers & Philosophers: Indian Thinkers | Western Thinkers
- Applied Ethics: Emotional Intelligence | Aptitude for Civil Service
- Public Administration Ethics: Probity in Governance | Ethical Governance
- Case Studies: Case Study Approach

---

## SYLLABUS ID FORMAT

**STRICT FORMAT: `PREFIX.1` — always end with `.1`**

Derive the prefix from subject + category using this exact table:

| Subject | Category | syllabus_id prefix |
|---------|----------|--------------------|
| History | Ancient India | HIS.ANC |
| History | Medieval India | HIS.MED |
| History | Modern India | HIS.MOD |
| History | Post-Independence India | HIS.POST |
| History | World History | HIS.WLD |
| Geography | Physical Geography | GEO.PHY |
| Geography | Indian Geography | GEO.IND |
| Geography | World Geography | GEO.WLD |
| Society | Indian Society | SOC.IND |
| Society | Women & Gender | SOC.WOM |
| Society | Population & Development | SOC.POP |
| Society | Globalization | SOC.GLOB |
| Polity | Constitutional Framework | POL.CON |
| Polity | Union Government | POL.UNI |
| Polity | State Government | POL.ST |
| Polity | Federalism | POL.FED |
| Polity | Constitutional Bodies | POL.CB |
| Polity | Statutory & Regulatory Bodies | POL.SRB |
| Polity | Elections & Representation | POL.ELX |
| Governance | Government Schemes & Policies | GOV.SCH |
| Governance | Development & Civil Society | GOV.DEV |
| Governance | Health & Education | GOV.HED |
| Governance | Poverty & Hunger | GOV.POV |
| Governance | E-Governance & Transparency | GOV.EGV |
| Governance | Civil Services | GOV.CS |
| Governance | Awards and Honours | GOV.AWD |
| Governance | Prominent Personalities | GOV.PERS |
| International Relations | India's Foreign Policy | IR.FP |
| International Relations | India & Neighbours | IR.NBR |
| International Relations | International Organizations | IR.IO |
| International Relations | Global Issues | IR.GLB |
| International Relations | Africa | IR.AFR |
| International Relations | Global Political Movements | IR.GPM |
| Economy | Macroeconomics | ECO.MAC |
| Economy | Public Finance | ECO.PUB |
| Economy | External Sector | ECO.EXT |
| Economy | Agriculture | ECO.AGR |
| Economy | Industry & Infrastructure | ECO.IND |
| Economy | Development & Planning | ECO.DEV |
| Environment | Ecology & Ecosystem | ENV.ECO |
| Environment | Environmental Issues | ENV.ISS |
| Environment | Conservation | ENV.CON |
| Environment | Disaster Management | ENV.DIS |
| Science & Technology | Space Technology | S&T.SPC |
| Science & Technology | Defence Technology | S&T.DEF |
| Science & Technology | Biotechnology | S&T.BIO |
| Science & Technology | IT & Communication | S&T.IT |
| Science & Technology | Nuclear Technology | S&T.NUC |
| Science & Technology | Basic Sciences | S&T.BSC |
| Science & Technology | Intellectual Property | S&T.IPR |
| Science & Technology | Astronomy | S&T.ASTRO |
| Science & Technology | Emerging Technologies | S&T.EMR |
| Internal Security | Security Challenges | SEC.CH |
| Internal Security | Border Security | SEC.BDR |
| Internal Security | Cyber & Communication Security | SEC.CYB |
| Internal Security | Security Forces | SEC.SF |
| Ethics | Ethics Fundamentals | ETH.FND |
| Ethics | Thinkers & Philosophers | ETH.THK |
| Ethics | Applied Ethics | ETH.APP |
| Ethics | Public Administration Ethics | ETH.PAE |
| Ethics | Case Studies | ETH.CS |
| CSAT | Quantitative Aptitude | CSAT.QA |
| CSAT | Logical Reasoning | CSAT.LR |
| CSAT | Reading Comprehension | CSAT.RC |

**Examples:** `HIS.MED.1` / `GEO.IND.1` / `CSAT.QA.1` / `S&T.BSC.1`
**NEVER use:** paper codes like `PTGS.x`, old codes like `S&T.PHY`, or numbers other than `.1`

---

## OUTPUT SCHEMA

Return a JSON array, one object per question, in the same order as given.

```json
{
  "idx": <position in batch, 0-indexed>,
  "subject": "<from taxonomy>",
  "category": "<from taxonomy>",
  "topic": "<from taxonomy>",
  "syllabus_id": "<e.g. HIS.MED.1>",
  "dimension": "<WHAT|WHY|HOW|WHEN|WHERE|WHO|VS|IMPACT>",
  "question_type": "<Factual|Conceptual|Analytical|Application|CSAT>",
  "difficulty": "<Easy|Medium|Hard>",
  "confidence_score": <0.0-1.0>,
  "prelims_priority": "<HIGH|MEDIUM|LOW>",
  "trap_factor": "<1-2 sentences: why wrong options look right — MCQ only, null for mains>",
  "elimination_hint": "<1-2 sentences: specific strategy to reach correct answer — MCQ only, null for mains>",
  "factual_hooks": ["<key fact to remember>", "<key fact 2>"],
  "prerequisite_concepts": ["<concept A>", "<concept B>"],
  "related_concepts": ["<topic X>", "<topic Y>"],
  "contrast_with": ["<ConceptZ — key differentiator>"],
  "mains_themes": ["<theme1>"],
  "mains_intro": "<1 sentence intro approach — mains only, null for prelims>",
  "mains_body_points": ["<point 1>", "<point 2>"],
  "mains_conclusion": "<1 sentence conclusion — mains only, null for prelims>",
  "mains_interlinkages": ["<related paper/topic>"],
  "contemporary_relevance": "<1 sentence or null>",
  "keywords": ["kw1", "kw2", "kw3", "kw4", "kw5"]
}
```

**Keep text fields concise** — trap_factor and elimination_hint max 2 sentences each. factual_hooks max 3 items. keywords max 6 items.

---

## NOW CLASSIFY THE QUESTIONS BELOW

Return ONLY the JSON array. No explanation. No markdown fences. Start directly with `[`.
