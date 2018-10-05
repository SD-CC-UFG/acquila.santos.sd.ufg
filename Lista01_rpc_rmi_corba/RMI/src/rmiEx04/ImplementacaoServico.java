// ACQUILA SANTOS ROCHA e JULIANA DE MELO TEIXEIRA
package rmiEx04;

import java.rmi.RemoteException;
import java.util.ArrayList;
import java.util.List;


class ImplementacaoServico implements Servico {

	private final List<ServicoListener> listeners = new ArrayList<>();

	private boolean setouX;
	private boolean setouY;

	private double Altura;
	private String Sexo;

	@Override
	public void addListener(ServicoListener listener) throws RemoteException {
		listeners.add(listener);
	}

	@Override
	public void setAltura(double altura) throws RemoteException {
		Altura = altura;
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
                        double resultado;
                        if ("feminino".equalsIgnoreCase(Sexo)) {
                            resultado = (62.1*Altura)-44.7;
                        }
                        else if ("masculino".equalsIgnoreCase(Sexo)) {
                            resultado = (72.7*Altura)-58;
                        }
                        else {
                            resultado = 0;
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

