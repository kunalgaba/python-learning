rankings = ["kunal", "ketav", "gaba", "sachit", "namit", "saksham"]

rankings.append("aadit")
rankings.remove("gaba")

rankings.insert(0,"shivi")
rankings.extend(["crow", "sparrow"])

print(rankings, len(rankings))

rankings.pop()
print(rankings, len(rankings))

title_case_rankings=[player.title() for player in rankings]
print(title_case_rankings, len(title_case_rankings))

rankings.clear()
print(rankings, len(rankings))
