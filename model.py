import random
import shar, pygame
import staya

st = staya.Staya(200, 500, 200, 500, "krug", 10)

st2 = staya.Staya(700, 1000, 100, 400, "romb", 10)

def go1():
    st.go()
    st2.go()
