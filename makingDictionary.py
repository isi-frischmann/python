
list1 = ['lucas', 'isi']
list2 = ['dog', 'horse']

# merge both lists into one >> result = [('lucas', 'dog'), ('isi', 'horse')]
both = zip(list1, list2)

# create a dic with dict() from both. 
# It takes the first tuple for KEY(isi,lucas) and the second tuple for VALUE(dog, horse) in the dictionary
d = dict(both)

# print it
print d