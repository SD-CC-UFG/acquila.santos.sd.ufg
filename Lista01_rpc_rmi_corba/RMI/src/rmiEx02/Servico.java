// ACQUILA SANTOS ROCHA e JULIANA DE MELO TEIXEIRA
package rmiEx02;

import java.rmi.Remote;
import java.rmi.RemoteException;

public interface Servico extends Remote {

	void addListener(ServicoListener listener) throws RemoteException;

	void setIdade(int idade) throws RemoteException;

	void setSexo(String sexo) throws RemoteException;
}