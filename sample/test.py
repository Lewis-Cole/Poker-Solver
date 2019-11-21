"""Tests other modules."""


from parse import parse_board, parse_range

print(parse_board("9h6hQc") == ["9h", "6h", "Qc"])

print(
    parse_range("JJ-99,98s")
    == [
        "9c9d",
        "9c9h",
        "9c9s",
        "9d9h",
        "9d9s",
        "9h9s",
        "TcTd",
        "TcTh",
        "TcTs",
        "TdTh",
        "TdTs",
        "ThTs",
        "JcJd",
        "JcJh",
        "JcJs",
        "JdJh",
        "JdJs",
        "JhJs",
        "9c8c",
        "9d8d",
        "9h8h",
        "9s8s",
    ]
)
