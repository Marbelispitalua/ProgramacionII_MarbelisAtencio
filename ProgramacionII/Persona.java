
package persona;


public class Persona {

  
    public static void main(String[] args) {
        
        Personas P = new Personas();
        
        P.setNombre("Marbelis");
        P.setCedula(1063145199);
        P.setTelefono("3223474678");
        P.setCorreo("matenciopitalua2005@gmail.com");
        
        
        System.out.println("mi nombre es "+ P.nombre); System.out.println("mi cedula "+ P.cedula); System.out.println("por si me quieres llamar "+ P.telefono); System.out.println("mi correo "+ P.correo);
        
    }
    
   
    
}
