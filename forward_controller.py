from controller import Robot, Motor, DistanceSensor

# The time of each step in ms
TIME_STEP = 64
MAX_SPEED = 6.28

robot = Robot()

# initialize proximity sensors
ps = []
psNames = ['Lsensor','Rsensor']
for i in range(2):
    ps.append(robot.getDevice(psNames[i]))
    ps[i].enable(TIME_STEP)

# Get motors devices
LFMotor = robot.getDevice('LFmotor')
LBMotor = robot.getDevice('LBmotor')
RFMotor = robot.getDevice('RFmotor')
RBMotor = robot.getDevice('RBmotor')

LFMotor.setPosition(float('inf'))
LBMotor.setPosition(float('inf'))
RFMotor.setPosition(float('inf'))
RBMotor.setPosition(float('inf'))

LFMotor.setVelocity(0.0)
LBMotor.setVelocity(0.0)
RFMotor.setVelocity(0.0)
RBMotor.setVelocity(0.0)


while robot.step(TIME_STEP) != -1:
    
    # Get proximity sensors values
    psValues = []
    psValues.append(ps[0].getValue())
    psValues.append(ps[1].getValue())
    # CHeck if there is any right or left obstacle
    left_obstacle = psValues[0] < 1000.0
    right_obstacle = psValues[1] < 1000.0
    
    
    # Initialize motors speeds at 50% of max speed 
    LFSpeed = 0.5 * MAX_SPEED
    LBSpeed = 0.5 * MAX_SPEED
    RFSpeed = 0.5 * MAX_SPEED
    RBSpeed = 0.5 * MAX_SPEED
    
    if left_obstacle:
        # turn right 
        LFSpeed = 0.7 * MAX_SPEED
        LBSpeed = 0.7 * MAX_SPEED
        RFSpeed = -1.5 * MAX_SPEED
        RBSpeed = -1.5 * MAX_SPEED
    elif right_obstacle:
        # turn left
        RFSpeed = 0.7 * MAX_SPEED
        RBSpeed = 0.7 * MAX_SPEED
        LFSpeed = -1.5 * MAX_SPEED
        LBSpeed = -1.5 * MAX_SPEED
        
    
    # Write actuators inputs
    LFMotor.setVelocity(LFSpeed)
    LBMotor.setVelocity(LBSpeed)
    RFMotor.setVelocity(RFSpeed)
    RBMotor.setVelocity(RBSpeed)
    
    
    
    
    
    
    
    
    