'''
Rewrite the grade program from the previous chapter using a function called computegrade
that takes a score as its parameter and returns a grade as a string.
'''

def computergrade(score):
    try:
        score = float(score)
    except ValueError:
        return "Bad Score"

    if score >= 0.9:
        return "A"
    elif score >= 0.8:
        return "B"
    elif score >= 0.7:
        return "C"
    elif score >= 0.6:
        return "D"
    elif score < 0.6:
        return "F"
    else:
        return "Bad Score"

print(computergrade("perfect"))