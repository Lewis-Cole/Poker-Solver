# Poker Solver

---

### Inputs:
    - IP and OOP range in text form : e.g. "QQ+,AKs", "JJ-99,98s"
        - This should contain various segments seperated by ","
            - "AhAs", "AA", "AKs", "AKo", "KK+", "AQs+", "AQo+", "KK-QQ", "AQs-AJs", "AQo-AJo"
    
    - board in text form : e.g. "9h6hQc" ; "QdTh4cQc" ; "7dQsAc5s4s"

### Output:
    - equity distribution data as spreadsheet or graph

---

## Method

### Parse text
    - parse board
        - split board into cards
        - group as 'board' : list
    - parse ranges
        - split range into segments of similar holdings
        - Parse each segment into individual holdings
        - transform text holdings into objects
        - group as 'range': list

### Find an individual IP holding's equity vs OOP range
    - take one holdings from OOP range
    - calculate equity for IP holding vs OOP holding
        - deal one possible runout
        - group board and holdings and IP hand vs OOP hand
        - compare hands
            - determine the poker value of each hand
            - if not equal, determine winner
                - which hand has higher value
            - if equal, determine winner
                - compare secondary features i.e. kickers
        - store result
        - iterate through every possible runout
    - iterate through every holding in OOP range and take the average

### Iterate through each holding in IP range
    - store result

### Graph data as either histogram or density plot

---

## Files

parse.py
    - parses text inputs into the appropriate format

rules.py
    - rules of poker and basic data

hand.py
    - Hand class with built in methods   
        - determine which hand is a winner between two hands of 7 cards

comparison.py
    - contains comparison functions:
        - compare_ranges
            - determine equity between two ranges for possible holdings
        - compare_holdings
            - determine equity between two holdings on possible runouts

graph_data.py
    - covert raw data into either excel spreadsheet, historgram or density plot
