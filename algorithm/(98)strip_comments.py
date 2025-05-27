#codewars challenge
#https://www.codewars.com/kata/51c8e37cee245da6b40000bd/




def strip_comments(text, comment_markers):
    lines = text.split('\n')
    result_lines = []

    for line in lines:
        for marker in comment_markers:
            index = line.find(marker)
            if index != -1:
                line = line[:index].rstrip()

        result_lines.append(line)

    result = '\n'.join(result_lines)
    return result

# example:
text_input = "apples, pears # and bananas\ngrapes\nbananas !apples"
comment_markers = ["#", "!"]
result = strip_comments(text_input, comment_markers)
print(result)
# Output: "apples, pears\ngrapes\nbananas"
