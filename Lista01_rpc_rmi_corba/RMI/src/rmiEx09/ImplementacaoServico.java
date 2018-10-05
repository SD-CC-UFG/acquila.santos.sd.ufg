// ACQUILA SANTOS ROCHA e JULIANA DE MELO TEIXEIRA
package rmiEx09;

import java.rmi.RemoteException;
import java.util.ArrayList;
import java.util.List;


class ImplementacaoServico implements Servico {

	private final List<ServicoListener> listeners = new ArrayList<>();

	private boolean setouX;

	private int Valor;
        private int Naipe;

	@Override
	public void addListener(ServicoListener listener) throws RemoteException {
		listeners.add(listener);
	}

	@Override
	public void setCarta(int valor, int naipe) throws RemoteException {
		Valor = valor;
		Naipe = naipe;
                setouX = true;
		verifica();
	}

	private void verifica() {
		if (setouX) {
                        String resultado = null;
                        if (Naipe == 1) {
                            if (Valor <= 10) {
                                resultado = Valor+" de ouros";
                            }
                            else if (Valor == 11) {
                                resultado = "Valete de ouros";
                            }
                            else if (Valor == 12) {
                                resultado = "Dama de ouros";
                            }
                            else if (Valor == 13) {
                                resultado = "Rei de ouros";
                            }
                        }
                        else if (Naipe == 2) {
                            if (Valor <= 10) {
                                resultado = Valor+" de paus";
                            }
                            else if (Valor == 11) {
                                resultado = "Valete de paus";
                            }
                            else if (Valor == 12) {
                                resultado = "Dama de paus";
                            }
                            else if (Valor == 13) {
                                resultado = "Rei de paus";
                            }
                        }
                        else if (Naipe == 3) {
                            if (Valor <= 10) {
                                resultado = Valor+" de copas";
                            }
                            else if (Valor == 11) {
                                resultado = "Valete de copas";
                            }
                            else if (Valor == 12) {
                                resultado = "Dama de copas";
                            }
                            else if (Valor == 13) {
                                resultado = "Rei de copas";
                            }
                        }
                        else if (Naipe == 2) {
                            if (Valor <= 10) {
                                resultado = Valor+" de espadas";
                            }
                            else if (Valor == 11) {
                                resultado = "Valete de espadas";
                            }
                            else if (Valor == 12) {
                                resultado = "Dama de espadas";
                            }
                            else if (Valor == 13) {
                                resultado = "Rei de espadas";
                            }
                        }
                        else {
                            resultado = "Carta inválida!";
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

