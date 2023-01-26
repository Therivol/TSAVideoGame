from game.component.Collider import Collider
from game.object.Object import Object
import pygame as p


class Collision:
    collision_layers = ["TERRAIN", "DEFAULT", "DEFAULT"]
    objects = {layer: {} for layer in collision_layers}

    @staticmethod
    def add(obj):
        Collision.objects[obj.get_component(Collider).layer][obj.get_id()] = obj

    @staticmethod
    def remove(obj):
        del Collision.objects[obj.get_component(Collider).layer][obj.get_id()]

    @staticmethod
    def clear():
        Collision.objects = {layer: {} for layer in Collision.collision_layers}

    @staticmethod
    def process_removals():
        for layer in Collision.collision_layers:
            Collision.objects[layer] = {obj.get_id(): obj for obj in Collision.objects[layer]
                                        if not obj.is_queued_for_removal}

    @staticmethod
    def update():
        Collision.resolve()

    @staticmethod
    def resolve():
        for layer in Collision.objects:
            for obj in Collision.objects[layer].values():
                collider = obj.get_component(Collider)

                if obj.transform.is_static:
                    continue

                for x in Collision.search(collider):
                    hit = x.get_component(Collider)
                    if hit.is_trigger:
                        hit.set_manifold(True, collider)
                        continue

                    m = collider.intersects(hit)
                    if m.colliding:
                        collider.resolve_overlap(m)
                        collider.reset_manifold()

    @staticmethod
    def search(collider):
        overlapping_objects = []

        for layer in collider.collide_layers:
            for obj_id, obj in Collision.objects[layer].items():
                if obj.get_component(Collider).get_rect().colliderect(collider.get_rect()):
                    overlapping_objects.append(obj)

        return overlapping_objects

    @staticmethod
    def load_level(map_data, tile_size):
        i = 0
        for y, row in enumerate(map_data):
            for x, tile in enumerate(row):
                if tile == '0':
                    continue
                obj = Object(str(i))
                collider = Collider(obj)
                collider.set_rect(p.Rect(0, 0, tile_size, tile_size), (0, 0))
                collider.set_layer("TERRAIN")
                obj.add_component(collider)
                obj.transform.set_position((x * tile_size, y * tile_size))
                Collision.add(obj)

                i += 1
