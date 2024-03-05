import pygame

import math

import time

from default_settings import (
    ENEMY_BASE_DAMAGE,
    ENEMY_BASE_HEALTH,
    ENEMY_BASE_SPAWN_COOLDOWN,
    ENEMY_BASE_SPEED,
    ENEMY_BASE_WORTH,
    ENEMY_SIZE,
)

from sprites import enemy_group, sprites_group, bullet_sprites_group

from player import *


class Enemy(pygame.sprite.Sprite):

    def __init__(self, position):
        super().__init__(enemy_group, sprites_group)
        self.image = pygame.image.load("assets/enemy/enemy.png")
        self.image = pygame.transform.rotozoom(self.image, 0, ENEMY_SIZE)
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.x = position[0]
        self.y = position[1]
        self.direction = pygame.math.Vector2()
        self.velocity = pygame.math.Vector2()
        self.position = pygame.math.Vector2(position)
        self.health = ENEMY_BASE_HEALTH
        self.damage = ENEMY_BASE_DAMAGE
        self.speed = ENEMY_BASE_SPEED
        self.worth = 10
        self.count = 0
        self.hit_interval = PLAYER_HIT_INTERVAL
        self.last_bullet = None

    def pathing(self):
        player_vector = pygame.math.Vector2(player.hitbox.center)
        enemy_vector = pygame.math.Vectbullet_hit = Vector2(self.rect.center)
        distance = (player_vector - enemy_vector).magnitude()

        if not pygame.sprite.collide_rect(self, player):
            self.direction = (player_vector - enemy_vector).normalize()
            self.timer = 0
            self.damage_applied = False
        else:
            self.count += 1
            self.direction = pygame.math.Vector2()
            if self.count == 1:
                self.timer = time.time()
                self.damage_applied = False

            if (not self.damage_applied) and (time.time() -
                                              self.timer) >= self.hit_interval:
                player.health -= self.damage
                self.count = 0
                self.damage_applied = True

        self.velocity = self.direction * self.speed
        self.position += self.velocity

        self.rect.centerx = self.position.x
        self.rect.centery = self.position.y

    def hit(self):
        bullet_collisions = 0
        
        bullet_hit = pygame.sprite.spritecollide(self, bullet_sprites_group,
                                                 player.penetrationStatus)
        for bullet in bullet_hit:
            if bullet != self.last_bullet:
                self.health -= bullet.damage
                self.last_bullet = bullet
                
    def death(self):
        chance = random.randint(0,10)
        if self.health <= 0:
            player.money = round(player.money + self.worth, 2)

            if chance == 10:
                player.stat_points += 1

            self.kill()

    def update(self):
        self.pathing()
        self.hit()
        self.death()

    def calculate_distance(self, vector_1, vector_2):
        return vector
