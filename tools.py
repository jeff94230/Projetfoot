from soccersimulator import Vector2D, SoccerState, SoccerAction
from soccersimulator import Simulation, SoccerTeam, Player, show_simu
from soccersimulator import Strategy
from soccersimulator import settings
import math

GAME_WIDTH = 150                # Longueur du terrain
GAME_HEIGHT = 90                # Largeur du terrain
GAME_GOAL_HEIGHT = 10           # Largeur des buts
PLAYER_RADIUS = 1.              # Rayon d un joueur
BALL_RADIUS = 0.65              # Rayon de la balle
MAX_GAME_STEPS = 2000           # duree du jeu par defaut
maxPlayerSpeed = 1.             # Vitesse maximale d un joueur
maxPlayerAcceleration = 0.2     # Acceleration maximale
maxBallAcceleration = 5         # Acceleration maximale de la balle

#__Nos constantes
GOAL = [Vector2D(0,GAME_HEIGHT//2),Vector2D(GAME_WIDTH,GAME_HEIGHT//2)]



class MyState(object):
    def __init__(self,state,idteam,idplayer):
        self.state = state
        self.key = (idteam,idplayer)
    
    def my_pos(self):
        return self.state.player_state(self.key[0],self.key[1]).position

    def ball_pos(self):
        return self.state.ball.position
        
    def my_goal(self):
        return GOAL[self.key[0]-1]
        
    def adv_goal(self):
        return GOAL[2-self.key[0]]
    
    def myPos_ball(self):
        return self.ball_pos() - self.my_pos()

    def myPos_stg(self,stg):
        return stg - self.my_pos()
    
    def ball_goal(self):
        return self.adv_goal() - self.ball_pos()
        
    def shoot(self,coeff):
        return self.ball_goal() * coeff

    def goTo_ball(self,coeff):
        return self.myPos_ball() * coeff

