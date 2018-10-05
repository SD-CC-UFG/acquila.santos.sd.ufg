//ACQUILA SANTOS ROCHA e JULIANA DE MELO TEIXEIRA
package defaultpackage;
import java.util.Scanner;

import org.omg.CORBA.ORB;
import org.omg.CosNaming.NamingContextExt;
import org.omg.CosNaming.NamingContextExtHelper;

import pesoApp.peso;
import pesoApp.pesoHelper;
import pesoApp.*;

public class StartClient {
	public static void main(String[] args) {
	      try {
		    ORB orb = ORB.init(args, null);
		    org.omg.CORBA.Object objRef =   orb.resolve_initial_references("NameService");
		    NamingContextExt ncRef = NamingContextExtHelper.narrow(objRef);
		    peso addobj = (peso) pesoHelper.narrow(ncRef.resolve_str("ABC"));
	 
	            Scanner input=new Scanner(System.in);
	            System.out.println("Sistema de peso ideal:");          		    
			    for(;;){
			      System.out.println("Informe o sexo:");
			      String sexo = input.next();
			      System.out.println("Informe a altura:");
			      double altura = input.nextDouble();
			      double r;
			      if ("feminino".equalsIgnoreCase(sexo)) {
			    	  r = addobj.pesoF(altura);
			      }
			      else {
			    	  r = addobj.pesoM(altura);
			      }
			      System.out.println("O seu peso ideal é: "+r);
			      System.out.println("-----------------------------------");
	            }
	       }
	       catch (Exception e) {
	          System.out.println("Hello Client exception: " + e);
		  e.printStackTrace();
	       }
	 
	    }
}
