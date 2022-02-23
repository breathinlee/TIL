def change(words):
    answer = ''
    words = list(words)

    for word in words:
        if word.islower():
            result = ord('z') - (ord(word) - ord('a'))
            answer += chr(result)
        elif word.isupper():
            if word == 'Z':
                answer += 'A'
            else:
                answer += chr(ord(word) + 1)
        else:
            if word.isdigit():
                if word == '0':
                    answer += str(word)
                else:
                    answer += str(10 - int(word))

    return answer


print(change("123abcABC"))
print(change("i0Lg8HZ"))


# output
# ["987zyxBCD"]
# ["r0Mt2IA"]