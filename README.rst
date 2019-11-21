Poker Solver
============

Inputs:
    - IP range in text form : "QQ+,AKs"
    - OOP range in text form : "JJ-99,98s"
        - different types of segments: 
            - "AhAs", "AA", "AKs", "AKo", "KK+", "AQs+", "AQo+", "KK-QQ", "AQs-AJs", "AQo-AJo"

    - board in text form        : "9h6hQc" ; "QdTh4cQc" ; "7dQsAc5s4s"

Output:
    - equity distribution data as spreadsheet or graph


**METHOD**

- Parse text
    - parse board
        - split board into cards
        - group as 'board' : list
    - parse ranges
        - split range into segments of similar holdings
        - Parse each segment into individual holdings
        - transform text holdings into objects
        - group as 'Range': object / list

- Find an individual IP holding's equity vs OOP range
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

- Iterate through each holding in IP range
    - store result

- Graph data as either histogram or density plot


**FILES**

parse.py
    - for parsing text of board and range into useful format

compare_holdings.py
    - determine equity between two holdings on possible runouts

compare_hands.py
    - determine which hand is a winner between two hands of 7 cards

compare_ranges.py
    - determine equity between two ranges for possible holdings

graph_data.py
    - covert raw data into either excel spreadsheet, historgram or density plot
