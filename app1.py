import mysql.connector
from difflib import get_close_matches

con = mysql.connector.connect(
    user="ardit700_student",
    password="ardit700_student",
    host="108.167.140.122",
    database="ardit700_pm1database"
)

cursor = con.cursor()


# word = input("Enter word: ")

def execquery(word):
    query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s' " % word)
    op = cursor.fetchall()
    # cursor.execute("select Expression from Dictionary")
    # bonus = cursor.fetchall()
    # if bonus:
    #     print([item2[0] for item2 in op])
    return op


def execquery2():
    query = cursor.execute("SELECT Expression FROM Dictionary")
    op = cursor.fetchall()
    if op:
        return [item2[0] for item2 in op]
    return op


# def prepare(word):
#     res = execquery(word)
#     return res
#     # if res:
#     #     return res
#     # else:
#     #     return "Please modify your search!!"
#     #

def srch(word):
    print(len(get_close_matches(word, execquery2())))
    word = word.lower()
    data = execquery(word)
    if data:
        return [item[1] for item in data]
    elif execquery(word.title()):
        return execquery(word.title())
    elif execquery(word.upper()):
        return execquery(word.upper())
            # print(it2[1])
    elif len(get_close_matches(word, execquery2())) > 0:
        formed = get_close_matches(word, execquery2())[0]
        yn = input("Did you mean %s instead? Enter Y if Yes , else N: " % formed)
        print(yn)
        if yn == 'Y' or yn == 'y':
            # print([item for item in execquery(formed)])
            return [item[1] for item in execquery(formed)]
        elif yn == 'N' or yn == 'n':
            return "Please re-enter correct word!!!"
        else:
            return "We could not get your request. Please try again"
    else:
        return "The word doesn't exist. Please re-verify!"

word = input("Enter word: ")
output1 = srch(word)
if type(output1) == list:
    for item in output1:
        print(item)
else:
    print(output1)
