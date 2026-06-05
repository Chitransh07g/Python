first = [1, 2, 3]
second = [4, 5, 6]

merged = first + second
simi = merged

# ye tarika  original list ko modify krta h ....(aur ".sort " kuch return nhi krta h )
merged.sort(reverse=True)
print (merged)


# agr original list ko badalna nhih to ye trika 
similar = sorted(simi , reverse=True)
print (similar)