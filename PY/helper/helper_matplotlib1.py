import matplotlib.pyplot

x=[1,2,3,4]
y=[2,4,6,7]

def create_graph(y, x):
    matplotlib.pyplot.plot(x, y)
    matplotlib.pyplot.show()
    
if __name__ == '__main__':
    create_graph(y, x)
