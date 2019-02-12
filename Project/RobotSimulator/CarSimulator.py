
import os
import pygame
from math import tan, radians, degrees, copysign
import numpy as np
from cinematica import *
from pygame.math import Vector2


class Car:
    def __init__(self, x, y, angle=0, length=15,radius=10):
        self.x= x
        self.y= y
        self.position = np.array([x, y])
        self.angle = angle
        self.length = length
        self.radius= radius
        self.max_velocity = 0.1
        self.tip = [self.x + self.length * math.cos(self.angle), self.y + self.length * math.sin(self.angle)]
        self.bottom = [self.x - self.length * math.cos(self.angle), self.y - self.length * math.sin(self.angle)]
        self.bottom_l = [self.bottom[0] - self.radius * math.sin(self.angle), self.bottom[1] + self.radius * math.cos(self.angle)]
        self.bottom_r = [self.bottom[0] + self.radius * math.sin(self.angle), self.bottom[1] - self.radius * math.cos(self.angle)]

    def go_to_goal(self,objetivo):
        kp=0.001
        print('distx: ',objetivo[0]-self.x,'\nx1: ',objetivo[0],
        '\nx2: ',self.x)
        theta_r = math.atan2(objetivo[0]-self.x,objetivo[1]-self.y)
        delta_theta= theta_r - self.angle
        omega=  delta_theta * kp

    def update(self, objetivo):
        [v,w]=go_to_goal(objetivo[0],self.position[0],
        objetivo[1],self.position[1],self.angle,self.length,
        self.radius,self.max_velocity)
        return [v,w]

    def show(self,screen):
        pygame.draw.polygon(screen, (255,0,0), [self.tip, self.bottom_l, self.bottom_r], 0)

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Differential Robot Simulator")
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.ticks = 300
        self.exit = False

    def run(self):
        clock = pygame.time.Clock()
        ticks = pygame.time.get_ticks()
        objective_path = os.path.join("flag.png")
        objective_image = pygame.image.load(objective_path)
        objective = Vector2(272.5, 265.5)
        self.screen.blit(objective_image, objective)
        pygame.display.flip()
        car_x=30;car_y=600;car_ang=0
        i=1

        while not self.exit:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit = True

                if event.type == pygame.MOUSEBUTTONUP:
                    objective = pygame.mouse.get_pos()
                    self.screen.blit(objective_image, objective)
                    pygame.display.flip()
                    self.clock.tick(self.ticks)
                    print(objective)

            self.screen.fill((0, 0, 0))
            car = Car(car_x, car_y,car_ang)
            car.show(self.screen)
            car.go_to_goal(objective)

            [vl,w]= car.update(objective)
            car_x+=vl*math.cos(car.angle)
            car_y+=vl*math.sin(car.angle)
            car_ang += w

            self.screen.blit(objective_image, objective)
            pygame.display.flip()
            clock.tick(300)
        pygame.quit()


if __name__ == '__main__':
    game = Game()
    game.run()
