// ACQUILA SANTOS ROCHA e JULIANA DE MELO TEIXEIRA
package rmiEx01;

import java.rmi.RemoteException;
import java.util.ArrayList;
import java.util.List;

import rmiEx01.Servico;
import rmiEx01.ServicoListener;

class ImplementacaoServico implements Servico {

	private final List<ServicoListener> listeners = new ArrayList<>();

	private boolean setouX;
	private boolean setouY;

	private double salAtual;
	private String Cargo;

	@Override
	public void addListener(ServicoListener listener) throws RemoteException {
		listeners.add(listener);
	}

	@Override
	public void setSalAtual(double valor) throws RemoteException {
		salAtual = valor;
		setouX = true;
		verifica();
	}

	@Override
	public void setCargo(String cargo) throws RemoteException {
		Cargo = cargo;
		setouY = true;
		verifica();
	}

	private void verifica() {
		if (setouX && setouY) {
                        double resultado;
                        if ("operador".equalsIgnoreCase(Cargo)) {
                            resultado = salAtual + (salAtual*0.2);
                        }
                        else if ("programador".equalsIgnoreCase(Cargo)) {
                            resultado = salAtual + (salAtual*0.18);
                        }
                        else {
                            resultado = salAtual;
                        }
			for (ServicoListener listener : listeners) {
				try {
					listener.calculoEfetuado(resultado);
				} catch (RemoteException e) {
					e.printStackTrace();
				}
			}
			setouX = false;
			setouY = false;
		}
	}
}

