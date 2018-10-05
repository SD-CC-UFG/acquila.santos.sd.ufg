//ACQUILA SANTOS ROCHA e JULIANA DE MELO TEIXEIRA
package defaultpackage;
import org.omg.CORBA.ORB;

import SalarioApp.*;

class SalarioObj extends SalarioPOA {
	private ORB orb;
	
	public void setORB(ORB orb_val) {
	    orb = orb_val; 
	}
 
	public double novoSal1(double sal) {
		double r = sal + (sal*0.2);
		return r;
	}
  
	public double novoSal2(double sal) {
	    double r = sal + (sal*0.18);
	    return r;
	}
 
  // implement shutdown() method
	public void shutdown() {
		orb.shutdown(false);
	}
}
