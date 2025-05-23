def compress_string(s):
    if not s:
        return ""

    result = []
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            if count >= 3:
                result.append(f"{s[i - 1]}{count}")
            else:
                result.append(s[i - 1] * count)
            count = 1

    if count >= 3:
        result.append(f"{s[-1]}{count}")
    else:
        result.append(s[-1] * count)

    return ''.join(result)
