#include <Arduino.h>
#include <ros.h>
#include <std_msgs/Float32.h>

int sensorPin = A0;
ros::NodeHandle nh;
std_msgs::Float32 tempC;
ros::Publisher pub("sensor_temperature", &tempC);

void setup()
{
  Serial.begin(9600);  
  nh.initNode();
  nh.advertise(pub);
}
 
void loop()                     
{
 int reading = analogRead(sensorPin);  
 float voltage = reading * 5.0;
 voltage /= 1024.0; 
 
 Serial.print(voltage); Serial.println(" volts");
 
 float temperatureC = (voltage - 0.5) * 100 ;  
 Serial.print(temperatureC); 
 Serial.println(" degrees C");
 
 tempC.data = temperatureC; 
 pub.publish(&tempC);
 nh.spinOnce();

 delay(2000);                                    
}