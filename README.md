# Netflix Movies Analysis — 1990s Edition 🎬

Every dataset hides a story. This one asks: **what did a "typical" movie look like in the 1990s?**

As a biotechnologist moving into data analysis, I used this project to practice the
core of the data workflow — asking a clear question, filtering data with intent,
and letting the numbers answer.

## The Questions ❓
- **What was the most frequent movie duration** in the 1990s (1990 as decade start)?
- **How many short action movies** (under 90 minutes) were released that decade?

## Tools & Skills 🛠️
- **Python** · **pandas** · **matplotlib**
- Boolean indexing & vectorized operations
- `.mode()` for central tendency · `.sum()` on boolean masks for counting
- Data visualization with styled histograms

## Approach 🔍
1. Filtered the dataset to movies released in the 1990s
2. Computed the mode of movie duration
3. Counted short action movies using a vectorized boolean mask
4. Visualized the full duration distribution with a histogram

## Key Findings 💡
- **Most frequent duration:** ~95 minutes (approximate)
- **Short action movies in the 1990s: 7

## How to Run ▶️
```bash
pip install pandas matplotlib
Use your favourite software