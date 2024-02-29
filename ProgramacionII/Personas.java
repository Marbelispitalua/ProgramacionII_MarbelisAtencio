
package persona;


public class Personas {
    
    String nombre;
    
    int cedula;
    
    String telefono;
    
    String correo;
    
    
    public Personas(String nombre,int cedula,String telefono,String correo){
        
       this.nombre = nombre;
       this.cedula = cedula;
       this.telefono = telefono;
       this.correo = correo;
        
    }
    
    public Personas(){
        
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public int getCedula() {
        return cedula;
    }

    public void setCedula(int cedula) {
        this.cedula = cedula;
    }

    public String getTelefono() {
        return telefono;
    }

    public void setTelefono(String telefono) {
        this.telefono = telefono;
    }

    public String getCorreo() {
        return correo;
    }

    public void setCorreo(String correo) {
        this.correo = correo;
    }
    
    
    
    
}
