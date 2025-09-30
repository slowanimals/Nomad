import render

def run(filename, color):
    try:
        render.plot(filename, color)
    except UserWarning:
        render.ploy(filename,'purple')

run('alaska','blue')
