# Permutation and Combination

**Subject:** CSAT > Quantitative Aptitude
**Syllabus ID:** CSAT.QA.1
**Total Questions:** 37 (Prelims: 37, Mains: 0)
**Year Range:** 2003 – 2010
**Last Asked:** 2010
**Revision Priority:** 🔴 HIGH

## Keywords
CSAT, permutation, combination, counting, combinations, combinatorics, arrangement, distribution, tournament, nC2

## Dimensions Tested
- **HOW**: 37 questions

## Related Concepts
- Circular permutations
- CSAT permutation problems
- Seating arrangements
- Grid-based counting
- Ball-box distribution problems
- Arrangements with constraints
- Constraint satisfaction
- Counting methods

## Prelims Questions

### 🔴 HIGH Priority — Full MCQ + Trap Intelligence

*Use these verbatim as Practice MCQs in CDF notes.*

**[Q115]** [2010]
> In a tournament 14 teams play league matches. If each team plays against every other team once only then how many matches are played ?

     A) 105
  ✅ B) 91
     C) 85
     D) 78

  ⚠️ **Trap:** Students may add instead of use combination formula; some compute 14×13=182 (without dividing by 2). Round-robin format means each pair plays once.
  💡 **Eliminate:** Total matches = C(14,2) = 14×13/2 = 91. Answer: B.
  📌 **Key facts:**
     - Round-robin tournament: n(n-1)/2 matches for n teams
     - C(14,2) = 91

**[Q3463]** [2010]
> A paper had ten questions. Each could only be answered as True (T) or False (F). Each candidate answered all the questions. Yet, no two candidates wrote the answers in an identical sequence. How many different sequences of answers are possible?

     A) 20
     B) 40
     C) 512
  ✅ D) 1024

  ⚠️ **Trap:** Students may multiply 10×2 = 20, confusing the number of options with sequential combinations. Each of 10 questions has 2 options — this is 2^10, not 10×2.
  💡 **Eliminate:** Each of 10 questions: 2 choices (T or F). Total sequences = 2^10 = 1024. Answer: D.
  📌 **Key facts:**
     - 2^10 = 1024 unique True/False sequences for 10 questions
     - Fundamental counting principle: multiply independent choices

**[Q4359]** [2010]
> A person X has four notes of Rupee 1, 2, 5 and 10 denomination. The number of different sums of money she can form from them is

     A) 16
  ✅ B) 15
     C) 12
     D) 8

  ⚠️ **Trap:** Candidates often include zero (no notes used) and get 16 instead of 15, forgetting that a 'sum' implies at least one note must be used.
  💡 **Eliminate:** Each note is either included or not: 2⁴ = 16 combinations, minus 1 (no notes) = 15 valid sums.
  📌 **Key facts:**
     - Number of non-empty subsets of n items = 2ⁿ − 1
     - Here: 2⁴ − 1 = 15

**[Q4368]** [2010]
> When ten persons shake hands with one another, in how many ways is it possible ?

     A) 20
     B) 25
     C) 40
  ✅ D) 45

  ⚠️ **Trap:** Candidates sometimes calculate 10×9=90 (ordered pairs) instead of combinations, or forget to use nC2.
  💡 **Eliminate:** Each handshake involves choosing 2 from 10 people: 10C2 = 10!/(2!×8!) = 45.
  📌 **Key facts:**
     - Handshakes formula = nC2 = n(n-1)/2
     - For 10 persons: 10×9/2 = 45

**[Q4533]** [2010]
> Each person's performance compared with all other persons is to be done to rank them subjectively. How many comparisons are needed in total, if there are 11 persons?

     A) 66
  ✅ B) 55
     C) 54
     D) 45

  ⚠️ **Trap:** Students may simply multiply 11×11=121 or do 11! instead of recognizing this is a combination problem (pairwise comparisons = nC2).
  💡 **Eliminate:** Pairwise comparisons of 11 persons = 11C2 = 11×10/2 = 55. Each pair compared once in total. Answer: 55.
  📌 **Key facts:**
     - Pairwise comparisons = nC2 = n(n-1)/2
     - For 11 persons: 11×10/2 = 55 comparisons

**[Q4888]** [2010]
> In how many ways can four children be made to stand in a line such that two of them, A and B are always together ?

     A) 6
  ✅ B) 12
     C) 18
     D) 24

  ⚠️ **Trap:** Students may treat AB as one unit but forget to also arrange A and B within that unit (2 ways), leading to answer 6 instead of 12.
  💡 **Eliminate:** Treat AB as one unit → 3 units in a line = 3! = 6 arrangements; A and B can switch within unit = 2 ways. Total = 6 × 2 = 12.
  📌 **Key facts:**
     - Grouping method: treat AB as 1 unit → 3! arrangements × 2! within unit = 12
     - Always multiply internal arrangements when grouping

**[Q3102]** [2009]
> A person has 4 coins each of different denomination. What is the number of different sums of money the person can form (using one or more coins at a time) ?

     A) 16
  ✅ B) 15
     C) 12
     D) 11

  ⚠️ **Trap:** Students may calculate 2^4 = 16 total subsets but forget to subtract the empty set (no coin selected), giving 15.
  💡 **Eliminate:** With 4 coins, number of non-empty subsets = 2^4 - 1 = 15; each subset gives a unique sum since coins have different denominations.
  📌 **Key facts:**
     - For n distinct denominations: number of distinct sums = 2^n - 1
     - Power set minus empty set approach gives all possible selections

**[Q1994]** [2008]
> A schoolteacher has to select the maximum possible number of different groups of 3 students out of a total of 6 students. In how many groups any particular student will be included?

     A) 6
     B) 8
  ✅ C) 10
     D) 12

  ⚠️ **Trap:** A particular student included in a group of 3 from 6: candidates may compute C(6,3)=20 and subtract groups without that student C(5,3)=10, getting 10 — which is correct.
  💡 **Eliminate:** Fix one particular student, choose 2 from remaining 5: C(5,2) = 10 groups. Answer: C.
  📌 **Key facts:**
     - Groups including a specific person = C(n-1, r-1) = C(5,2) = 10
     - Complementary: C(6,3) - C(5,3) = 20 - 10 = 10

**[Q4865]** [2006]
> In a tournament each of the participants was to play one match against each of the other participants. 3 players fell ill after each of them had played three matches and had to leave the tournament. What was the total number of participants at the beginning, if the total number of matches played was 75?

     A) 8
     B) 10
     C) 12
  ✅ D) 15

  ⚠️ **Trap:** Students may set up the equation incorrectly by not accounting for the matches already played by the 3 players who dropped out, leading to wrong total.
  💡 **Eliminate:** If n players total, matches without dropouts = nC2. But 3 dropped after 3 matches each: remaining = (n-3)C2 + 3×3 = 75. Solve: (n-3)(n-4)/2 + 9 = 75; n=15.
  📌 **Key facts:**
     - Total matches = (n-3)C2 + 9 = 75 gives n = 15
     - Combination formula nC2 = n(n-1)/2

**[Q1045]** [2005]
> A square is divided into 9 identical smaller squares. Six identical balls are to be placed in these smaller squares such that each of the three rows gets at least one ball (one ball in one square only). In how many different ways can this be done?

     A) 27
     B) 36
     C) 54
  ✅ D) 81

  ⚠️ **Trap:** Candidates confuse placing 6 balls in 9 squares (with at least one per row) with simpler distribution problems; overcounting or undercounting rows is common.
  💡 **Eliminate:** Each row has 3 squares; choose one square per row for guaranteed coverage (3×3×3=27 ways), then distribute remaining 3 balls freely among all 9 squares giving 9³=729... approach carefully using inclusion-exclusion or structured logic giving 81.
  📌 **Key facts:**
     - Answer: 81 (3^4 approach)
     - Each row must have at least one of 6 balls in 9 squares

**[Q1952]** [2005]
> There are 6 persons-A, B, C, D, E and F. They are to be seated in a row such that B never sits any where ahead of A and C never sits any where ahead of B. In how many different ways can this be done?

     A) 60
     B) 72
  ✅ C) 120
     D) None of the above

  ⚠️ **Trap:** Candidates may think the constraint (B not ahead of A, C not ahead of B) simply eliminates some permutations, but the answer is 6!/3! = 120 since exactly 1/6 of arrangements satisfy the ordering constraint.
  💡 **Eliminate:** Total arrangements of 6 persons = 720. Exactly 1/6 satisfy A before B before C (since all 3! orderings are equally likely). 720/6 = 120. Answer: C.
  📌 **Key facts:**
     - For 3 elements with a fixed relative order, divide total permutations by 3! = 6
     - 6!/3! = 120

**[Q4857]** [2005]
> On a railway route between two places A and B there are 10 stations on the way. If 4 new stations are to be added, how may types of new tickets will be required if each ticket is issued for a oneway journey?

     A) 14
     B) 48
     C) 96
  ✅ D) 108

  ⚠️ **Trap:** Candidates calculate total new tickets needed but forget to include tickets FROM new stations TO new stations (4×3=12) and FROM new to existing+endpoints (4×12=48) and FROM existing+endpoints TO new (12×4=48). Total new = 4×12+12×4−4×4+4×3 is the confusion.
  💡 **Eliminate:** Total stations after adding 4 = A+10+4+B = 16 stations. Old total one-way tickets = 12×11=132. New total = 16×15=240. New tickets required = 240−132=108. Answer D.
  📌 **Key facts:**
     - Total stations (including A and B) = 2+10+4=16; one-way tickets = n(n-1) = 16×15=240; original = 12×11=132; new tickets = 108

**[Q4677]** [2004]
> Nine different letters are to be dropped in three different letter boxes. In how many different ways can this be done?

     A) 27
  ✅ B) 19683
     C) 729
     D) 19680

  ⚠️ **Trap:** Candidates may apply 9! (permutations) or compute 3×9=27 (wrong approach) instead of recognizing each letter has 3 independent choices.
  💡 **Eliminate:** Each letter independently goes into any of 3 boxes: 3 choices × 3 choices × ... (9 times) = 3⁹ = 19683.
  📌 **Key facts:**
     - Each item distributed independently: n boxes, k items → n^k arrangements
     - 3⁹ = 19,683

**[Q4662]** [2003]
> Three flags, each of different colour, are available for a military exercise. Using these flags, different codes can be generated by waving (i) Single flag of different colours, or (ii) Any two flags in a different sequence of colours, or (iii) Three flags in a different sequence of colour The maximum number of codes that can be generated is

     A) 6
     B) 9
  ✅ C) 15
     D) 18

  ⚠️ **Trap:** Candidates forget to add up all three cases — single flags (3), two-flag sequences (3P2=6), three-flag sequences (3P3=6) — total 15, not just one case.
  💡 **Eliminate:** Single: 3 codes. Two flags (ordered): 3×2=6. Three flags (ordered): 3×2×1=6. Total: 3+6+6=15.
  📌 **Key facts:**
     - Permutation: ordered arrangement; P(n,r) = n!/(n-r)!
     - Sum of cases: single (3) + two-flag (6) + three-flag (6) = 15

### 🟡 MEDIUM Priority — Full Options

**[Q68]** [2009] In a carrom board game competition, m boys and n girls (m > n > 1) of a school participate in which every student has to play exactly one game with every other student. Out of the total games played, it was found that in 221 games one player was a boy and the other-player was a girl. Consider the following statements : 1. The total number of students that participated in the competition is 30. 2. The number of games in which both players were girls is 78. Which of the statements given above is/are correct ?

     A) 1 only
     B) 2 only
  ✅ C) Both 1 and 2
     D) Neither 1 nor 2

  ⚠️ **Trap:** Students may set up mn = 221 directly but 221 = 13×17, so m=17, n=13. Statement 2 requires nC2 = 13×12/2 = 78 — students often forget to verify both statements.

**[Q2327]** [2009] How many three-digit numbers can be generated from 1, 2, 3, 4, 5, 6, 7, 8, 9 such that the digits are in ascending order

     A) 80
     B) 81
     C) 83
  ✅ D) 84

  ⚠️ **Trap:** Students may try to enumerate or use permutations; since digits must be in ascending order, choosing any 3 digits from 9 automatically gives one ascending arrangement — this is a combination problem.

**[Q1479]** [2008] In how many different ways can four books A, B, C and D be arranged one above another in a vertical order such that the books A and B are never in continuous position?

     A) 9
     B) 12
     C) 14
  ✅ D) 18

  ⚠️ **Trap:** Students often compute total arrangements minus arrangements where A and B are adjacent, but may miscalculate the 'A and B together' cases by not treating them as a block correctly.

**[Q2960]** [2008] There are two identical red, two identical black and two identical white balls. In how many different ways can the balls be placed in the cells (each cell to contain one ball) shown above such that balls of the same colour do not occupy any two consecutive cells?

     A) 15
  ✅ B) 18
     C) 24
     D) 30

  ⚠️ **Trap:** The constraint 'no two consecutive cells with same colour' requires careful case enumeration. Treating all arrangements as independent without the adjacency constraint leads to overcounting.

**[Q3291]** [2008] In how many different ways can all of 5 identical balls be placed in the cells shown above such that each row contains at least 1 ball?

     A) 64
     B) 81
     C) 84
  ✅ D) 108

**[Q1356]** [2007] Five balls of different colours are to be placed in three different boxes such that any box contains at least one ball. What is the maximum number of different ways in which this can be done?

     A) 90
  ✅ B) 120
     C) 150
     D) 180

  ⚠️ **Trap:** Candidates often use only combinations without considering that boxes are distinct and the 'at least one ball' constraint requires inclusion-exclusion.

**[Q1362]** [2007] In how many maximum different ways can 3 identical balls be placed in the 12 squares (each ball to be placed in the exact centre of the squares and only one ball is to be placed in one square) shown in the figure given above such that they do not lie along the same straight line?

     A) 144
     B) 200
     C) 204
  ✅ D) 216

  ⚠️ **Trap:** Candidates often calculate total combinations (C(12,3) = 220) and subtract only obvious collinear sets, missing diagonal lines.

**[Q1363]** [2007] Groups each obtaining 3 boys are to be formed out of 5 boys—A, B, C, D and E such that no one group contains both C and D together. What is the maximum number of such different groups?

     A) 5
     B) 6
  ✅ C) 7
     D) 8

  ⚠️ **Trap:** Candidates may forget to subtract ONLY groups containing both C AND D; they calculate all groups with C plus all with D and double-subtract.

**[Q2623]** [2007] Amit has five friends: 3 girls and 2 boys. Amit’s wife also has 5 friends: 3 boys and 2 girls. In how many maximum number of different ways can they invite 2 boys and 2 girls such that two of them are Amit’s friends and two are his wife’s?

     A) 24
     B) 38
  ✅ C) 46
     D) 58

  ⚠️ **Trap:** Students may fail to account for all combinations: Amit's 2 friends can be (2 boys, 0 girls), (1 boy, 1 girl), or (0 boys, 2 girls) while maintaining overall 2 boys 2 girls constraint. Missing cases leads to wrong answer.

**[Q2624]** [2007] All the six letters of the name SACHIN are arranged to form different words without repeating any letter in any one word. The words so formed are then arranged as in a dictionary. What will be the position of the word SACHIN in that sequence?

     A) 436
     B) 590
  ✅ C) 601
     D) 751

  ⚠️ **Trap:** Arranging SACHIN in dictionary order requires counting permutations of letters starting with A, C, H, I, N before reaching S — a multi-step process that candidates often miscalculate.

**[Q2644]** [2007] In the figure shown, what is the maximum number of different ways in which 8 identical balls can be placed in the small triangles 1, 2, 3 and 4 such that each triangle contains at least one ball?

  ✅ A) 32
     B) 35
     C) 44
     D) 56

  ⚠️ **Trap:** This is a stars and bars (partitioning) problem with constraints. Candidates may confuse it with simple combination or forget the 'at least one ball per triangle' condition.

**[Q3620]** [2007] Each of the 3 persons is to be given some identical items such that product of the numbers of items received by each of the three persons is equal to 30. In how many maximum different ways can this distribution be done?

     A) 21
     B) 24
  ✅ C) 27
     D) 33

  ⚠️ **Trap:** Candidates may only count ordered triplets of factors of 30 without accounting for all permutations including repeated values, undercounting arrangements.

**[Q1958]** [2006] A box contains five set of balls while there are three balls in each set. Each set of balls has one colour which is different from every other set. What is the least number of balls that must be removed from the box in order to claim with certainly that a pair of balls of the same colour has been removed?

  ✅ A) 6
     B) 7
     C) 8
     D) 9

  ⚠️ **Trap:** The question asks for pairs (minimum 2 of same colour) — candidates may think they need 11 draws (5×2+1) but the structure of 5 sets of 3 means after 6 draws, by pigeonhole principle, two must share a color.

**[Q1966]** [2006] A mixed doubles tennis games is to be played between two teams (each team consists of one male and one female). There are four married couples. No team is to consist of a husband and his wife. What is the maximum number of games that can be played?

     A) 12
     B) 21
     C) 36
  ✅ D) 42

  ⚠️ **Trap:** Students may compute total team pairings without applying the husband-wife constraint, yielding 12 × 12 = 144 / 2 = 72 games; the correct constraint analysis gives 42.

**[Q1284]** [2005] 2 men and 1 women board a bus in which 5 seats are vacant. One of these five seats is reserved for ladies. A woman may or may not sit on the seat reserved for ladies but a man can not sit on the seat reserved for ladies. In how may different ways can the five seats be occupied by these three passengers?

     A) 15
  ✅ B) 36
     C) 48
     D) 60

  ⚠️ **Trap:** Students may forget that the woman has the OPTION of either sitting in the reserved seat or in the other 4 seats, and men can only sit in 4 of the 5 seats. Overcounting or undercounting arrangements is common.

**[Q553]** [2004] In how many different ways can six players be arranged in a line such that two of them, Ajit and Mukherjee, are never together?

     A) 120
     B) 240
     C) 360
  ✅ D) 480

  ⚠️ **Trap:** Students calculate total arrangements (6! = 720) and forget to subtract properly; the complement method requires subtracting cases where Ajit and Mukherjee ARE together.

**[Q3029]** [2003] A two member committee comprising of one male and one female member is to be constituted out of five males and three females. Amongst the females. Ms. A refuses to be a member of the committee in which Mr. B is taken as the member. In how many different ways can the committee be constituted?

     A) 11
     B) 12
     C) 13
  ✅ D) 14

### 🟢 LOW Priority — Reference Stubs

- **[Q1110]** [2006] How many numbers are there in all from 6000 to 6999 (both 6000 and 6999 included) having at least one of their digits repeated?
  - Dim: HOW | Ans: C
- **[Q1144]** [2006] In a paper, there are four multiple-choice questions. Each has five choices with only one choice for its correct answer. What is t...
  - Dim: HOW | Ans: C
- **[Q1151]** [2006] Each of 8 identical balls is to be placed in the squares shown in the figures given in a horizontal direction such that one horizo...
  - Dim: HOW | Ans: A
- **[Q1156]** [2006] Each of 8 identical balls is to be placed in the squares shown in the figures given in a horizontal direction such that one horizo...
  - Dim: HOW | Ans: B
- **[Q1178]** [2006] Each of two women and three men is to occupy one chair out of eight chairs, each of which is numbered from one to right. First, wo...
  - Dim: HOW | Ans: C
- **[Q4467]** [2004] In a of a test paper, there are five items each under List-A and List-B. The examinees are required to match each item under List-...
  - Dim: HOW | Ans: C

## Exam Patterns & Insights

- **Most tested dimension:** HOW (37/37 = 100% of questions)
- **Question types (Prelims):** CSAT: 37
- **Trend:** Not asked since 2010 — lower probability but classic syllabus topic

### Common Trap Patterns on This Topic
- Students may set up mn = 221 directly but 221 = 13×17, so m=17, n=13. Statement 2 requires nC2 = 13×12/2 = 78 — students often forget to verify both statements.
- Students may add instead of use combination formula; some compute 14×13=182 (without dividing by 2). Round-robin format means each pair plays once.
- Students calculate total arrangements (6! = 720) and forget to subtract properly; the complement method requires subtracting cases where Ajit and Mukherjee ARE together.
- Candidates confuse placing 6 balls in 9 squares (with at least one per row) with simpler distribution problems; overcounting or undercounting rows is common.
- Students may calculate total numbers (1000) minus all-distinct digits (9×9×8×7 = 4536 is wrong approach for 4-digit numbers starting with 6). Confusing complementary counting steps leads to wrong answer.
