// ACQUILA SANTOS ROCHA e JULIANA DE MELO TEIXEIRA
package rmiEx08;

import java.rmi.Remote;
import java.rmi.RemoteException;

public interface Servico extends Remote {

	void addListener(ServicoListener listener) throws RemoteException;

	void setSaldo(double saldo) throws RemoteException;

}