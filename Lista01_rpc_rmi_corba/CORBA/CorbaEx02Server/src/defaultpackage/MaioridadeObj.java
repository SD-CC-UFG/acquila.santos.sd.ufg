//ACQUILA SANTOS ROCHA e JULIANA DE MELO TEIXEIRA
package defaultpackage;

import org.omg.CORBA.ORB;

import MaioridadeApp.*;
import MaioridadeApp.MaioridadePOA;

class MaioridadeObj extends MaioridadePOA {
	private ORB orb;
	
	public void setORB(ORB orb_val) {
	    orb = orb_val; 
	}
 
	public int maioridadeF(int idade) {
		int r;
		if (idade >= 21) {
			r = 1;
		}
		else {
			r = 0;
		}
		return r;
	}
  
	public int maioridadeM(int idade) {
		int r;
		if (idade >= 18) {
			r = 1;
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
