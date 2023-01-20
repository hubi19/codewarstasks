def find_needle(haystack):

    position = 0

    for word in haystack:

        position += 1
        if word == "needle":

            return f"found the needle at position {position-1}"

print(find_needle(["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]))