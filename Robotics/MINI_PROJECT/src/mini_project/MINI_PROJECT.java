/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package mini_project;

import ch.aplu.robotsim.Gear;
import ch.aplu.robotsim.LegoRobot;
import ch.aplu.robotsim.LightSensor;
import ch.aplu.robotsim.RobotContext;
import ch.aplu.robotsim.SensorPort;

/**
 *
 * @author bhakt
 */
public class MINI_PROJECT {

   MINI_PROJECT(){
        LegoRobot r=new LegoRobot();
        Gear g = new Gear();
        LightSensor ls= new LightSensor(SensorPort.S3);
        r.addPart(g);
        r.addPart(ls);
        g.forward();
        g.setSpeed(100);
        while(true){
        int v =ls.getValue();

        if(v >= 1000)
        g.forward();
        if(v < 1000)
        g.left();
        if(v < 100)
        g.stop();

    }
    }
    static {
        RobotContext.setStartPosition(430,200);
        RobotContext.useBackground("sprites/yellowpath.gif");
    }
    public static void main (String[] args) {
        new MINI_PROJECT();
    }
}
