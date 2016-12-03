from sklearn import datasets

from sklearn.cluster import KMeans
import traceback
from submissions.Ottenlips import billionaires


from submissions.Ottenlips import billionaires

class DataFrame:
    data = []
    feature_names = []
    target = []
    target_names = []

bill = DataFrame()

list_of_billionaire = billionaires.get_billionaires()


def billtarget(billions):
    if billions<3.0:
        return 1
    else:
        return 0


for billionaires in list_of_billionaire:
    # print(billionaires['wealth']['type'])
    # print(billionaires)
    bill.target.append(billtarget(billionaires['wealth']['worth in billions']))
    # bill.target.append(billionaires['wealth']['how']['inherited'])
    bill.data.append([
        float(billionaires['demographics']['age']),
        float(billionaires['location']['gdp']),
        float(billionaires['rank']),
    ])


bill.feature_names = [
    'age',
    'gdp of origin country',
    'rank',
]

bill.target_names = [
    'very rich',
    'less rich',
]


'''
Make a customn classifier,
'''
km = KMeans(
    n_clusters=2,
    # max_iter=300,
    # n_init=10,
    # init='k-means++',
    # algorithm='auto',
    # precompute_distances='auto',
    # tol=1e-4,
    # n_jobs=-1,
    # random_state=numpy.RandomState,
    # verbose=0,
    # copy_x=True,
)

billScaled = DataFrame()

def setupScales(grid):
    global min, max
    min = list(grid[0])
    max = list(grid[0])
    for row in range(1, len(grid)):
        for col in range(len(grid[row])):
            cell = grid[row][col]
            if cell < min[col]:
                min[col] = cell
            if cell > max[col]:
                max[col] = cell

def scaleGrid(grid):
    newGrid = []
    for row in range(len(grid)):
        newRow = []
        for col in range(len(grid[row])):
            try:
                cell = grid[row][col]
                scaled = (cell - min[col]) \
                         / (max[col] - min[col])
                newRow.append(scaled)
            except:
                pass
        newGrid.append(newRow)
    return newGrid

setupScales(bill.data)
billScaled.data = scaleGrid(bill.data)
billScaled.feature_names = bill.feature_names
billScaled.target = bill.target
billScaled.target_names = bill.target_names

Examples = {

   'BillMLPC': {
        'frame': bill,
        'kmeans': km,
},
 'BillMLPCTwo': {
        'frame': bill,
        'kmeans': km,
},
    'BillScaled':{
        'frame':billScaled,
    },
'BillScaled':{
        'frame':billScaled,
    },
    'Bill': {'frame':bill},

}

