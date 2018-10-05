//ACQUILA SANTOS ROCHA e JULIANA DE MELO TEIXEIRA
package defaultpackage;
import java.util.Scanner;

import org.omg.CORBA.ORB;
import org.omg.CosNaming.NamingContextExt;
import org.omg.CosNaming.NamingContextExtHelper;

import nadadorApp.nadador;
import nadadorApp.nadadorHelper;
import nadadorApp.*;

public class StartClient {
	public static void main(String[] args) {
	      try {
		    ORB orb = ORB.init(args, null);
		    org.omg.CORBA.Object objRef =   orb.resolve_initial_references("NameService");
		    NamingContextExt ncRef = NamingContextExtHelper.narrow(objRef);
		    nadador addobj = (nadador) nadadorHelper.narrow(ncRef.resolve_str("ABC"));
	 
	            Scanner input=new Scanner(System.in);
	            System.out.println("Sistema de categoria nadador:");          		    
			    for(;;){
			      System.out.println("Informe a idade:");
			      int idade = input.nextInt();
			      
			      String r = addobj.pesoF(idade);
			      
			      System.out.println("A sua categoria é: "+r);
			      System.out.println("-----------------------------------");
	            }
	       }
	       catch (Exception e) {
	          System.out.println("Hello Client exception: " + e);
		  e.printStackTrace();
	       }
	 
	    }
}
