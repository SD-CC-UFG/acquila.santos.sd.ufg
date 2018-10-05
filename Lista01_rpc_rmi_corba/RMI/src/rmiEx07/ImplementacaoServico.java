// ACQUILA SANTOS ROCHA e JULIANA DE MELO TEIXEIRA
package rmiEx07;

import java.rmi.RemoteException;
import java.util.ArrayList;
import java.util.List;


class ImplementacaoServico implements Servico {

	private final List<ServicoListener> listeners = new ArrayList<>();

	private boolean setouX;
	private boolean setouY;

	private int Idade;
	private int Temp;

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

	@Override
	public void setTempo(int temp) throws RemoteException {
		Temp = temp;
		setouY = true;
		verifica();
	}

	private void verifica() {
		if (setouX && setouY) {
                        String resultado;
                        if (Idade >= 65) {
                            if (Temp >= 30) {
                                resultado = "Sim!";
                            }
                            else {
                                resultado = "Não!";
                            }
                        }
                        else if (Idade >= 60 && Temp >= 25) {
                            resultado = "Sim!";
                        }
                        else {
                            resultado = "Não!";
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

