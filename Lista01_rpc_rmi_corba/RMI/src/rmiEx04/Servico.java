// ACQUILA SANTOS ROCHA e JULIANA DE MELO TEIXEIRA
package rmiEx04;

import java.rmi.Remote;
import java.rmi.RemoteException;

public interface Servico extends Remote {

	void addListener(ServicoListener listener) throws RemoteException;

	void setAltura(double altura) throws RemoteException;

	void setSexo(String sexo) throws RemoteException;
}