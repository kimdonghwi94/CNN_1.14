from PIL import Image
import glob
import numpy as np

categori = ['A', 'B', 'C', 'D', 'E']
test = '/home/kim/server/alphabet/'
X = []
Y = []

for a, b in enumerate(categori):
    Label = [0 for i in range(len(categori))]
    Label[a] = 1
    print(Label)
    files = glob.glob(test + b + "/*")

    for c, file in enumerate(files):
        img = Image.open(file)

        img = img.convert('L')
        img = np.array(img)
        img = img / 255
        X.append(img)
        Y.append(Label)
X=np.array(X)
Y=np.array(Y)
print(Y)
print(X.shape, Y.shape)
