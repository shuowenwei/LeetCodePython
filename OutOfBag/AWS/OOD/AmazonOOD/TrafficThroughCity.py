
# https://leetcode.com/discuss/interview-question/object-oriented-design/2032949/Amazon-or-Onsite-or-Traffic-Through-City

from typing import List, Set, Callable
from enum import Enum

class Timer:
    def __init__(self, interval: int) -> None:
        self.time = 0
        self.interval = interval
    def tick(self) -> int:
        self.time += self.interval

class Road:
    def __init__(self, size: int) -> None:
        self.size = size

class Actor:
    def update(self) -> None:
        raise NotImplemented()

class Car(Actor):
    def __init__(self, road: Road, section: int = 0, speed: int = 1, dir: int = +1) -> None:
        self.road: Road = road
        self.section: int = section
        self.dir: int = dir
        self.speed: int = speed

    def update(self):
        if self.section < 0 or self.section > self.road.size:
            return

        self.section += self.speed * self.dir

class LightState(Enum):
    GREEN, YELLOW, RED = range(3)      
  
class Light(Actor):
    def __init__(self, road: Road, section: int = 0) -> None:
        self.road: Road = road
        self.section: int = section
        self.state: LightState = LightState.GREEN

    def update(self) -> None:
        self.state = LightState((self.state.value + 1) % len(LightState))

class Engine:
    def __init__(self, timer: Timer) -> None:
        self.timer: Timer = timer
        self.actors: set[Actor] = set()
        self.beforeCallbacks: list[Callable[[Engine], None]] = list()
        self.afterCallbacks: list[Callable[[Engine], None]] = list()

    def render(self) -> None:
        self.timer.tick()

        for before in self.beforeCallbacks:
            try: before(self)
            except Exception as e: 
                print('(*ﾟﾛﾟ)', e)

        for a in self.actors:
            a.update()

        for after in self.afterCallbacks:
            try: after(self)
            except Exception as e: 
                print('(*ﾟﾛﾟ)', e)

    def start(self):
        limit = 10
        while limit:
            limit -= 1
            self.render()

road = Road(10)
car = Car(road)
cars: Set[Car] = set([car])
light = Light(road, 2)
light2 = Light(road, 6)
lights: Set[Light] = set([light, light2])

timer = Timer(1)
engine = Engine(timer)
engine.actors.add(car)
engine.actors.add(light)
engine.actors.add(light2)

def before(engine: Engine) -> None:
    for car in cars:
        for light in lights:
            if car.road == light.road and car.section == light.section:
                if light.state is LightState.RED:
                    car.speed = 0
                elif car.speed == 0:
                    car.speed = 1

def after(engine: Engine) -> None:
    for car in cars:
        print(f'section: {car.section} speed: {car.speed}')
        for light in lights:
            if car.road == light.road and car.section == light.section:
                print(f'light: {light.state.name}')

engine.beforeCallbacks.append(before)
engine.afterCallbacks.append(after)

engine.start()
