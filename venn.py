from matplotlib import pyplot as plt
from matplotlib_venn import venn3,venn3_unweighted,venn3_circles
items=[80,43,6,62,18,3,15]
labels=['set1','set2','set3']
venn3_unweighted(subsets=items,set_labels=labels)
plt.show()
