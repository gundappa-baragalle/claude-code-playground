# Set Theory and Venn Diagrams

**Subject:** CSAT > Quantitative Aptitude
**Syllabus ID:** CSAT.QA.1
**Total Questions:** 15 (Prelims: 15, Mains: 0)
**Year Range:** 1995 – 2010
**Last Asked:** 2010
**Revision Priority:** 🔴 HIGH

## Keywords
Venn diagram, set theory, CSAT, percentage, inclusion-exclusion, intersection, inclusion exclusion, logical reasoning, union, phone

## Dimensions Tested
- **HOW**: 15 questions

## Related Concepts
- Complement sets
- Set Theory and Venn Diagrams
- Union and intersection of sets
- Combinatorial logic
- Tea-coffee problems in CSAT
- Probability bounds
- Venn diagrams
- Combinatorics

## Prelims Questions

### 🔴 HIGH Priority — Full MCQ + Trap Intelligence

*Use these verbatim as Practice MCQs in CDF notes.*

**[Q1995]** [2008]
> In an examination, 70% of the students passed in the Paper I, and 60% of the students passed in the Paper II: 15% of the students failed in both the papers while 270 students passed in both the papers. What is the total number of students?

  ✅ A) 600
     B) 580
     C) 560
     D) 540

  ⚠️ **Trap:** Candidates may add 70%+60%=130% and subtract 100% to get 30% passing both, but must account for 15% failing both. Using inclusion-exclusion correctly is key.
  💡 **Eliminate:** Passed both = 70+60-15-100+15... Correct: Passed at least one = 100-15=85%. Passed both = 70+60-85=45%. 45% of N = 270 → N = 600. Answer: A.
  📌 **Key facts:**
     - Venn diagram: P(A∪B) = 1 - P(fail both) = 85%; P(A∩B) = P(A)+P(B)-P(A∪B) = 70+60-85 = 45%
     - Total students = 270/0.45 = 600

**[Q4497]** [2005]
> 300 persons are participating in a meeting, out of which 120 are foreigners, and the rest are Indians. Out of the Indians, there are 110 men who are not judges; 160 are men or judges, and 35 are women judges. How many Indian women attended the meeting?

     A) 35
     B) 45
  ✅ C) 55
     D) 60

  ⚠️ **Trap:** Multiple overlapping categories (foreigners, Indians, men, judges, women) can cause confusion; students may forget to subtract foreigners (120) first.
  💡 **Eliminate:** Indians = 300-120 = 180. Men who are not judges = 110. Men or judges = 160. Men judges = 160-110=50. Total judges = 50+35=85. Women = 180-110-35=35? Recalculate: Indian men = use inclusion-exclusion properly. Indian women = 180 - Indian men = 180 - 125 = 55.
  📌 **Key facts:**
     - Total Indians = 300-120 = 180
     - Indian women = 55 (after set theory calculation)

**[Q37]** [2001]
> In a survey, it was found that 80% of those surveyed owned a car while 60% of those surveyed owned a mobile phone. If 55% owned both a car and a mobile phone, what per cent of those surveyed owned a car or a mobile phone or both ?

     A) 65%
     B) 80%
  ✅ C) 85%
     D) 97.5%

  ⚠️ **Trap:** Many pick 80% thinking 'car owners' is already the maximum; they forget to add phone-only owners and subtract double-counted 'both' group.
  💡 **Eliminate:** P(A∪B) = P(A) + P(B) − P(A∩B) = 80 + 60 − 55 = 85%. Standard Venn diagram formula.
  📌 **Key facts:**
     - P(A∪B) = P(A) + P(B) − P(A∩B)
     - Always subtract the intersection to avoid double counting

**[Q51]** [1999]
> In a town 25% families own a phone and 15% own a car. 65% families own neither a phone nor a car. 2000 families own both a car and a phone. Consider the following statements in this regard: I. 10% families own both a car and a phone. II. 35% families own either a car or a phone. III. 40,000 families live in the town. Which of the above statements are correct ?

     A) I and II
     B) I and III
  ✅ C) II and III
     D) I, II and III

  ⚠️ **Trap:** Statement I says 10% own both — but the correct 'both' is 5% (25+15−35=5%). Statement III says 40,000 total — this is correct (5%=2000 → total=40,000). Statement I is the deliberate wrong statement.
  💡 **Eliminate:** P(phone∪car)=100−65=35%. P(both)=25+15−35=5%. If 5%=2000 families, total=40,000 ✓ (III). 35% own either ✓ (II). But 10% own both is wrong (I). So II and III only = C.
  📌 **Key facts:**
     - P(neither)=65% → P(union)=35%
     - P(both)=P(A)+P(B)−P(union)=25+15−35=5%
     - If 5%=2000, total population=40,000

**[Q4619]** [1995]
> In the given diagram, circle A represents teachers who can teach Physics, circle B represents teachers who can teach Chemistry and circle C represents those who can teach Mathematics. Among the regions marked p, q, r ........ the one which represents teachers who can teach Physics and Mathematics but not Chemistry, is

     A) v
     B) u
  ✅ C) s
     D) t

  ⚠️ **Trap:** Candidates may confuse regions in Venn diagrams, especially when multiple overlapping circles share regions. 'Physics and Mathematics but not Chemistry' means the region in circles A and C but outside circle B.
  💡 **Eliminate:** In a three-circle Venn diagram (A=Physics, B=Chemistry, C=Mathematics), the region in A∩C but NOT in B represents teachers who teach Physics and Maths but not Chemistry. This is region 's' in standard Venn diagram labeling.
  📌 **Key facts:**
     - Venn diagram: A∩C minus B = Physics+Maths but not Chemistry = region 's'
     - Standard three-circle Venn has 7 regions excluding the universal set exterior

### 🟡 MEDIUM Priority — Full Options

**[Q1428]** [2010] How many numbers from 0 to 999 are divisible by either 5 or 7?

     A) 313
     B) 341
  ✅ C) 686
     D) 786

  ⚠️ **Trap:** Students often forget to include 0 in the count (0 is divisible by both 5 and 7). Also forgetting to subtract overlap (divisible by both 5 and 7 = 35) leads to overcounting.

**[Q2331]** [2009] In an examination, there are three subjects A, B and C. A student has to pass in each subject. 20% students failed iv A, 22% students failed in B and 16% failed in C. The total number of students passing the whole examination lies between

  ✅ A) 42% and 84%
     B) 42% and 78%
     C) 58% and 78%
     D) 58% and 84%

  ⚠️ **Trap:** The pass percentage calculation requires understanding minimum and maximum pass bounds using inclusion-exclusion; minimum pass = 100-(20+22+16)=42%; maximum pass requires careful set theory.

**[Q4357]** [2009] There are three cans A, B and C. The capacities of A, B and C are 6 litres, 10 litres and 16 litres respectively. The can C contains 16 litres of milk. The milk has to be divided in them using these three cans only. Consider the following statements : 1. It is possible to have 6 litres of milk each in can A and can B. 2. It is possible to have 8 litres of milk each in can B and can C. Which of the statements given above is/are correct ?

     A) 1 only
     B) 2 only
  ✅ C) Both 1 and 2
     D) Neither 1 nor 2

  ⚠️ **Trap:** The constraint of using only three cans without any measuring instrument makes this a liquid puzzle; candidates may assume simpler divisions are impossible.

**[Q529]** [2000] The given diagram shows the number of students who failed in an examination comprising papers in English, Hindi and Mathematics. The total number of students who took the test is 500. What is the percentage of students who failed in at least two subjects ?

     A) 6.8
  ✅ B) 7.8
     C) 34
     D) 39

  ⚠️ **Trap:** Students often confuse 'failed in at least two subjects' with 'failed in exactly two subjects'; must include those who failed in all three as well.

**[Q531]** [2000] In an examination, every candidate took Physics or Mathematics or both. 65.8% took Physics and 59.2% took Mathematics. The total number of candidates was 2000. How many candidates took both Physics and Mathematics ?

     A) 750
  ✅ B) 500
     C) 250
     D) 125

  ⚠️ **Trap:** Students add 65.8 + 59.2 and forget to subtract 100 (since total is 100%, not 125%). The overlap (both subjects) = sum of percentages − 100.

**[Q2736]** [1998] There are 50 students admitted to a nursery class. Some students can speak only English and some can speak only Hindi. 10 students can speak both English and Hindi. If the number of students who can speak English is 21, then how many students can speak Hindi, how many can speak only Hindi and how many can speak only English ?

     A) 21, 11 and 29 respectively
     B) 28, 18 and 22 respectively
     C) 37, 27 and 13 respectively
  ✅ D) 39, 29 and 11 respectively

**[Q2590]** [1997] In a group of persons travelling in a bus, 6 persons can speak Tamil, 15 can speak Hindi and 6 can speak Gujarati. In that group none can speak any other language. If 2 persons in the group can speak two languages and one person can speak all the three languages, then how many persons are there in the group ?

     A) 21
     B) 22
     C) 23
  ✅ D) 24

  ⚠️ **Trap:** Candidates may incorrectly add all values (6+15+6=27) then simply subtract the bilingual (2) people without properly accounting for the trilingual person being included in both.

**[Q5021]** [1997] A survey was conducted on a sample of 1000 persons with reference to their knowledge of English, French and German. The results of the survey are presented in the given Venn diagram. The ratio of the number of persons who do not know any of the three languages to those who know all the three languages is

     A) 1/27
  ✅ B) 1/25
     C) 1/550
     D) 175/1000

  ⚠️ **Trap:** Without the actual Venn diagram figure, exact numbers cannot be determined; this is a figure-based question. The ratio logic requires reading off intersection and complement values from the diagram.

### 🟢 LOW Priority — Reference Stubs

- **[Q1132]** [2006] In an office, the number of persons who take tea is twice the number of persons who take only coffee. The number of persons who ta...
  - Dim: HOW | Ans: B
- **[Q4446]** [1995] Out of a total of 120 musicians in a club, 5% can play all the three instruments-guitar, violin and flute. It so happens that the ...
  - Dim: HOW | Ans: B

## Exam Patterns & Insights

- **Most tested dimension:** HOW (15/15 = 100% of questions)
- **Question types (Prelims):** CSAT: 15
- **Trend:** Not asked since 2010 — lower probability but classic syllabus topic

### Common Trap Patterns on This Topic
- Many pick 80% thinking 'car owners' is already the maximum; they forget to add phone-only owners and subtract double-counted 'both' group.
- Statement I says 10% own both — but the correct 'both' is 5% (25+15−35=5%). Statement III says 40,000 total — this is correct (5%=2000 → total=40,000). Statement I is the deliberate wrong statement.
- Students often confuse 'failed in at least two subjects' with 'failed in exactly two subjects'; must include those who failed in all three as well.
- Students add 65.8 + 59.2 and forget to subtract 100 (since total is 100%, not 125%). The overlap (both subjects) = sum of percentages − 100.
- Setting up algebraic variables for 'only tea', 'only coffee', 'both' is tricky; students may confuse 'takes tea' (includes both) with 'takes only tea'.
