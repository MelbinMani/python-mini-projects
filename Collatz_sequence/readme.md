# Collatz Sequence Simulator

This is a simple Python CLI tool that simulates the **Collatz sequence** for any positive integer input. It prints each step of the transformation and counts how many steps it takes to reach 1.

---

## 🧠 What is the Collatz Hypothesis?

The **Collatz conjecture** (also known as the 3n + 1 problem) is an unsolved mathematical puzzle proposed by Lothar Collatz in 1937.

It states:

> Start with any positive integer `n`.  
> If `n` is even → divide it by 2  
> If `n` is odd → multiply by 3 and add 1  
> Repeat the process.  
> Eventually, you will reach the number 1.

Despite its simplicity, no one has proven whether this always holds true for all positive integers.

---

## 🚀 How to Run

Make sure you have Python installed. Then run:

```bash
python collatz_sequence.py

## 🧪 Sample Input/Output

**Input:**Enter any non-negative and non-zero integer number: 6
**Output:**6 3 10 5 16 8 4 2 1 Steps: 8
