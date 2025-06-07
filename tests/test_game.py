import pytest

from game import Entity


def test_move_within_bounds():
    e = Entity(0, 0)
    e.move(3, 4, bounds=(10, 10))
    assert (e.x, e.y) == (3, 4)


def test_move_clamped_to_bounds():
    e = Entity(8, 8, width=2, height=2)
    e.move(5, 5, bounds=(10, 10))
    # should be clamped so entity stays in bounds
    assert (e.x, e.y) == (8, 8)


def test_collision_true():
    a = Entity(0, 0, width=2, height=2)
    b = Entity(1, 1, width=2, height=2)
    assert a.collides_with(b)
    assert b.collides_with(a)


def test_collision_false():
    a = Entity(0, 0, width=2, height=2)
    b = Entity(3, 3, width=2, height=2)
    assert not a.collides_with(b)
    assert not b.collides_with(a)
