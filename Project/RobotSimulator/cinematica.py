import math

'''
to-do-list:
-definir como sera somado delta_t, se utilizar dicionário, definir como criar
e colocar um assert para garantir que as infos estejam corretas.

'''

def deltas(x_f,x_i,y_f,y_i,t_pos):
    '''
    Recebe os pontos do objetivo e as informações do veículo e
    processa tais parametros chegando as informações necessárias
    para atingir o objetivo
    '''
    delta_x= x_f-x_i
    delta_y= y_f-y_i
    delta_t= math.atan2(delta_y,delta_x)-t_p
    
    return delta_x,delta_y,delta_t

def PID(e,sum_e,e_ant,Kp,Ki,Kd):
    '''
    PID do veículo
    '''
    PID= e * Kp + sum_e * Ki + (e - e_ant)*Kd
    return PID
