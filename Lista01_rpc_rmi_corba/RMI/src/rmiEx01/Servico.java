// ACQUILA SANTOS ROCHA e JULIANA DE MELO TEIXEIRA
package rmiEx01;

import java.rmi.Remote;
import java.rmi.RemoteException;

public interface Servico extends Remote {

	void addListener(ServicoListener listener) throws RemoteException;

	void setSalAtual(double valor) throws RemoteException;

	void setCargo(String cargo) throws RemoteException;
}