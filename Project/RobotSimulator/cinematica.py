import math

'''
to-do-list:
-definir como sera somado delta_t, se utilizar dicionário mov, definir como criar
e colocar um assert para garantir que as infos estejam corretas.

'''

def deltas(x_f,x_i,y_f,y_i):
    '''
    Recebe os pontos do objetivo e as informações do veículo e
    processa tais parametros chegando as informações necessárias
    para atingir o objetivo
    '''
    delta_x= x_f-x_i
    delta_y= y_f-y_i

    return delta_x,delta_y

def PID(e,sum_e=0,e_ant=0,Kp=0.01,Ki=1,Kd=1):
    '''
    PID do veículo
    '''
    PID= e * Kp + sum_e * Ki + (e - e_ant)*Kd
    return PID

def vel_linear(vmax,omega,length,w_radius):
    if omega < 0:
        vr= vmax
        vl = vr - (omega*length)/w_radius
        velocity= ((vr+vl)/2)*w_radius
        return velocity
    elif omega>0:
        vl= vmax
        vr = vl + (omega*length)/w_radius
        velocity=((vr+vl)/2)*w_radius
        return velocity

def go_to_goal(xf,xi,yf,yi,theta,length,radius,mxv,kp=0.01,ki=0.01,kd=0.01):
    delta_x,delta_y= deltas(xf,xi,yf,yi)
    theta_r = math.atan2(delta_y, delta_x)  # Desired heading
    delta_theta= theta_r - theta
    omega = kp*delta_theta    # Only P part of a PID controller to give omega as per desired heading
    if delta_theta <0:
        vr= mxv
        vl= vr - (omega*length)/radius
        v= ((vr+vl)/2)*radius
    else:
        vl= mxv
        vr=  vl+(omega*length)/radius
        v= ((vr+vl)/2)*radius
    return [v, omega]
