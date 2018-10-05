// ACQUILA SANTOS ROCHA e JULIANA DE MELO TEIXEIRA
package rmiEx02;

import java.rmi.RemoteException;
import java.util.ArrayList;
import java.util.List;


class ImplementacaoServico implements Servico {

	private final List<ServicoListener> listeners = new ArrayList<>();

	private boolean setouX;
	private boolean setouY;

	private int Idade;
	private String Sexo;

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
	public void setSexo(String sexo) throws RemoteException {
		Sexo = sexo;
		setouY = true;
		verifica();
	}

	private void verifica() {
		if (setouX && setouY) {
                        String resultado;
                        if ("feminino".equalsIgnoreCase(Sexo)) {
                            if (Idade >= 21) {
                                resultado = "Maior de idade!";
                            }
                            else {
                                resultado = "Menor de idade!";
                            }
                        }
                        else if ("masculino".equalsIgnoreCase(Sexo)) {
                            if (Idade >= 18) {
                                resultado = "Maior de idade!";
                            }
                            else {
                                resultado = "Menor de idade!";
                            }
                        }
                        else {
                            resultado = "Não definido!";
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

