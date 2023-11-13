with open("Question.txt", 'r') as f_obj:
    con = f_obj.read().lower().split()
    x = con.count('a')
    print(x)
