def greedy_children_cookie_distribution(g: list[int],s: list[int]) -> int:
    # g is array containing greed factors of children
    # s is array containing size of the cookie
    # greed factor will be satisfied if same or more size of cookie is available for the child.
    g.sort(reverse = True)
    s.sort(reverse = True)
    result, i, j = 0, 0, 0
    while i < len(g) and j < len(s):
        if g[i] <= s[j]:
            result += 1
            i += 1
            j += 1
        else:
            i += 1
    return result

print(greedy_children_cookie_distribution([1,2],[1,2,3]))

# Approach is to sort both the arrays. We sort so that the morst greedy child gets the biggest cookie available.
# If the cookie size is favourable (>= greed factor) then result is incremented along with i and j.
# If the cookie size is not favourable (< greed factor) then only i is incremented and we move to the next child.