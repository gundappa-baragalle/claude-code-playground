# Probability

**Subject:** CSAT > Quantitative Aptitude
**Syllabus ID:** CSAT.QA.1
**Total Questions:** 11 (Prelims: 11, Mains: 0)
**Year Range:** 1995 – 2008
**Last Asked:** 2008
**Revision Priority:** 🔴 HIGH

## Keywords
probability, CSAT, conditional probability, Bayes theorem, coins, 0.25, complementary events, traffic light, 7/12, balls in bag

## Dimensions Tested
- **HOW**: 11 questions

## Related Concepts
- Total probability
- Mutually exclusive events
- Combinations
- Event probability
- Probability distributions
- Counting principles
- Binomial probability
- Boltzmann distribution

## Prelims Questions

### 🔴 HIGH Priority — Full MCQ + Trap Intelligence

*Use these verbatim as Practice MCQs in CDF notes.*

**[Q1771]** [2000]
> A bag contains 20 balls. 8 balls are green, 7 are white and 5 are red. What is the minimum number of balls that must be picked up from the bag blind-folded (without replacing any of it) to be assured of picking at least one ball of each colour ?

     A) 4
     B) 7
     C) 11
  ✅ D) 16

  ⚠️ **Trap:** Candidates may calculate minimum balls to get any two colors (8+7+1=16 is the worst case for at least one of each) without accounting for worst-case scenario logic.
  💡 **Eliminate:** Worst case: pick all 8 green and all 7 white (15 balls) with no red. Next ball must be red. So minimum = 15+1 = 16. Answer D.
  📌 **Key facts:**
     - Pigeonhole principle: worst case requires exhausting largest groups before guaranteed diversity
     - Min balls for at least one of each = (all of largest group) + (all of second group) + 1

### 🟡 MEDIUM Priority — Full Options

**[Q2166]** [2008] There are 6 different letters and 6 correspondingly addressed envelopes. If the letters are randomly put in the envelopes, what is the probability that exactly 5 letters go into the correctly addressed envelopes?

  ✅ A) zero
     B) 1/6
     C) 1/2
     D) 5/6

  ⚠️ **Trap:** Students think it is possible for exactly 5 letters to be correct, forgetting that if 5 are correct the 6th must also be correct by elimination.

**[Q2625]** [2007] Three dice (each having six faces with each face having one number from 1 to 6) are rolled. What is the number of possible outcomes such that at least one dice shows the number 2?

     A) 36
     B) 81
  ✅ C) 91
     D) 116

  ⚠️ **Trap:** Candidates may calculate P(at least one shows 2) directly and make errors; using complementary counting (1 - P(none shows 2)) is more reliable but students often forget to subtract from total outcomes.

**[Q1967]** [2006] 3 digits are chosen at random from 1, 2, 3, 4, 5, 6, 7, 8 and 9 without repeating any digit. What is the probability that their product is odd?

     A) 2/3
     B) 5/108
  ✅ C) 5/42
     D) 7/48

  ⚠️ **Trap:** Product is odd only when ALL three digits chosen are odd. Candidates may not restrict to odd digits only and compute incorrectly.

**[Q1926]** [2004] Three students are picked at random from a school having a total of 1000 students. The probability that these three students will have identical data and month of their birth is:

     A) 3/1000
     B) 3/365
  ✅ C) 1/(365)^2
     D) None of these

  ⚠️ **Trap:** Students may compute probability as 3/365 thinking only about matching months, forgetting that both date AND month must match between three specific students.

**[Q704]** [2002] A complete cycle of a traffic light takes 60 seconds. During each cycle the light is green for 25 second, yellow for 5 second and red for 30 second. At a randomly chosen time, the probability that the light will not be green is

     A) 1/3
     B) 1/4
     C) 5/12
  ✅ D) 7/12

  ⚠️ **Trap:** Candidates may calculate P(green) = 25/60 and then subtract from 1, but may make arithmetic errors; the straightforward calculation is (30+5)/60 = 35/60 = 7/12.

**[Q2826]** [1997] When three coins are tossed together the probability that all coins have the same face up is

     A) 1/3
     B) 1/6
  ✅ C) 1/8
     D) 1/12

  ⚠️ **Trap:** Students may count only the all-heads case (1/8) and forget that all-tails also satisfies 'same face up'; both cases must be counted.

**[Q3708]** [1997] There are three drawers in a table. One contains two gold coins, another two silver coins, and the third, a silver coin and a gold coin. One of the drawers is pulled out and a coin is taken out. It turns out to be a silver coin. What is the probability of drawing a gold coin, if one of the other two drawers is pulled out next and one of the coins in it is drawn at random ?

     A) 37.5%
  ✅ B) 50%
     C) 62.5%
     D) 75%

  ⚠️ **Trap:** Candidates may compute the probability for just the second draw without accounting for conditional probability from the first draw revealing a silver coin from a mixed drawer.

**[Q4787]** [1996] Two packs of cards are thoroughly mixed and stuffed and two cards are drawn at random, one after the other. What is the probability that both of them are Jacks?

     A) 1/13
     B) 2/13
  ✅ C) 7/1339
     D) 1/169

  ⚠️ **Trap:** Two packs = 104 cards with 8 Jacks total. Candidates may use 1/13 × 1/13 = 1/169 (treating draws as independent), ignoring the without-replacement condition.

**[Q212]** [1995] A table has three drawers. It is known that one of the drawers contains two silver coins, another contains two gold coins and the third one contains a silver coin and a gold coin. One of the drawers is opened at random and a coin is drawn. It is found to be a silver coin. What is the probability that the other coin in the drawer is a gold coin ?

  ✅ A) 0.25
     B) 1.00
     C) 0.50
     D) 0.60

  ⚠️ **Trap:** Most students answer 1/3 or 1/2 by assuming equal probability among drawers. The correct approach uses conditional probability (Bayes' theorem): given a silver coin is drawn, the probability it came from the mixed drawer is 1/3, not 1/2.

### 🟢 LOW Priority — Reference Stubs

- **[Q1927]** [2005] Ten identical particles are moving randomly inside a closed box. What is the probability that at any given point of time all the t...
  - Dim: HOW | Ans: D

## Exam Patterns & Insights

- **Most tested dimension:** HOW (11/11 = 100% of questions)
- **Question types (Prelims):** CSAT: 11
- **Trend:** Not asked since 2008 — lower probability but classic syllabus topic

### Common Trap Patterns on This Topic
- Most students answer 1/3 or 1/2 by assuming equal probability among drawers. The correct approach uses conditional probability (Bayes' theorem): given a silver coin is drawn, the probability it came from the mixed drawer is 1/3, not 1/2.
- Candidates may calculate P(green) = 25/60 and then subtract from 1, but may make arithmetic errors; the straightforward calculation is (30+5)/60 = 35/60 = 7/12.
- Candidates may calculate minimum balls to get any two colors (8+7+1=16 is the worst case for at least one of each) without accounting for worst-case scenario logic.
- Students may compute probability as 3/365 thinking only about matching months, forgetting that both date AND month must match between three specific students.
- Students may think probability is simply (1/2)^10 or use combinatorics incorrectly. This is a challenging statistical mechanics problem dressed as simple probability.
