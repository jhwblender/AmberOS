void setup(){
  size(90,90);
  background(0);
  stroke(255);
  
  noSmooth();
}

void draw(){
  //clear();
  for(int i=0; i<200; i++){
    point(random(90),random(90));
  }

}