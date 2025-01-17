from typing import Any

import yaml
import numpy as np


def time_taken(tickets: list[int], k: int) -> int:
    res = 0
    m = tickets[k]
    
    for i in range(k):
        if tickets[i] >= m: res += m
        else: res += tickets[i]
        
    for i in range(k, len(tickets)):
        if tickets[i] >= m: res += m - 1
        else: res += tickets[i]
            
    return res + 1


if __name__ == "__main__":
    # Let's solve Time Needed to Buy Tickets problem from leetcode.com:
    # https://leetcode.com/problems/time-needed-to-buy-tickets/
    with open("practicum_4/time_needed_to_buy_tickets_cases.yaml", "r") as f:
        cases = yaml.safe_load(f)
    for c in cases:
        res = time_taken(tickets=c["input"]["tickets"], k=c["input"]["k"])
        print(f"Input: {c['input']}. Output: {res}. Expected output: {c['output']}")
