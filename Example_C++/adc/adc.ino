/*
PHOTONTECH 
  S-Core ADC örneği
  
  S-Core üzerinde ki 26. pine bağlı potansiyometre çevrildikçe okunan değer print komutu ile ekrana yazdırılıyor.
   
  Bu örnek kod C++ ile yazılarak PHOTONTECH tarafından kamuya sunulmuştur.
  
  https://github.com/GitPhotontech/Photontech_S-Core
  
*/
#define potpin 28 //Potansiyometreyi 28. pine tanımladık.


int deger = 0; //"deger" adlı 0 başlangıçlı bir değişken tanımlandı.


void setup() {
  Serial1.begin(115200); //115200 Baund bir seri haberleşme başlatıldı.  
}


void loop() {
  deger = analogRead(potpin); //"deger" değişkeni potansiyometrenin değerine göre değişir
  Serial1.print("Potansiyometre Değeri : "); 
  Serial1.println(deger); //Okunan değer seri monitörde mesaj olarak gönderilir.
  delay(100); //Bu işlem 100 milisaniye aralıklarla yapılır
}
