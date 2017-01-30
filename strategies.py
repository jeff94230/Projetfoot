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


from tools import *

class Fonceur_niveau1(Strategy):
    
    def __init__(self):
        Strategy.__init__(self,"Fonceur")
        
    def compute_strategy(self,state,id_team,id_player):
        etat = MyState(state,id_team,id_player)
        return SoccerAction(etat.myPos_ball(),etat.ball_goal())


class Fonceur_niveau2(Strategy):
    
    def __init__(self):
        Strategy.__init__(self,"Fonceur")
        
    def compute_strategy(self,state,id_team,id_player):
        etat = MyState(state,id_team,id_player)
        if etat.myPos_ball().norm <= (PLAYER_RADIUS + BALL_RADIUS):
            return SoccerAction(etat.myPos_ball(),etat.ball_goal())
        return SoccerAction(etat.myPos_ball(),Vector2D())
        

class Fonceur_niveau3(Strategy):
    
    def __init__(self):
        Strategy.__init__(self,"Fonceur")
        
    def compute_strategy(self,state,id_team,id_player):
        STG = [Vector2D(5,GAME_HEIGHT//2),Vector2D(GAME_WIDTH-5,GAME_HEIGHT//2)]
        my_etat = MyState(state,id_team,id_player)
        adv_etat = MyState(state,3-id_team,id_player)
        
        if my_etat.myPos_ball().norm >= adv_etat.myPos_ball().norm:
            if my_etat.myPos_ball().norm <= (PLAYER_RADIUS + BALL_RADIUS):
                return SoccerAction(my_etat.myPos_ball(),my_etat.ball_goal())
            return SoccerAction(my_etat.myPos_ball(),Vector2D())
        
        return SoccerAction(my_etat.myPos_stg(STG[id_team-1]),Vector2D())
