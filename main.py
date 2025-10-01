import render

def run(filename, color):
    try:
        render.plot(filename, color)
    except UserWarning:
        render.plot(filename,'purple')

run('yellowstone','blue')
