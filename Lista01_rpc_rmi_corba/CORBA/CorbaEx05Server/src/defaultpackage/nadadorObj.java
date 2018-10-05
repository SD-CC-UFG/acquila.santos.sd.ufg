//ACQUILA SANTOS ROCHA e JULIANA DE MELO TEIXEIRA
package defaultpackage;

import org.omg.CORBA.ORB;

import nadadorApp.*;
import nadadorApp.nadadorPOA;

class nadadorObj extends nadadorPOA {
	private ORB orb;
	
	public void setORB(ORB orb_val) {
	    orb = orb_val; 
	}
	
	public String pesoF(int altura) {
		String r;
		if (altura >= 5 && altura <= 7) {
			r = "infaltil A";
		}
		else if (altura >= 8 && altura <= 10) {
			r = "infaltil B";
		}
		else if (altura >= 11 && altura <= 13) {
			r = "juvenil A";
		}
		else if (altura >= 14 && altura <= 17) {
			r = "juvenil B";
		}
		else if (altura >= 18) {
			r = "adulto";
		}
		else {
			r = "Categoria não definida!";
		}
		return r;
	}
	
  // implement shutdown() method
	public void shutdown() {
		orb.shutdown(false);
	}
}
