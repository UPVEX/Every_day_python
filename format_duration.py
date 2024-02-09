#codewars challenge
#https://www.codewars.com/kata/52742f58faf5485cae000b9a/




def format_duration(seconds):
    if seconds == 0:
        return "now"

    years, seconds = divmod(seconds, 365 * 24 * 3600)
    days, seconds = divmod(seconds, 24 * 3600)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)

    components = []

    if years:
        components.append(f"{years} year{'s' if years > 1 else ''}")

    if days:
        components.append(f"{days} day{'s' if days > 1 else ''}")

    if hours:
        components.append(f"{hours} hour{'s' if hours > 1 else ''}")

    if minutes:
        components.append(f"{minutes} minute{'s' if minutes > 1 else ''}")

    if seconds:
        components.append(f"{seconds} second{'s' if seconds > 1 else ''}")

    if len(components) == 1:
        return components[0]
    else:
        return ', '.join(components[:-1]) + f" and {components[-1]}"


user_input = int(input("enter your seconds : "))

result = format_duration(user_input)
print(result)