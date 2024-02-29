package Clase_vehiculos;

public class Vehiculos {

    String marca;
    String modelo;
    Integer CaballosDeFuerza;
    String traccion;
    String velocidad_maxima;


   public Vehiculos(String marca, String modelo, Integer caballosDeFuerza,String traccion,String velocidad_maxima) {
    this.marca = marca;
    this.modelo = modelo;
    this.CaballosDeFuerza = caballosDeFuerza;
    this.velocidad_maxima = velocidad_maxima;
    this.traccion = traccion;
    
   }

   public Vehiculos(){


   }

    public String getTraccion() {
        return traccion;
    }

    public void setTraccion(String traccion) {
        this.traccion = traccion;
    }

    public String getVelocidad_maxima() {
        return velocidad_maxima;
    }

    public void setVelocidad_maxima(String velocidad_maxima) {
        this.velocidad_maxima = velocidad_maxima;
    }


    public String getMarca() {
        return marca;
    }


    public void setMarca(String marca) {
        this.marca = marca;
    }


    public String getModelo() {
        return modelo;
    }


    public void setModelo(String modelo) {
        this.modelo = modelo;
    }


    public Integer getCaballosDeFuerza() {
        return CaballosDeFuerza;
    }


    public void setCaballosDeFuerza(Integer caballosDeFuerza) {
        CaballosDeFuerza = caballosDeFuerza;
    }



}
