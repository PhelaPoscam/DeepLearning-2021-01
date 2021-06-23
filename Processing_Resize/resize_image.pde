PImage[] pics; //i want to put all of the files in data/ in here

void setup() {

String path = sketchPath("")+"/data/";
File[] files = listFiles(path);

print(path+"\n");
print(files.length+"\n"); //how many files are here
println();

size(74, 74);

pics=new PImage[files.length];


for(int i=0;i<files.length;i++) {
println(files[i]);
  

// I really want to be able to:
PImage img=loadImage(files[i].getName());
//but there is a type mismatch, as files is an array of File, and load image wants a string
//can I do a simple conversion?
    imageMode(CENTER);
      
  background(0);
  img.resize(74,0);
  img.filter(GRAY);
  image(img, width/2, height/2, img.width, img.height);
  save(files[i].getName());

}

}


//taken from http://processing.org/learning/topics/directorylist.html
File[] listFiles(String dir) {
 File file = new File(dir);
 if (file.isDirectory()) {
   File[] files = file.listFiles();
   return files;
 } else {
   // If it's not a directory
   return null;
 }
}
