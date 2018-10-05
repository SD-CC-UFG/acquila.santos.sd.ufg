// ACQUILA SANTOS ROCHA e JULIANA DE MELO TEIXEIRA
package rmiEx06;

import java.rmi.RemoteException;
import java.util.ArrayList;
import java.util.List;


class ImplementacaoServico implements Servico {

	private final List<ServicoListener> listeners = new ArrayList<>();
        
        private boolean v1;
        private boolean v2;
        private boolean v3;
        private boolean v4;
        
	private double salAtual;
	private String Nome;
        private String Nivel;
        private int Depen;

	@Override
	public void addListener(ServicoListener listener) throws RemoteException {
		listeners.add(listener);
	}

	@Override
	public void setSalAtual(double valor) throws RemoteException {
		salAtual = valor;
                v1 = true;
		verifica();
	}

	@Override
	public void setNome(String nome) throws RemoteException {
		Nome = nome;
                v2 = true;
		verifica();
	}

        @Override
	public void setNivel(String nivel) throws RemoteException {
		Nivel = nivel;
                v3 = true;
		verifica();
	}
        
        @Override
	public void setDepen(int depen) throws RemoteException {
		Depen = depen;
                v4 = true;
		verifica();
	}
        
	private void verifica() {
		if (v1 && v2 && v3 && v4) {
                        String resultado;
                        double salLiq = salAtual;
                        if ("A".equalsIgnoreCase(Nivel)) {
                            if (Depen > 0){
                                salLiq = salLiq - (salLiq * 0.08);
                            }
                            else {
                                salLiq = salLiq - (salLiq * 0.03);
                            }
                        }
                        else if ("B".equalsIgnoreCase(Nivel)) {
                            if (Depen > 0){
                                salLiq = salLiq - (salLiq * 0.10);
                            }
                            else {
                                salLiq = salLiq - (salLiq * 0.05);
                            }
                        }
                        else if ("C".equalsIgnoreCase(Nivel)) {
                            if (Depen > 0){
                                salLiq = salLiq - (salLiq * 0.15);
                            }
                            else {
                                salLiq = salLiq - (salLiq * 0.08);
                            }
                        }
                        else if ("D".equalsIgnoreCase(Nivel)) {
                            if (Depen > 0){
                                salLiq = salLiq - (salLiq * 0.17);
                            }
                            else {
                                salLiq = salLiq - (salLiq * 0.10);
                            }
                        }
                        if (salLiq != salAtual) {
                            resultado = "Nome: "+Nome+"\nNível: "+Nivel+"\nSalário Líquido: "+salLiq;
                        }
                        else {
                            resultado = "Nível inválido!";
                        }
                        
			for (ServicoListener listener : listeners) {
				try {
					listener.calculoEfetuado(resultado);
				} catch (RemoteException e) {
					e.printStackTrace();
				}
			}
			v1 = false;
			v2 = false;
                        v3 = false;
                        v4 = false;
		}
	}
}

