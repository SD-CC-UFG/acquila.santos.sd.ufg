// ACQUILA SANTOS ROCHA e JULIANA DE MELO TEIXEIRA
package rmiEx03;

import java.rmi.RemoteException;
import java.util.ArrayList;
import java.util.List;


class ImplementacaoServico implements Servico {

	private final List<ServicoListener> listeners = new ArrayList<>();

	private boolean setouX;
	private boolean setouY;
        private boolean setouZ;

	private double n1;
        private double n2;
        private double n3;

	@Override
	public void addListener(ServicoListener listener) throws RemoteException {
		listeners.add(listener);
	}

	@Override
	public void setN1(double N1) throws RemoteException {
		n1 = N1;
		setouX = true;
		verifica();
	}
        
        @Override
	public void setN2(double N2) throws RemoteException {
		n2 = N2;
		setouY = true;
		verifica();
	}

        @Override
	public void setN3(double N3) throws RemoteException {
		n3 = N3;
		setouZ = true;
		verifica();
	}

	private void verifica() {
		if ((setouX && setouY) && setouZ) {
                        String resultado;
                        double M = (n1+n2)/2;
                        if (M >= 7.0) {
                            resultado = "Aluno aprovado!";
                        }
                        else if (M < 7.0 && M > 3) {
                            M = (M + n3)/2;
                            if (M >=5.0) {
                                resultado = "Aluno aprovado!";
                            }
                            else {
                                resultado = "Aluno reprovado!";
                            }
                        }
                        else {
                            resultado = "Aluno reprovado!";
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
                        setouZ = false;
		}
	}
}

