from pico2d import *
from boy import Boy
from grass import Grass
# Game object class here
def handle_events():
    global running
    # get_event : pico2d내부 정의 함수
    #사용자의 입력 이벤트를 감지하여 리스트 형태로 돌려주는 함수
    #event.type , event.key , event.x , event.y 등의 속성이 있음
    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
            boy.handle_event(event) # SPACE 들어오면, 소년에게 전달.

def reset_world():
    global world
    global boy

    world = [] # list

    grass = Grass()
    world.append(grass) #append : list 내장 함수

    boy = Boy()
    world.append(boy)

def update_world():
    for o in world:
        o.update()
    pass
def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()
running = True

open_canvas()
reset_world()
# game loop
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.01)
# finalization code
close_canvas()