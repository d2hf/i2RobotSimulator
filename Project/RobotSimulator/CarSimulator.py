
import os
import pygame
from math import tan, radians, degrees, copysign
import math
import numpy as np
from pygame.math import Vector2


class Car:
    def __init__(self, x, y, angle=0, length=20,radius=10):
        self.x= x
        self.y= y
        self.position = np.array([x, y])
        self.angle = angle
        self.length = length
        self.radius= radius
        self.max_velocity = 0.2

        self.tip = [self.x + self.length * math.cos(self.angle), self.y + self.length * math.sin(self.angle)]
        self.bottom = [self.x - self.length * math.cos(self.angle), self.y - self.length * math.sin(self.angle)]
        self.bottom_l = [self.bottom[0] - self.radius * math.sin(self.angle), self.bottom[1] + self.radius * math.cos(self.angle)]
        self.bottom_r = [self.bottom[0] + self.radius * math.sin(self.angle), self.bottom[1] - self.radius * math.cos(self.angle)]

    def go_to_goal(self,theta_a,sum_theta,kp=0.01,ki=0,kd=0):
        x_dis= self.goal_x - self.x
        y_dis= self.goal_y - self.y
        euc_dis= (x_dis**2 + y_dis**2)**(1/2)
        print(euc_dis)

        theta_r = math.atan2(y_dis, x_dis)
        delta_theta= theta_r - self.angle
        omega = kp*math.atan2(math.sin(delta_theta),math.cos(delta_theta)) + sum_theta * ki + (self.angle - theta_a)*kd

        if delta_theta <0:
            vr= self.max_velocity
            vl= vr - (omega*self.length)/self.radius
            v= ((vr+vl)/2)*self.radius

        elif delta_theta>0:
            vl= self.max_velocity
            vr=  vl+(omega*self.length)/self.radius
            v= ((vr+vl)/2)*self.radius

        else:
            v= self.max_velocity
            w=0

        if euc_dis < 50:
            v=0
            w=0
        return [v, omega]

    def goal(self,objetivo):
        self.goal_x = objetivo[0]
        self.goal_y= objetivo[1]


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

        car_x=500;car_y=50;car_ang=0

        black_box= {"theta":car_ang,
                    "theta_a":0,
                    "sum_theta":0}

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
            car.goal(objective)

            car.show(self.screen)

            [vl,w]= car.go_to_goal(black_box["theta_a"],black_box["sum_theta"])
            car_x+=vl*math.cos(car.angle)
            car_y+=vl*math.sin(car.angle)
            car_ang += w

            black_box["theta_a"]= black_box["theta"]
            black_box["sum_theta"]+=black_box["theta"]
            black_box["theta"]=car_ang

            self.screen.blit(objective_image, objective)
            pygame.display.flip()
            clock.tick(1000)
        pygame.quit()


if __name__ == '__main__':
    game = Game()
    game.run()
