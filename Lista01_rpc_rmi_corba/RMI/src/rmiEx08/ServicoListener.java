// ACQUILA SANTOS ROCHA e JULIANA DE MELO TEIXEIRA
package rmiEx08;

import java.rmi.Remote;
import java.rmi.RemoteException;

public interface ServicoListener extends Remote {

	void calculoEfetuado(double resultado) throws RemoteException;
}
