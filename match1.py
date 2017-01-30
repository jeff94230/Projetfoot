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




# Creation des des joueurs
joueur_1 = Player("1",Fonceur_niveau3())
joueur_2 = Player("2",Fonceur_niveau1())

# Creations des equipes
equipe_1 = SoccerTeam("Equipe_1",[joueur_1])
equipe_2 = SoccerTeam("Equipe_2",[joueur_2])

# Creation d'un match
match = Simulation(equipe_1,equipe_2,2000)

#Demarrer le match
show_simu(match)
