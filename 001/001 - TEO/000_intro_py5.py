import py5


def setup():
    py5.size(500, 500)
    py5.fill("#00D92F")
    py5.rect(150, 150, 200, 200)
    py5.save("/img/testing/000_intro_py5.png")


py5.run_sketch()
