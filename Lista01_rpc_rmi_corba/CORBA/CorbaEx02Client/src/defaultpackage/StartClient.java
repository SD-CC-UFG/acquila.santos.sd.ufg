//ACQUILA SANTOS ROCHA e JULIANA DE MELO TEIXEIRA
package defaultpackage;
import java.util.Scanner;

import org.omg.CORBA.ORB;
import org.omg.CosNaming.NamingContextExt;
import org.omg.CosNaming.NamingContextExtHelper;

import MaioridadeApp.Maioridade;
import MaioridadeApp.MaioridadeHelper;
import MaioridadeApp.*;

public class StartClient {
	public static void main(String[] args) {
	      try {
		    ORB orb = ORB.init(args, null);
		    org.omg.CORBA.Object objRef =   orb.resolve_initial_references("NameService");
		    NamingContextExt ncRef = NamingContextExtHelper.narrow(objRef);
		    Maioridade addobj = (Maioridade) MaioridadeHelper.narrow(ncRef.resolve_str("ABC"));
	 
	            Scanner input=new Scanner(System.in);
	            System.out.println("Sistema de maioridade:");          		    
			    for(;;){
			      System.out.println("Informe o sexo:");
			      String sexo = input.next();
			      System.out.println("Informe a idade:");
			      int idade = input.nextInt();
			      int r;
			      if ("feminino".equalsIgnoreCase(sexo)) {
			    	  r = addobj.maioridadeF(idade);
			      }
			      else {
			    	  r = addobj.maioridadeM(idade);
			      }
			      if (r == 1) {
			    	  System.out.println("Maior de idade!");
				      System.out.println("-----------------------------------");
			      }
			      else {
			    	  System.out.println("Menor de idade!");
				      System.out.println("-----------------------------------");
			      }
	            }
	       }
	       catch (Exception e) {
	          System.out.println("Hello Client exception: " + e);
		  e.printStackTrace();
	       }
	 
	    }
}
