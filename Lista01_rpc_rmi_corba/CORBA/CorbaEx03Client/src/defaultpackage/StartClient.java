//ACQUILA SANTOS ROCHA e JULIANA DE MELO TEIXEIRA
package defaultpackage;
import java.util.Scanner;

import org.omg.CORBA.ORB;
import org.omg.CosNaming.NamingContextExt;
import org.omg.CosNaming.NamingContextExtHelper;

import AprovadoApp.Aprovado;
import AprovadoApp.AprovadoHelper;
import AprovadoApp.*;

public class StartClient {
	public static void main(String[] args) {
	      try {
		    ORB orb = ORB.init(args, null);
		    org.omg.CORBA.Object objRef =   orb.resolve_initial_references("NameService");
		    NamingContextExt ncRef = NamingContextExtHelper.narrow(objRef);
		    Aprovado addobj = (Aprovado) AprovadoHelper.narrow(ncRef.resolve_str("ABC"));
	 
	            Scanner input=new Scanner(System.in);
	            System.out.println("Sistema de aprovação:");          		    
			    for(;;){
			      System.out.println("Informe a n1:");
			      double n1 = input.nextDouble();
			      System.out.println("Informe a n2:");
			      double n2 = input.nextDouble();
			      System.out.println("Informe a n3:");
			      double n3 = input.nextDouble();
			      int r = addobj.aprovar(n1, n2, n3);
			      if (r == 1) {
			    	  System.out.println("Aprovado!");
				      System.out.println("-----------------------------------");
			      }
			      else {
			    	  System.out.println("Reprovado!");
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
