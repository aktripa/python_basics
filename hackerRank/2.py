def lst_sort(lst):
    lst.sort(key=lambda x:x[1])
    
    # Drop the lowest score.
    lowest = min(score for _, score in lst)
    lst = [(name, score) for name, score in lst if score > lowest]

    # Drop all EXCEPT the lowest of what remains.
    lowest = min(score for _, score in lst)
    lst = [(name, score) for name, score in lst if score == lowest]

    # Sort and print.
    lst.sort()
    for name, _ in lst:
        print(name)



if __name__ == '__main__':
    lst = []

    for _ in range(int(input())):
        name = input()
        score = float(input())

        lst.append([name,score])

    lst_sort(lst)    

