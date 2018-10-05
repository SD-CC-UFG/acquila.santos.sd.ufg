// ACQUILA SANTOS ROCHA e JULIANA DE MELO TEIXEIRA
package rmiEx03;

import java.rmi.Remote;
import java.rmi.RemoteException;

public interface Servico extends Remote {

	void addListener(ServicoListener listener) throws RemoteException;

	void setN1(double N1) throws RemoteException;
        
        void setN2(double N2) throws RemoteException;
        
        void setN3(double N3) throws RemoteException;

}