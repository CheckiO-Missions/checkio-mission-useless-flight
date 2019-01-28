"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [[
                ['A', 'B', 50],
                ['B', 'C', 40],
                ['A', 'C', 100]
            ]],
            "answer": [2]
        },
        {
            "input": [[
                ['A', 'B', 50],
                ['B', 'C', 40],
                ['A', 'C', 90]
            ]],
            "answer": []
        },
        {
            "input": [[
                ['A', 'B', 50],
                ['B', 'C', 40],
                ['A', 'C', 40]
            ]],
            "answer": []
        },
        {
            "input": [[
                ['A', 'C', 10],
                ['C', 'B', 10],
                ['C', 'E', 10],
                ['C', 'D', 10],
                ['B', 'E', 25],
                ['A', 'D', 20],
                ['D', 'F', 50],
                ['E', 'F', 90],
            ]],
            "answer": [4, 7]
        },
    ],
    "Extra": [
        {
            "input": [[
                ['A', 'C', 10],
                ['C', 'B', 10],
                ['C', 'E', 10],
                ['C', 'D', 10],
                ['B', 'E', 25],
                ['A', 'D', 20],
                ['D', 'F', 50],
                ['E', 'F', 70],
            ]],
            "answer": [4]
        },
    ]
}
