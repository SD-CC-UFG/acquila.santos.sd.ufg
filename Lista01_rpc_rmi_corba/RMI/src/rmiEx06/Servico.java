// ACQUILA SANTOS ROCHA e JULIANA DE MELO TEIXEIRA
package rmiEx06;

import java.rmi.Remote;
import java.rmi.RemoteException;

public interface Servico extends Remote {

	void addListener(ServicoListener listener) throws RemoteException;

	void setSalAtual(double valor) throws RemoteException;
        
        void setNome (String nome) throws RemoteException;
        
        void setNivel (String nivel) throws RemoteException;
        
        void setDepen (int depen) throws RemoteException;

}