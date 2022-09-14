def words(list):
    vowel_l = ['a', 'e', 'i', 'o', 'u', 'y']
    for x in list:
        i = 0
        if x[0] not in vowel_l:
            while x[i] not in vowel_l:
                x = x[(i+1):] + x[i]
            print(x + 'ay')
        else:
            print(x + 'yay')

s_l = input().split()
words(s_l)
#done