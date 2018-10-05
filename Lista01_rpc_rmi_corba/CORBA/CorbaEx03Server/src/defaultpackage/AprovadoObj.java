//ACQUILA SANTOS ROCHA e JULIANA DE MELO TEIXEIRA
package defaultpackage;

import org.omg.CORBA.ORB;

import AprovadoApp.*;
import AprovadoApp.AprovadoPOA;

class AprovadoObj extends AprovadoPOA {
	private ORB orb;
	
	public void setORB(ORB orb_val) {
	    orb = orb_val; 
	}
 
	public int aprovar(double n1, double n2, double n3) {
		int r;
		double M = (n1+n2)/2;
		if (M >= 7.0) {
			r = 1;
		}
		else if (M >= 3.0 && M < 7.0) {
			if ((M+n3)/2 >= 5.0) {
				r = 1;
			}
			else {
				r = 0;
			}
		}
		else {
			r = 0;
		}
		return r;
	}
 
  // implement shutdown() method
	public void shutdown() {
		orb.shutdown(false);
	}
}
