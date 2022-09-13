wk = {"act","god","cat","dog","tac"}


for i in wk:

   for j in wk:
        sorted_str1 = sorted(i)
        sorted_str2 = sorted(j)
        if sorted_str1==sorted_str2:
            print(" string is anagram")

        else:
            print("string is not anagram")