

void serialOutput(){  
  switch(outputType){
    case PROCESSING_VISUALIZER:
      sendDataToSerial('S', Signal);    
      break;
    case SERIAL_PLOTTER:  
      Serial.print(BPM);
      Serial.print(",");
      Serial.print(IBI);
      Serial.print(",");
      Serial.println(Signal);
      break;
    default:
      break;
  }

}

void serialOutputWhenBeatHappens(){
  switch(outputType){
    case PROCESSING_VISUALIZER:    // find it here https://github.com/WorldFamousElectronics/PulseSensor_Amped_Processing_Visualizer
      sendDataToSerial('B',BPM);  
      sendDataToSerial('Q',IBI);  
      break;

    default:
      break;
  }
}

void sendDataToSerial(char symbol, int data ){
    Serial.print(symbol);
    Serial.println(data);
  }
