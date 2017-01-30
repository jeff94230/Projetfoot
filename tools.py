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

