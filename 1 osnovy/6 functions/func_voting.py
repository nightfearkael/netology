def vote(votes):
    # your code
    counter = 0
    result = 0
    for item in votes:
        if votes.count(item) > counter:
            counter = votes.count(item)
            result = item
    return result


if __name__ == '__main__':
    print(vote([1, 1, 1, 2, 3]))
    print(vote([1, 2, 3, 2, 2]))
