//ACQUILA SANTOS ROCHA e JULIANA DE MELO TEIXEIRA
package defaultpackage;
import java.util.Scanner;

import org.omg.CORBA.ORB;
import org.omg.CosNaming.NamingContextExt;
import org.omg.CosNaming.NamingContextExtHelper;

import SalarioApp.Salario;
import SalarioApp.SalarioHelper;
import SalarioApp.*;

public class StartClient {
	public static void main(String[] args) {
	      try {
		    ORB orb = ORB.init(args, null);
		    org.omg.CORBA.Object objRef =   orb.resolve_initial_references("NameService");
		    NamingContextExt ncRef = NamingContextExtHelper.narrow(objRef);
		    Salario addobj = (Salario) SalarioHelper.narrow(ncRef.resolve_str("ABC"));
	 
	            Scanner input=new Scanner(System.in);
	            System.out.println("Sistema para definir novo salário:");          		    
			    for(;;){
			      System.out.println("Informe o nome:");
			      String nome = input.next();
			      System.out.println("Informe o cargo:");
			      String cargo = input.next();
			      System.out.println("Informe o salário atual:");
			      double salario = input.nextDouble();
			      double r;
			      if ("programador".equalsIgnoreCase(cargo)) {
			    	  r = addobj.novoSal1(salario);
			      }
			      else {
			    	  r = addobj.novoSal2(salario);
			      }
			      System.out.println("O novo salário é : "+r);
			      System.out.println("-----------------------------------");
	            }
	       }
	       catch (Exception e) {
	          System.out.println("Hello Client exception: " + e);
		  e.printStackTrace();
	       }
	 
	    }
}
