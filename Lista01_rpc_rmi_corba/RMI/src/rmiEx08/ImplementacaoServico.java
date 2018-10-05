// ACQUILA SANTOS ROCHA e JULIANA DE MELO TEIXEIRA
package rmiEx08;

import java.rmi.RemoteException;
import java.util.ArrayList;
import java.util.List;


class ImplementacaoServico implements Servico {

	private final List<ServicoListener> listeners = new ArrayList<>();

	private boolean setouX;

	private double Saldo;

	@Override
	public void addListener(ServicoListener listener) throws RemoteException {
		listeners.add(listener);
	}

	@Override
	public void setSaldo(double saldo) throws RemoteException {
		Saldo = saldo;
		setouX = true;
		verifica();
	}

	private void verifica() {
		if (setouX) {
                        double resultado;
                        if (Saldo >= 0 && Saldo <= 200) {
                            resultado = 0;
                        }
                        else if (Saldo >= 201 && Saldo <= 400) {
                            resultado = Saldo * 0.2;
                        }
                        else if (Saldo >= 401 && Saldo <= 600) {
                            resultado = Saldo * 0.3;
                        }
                        else {
                            resultado = Saldo * 0.4;
                        }                       
			for (ServicoListener listener : listeners) {
				try {
					listener.calculoEfetuado(resultado);
				} catch (RemoteException e) {
					e.printStackTrace();
				}
			}
			setouX = false;
		}
	}
}

