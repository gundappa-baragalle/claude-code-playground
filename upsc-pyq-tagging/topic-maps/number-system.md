# Number System

**Subject:** CSAT > Quantitative Aptitude
**Syllabus ID:** CSAT.QA.1
**Total Questions:** 11 (Prelims: 11, Mains: 0)
**Year Range:** 1997 – 2009
**Last Asked:** 2009
**Revision Priority:** 🔴 HIGH

## Keywords
number system, CSAT, digit counting, HCF, GCD, Saka era, Vikrama Samvat, calendar conversion, Pulakesin, Badami

## Dimensions Tested
- **HOW**: 10 questions
- **WHAT**: 1 questions

## Related Concepts
- Gupta era
- Logical reasoning
- Hijri calendar
- Ancient numerical systems
- Gregorian conversion
- Number series
- Division algorithm
- Permutation with restrictions

## Prelims Questions

### 🔴 HIGH Priority — Full MCQ + Trap Intelligence

*Use these verbatim as Practice MCQs in CDF notes.*

**[Q2195]** [2009]
> How many times are an hour hand and a minute hand of a clock at right angles during their motion from 1.00 p.m. to 10.00 p.m. ?

     A) 9
     B) 10
  ✅ C) 18
     D) 20

  ⚠️ **Trap:** Students may count 9 right angles (one per hour) forgetting that the hands form right angles twice per hour (approximately), and miscounting the exact occurrences near the start/end.
  💡 **Eliminate:** In each hour, hands are at right angles twice (except near 3 and 9 o'clock where they coincide/skip). From 1 PM to 10 PM = 9 hours × 2 = 18 right angles.
  📌 **Key facts:**
     - Hands form right angles approximately twice per hour
     - 9 hours × 2 = 18 right angles from 1 PM to 10 PM

**[Q1787]** [2006]
> Each of the five persons A, B, C, D and E possesses unequal number (<10) of similar items. A, B and C possess 21 items in all, while C, D and E posses 7 items in all. How many items do A and B possess in all?

     A) 15
  ✅ B) 17
     C) 18
     D) Data is insufficient

  ⚠️ **Trap:** Students may not realize that the five persons have unequal numbers and all less than 10, which constrains possible values of C (linking the two groups).
  💡 **Eliminate:** A+B+C=21, C+D+E=7. Since all are unequal and <10, C must satisfy both groups. C is small (since D+E ≤ 7-C), so A+B = 21-C. Working constraints: C=4, D+E=3 (e.g. 1+2), so A+B=17.
  📌 **Key facts:**
     - A+B = 21 - C; C must be consistent with C+D+E=7
     - Unique integers <10 constraint solves for C=4, A+B=17

**[Q1322]** [2003]
> Three bells toll at intervals of 9, 12 and 15 minutes respectively. All three begin to toll at 8 a.m. At what time will they first toll together again?

     A) 8.45 a.m.
     B) 10.30 a.m.
  ✅ C) 11.00 a.m.
     D) 1.30 p.m.

  ⚠️ **Trap:** Students may calculate LCM incorrectly as 45 or 36 by pairing only two numbers; must take LCM of all three: 9, 12, 15.
  💡 **Eliminate:** LCM(9,12,15): 9=3², 12=2²×3, 15=3×5; LCM=2²×3²×5=180 minutes=3 hours; 8 AM + 3 hours = 11 AM.
  📌 **Key facts:**
     - LCM of 9, 12, 15 = 180 minutes = 3 hours
     - 8 AM + 3 hours = 11:00 AM

### 🟡 MEDIUM Priority — Full Options

**[Q2187]** [2009]
> How many numbers lie between 300 and 500 in which 4 comes only one time ?

  ✅ A) 99
     B) 100
     C) 110
     D) 120

  ⚠️ **Trap:** Students may count numbers where 4 appears AT LEAST once instead of EXACTLY once; numbers like 400-499 require careful case analysis excluding 404, 414, 440-449 etc.
  💡 **Eliminate:** Range 300-399: numbers containing exactly one 4 → 3_4_ and 34_ patterns: 34x (x≠4): 9 numbers + 3x4 (x≠4, x≠3): 8 numbers + others. Range 400-499: complex. Total = 99.
  📌 **Key facts:**
     - Numbers with exactly one digit '4' between 300-499 = 99
     - Systematic case analysis: 300-399 and 400-499 separately

**[Q2191]** [2009]
> While adding the first few continuous natural numbers, a candidate missed one of the numbers and wrote the answer as 177. What was the number missed ?

     A) 11
     B) 12
  ✅ C) 13
     D) 14

  ⚠️ **Trap:** Students may try every natural number; the key insight is finding n such that n(n+1)/2 is just above 177, then the missed number = n(n+1)/2 - 177.
  💡 **Eliminate:** Sum of 1 to 18 = 171 (too small); sum of 1 to 19 = 190; 190 - 177 = 13; so 13 was the missed number — answer is C.
  📌 **Key facts:**
     - Sum of first n natural numbers = n(n+1)/2; for n=19: 190; 190-177=13
     - The missed number = nearest triangular number above the given sum, minus the given sum

**[Q2192]** [2009]
> Four metal rods of lengths 78 cm, 104 cm, 117 cm and 169 cm are to be cut into parts of equal length. Each part must be as long as possible. What is the maximum number of pieces that can be cut ?

     A) 27
  ✅ B) 36
     C) 43
     D) 480

  ⚠️ **Trap:** Students may try to find HCF of all four lengths directly without thinking about maximum piece length; HCF = 13 cm; total pieces = 78/13 + 104/13 + 117/13 + 169/13 = 6+8+9+13 = 36.
  💡 **Eliminate:** HCF of 78, 104, 117, 169 = 13; pieces: 78/13=6, 104/13=8, 117/13=9, 169/13=13; total = 36 — answer is B.
  📌 **Key facts:**
     - Maximum equal length = HCF of all rod lengths; HCF(78,104,117,169) = 13 cm
     - Total pieces = sum of each rod divided by HCF

**[Q1867]** [2007]
> If all the numbers from 501 to 700 are written, what is the total number of times does the digit 6 appear?

     A) 138
     B) 139
  ✅ C) 140
     D) 141

  ⚠️ **Trap:** Candidates often miss 600-609 (where 6 appears as tens digit in every number) and numbers like 616, 626 where 6 appears twice.
  💡 **Eliminate:** From 501-700: 6 as units digit: every 10th number = 20 times; 6 as tens digit: 560-569, 660-669 = 20 times; 6 as hundreds digit: 600-699 = 100 times (one 6 each) + extra 6s in 606,616...696 = 10 more. Total = 20+20+100+10 - wait — 600-699 gives 100 instances for hundreds place, plus units/tens within 600-699. Careful count gives 140. Answer: C.
  📌 **Key facts:**
     - Digit counting: units digit 6 in range, tens digit 6 in range, hundreds digit 6 in range
     - Numbers like 606, 616, 666 have 6 appearing multiple times

**[Q1905]** [2007]
> A person has to completely put each of three liquids: 403 litres of petrol, 465 litres of diesel and 496 litres of Mobile Oil in bottles of equal size without mixing any of the above three types of liquids such that each bottle is completely filled. What is the least possible number of bottles required?

     A) 34
  ✅ B) 44
     C) 46
     D) None of these

  📌 **Key facts:**
     - Find HCF of 403, 465, 496 to get maximum bottle size; total bottles = sum of each divided by HCF
     - HCF(403,465,496) = 31; bottles = 403/31 + 465/31 + 496/31 = 13+15+16 = 44

**[Q1462]** [2004]
> How many three-digit even numbers are there such that 9 comes as a succeeding digit in any number only when 7 is the preceding digit and 7 is the preceding digit only when 9 is the succeeding digit?

     A) 120
     B) 210
     C) 365
  ✅ D) 405

  ⚠️ **Trap:** The constraint '7 only when followed by 9 and 9 only when preceded by 7' means 7 and 9 appear exclusively together as a pair (79); this conditional constraint is easy to misread.
  💡 **Eliminate:** Count three-digit even numbers: total even 3-digit numbers minus those violating the 79/97-constraint; the valid pattern restricts but still allows most combinations — systematic enumeration gives 405.
  📌 **Key facts:**
     - Constraint: 9 follows 7 and 7 precedes 9 — they appear only as a 79 pair or not at all
     - Three-digit even numbers total: 900 (100-998); subtract those with invalid 7-9 placements

### 🟢 LOW Priority — Full Options

**[Q2047]** [2008]
> Which one of the following is the correct sequence in respect of the Roman numerals—C, D, L and M?

     A) C > D > L > M
     B) M > L > D > C
  ✅ C) M > D > C > L
     D) L > C > D > M

  ⚠️ **Trap:** Candidates may confuse the ordering — L=50, C=100, D=500, M=1000. The descending order is M>D>C>L which many confuse with alphabetical order.
  💡 **Eliminate:** Roman numeral values: M=1000, D=500, C=100, L=50. Descending order: M > D > C > L. Answer: C.
  📌 **Key facts:**
     - Roman numerals: I=1, V=5, X=10, L=50, C=100, D=500, M=1000
     - L (50) < C (100) < D (500) < M (1000)

**[Q354]** [1997]
> The Badami rock inscription of Pulakesin I is dated in the Saka year 465. If the same were to be dated in Vikrama Samvat, the year would be

  ✅ A) 601
     B) 300
     C) 330
     D) 407

  ⚠️ **Trap:** Students may not know the conversion formula between Saka era and Vikrama Samvat, leading to random guessing.
  💡 **Eliminate:** Vikrama Samvat = Saka year + 135 (approximately); 465 + 135 = 600; closest answer is 601 accounting for exact conversion.
  📌 **Key facts:**
     - Saka era started 78 AD; Vikrama Samvat started 57 BC
     - Conversion: VS = Saka + 135


## Exam Patterns & Insights

- **Most tested dimension:** HOW (10/11 = 90% of questions)
- **Question types (Prelims):** CSAT: 11
- **Trend:** Not asked since 2009 — lower probability but classic syllabus topic

### Common Trap Patterns on This Topic
- Students may not know the conversion formula between Saka era and Vikrama Samvat, leading to random guessing.
- Students may calculate LCM incorrectly as 45 or 36 by pairing only two numbers; must take LCM of all three: 9, 12, 15.
- The constraint '7 only when followed by 9 and 9 only when preceded by 7' means 7 and 9 appear exclusively together as a pair (79); this conditional constraint is easy to misread.
- Students may not realize that the five persons have unequal numbers and all less than 10, which constrains possible values of C (linking the two groups).
- Candidates often miss 600-609 (where 6 appears as tens digit in every number) and numbers like 616, 626 where 6 appears twice.
