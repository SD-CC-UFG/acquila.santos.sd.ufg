//ACQUILA SANTOS ROCHA e JULIANA DE MELO TEIXEIRA
package defaultpackage;

import org.omg.CORBA.ORB;

import pesoApp.*;
import pesoApp.pesoPOA;

class pesoObj extends pesoPOA {
	private ORB orb;
	
	public void setORB(ORB orb_val) {
	    orb = orb_val; 
	}
 
	public double pesoF(double altura) {
		double r;
		r = (62.1*altura)-44.7;
		return r;
	}
	public double pesoM(double altura) {
		double r;
		r = (72.7*altura)-58;
		return r;
	}
 
  // implement shutdown() method
	public void shutdown() {
		orb.shutdown(false);
	}
}
