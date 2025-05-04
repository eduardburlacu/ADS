from enum import Enum, auto
from typing import NamedTuple, List, Set, FrozenSet, Tuple, Optional
import random
from random import choice, randint

class Direction(Enum):
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()

    def opposite(self)->"Direction":
        match self:
            case Direction.UP:
                return Direction.DOWN
            case Direction.DOWN:
                return Direction.UP
            case Direction.LEFT:
                return Direction.RIGHT
            case Direction.RIGHT:
                return Direction.LEFT


class Tile(NamedTuple("Tile",[
    ("row",int),
    ("column",int),
])):

    def move(self, direction:Direction)->"Tile":
        match direction:
            case Direction.UP:
                return Tile(self.row+1, self.column)
            case Direction.DOWN:
                return Tile(self.row-1, self.column)
            case Direction.LEFT:
                return Tile(self.row, self.column-1)
            case Direction.RIGHT:
                return Tile(self.row, self.column+1)

    def neighbors(self)->List["Tile"]:
        ns =[]
        for dr in [-1,0,1]:
            for dc in [-1,0,1]:
                if dr==0 and dc==0:
                    continue
                ns.append(
                    Tile(self.row+dr, self.column+dc)
                )
        return ns

    def distance_to(self, other:"Tile"):
        """
        Returns the Manhattan distance to the other Tile
        """
        return abs(self.row-other.row) + abs(self.column-other.column)

def get_room(open_tiles:Set[Tile], t:Tile)->Set[Tile]:
    """
    Run DFS starting from t
    """
    stack = [t]
    room = {t}
    while stack:
        node = stack.pop()
        for neighbor in node.neighbors():
            if neighbor in open_tiles and neighbor not in room:
                stack.append(neighbor)
                room.add(neighbor)
    return room

def room_dividers(
        open_tiles:Set[Tile],
        walls: Set[Tile],
        room: Set[Tile]
)->Set[Tile]:
    """
    Returns the set of wall tiles which separate
     a room from other rooms
    """
    dividers = set()
    for node in room:
        for d in Direction:
            wall = node.move(d)
            if wall in walls:
                floor = wall.move(d)
                if floor in open_tiles and floor not in room:
                    dividers.add(wall)
    return dividers

def generate_maze(rows:int, columns:int)->Set[Tile]:
    """
    Generate a random tomb
    """
    walls, floors = set(), set()
    for r in range(rows):
        for c in range(columns):
            if not(r%2 and c%2):
                floors.add(Tile(r,c))
            else:
                walls.add(Tile(r, c))

    for tile in floors:
        walls_curr = []
        for d in Direction:
            tile_wall = tile.move(d)
            tile_n = tile_wall.move(d)
            if tile_n in floors and tile_wall in walls:
                walls_curr.append(tile_wall)

        w = choice(walls_curr)
        walls.remove(w)
        floors.add(w)
        for tile in floors:
            room = get_room(floors ,tile)
            if room == floors:
                return walls, floors

            room_divs = room_dividers(room, walls, floors)
            separation_wall = choice(room_divs)
            walls.remove(separation_wall)
            floors.add(separation_wall)
    return walls, floors

class Boulder( NamedTuple("Boulder"),[("tile", Tile),("direction", Direction)]):
    def step(self, open_tiles:Set[Tile], boulder_tiles: Set[Tile]):
        for boulder in boulder_tiles:
            next_tile = boulder.move(self.direction)
            previous_tile = boulder.move(self.direction.opposite())
            if next_tile in open_tiles and next_tile not in boulder_tiles:
                return Boulder(next_tile, self.direction)
            elif previous_tile in open_tiles and previous_tile not in boulder_tiles:
                return Boulder(previous_tile, self.direction.opposite())
            return self

class Tomb(NamedTuple("Tomb", [
    ("rows", int),
    ("columns", int),
    ("start",Tile),
    ("goal", Tile),
    ("open_tiles", FrozenSet[Tile]),
    ("boulders", Tuple[Boulder]),
])):

    @staticmethod
    def create(rows:int, columns:int, num_boulders: int, seed:int):
        random.seed(seed)
        walls, open_tiles = generate_maze(rows, columns)
        c_start, c_end = randint(0, columns - 1), randint(0, columns - 1)
        start_tile = Tile(1, c_start),
        end_tile = Tile(rows - 1, c_end)

        walls = frozenset(walls)
        open_tiles =frozenset(open_tiles)
        boulder_tiles = set()
        boulders = set()

        directions = [d for d in Direction]
        num = 0
        while num < num_boulders:
            tile_boulder = choice(open_tiles)
            if tile_boulder not in boulder_tiles and tile_boulder not in {start_tile, end_tile}:
                boulder_tiles.add(tile_boulder)
                num+=1

        for tile in tile_boulder:
            d = directions[randint(4)]
            boulders.add(Boulder(tile, d))


        return Tomb(
            rows, columns,
            start_tile,
            end_tile,
            open_tiles,
            boulder_tiles
        )

    def step(self):
        boulder_tiles = {boulder.tile for boulder in self.boulders}
        boulders = (boulder.step(self.open_tiles, boulder_tiles) for boulder in self.boulders)
        return self._replace(boulders=boulders)

    def a_star(self, ):
        pass

    def solve(self)->Optional[List[Tile]]:
        path = [self.start]
        tile = self.start
        while tile != self.goal:
            next_tile = self.a_star()
            path.append(next_tile)
            self.step()




if __name__=="__main__":
    generate_maze(3,2)