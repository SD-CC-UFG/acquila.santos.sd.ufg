// ACQUILA SANTOS ROCHA e JULIANA DE MELO TEIXEIRA
package rmiEx05;

import java.rmi.RemoteException;
import java.util.ArrayList;
import java.util.List;


class ImplementacaoServico implements Servico {

	private final List<ServicoListener> listeners = new ArrayList<>();

	private boolean setouX;

	private int Idade;

	@Override
	public void addListener(ServicoListener listener) throws RemoteException {
		listeners.add(listener);
	}

	@Override
	public void setIdade(int idade) throws RemoteException {
		Idade = idade;
		setouX = true;
		verifica();
	}

	private void verifica() {
		if (setouX) {
                        String resultado;
                        if (Idade >= 5 && Idade <= 7) {
                            resultado = "infantil A";
                        }
                        else if (Idade >= 8 && Idade <= 10) {
                            resultado = "infantil B";
                        }
                        else if (Idade >= 11 && Idade <= 13) {
                            resultado = "juvenil A";
                        }
                        else if (Idade >= 14 && Idade <= 17) {
                            resultado = "juvenil B";
                        }else if (Idade >= 18) {
                            resultado = "adulto";
                        }
                        else {
                            resultado = "não definido!";
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

